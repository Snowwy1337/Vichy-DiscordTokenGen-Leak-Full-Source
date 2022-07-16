from ...utils.database import Database
import httpx, toml,  random, string
from .rs_hcaptcha import RSolver

__config__ = toml.loads(open('../config/config.toml', 'r+').read())

class Solver:
    def __init__(self, database: Database, proxyAddress: str):
        self.proxy = proxyAddress
        self.database = database
    
    def solve_captcha(self):
        if __config__['solver']['captcha_input']:
            return input('captcha key: ')
        else:
            task_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

            if __config__['solver']['version'] == 1:
                resp = httpx.post(f'http://{next(self.database.nodes)}/{task_name}', timeout=None, json={
                    'site_key': '4c672d35-0701-42b2-88c3-78380b0db560',
                    'legit': "y" if __config__['solver']['legit_solver'] else "n",
                    'proxy': self.proxy if not __config__['proxy']['proxyless'] else 'x:x'
                }).json()

                if 'key' in str(resp):
                    return resp['key']
                else:
                    return None
            
            else:
                resp = RSolver(self.proxy)
                return resp
