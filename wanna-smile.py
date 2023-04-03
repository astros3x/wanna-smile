#Created by 2Loop & CaptainBeluga
import random
import os
from os.path import expanduser

files = []

desk = expanduser('~/Desktop')
extensions_list = ['pdf','txt','png','docx','xlsx','jpg','ini','pptx','dll','apk','mp4','zip','exe','mp3','dat','vbs','lnk','ogg','stl','fbx','iso','bat','cfg','md','dds','js','jpeg','png','html','css']
names_list = ['astri', 'beluga', 'XDDDD', '6969', 'fucked', 'imagine', 'defalt','watch-dogs','fortnite','vbuck-kid','scammer','pwned']


def generate():
    name = random.choice(extensions_list)
    extension = random.choice(names_list)

    result = f'{extension}.{name}'

    return result

while True:

    result = generate()

    if(result not in files):

        os.system(f"echo '' > {desk}/{result}")

        files.append(result)

        print(f'[+] File generated > {result}')

    else:
        print(f"[+] {result} already added :) ... generating another....")