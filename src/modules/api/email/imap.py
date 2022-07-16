import time, httpx, imap_tools, re, toml
from ...utils.database import Database
from ...utils.console import Console

__config__ = toml.loads(open('../config/config.toml', 'r+').read())

class ImapWrapper:
    @staticmethod
    def get_verification_token(email: str, password: str= __config__['email']['imap_password'], host: str= __config__['email']['imap_server'], port: str= __config__['email']['imap_port'], imapUsername: str=  __config__['email']['imap_mail'], ignoreImapUser: bool= True, db: Database= None):
        if db != None:
            while db.stats._imap_connected >= __config__['email']['concurent_connection']:
                time.sleep(1)

            db.stats._imap_connected += 1
            
        while True:
            try:
                with imap_tools.MailBox(host, port).login(email if ignoreImapUser else imapUsername, password, 'INBOX') as mailbox:
                    for msg in mailbox.fetch():
                        if msg.to[0].lower() == email.lower() and msg.from_ == 'noreply@discord.com':
                            body = msg.html
                            for url in re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body):
                                redirect = None
                                while redirect is None:
                                    try:
                                        redirect = httpx.get(url, follow_redirects=True, timeout=None).url
                                    except Exception as e:
                                        Console.debug(f'(-) Mail-redirection error: {e}')
                                        pass

                                if 'https://discord.com/verify#token=' in str(redirect):
                                    if db != None:
                                        db.stats._imap_connected -= 1

                                    try:
                                        mailbox.delete(msg.uid)
                                    except Exception as e:
                                        Console.debug(f'(-) Cannot delete mail: {e}')
                                        pass

                                    return str(redirect).split('https://discord.com/verify#token=')[1]
                    time.sleep(1)
            except Exception as e:
                Console.debug(f'Mail verification error: {e}')
                time.sleep(3)
                pass
        
        db.stats._imap_connected -= 1