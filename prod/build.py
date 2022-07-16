# To lazy to build all by hand lol

from distutils.dir_util import copy_tree
import os, shutil, re

def replace_content(path, content):
    with open(path, 'w') as file :
        file.truncate(0)
    
    with open(path, 'a') as file:
        file.write(content)

def obfuscate():
    os.system('pyarmor obfuscate --recursive ../src/main.py')

def pack_to_exe():
    os.system('pyinstaller --noconfirm --onefile --console --icon "./logo.ico" --name "DTG" --clean --add-data "./dist/security;security/" --add-data "./dist/pytransform;pytransform/" --add-data "./dist/modules;modules/" --hidden-import "psutil" --hidden-import "multiprocessing" --hidden-import "colorama" --hidden-import "httpx" --hidden-import "AuthGG" --hidden-import "toml" --hidden-import "imap_tools" --hidden-import "AuthGG.client" --hidden-import "websocket" --add-data "./dist/pytransform/_pytransform.dll;."  "./dist/main.py"')

def clear_files():
    os.mkdir('./DTG')
    os.mkdir('./DTG/src')
    shutil.move('./dist/DTG.exe', './DTG/src')
    
    for root, dirs, files in os.walk('./build', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    
    for root, dirs, files in os.walk('./dist', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    os.rmdir('./build')
    os.remove('DTG.spec')
    os.removedirs('./dist')

def copy_files():
    copy_tree('../script', './DTG/script')
    copy_tree('../config', './DTG/config')
    copy_tree('../data', './DTG/data')
    copy_tree('../solver', './DTG/src')
    
def replace_file_content():
    replace_content('./DTG/data/logs/logs.log', '')
    replace_content('./DTG/data/gen/mail_verified.txt', 'email:pass:token')
    replace_content('./DTG/data/gen/unverified.txt', 'token | warning, verified token will be in this file so somes can ve invalid because they are verified and the token have changed')
    replace_content('./DTG/data/usernames.txt', 'username1\nusername2\nusername3\n...')
    replace_content('./DTG/config/auth.key', 'user:pass:email:license-key')
    replace_content('./DTG/data/proxies.txt', 'ip:port\nuser:pass@ip:port')
    replace_content('./DTG/script/run.bat', '@echo off\ncd ../src/\nDTG.exe\npause')
    replace_content('./DTG/script/solver.bat', '@echo off\ncd ../src/\nnode index.js\npause')

    c = None
    with open ('./DTG/config/config.toml', 'r') as f:
        content = f.read()
        c = re.sub('"[a-zA-Z]+"', '""', content, flags = re.M)

    with open ('./DTG/config/config.toml', 'w+') as f:
        f.truncate(0)
        f.write(c)

def zip():
    shutil.make_archive("DTG-Prod", 'zip', "./DTG")

    for root, dirs, files in os.walk('./DTG', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.removedirs('./DTG')

if __name__ == '__main__':
    obfuscate()
    pack_to_exe()
    clear_files()
    copy_files()
    replace_file_content()

    os.system('node ./obfuscate_solver.js')

    zip()