luku = 1
list1 = []
while luku != "":
    luku = input('Anna luku ')
    list1.append(luku)

list1.sort()
print("Suurin numero " + list1[-1])
print("Pienin numero " + list1[1])