import time
import random


for randint in range(0,100):
    print(random.randint(0,100))
    time.sleep(1)
    if randint == 34:
        print("İşlem Tamamlandi !")
        break