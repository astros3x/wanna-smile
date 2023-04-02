import random
import string
import time

extension = ["pdf","txt","png","docx","xlsx","jpg","ini","pptx","dll","apk","mp4","zip","blend"]
length_ex = len(extension) - 1

while True:
    letters = string.ascii_letters
    name = "".join(random.choice(letters) for i in range(7))
    generate = random.randint(0,length_ex)
    total = f"file/{name}.{extension[generate]}"
    new = open(total,"w")
    new.write(name)
    new.close()
    time.sleep(0.3)
