from modules.utils.database import Database
import threading, os, toml, logging, time
from colorama import Fore, init; init()

__config__, __lock__ = toml.loads(open('../config/config.toml', 'r+').read()), threading.RLock()
logging.basicConfig(filename= '../data/logs/logs.log', level= logging.DEBUG, format='[%(asctime)s] %(message)s')

class Console:
    @staticmethod
    def titleThead(database: Database):
        if os.name == 'nt':
            while True:
                time.sleep(1)

                try:
                    avg_time = sum(database.stats._solved_captcha_times) / len(database.stats._solved_captcha_times)
                except:
                    avg_time = 0

                os.system(f'title DTG V1 - @its_vichy | Gen: {database.stats._locked+database.stats._unlocked} Locked: {database.stats._locked} Unlocked: {database.stats._unlocked} MailVerified: {database.stats._mail_verified} Worker: {database.stats._worker} Threads: {threading.active_count()} | {database.stats._gen_min}/m - {database.stats._valid_min}/vm - {round(database.stats._lock_rate)}% lr - ~{round(avg_time)}s AverageSolvingTime'.replace('|', '^|'))

    @staticmethod
    def printLogo():
        os.system('cls && title DTG V1 - @its_vichy' if os.name == 'nt' else 'clear')
        main = Fore.LIGHTBLUE_EX

        print(main + '''
    ·▄▄▄▄  ▄▄▄▄▄ ▄▄ • 
    ██▪ ██ •██  ▐█ ▀ ▪
    ▐█· ▐█▌ ▐█.▪▄█ ▀█▄
    ██. ██  ▐█▌·▐█▄▪▐█
    ▀▀▀▀▀•  ▀▀▀ ·▀▀▀▀ 
        '''.replace('.', f'{Fore.LIGHTWHITE_EX}.{main}').replace('▪', f'{Fore.LIGHTWHITE_EX}▪{main}').replace('•', f'{Fore.LIGHTWHITE_EX}•{main}').replace('·', f'{Fore.LIGHTWHITE_EX}·{main}') + Fore.RESET)
    
    @staticmethod
    def printF(content: str):
        __lock__.acquire()
        print(str(content).replace('(', f'({Fore.LIGHTBLUE_EX}').replace(')', f'{Fore.RESET})').replace('+', f'{Fore.LIGHTGREEN_EX}+{Fore.RESET}').replace('*', f'{Fore.LIGHTYELLOW_EX}*{Fore.RESET}'))
        __lock__.release()
    
    @staticmethod
    def debug(content: str):
        with __lock__:
            if __config__['logs']['debug']:
                print(str(content).replace('(', f'({Fore.LIGHTBLUE_EX}').replace(')', f'{Fore.RESET})'))

            if __config__['logs']['save_logs']:
                logging.debug(str(content))