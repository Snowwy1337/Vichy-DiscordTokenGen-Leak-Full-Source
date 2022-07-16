import itertools, threading, os, toml, time

__lock__, __config__  = threading.RLock(), toml.loads(open('../config/config.toml', 'r+').read())

class Stats:
    def __init__(self):
        self._locked = 0
        self._unlocked = 0
        self._mail_verified = 0
        self._gen_min = 0
        self._valid_min = 0
        self._worker = 0
        self._lock_rate = 0
        self._solved_captcha_times = []
        self._imap_connected = 0
        self._failed_captcha = 0

    def gen_calculator_thread(self):
        start_time = time.time()

        while True:
            try:
                self._gen_min   = round((self._locked + self._unlocked) / ((time.time() - start_time) / 60))
                self._valid_min = round(self._unlocked / ((time.time() - start_time) / 60))
                self._lock_rate = (100 * self._locked) / (self._locked + self._unlocked)
            except:
                pass

            time.sleep(1)

class Database:
    def __init__(self):
        self.username = itertools.cycle(list(set(open('../data/usernames.txt', 'r+', encoding='utf-8', errors='ignore').read().splitlines())))
        self.bios = itertools.cycle(list(set(open('../data/bios.txt', 'r+', encoding='utf-8', errors='ignore').read().splitlines())))
        self.avatars  = itertools.cycle(os.listdir('../data/avatar/'))
        self.proxies  = itertools.cycle(list(set(open('../data/proxies.txt', 'r+').read().splitlines())))
        self.nodes = itertools.cycle(__config__["solver"]["nodes"])
        self.img_nodes = itertools.cycle(__config__["solver"]["img_processing_nodes"])
        self.hsw_nodes = itertools.cycle(__config__['solver']['hsw_nodes_address'])
        self.stats = Stats()

    @staticmethod
    def saveToken(token: str, IsVerified: bool= False, IsOg: bool= False):
        with __lock__:
            with open(f'../data/gen/{"mail_verified.txt" if IsVerified else "unverified.txt"}', 'a+') as f:
                f.write(f'{token}\n')
            
            if IsOg:
                with open(f'../data/gen/og.txt', 'a+') as f:
                    f.write(f'{token}\n')
    
    @staticmethod
    def removeLiveFromFile(content: str, filePath: str):
        with __lock__:
            with open(filePath, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()

            with open(filePath, 'w', encoding='utf-8', errors='ignore') as f:
                for line in lines:
                    if line.strip('\n') != content:
                        f.write(line)