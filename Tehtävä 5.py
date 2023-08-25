i = 0
while i < 5:
    tunnus = input('Anna käyttäjä tunnus: ')
    salasana = input('Anna salasana: ')

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        i = i +1

    if i == 5:
        print("Pääsy evätty")

