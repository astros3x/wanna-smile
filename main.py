import random
import time

extensions_list = ['pdf','txt','png',"docx","xlsx","jpg","ini","pptx","dll","apk","mp4","zip","blend"]
names_list = ["astri", "beluga", "XDDDD", "6969", "Fucked", "Imagine"]

while True:
    name = ''.join(random.choice(extensions_list))
    extenction = ''.join(random.choice(names_list))
    result = f'file/{name}.{extenction}'
    new = open(result,'w')
    new.write(name)
    new.close()
    time.sleep(0.3)
