from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import threading, httpx, time
from selenium import webdriver
from os import system

__login__, __password__ = '', ''

class BrowserThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.token = httpx.post('https://anty-api.com/auth/login', json={'username': __login__,'password': __password__}, timeout=None).json()['token']

    def generate_browser(self):
        payload = {
            "name": "Discord",
            "useragent[mode]": "manual",
            "mainWebsite": "google",
            "useragent[value]": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9005 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "platform": "windows",
            "webrtc[mode]": "off",
            "canvas[mode]": "noise",
            "webgl[mode]": "noise",
            "locale[mode]": "auto",
            "cpu[mode]": "noise",
            "memory[mode]": "noise",
            "browserType": "anty",
            "webglInfo[mode]": "noise",
            "timezone[mode]": "auto",
            "geolocation[mode]": "auto",
            "doNotTrack": 1,
        }

        response = httpx.post('https://anty-api.com/browser_profiles', headers={'Authorization': f'Bearer {self.token}'}, data=payload).json()
        return response['browserProfileId']

    def get_profil_port(self, profil_id: str):
        r = httpx.get(f'http://localhost:3001/v1.0/browser_profiles/{profil_id}/start?automation=1', timeout=None).json()
        return r['automation']['port']

    def get_driver(self):
        browser_id = self.generate_browser()
        port = self.get_profil_port(browser_id)

        print(f'[+] Browser id: {browser_id} - port: {port}')

        chrome_options = Options()
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--disable-site-isolation-trials')
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        
        return webdriver.Chrome(options=chrome_options), browser_id

    def stop_and_delete(self, profil_id: str):
        print('[+] Stopping and deleting browser #{profil_id}')
        httpx.get(f'http://localhost:3001/v1.0/browser_profiles/{profil_id}/stop')
        time.sleep(3)
        httpx.delete(f'https://anty-api.com/browser_profiles/{profil_id}', headers={'Authorization': f'Bearer {self.token}'})

    def run(self):
        driver, browser_id = self.get_driver()
        driver.get('https://accounts.hcaptcha.com/demo?sitekey=4c672d35-0701-42b2-88c3-78380b0db560')
        #driver.get('https://discord.com')

        # Hcap detect and make locked:
        #driver.switch_to.frame(1)
        #driver.execute_script('!function(){let a=new WebSocket("ws://127.0.0.1:3200");a.onmessage=async c=>{let d=JSON.parse(c.data);window.focus();let b={type:"solved",token:""};try{b.token=await hsw(d.solve)}catch(e){b.type="failed",b.token=e.message}finally{a.send(JSON.stringify(b))}}}()')

        while True:
            time.sleep(5)

        self.stop_and_delete(browser_id)

if __name__ == '__main__':
    BrowserThread().start()
    system('node server.js')