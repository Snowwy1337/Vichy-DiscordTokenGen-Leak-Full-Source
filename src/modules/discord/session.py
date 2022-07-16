import httpx, toml, random, string, json, base64
from ..utils.browser import Firefox, Chrome
from ..utils.database import Database
from ..utils.console import Console

__config__ = toml.loads(open('../config/config.toml', 'r+').read())

from modules.api.captcha.capmonster import CaptchaSolver
from modules.api.captcha.rs_hcaptcha import RSolver
from modules.utils.benchmark import Benchmak

class DiscordSession():
    def __init__(self, database: Database):
        self._client = httpx.Client(timeout=3000)
        self._fingerprint = None
        self.__setupSession()
        self._db = database

    def __setupSession(self):
        B = Benchmak("Setup HttpSession")
        self._client.headers = Firefox.base_header() if __config__['browser']['browser_id'] == 1 else Chrome.base_header()

        self._client.headers['X-Track'] = Firefox.super_properties() if __config__['browser']['browser_id'] == 1 else Chrome.super_properties()

        response = self._client.get('https://discord.com/api/v9/experiments')

        self._fingerprint = response.json()['fingerprint']
        self._client.headers['Cookie'] = f"locale=fr; __dcfduid={response.cookies.get('__dcfduid')}; __sdcfduid={response.cookies.get('__sdcfduid')}" #locale,cfbm,cdf,sdcf
        self._client.cookies.set('locale', 'fr', 'discord.com')
        self._client.headers['X-Fingerprint']  = self._fingerprint
        B.end()
    
    def isLocked(self):
        if self._client.get('https://discord.com/api/v9/users/@me/library').status_code == 200:
            if __config__['profil']['save_og']:
                response = self._client.get('https://discord.com/api/v9/users/@me').json()
                token = self._client.headers["Authorization"]

                tag = response['discriminator']
                flag = response['public_flags']

                if __config__['profil']['check_flag']:
                    if flag != 0:
                        Console.printF(f"(-) Token is flagged '{flag}': {token}")
                    else:
                        Console.printF(f"(+) Token is not flagged: {token}")
                
                if tag in __config__['profil']['og_custom'] or '000' in tag or tag in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999']:
                    Console.printF(f'(OG) Got OG #{tag}, {token}')
                    self._db.saveToken(f'{tag}:{token}', IsOg= True)

            return False
        else:
            return True

    def createAccount(self, captchaKey: str, proxy: str= None):
        username = ''.join(random.choice(string.ascii_letters) for _ in range(10)) if __config__['profil']['username'] == 1 else next(self._db.username)

        payload = {
            'consent': True,
            'fingerprint': self._fingerprint,
            'username': username,
            'captcha_key': captchaKey
        }

        self._client.headers['Content-Length'] = str(len(json.dumps(payload)))
        self._client.headers['Content-Type']   = 'application/json'

        ## that
        response = httpx.post('https://discord.com/api/v9/auth/register', json= payload, proxies= None if __config__['proxy']['proxyless'] else proxy, headers= self._client.headers, cookies= self._client.cookies, timeout=3000).json()

        ## here
        self._client.headers['X-Debug-Options'] = 'bugReporterEnabled'
        self._client.headers['X-Discord-Locale'] = 'fr'
        self._client.headers['X-Super-Properties'] = Firefox.super_properties(is_xtrack=False) if __config__['browser']['browser_id'] == 1 else Chrome.super_properties(is_xtrack=False)
        self._client.headers.pop('x-track')
        
        try:
            self._client.headers.pop('Content-Length')
        except:
            pass

        if 'token' in str(response):
            self._client.headers['Authorization'] = response['token']
            return response['token']
        else:
            # {'code': 50035, 'errors': {'username': {'_errors': [{'code': 'USERNAME_TOO_MANY_USERS', 'message': 'Too many users have this username, please try another.'}]}}, 'message': 'Invalid Form Body'}
            if 'USERNAME_TOO_MANY_USERS' in str(response):
                Console.debug(f'(-) Username overused, deleting')
                self._db.removeLiveFromFile(username, '../data/usernames.txt')
                return ''
                # {'code': 50035, 'errors': {'username': {'_errors': [{'code': 'USERNAME_INVALID_CONTAINS', 'message': 'Username cannot contain "discord"'}]}}, 'message': 'Invalid Form Body'}
            else:
                return response
    
    def addEmail(self, emailAddress: str):
        payload = {
            'email': emailAddress,
            'password': __config__['profil']['password'],

            'date_of_birth': '1998-01-05',
            'bio': f"*{httpx.get('https://free-quotes-api.herokuapp.com', timeout=30).json()['quote']}*" if __config__['profil']['bio_from_file'] == False else next(self._db.bios),
            'avatar': f"data:image/png;base64,{base64.b64encode(open(f'../data/avatar/{next(self._db.avatars)}', 'rb').read()).decode()}",
        }

        self._client.headers['Content-Length'] = str(len(json.dumps(payload)))

        response = self._client.patch('https://discord.com/api/v9/users/@me', json=payload)
        try:
            self._client.headers.pop('Content-Length')
        except:
            pass

        if response.status_code == 200:
            return True
        else:
            Console.debug(f"Can't add Email: {response.json()}")
            return False
            
    def verifyEmail(self, verificationToken: str, proxy: str):
        def submitVerificationToken(captcha_key: str= None):
            payload = {
                'captcha_key': captcha_key,
                'token': verificationToken
            }

            self._client.headers['Content-Length'] = str(len(json.dumps(payload)))
            
            try:
                self._client.headers.pop('Authorization')
            except:
                pass

            response = self._client.post('https://discord.com/api/v9/auth/verify', json=payload)
            
            try:
                self._client.headers.pop('Content-Length')
            except:
                pass

            if response.status_code == 200:
                token = response.json()['token']
                self._client.headers['Authorization'] = token
                if captcha_key != None:
                    Console.debug('--> Verified after captcha !')
                return True, token
            else:
                # {'captcha_key': ['captcha-required'], 'captcha_sitekey': 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34', 'captcha_service': 'hcaptcha'}
                Console.debug(f"Can't verify Email: {response.json()}")
                return False, response.json()
        
        retry = 0
        key = None
        while True:
            passed, token = submitVerificationToken(key)

            if passed:
                return True, token
            else:
                if __config__['email']['solve_captcha'] and __config__['email']['max_retry'] <= retry:
                    retry += 1
                    Console.debug(f'(!) Got a captcha on verification, try solving (retry #{retry})') # CaptchaSolver().get_captcha_key(proxy, site_key='f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34') #
                    key = RSolver(self._db, proxy, site_key='f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34').solve_captcha() # if __config__['solver']['version'] == 2 else Solver(self._db, proxy).solve_captcha()
                else:
                    return False, ''

    def joinServer(self, inviteCode: str):
        self._client.headers['Content-Length'] = '2'
        response = self._client.post(f'https://discord.com/api/v9/invites/{inviteCode}', json={})
        
        try:
            self._client.headers.pop('Content-Length')
        except:
            pass

        if response.status_code != 400:
            #Console.debug(f'Joined server: {response.json()}')
            return True
        else:
            return False
    
    def unverifiedRealist(self):
        payload = {
            'date_of_birth': '1998-01-05',
            'bio': (f"*{httpx.get('https://free-quotes-api.herokuapp.com', timeout=30).json()['quote']}*" if __config__['profil']['bio_from_file'] == False else next(self._db.bios)) if __config__['profil']['unverified_bio'] == True else None,
            'avatar': f"data:image/png;base64,{base64.b64encode(open(f'../data/avatar/{next(self._db.avatars)}', 'rb').read()).decode()}" if __config__['profil']['unverified_pfp'] else None,
        }

        self._client.headers['Content-Length'] = str(len(json.dumps(payload)))

        response = self._client.patch('https://discord.com/api/v9/users/@me', json=payload)
        try:
            self._client.headers.pop('Content-Length')
        except:
            pass

        if response.status_code == 200:
            return True
        else:
            Console.debug(f"Can't add pfp and bio: {response.json()}")
            return False
    
    def setHypesquad(self):
        response = self._client.post('https://discord.com/api/v9/hypesquad/online', json={'house_id': random.randint(1, 3)})
        return True if response.status_code == 204 else False