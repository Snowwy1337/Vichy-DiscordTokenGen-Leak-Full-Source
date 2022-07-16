# https://github.com/Its-Vichy
# Hi skid

from modules.discord.session import DiscordSession
from modules.discord.websocket import DiscordWs
from modules.api.email.imap import ImapWrapper
from modules.utils.benchmark import Benchmak
import toml, threading, random, string, time
from modules.utils.database import Database
from security.anti_debug import AntiDebug
from modules.utils.console import Console
from security.auth import Auth

from modules.api.email.hotmailbox import HotmailboxServiceClient
from modules.api.captcha.capmonster import CaptchaSolver
from modules.api.captcha.rs_hcaptcha import RSolver
from modules.api.captcha.hcaptcha import Solver


__config__ = toml.loads(open('../config/config.toml', 'r+').read())


class Worker(threading.Thread):
    def __init__(self, database: Database):
        threading.Thread.__init__(self)
        self.discordSession = DiscordSession(database)
        self._db = database

    def run(self):
        self._db.stats._worker += 1
        proxy = None if __config__['proxy']['proxyless'] else next(self._db.proxies)
        
        start = time.time()
        CB = Benchmak("Solve Hcaptcha")
        cap = RSolver(self._db, proxy).solve_captcha() if __config__['solver']['version'] == 2 else Solver(self._db, proxy).solve_captcha()
        #CaptchaSolver().get_captcha_key(proxy, cookie= self.discordSession._client.headers['cookie'])
        #RSolver(self._db, proxy).solve_captcha() if __config__['solver']['version'] == 2 else Solver(self._db, proxy).solve_captcha() 
        CB.end()

        if cap == None or cap == '' or cap == 'null' or cap == 'error':
            self._db.stats._worker -= 1
            return
        else:
            end = time.time()
            elapsed = end - start
            self._db.stats._solved_captcha_times.append(elapsed)
            Console.debug(f'(*) Solved captcha: {cap[:30]}, returned in {round(elapsed)}s')

        token = self.discordSession.createAccount(cap, 'http://'+ str(proxy))

        if 'captcha_key' not in str(token) and str(token) != '':
            if not self.discordSession.isLocked():
                Console.printF(f"(+) Unlocked: {token}")
                self._db.stats._unlocked += 1
                Database.saveToken(token)

                 # Connect to websocket
                if __config__['discord']['websocket_connect']:
                    DiscordWs(token).start()

                def verify():
                    D = Benchmak("Verify account")
                    if __config__['email']['enabled']:
                        verificationToken = None

                        # Hotmailbox - Mail verification
                        if __config__['email']['service'] == 1:
                            client = HotmailboxServiceClient()

                            mailAddress, mailPassword = client.get_mail_pass()

                            if self.discordSession.addEmail(mailAddress):
                                Console.debug(f'(*) Add Email, Bio, Pfp: {mailAddress}')
                                verificationToken = client.get_verification_token(mailAddress, mailPassword)

                        # IMAP - Mail verification
                        if __config__['email']['service'] == 3:
                            mailAddress = ''.join(random.choice(string.ascii_lowercase) for _ in range(15)) + '@' + __config__['email']['imap_domain']

                            if self.discordSession.addEmail(mailAddress):
                                Console.debug(f'(*) Add Email, Bio, Pfp: {mailAddress}')
                                verificationToken = ImapWrapper().get_verification_token(mailAddress, ignoreImapUser=False, db=self._db)
                        
                        if verificationToken != None:
                            Console.debug(f'(*) ({mailAddress}) Get verification token: {verificationToken[:15]}')

                            isVerified, newToken = self.discordSession.verifyEmail(verificationToken, str(proxy))
                                
                            if isVerified:
                                Console.printF(f'(*) Email verified: {newToken}')
                                self._db.stats._mail_verified += 1
                                Database.saveToken(f'{mailAddress}:{__config__["profil"]["password"]}:{newToken}', True)
                                Database.removeLiveFromFile(token, '../data/gen/unverified.txt')
                
                    if __config__['email']['enabled'] == False and (__config__['profil']['unverified_bio'] == True or __config__['profil']['unverified_pfp'] == True):
                        if self.discordSession.unverifiedRealist():
                            Console.debug(f'(+) Bio, Pfp added: {token}')
                    D.end()

                if __config__['perf']['fast_singe_thread']:
                    threading.Thread(target=verify).start()
                else:
                    verify()
                
                D = Benchmak("Add Hypesquad + join server")
                if __config__['profil']['random_hypesquad']:
                    if self.discordSession.setHypesquad():
                        Console.printF(f'(*) Hypesquad set: {token}')

                if __config__['discord']['join_server'] != '':
                    if self.discordSession.joinServer(__config__['discord']['join_server']):
                        Console.printF(f'(+) Joined server: {token}')
                D.end()
                
                if __config__['proxy']['proxyless']:
                    time.sleep(110)
            else:
                Console.printF(f'(-) Locked: {token}')
                self._db.stats._locked += 1

        self._db.stats._worker -= 1

if __name__ == '__main__':
    AntiDebug().start()


    D = Database()
    Console.printLogo()
    threading.Thread(target=Console.titleThead, args=[D]).start()
    threading.Thread(target=D.stats.gen_calculator_thread).start()

    while True:
        while D.stats._worker >= __config__['perf']['threads']:
            time.sleep(1)
        
        Worker(D).start()
