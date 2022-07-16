import httpx, itertools, toml, time
from .imap import ImapWrapper

__proxies__, __config__ = itertools.cycle(open('../data/proxies_api.txt', 'r+').read().splitlines()), toml.loads(open('../config/config.toml', 'r+').read())

class HotmailboxServiceClient:
    @staticmethod
    def get_mail_pass():
        while True:
            try:
                proxy = 'http://' + next(__proxies__).split('\n')[0] if __config__['proxy']['proxy_for_api'] else None

                with httpx.Client(proxies=proxy, timeout=30) as client:
                    stock = client.get('https://api.hotmailbox.me/mail/currentstock').json()['Data']
                    mail_code = None

                    for data in stock:
                        if data['Instock'] > 1:
                            mail_code = data['MailCode']

                    email = client.get(
                        f'https://api.hotmailbox.me/mail/buy?apikey={__config__["email"]["api_key"]}&mailcode={mail_code}&quantity=1').json()

                    return email['Data']['Emails'][0]['Email'], email['Data']['Emails'][0]['Password']
            except Exception as e:
                time.sleep(5)
                #Console.debug(f'Get mail error: {e}')
                pass

    @staticmethod
    def get_verification_token(email: str, password: str):
        return ImapWrapper.get_verification_token(email, password, 'pop-mail.outlook.com', '993')