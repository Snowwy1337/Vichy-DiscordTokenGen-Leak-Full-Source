# Here is the fun with full requests solver
# https://github.com/Its-Vichy

import httpx, base64, urllib, json, toml, threading, time
from ...utils.browser import Chrome, Firefox
from .motion_data import get_motion_data
from ...utils.benchmark import Benchmak
from ...utils.database import Database
from ...utils.console import Console


__config__ = toml.loads(open('../config/config.toml', 'r+').read())


class RSolver:
    def __init__(self, database: Database, proxy, site_key: str = '4c672d35-0701-42b2-88c3-78380b0db560'):
        self.site_key = site_key

        self.database = database
        self.base_header = Firefox.solver_base_header() if __config__['browser']['browser_id'] == 1 else Chrome.solver_base_header()

        self.client = httpx.Client(headers=self.base_header)
        self.proxy = 'http://' + proxy if __config__['proxy']['proxyless'] == False else None

        self._recognition_running = 0

    def is_img(self, img_type: str, img_url: str):
        B = Benchmak("Recognize image")
        while self._recognition_running >= __config__['perf']['threaded_recognition_chunck']:
            time.sleep(0.1)

        """resp = is_imgv2(img_type, img_url) if __config__['solver']['use_v2'] else is_imgv1(img_type, img_url)

        try:
            B.end()
            return resp
        except Exception as e:
            B.end()
            print(e)"""

        try:
            self._recognition_running += 1
            img_type: str = base64.b64encode(img_type.encode("utf-8")).decode()
            img_url: str = base64.b64encode(img_url.encode("utf-8")).decode()

            with httpx.Client(timeout=None) as client:
                response = client.get(f'http://{next(self.database.img_nodes)}/check/{img_type}/{img_url}').text
                self._recognition_running -= 1
                B.end()
                return True if response == "True" else False
        except Exception as e:
            Console.debug('ImageRecognitionError: ' + str(e))
            B.end()
            return False

    def hsw(self, task_id: str):
        B = Benchmak("Get HSW")
        while True:
            try:
                resp = httpx.get(f'http://{next(self.database.hsw_nodes)}/n?req={task_id}', timeout=None)
                B.end()
                return resp.text
            except:
                pass

    def get_task(self):
        B = Benchmak("Get HCaptcha Task")
        payload = {
            'v': __config__['solver']['hcaptcha_version'],
            'host': 'discord.com',
            'sitekey': self.site_key,
            'sc': '1',
            'swa': '1',
        }

        payload = urllib.parse.urlencode(payload)
        self.base_header['Content-Type'] = 'application/x-www-form-urlencoded'
        self.base_header['Content-Length'] = str(len(payload))

        with httpx.Client(headers= self.base_header, proxies= self.proxy if __config__['proxy']['full_proxy_solving'] else None) as client:
            response = client.post(f"https://hcaptcha.com/checksiteconfig?v={__config__['solver']['hcaptcha_version']}&host=discord.com&sitekey={self.site_key}&sc=1&swa=1", data=payload).json()
            B.end()
            return response['c']

    def get_captcha(self, n: str, c: dict):
        B = Benchmak("Get captcha questions")
        payload = {
            'v': __config__['solver']['hcaptcha_version'],
            'sitekey': self.site_key,
            'host': 'discord.com',
            'hl': 'fr',
            'motionData': get_motion_data(),
            'n': n,
            'c': json.dumps(c)
        }

        payload = urllib.parse.urlencode(payload)
        self.base_header['Content-Type'] = 'application/x-www-form-urlencoded'
        self.base_header['Content-Length'] = str(len(payload))

        with httpx.Client(headers=self.base_header, proxies=self.proxy) as client:
            response = client.post(f"https://hcaptcha.com/getcaptcha?s={self.site_key}", data=payload).json()
            B.end()
            return response

    def solve_task(self, task: dict):
        n = self.hsw(task['c']['req'])
        task_key = task['key']

        c = task['c']
        
        if 'containing a ' in task['requester_question']['en']:
            img_type = task['requester_question']['en'].split('Please click each image containing a ')[1].strip()
        else:
            img_type = task['requester_question']['en'].split('Please click each image containing an ')[1].strip()
        solved_task = {}
        task_thread = []

        if img_type in ['bedroom', 'bridge', 'lion'] and __config__['solver']['use_v2'] == False:
            print('unsuported img, please use V2')
            return ''

        def solve(task):
            solved_task[task['task_key']] = str(self.is_img(img_type, task["datapoint_uri"])).lower()

        B = Benchmak("Recognize all hcaptcha images")
        if __config__['perf']['threaded_recognition']:
            for task in task['tasklist']:
                task_thread.append(threading.Thread(target= solve, args=[task]))
            
            for t in task_thread:
                t.start()
            
            for t in task_thread:
                t.join()
        else:
            for task in task['tasklist']:
                solve(task)
        B.end()

        with httpx.Client(headers=self.base_header, proxies=self.proxy) as client:
            payload = {
                'answers': solved_task,
                'c': json.dumps(c),
                'job_mode': 'image_label_binary',
                'motionData': get_motion_data(),
                'n': n,
                'serverdomain': 'discord.com',
                'sitekey': self.site_key,
                'v': __config__['solver']['hcaptcha_version']
            }

            client.headers['Content-Length'] = str(len(json.dumps(payload)))
            client.headers['Content-Type'] = 'application/json;charset=UTF-8'

            #print(payload)

            response = client.post(f'https://hcaptcha.com/checkcaptcha/{task_key}?s={self.site_key}', json=payload).json()

            # 'pass': False, 'error': 'missing data'}

            if 'pass' in str(response):
                if response['pass']:
                    return response['generated_pass_UUID']
            else:
                #print(response)
                Console.debug("Captcha solving failed")
                self.database.stats._failed_captcha += 1
                pass

    def solve_captcha(self):
        if __config__['solver']['captcha_input']:
            return input('captcha key: ')
        else:
            try:
                task = self.get_task()
                #print(task)
                #if task['success']:
                #print(task)
                Console.debug('(*) get a task')
                n = self.hsw(task['req'])

                captcha_task = self.get_captcha(n, task)

                #print(captcha_task)
                Console.debug('(*) solving')

                if 'key' in str(captcha_task):
                    return self.solve_task(captcha_task)
                else:
                    return ''
            except Exception as e:
                print(e)
                if __config__['proxy']['remove_dead']:
                    if str(e) in ['timed out', '403 Forbidden', 'Server disconnected without sending a response.', '400 Bad Request']:
                        self.database.removeLiveFromFile(self.proxy.split('://')[1], '../data/proxies.txt')
                return ''
