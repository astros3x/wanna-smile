#Created by 2Loop & CaptainBeluga
import random
import os

names_list = ["astri", "beluga", "XDDDD", "6969", "Fucked", "fuck","Immagine","kill-me","gaio","troll","pwned","5006","you-suck"]
extensions_list = ['pdf','txt','png',"docx","xlsx","jpg","ini","pptx","dll","apk","mp4","zip","blend","exe","iso","mp3"]

while True:
    name = random.choice(names_list)
    extension = random.choice(extensions_list)

    result = f"{name}.{extension}"

    os.system(f"echo "" > {result}")

    new = open(result,'w')
    new.write(name)
    new.close()

    print(f"[+] File generated: {result}")