import re
import datetime

recepty = "pivo, lezaks"
obchod_inv_cesta = "Sem zadejte cestu k souboru inventáře obchodu"
ja_inv_cesta = "Sem zadejte cestu k souboru vašeho inventáře"

ja_obchod = int(input("Muj inv nebo v obchodě? (1/2)  "))

if ja_obchod == 1:
    with open(ja_inv_cesta, "r") as file:
        jainv = file.readlines()
    print(jainv)
elif ja_obchod == 2:
    with open(obchod_inv_cesta, "r") as file:
        obchodinv = file.readlines()
    print(obchodinv)

zapis = int(input("Kemě nebo odemě do obchodu nebo z obchodu? (1/2/3)"))

jmeno = "Krasnaya Zavodskaya Destilerka"
datum = datetime.date.today()

if zapis == 1:
    with open(ja_inv_cesta, "r") as file:
        jainv = file.readlines()
    kdo_co = input(f"Co se poslalo do obchodu? ({recepty})  ")
    kolik = int(input("Kolik?  "))
    for i, line in enumerate(jainv):
        if kdo_co in line:
            hodnota = int(re.findall(r'\d+', line)[0])
            nova_hodnota = hodnota + kolik
            jainv[i] = f"{kdo_co} = {nova_hodnota}\n"
            break
    # Uložení změněných dat zpět do souboru
    with open(ja_inv_cesta, "w") as file:
        file.writelines(jainv)
elif zapis == 2:
    with open(ja_inv_cesta, "r") as file:
        jainv = file.readlines()
    with open(obchod_inv_cesta, "r") as file:
        obchodinv = file.readlines()
    kdo_co = input(f"Co se dalo odemě do obchodu? ({recepty})  ")
    kolik = int(input("Kolik?  "))
    for i, line in enumerate(jainv):
        if kdo_co in line:
            hodnota = int(re.findall(r'\d+', line)[0])
            nova_hodnota1 = hodnota - kolik
            jainv[i] = f"{kdo_co} = {nova_hodnota1}\n"
            break
    for i, line in enumerate(obchodinv):
        if kdo_co in line:
            hodnota = int(re.findall(r'\d+', line)[0])
            nova_hodnota2 = hodnota + kolik
            obchodinv[i] = f"{kdo_co} = {nova_hodnota2}\n"
            break
    print("")
    print("-------------------------------------------")
    print(f"Faktura ({jmeno})")
    print(f"Odesílám zboží ({kolik}) ({kdo_co})")
    print(f"Celkem v obchodě zboží ({nova_hodnota2})")
    print(f"Datum ({datum})")
    print("-------------------------------------------")
    # Uložení změněných dat zpět do souboru
    with open(ja_inv_cesta, "w") as file:
        file.writelines(jainv)
    # Uložení změněných dat zpět do souboru
    with open(obchod_inv_cesta, "w") as file:
        file.writelines(obchodinv)
elif zapis == 3:
    with open(obchod_inv_cesta, "r") as file:
        obchodinv = file.readlines()
    kdo_co = input(f"Co se prodalo z obchodu? ({recepty})  ")
    kolik = int(input("Kolik?  "))
    for i, line in enumerate(obchodinv):
        if kdo_co in line:
            hodnota = int(re.findall(r'\d+', line)[0])
            nova_hodnota = hodnota - kolik
            obchodinv[i] = f"{kdo_co} = {nova_hodnota}\n"
            break
    # Uložení změněných dat zpět do souboru
    with open(obchod_inv_cesta, "w") as file:
        file.writelines(obchodinv)

input("kliknutim zavres")
