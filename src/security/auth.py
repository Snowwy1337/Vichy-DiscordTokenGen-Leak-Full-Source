from modules.utils.console import Console
from AuthGG.client import Client
import sys, time, toml

__key__, __config__ = open('../config/auth.key', 'r+').read().split(':'), toml.loads(open('../config/config.toml', 'r+').read())

class Auth:
    def __init__(self):
        self.__client = Client(api_key= "xxxx", aid= "xxxx", application_secret= "xxxxx")

    def __check_key(self):
        if len(__key__) != 4:
            Console.printF('(-) Please add your key in auth.key file, format: username:password:email:licence-key.')
            return False
        else:
            return True

    def __loggin(self):
        try:
            self.__client.login(__key__[0], __key__[1])
            return True
        except Exception as e:
            Console.debug(e)
            return False
    
    def __register(self):
        try:
            self.__client.register(__key__[3], __key__[2], __key__[0], __key__[1])
            return True
        except Exception as e:
            Console.debug(e)
            return False
    
    def __animation(self):
        idx = 0
        for _ in range(4):
            print("--> Loading " + idx * '.', end="\r")
            idx += 1
            time.sleep(1)

    def log(self):
        logged = False

        if self.__check_key():
            if self.__loggin():
                Console.printF(f'(+) Welcome back, {__key__[0]}')
                logged = True
            else:
                if self.__register():
                    Console.printF(f'(+) You have been successfully registered as {__key__[0]}')

                    if self.__loggin():
                        Console.printF(f'(+) Welcome {__key__[0]}')
                        logged= True
                else:
                    Console.printF(f'(-) Failed to register your account, please check your key in auth.key file, format: username:password:email:licence-key or buy one.')
        
        if not logged:
            sys.exit(0)
        else:
            if not __config__['console']['skip_login_animation']:
                self.__animation()