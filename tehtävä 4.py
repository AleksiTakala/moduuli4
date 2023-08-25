import random

num = random.randint(1,10)
veik = 0
while veik != num:
    veik = float(input())
    if veik == num:
        print("oikein")
    elif veik < num:
        print("Liian pieni arvaus")
    elif veik > num:
        print("Liian  suuri arvaus")
    if(veik == num):
        break
