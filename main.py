#Created by 2Loop & CaptainBeluga
import random
import os
from os.path import expanduser

desk = expanduser('~/Desktop')
extensions_list = ['pdf','txt','png','docx','xlsx','jpg','ini','pptx','dll','apk','mp4','zip','blend']
names_list = ['astri', 'beluga', 'XDDDD', '6969', 'Fucked', 'Imagine']

while True:
    name = random.choice(extensions_list)
    extension = random.choice(names_list)

    result = f'{extension}.{name}'

    os.system(f"echo '' > {desk}/{result}")

    print(f'[+] File generated > {result}')