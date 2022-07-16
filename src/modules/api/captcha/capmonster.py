from ...utils.console import Console
import httpx, toml, time

__config__ = toml.loads(open('../config/config.toml', 'r+').read())

class CaptchaSolver:
    @staticmethod
    def get_captcha_key_by_hand():
        return input('Captcha-key: ')

    @staticmethod
    def get_captcha_key(static_proxy: str, cookie: str=None, site_key: str = '4c672d35-0701-42b2-88c3-78380b0db560'):
        print(cookie)
        task_payload = {
            'clientKey': __config__['solver']['captcha_key'],
            'task': {
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'websiteKey': site_key,
                'websiteURL': 'https://discord.com',
                'type': 'HCaptchaTask',
                'cookies': cookie,

                'proxyPassword': static_proxy.split('@')[0].split(':')[1],
                'proxyAddress': static_proxy.split('@')[1].split(':')[0],
                'proxyLogin': static_proxy.split('@')[0].split(':')[0],
                'proxyPort': static_proxy.split('@')[1].split(':')[1],
                'proxyType': 'http',
            }
        }
        key = None

        with httpx.Client(headers={'content-type': 'application/json', 'accept': 'application/json'}, timeout=30) as client:
            try:
                task_id = client.post(f'https://api.{__config__["solver"]["captcha_api"]}/createTask', json=task_payload).json()['taskId']
                Console.debug(f'Recieved captcha task ID: {task_id}')

                get_task_payload = {
                    'clientKey': __config__["solver"]['captcha_key'],
                    'taskId': task_id
                }

                while key is None:
                    try:
                        response = client.post(f'https://api.{__config__["solver"]["captcha_api"]}/getTaskResult', json=get_task_payload,  timeout=30).json()

                        if 'ERROR_PROXY_CONNECT_REFUSED' in str(response):
                            return 'ERROR'

                        if 'ERROR' in str(response):
                            return 'ERROR'

                        if response['status'] == 'ready':
                            key = response['solution']['gRecaptchaResponse']
                        else:
                            time.sleep(3)
                    except Exception as e:
                        Console.debug(f'Captcha task result error: {e}')

                        if 'ERROR_PROXY_CONNECT_REFUSED' in str(e):
                            key = 'ERROR'
                        else:
                            pass
                return key

            except Exception as e:
                Console.debug(f'Captcha task result error: {e}')

                if 'ERROR_PROXY_CONNECT_REFUSED' in str(e):
                    return 'ERROR'
                else:
                    pass