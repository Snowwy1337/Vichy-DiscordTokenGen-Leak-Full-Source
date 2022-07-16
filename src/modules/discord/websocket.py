import threading, websocket, json, time, toml
from ..utils.browser import Firefox, Chrome
from ..utils.console import Console

__config__ = toml.loads(open('../config/config.toml', 'r+').read())

class DiscordWs(threading.Thread):
    def __init__(self, acc_token: str):
        self.token = acc_token
        self.running = True
        self.ws = websocket.WebSocket()
        threading.Thread.__init__(self)

    def send_payload(self, payload: dict):
        self.ws.send(json.dumps(payload))

    def recieve(self):
        data = self.ws.recv()

        if data:
            return json.loads(data)

    def heartbeat(self, interval: float):
        while self.running:
            time.sleep(interval)
            self.send_payload({
                'op': 1,
                'd': None
            })
            Console.debug(f'(*) Heartbeat sent: {self.token}')

    def login(self):
        self.ws.connect('wss://gateway.discord.gg/?encoding=json&v=9')
        interval = self.recieve()['d']['heartbeat_interval'] / 1000
        threading.Thread(target=self.heartbeat, args=(interval,)).start()

    def online(self):
        self.send_payload({
            "op": 2,
            "d": {
                "token": self.token,
                "capabilities": 125,
                "properties": Firefox.super_properties(False, False) if __config__['browser']['browser_id'] == 1 else Chrome.super_properties(False, False),
                "presence": {
                    "status": "online",
                    "since": 0,
                    "activities": [
                        {
                            "name": "Custom Status",
                            "type": 4,
                            "state": "DTG V1",
                            "emoji": None
                        }
                    ],
                    "afk": False
                },
                "compress": False,
                "client_state": {
                    "guild_hashes": {},
                    "highest_last_message_id": "0",
                    "read_state_version": 0,
                    "user_guild_settings_version": -1,
                    "user_settings_version": -1
                }
            }
        })
        Console.debug(f'(*) Websocket online: {self.token}')

    def run(self):
        self.login()
        self.online()
        time.sleep(30)
        self.running = False