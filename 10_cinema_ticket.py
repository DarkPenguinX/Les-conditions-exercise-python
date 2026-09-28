print("Bienvenue dans le programme pour calculer les prix de ton billet de cinéma")
print("Indique ton age")
age=int(input())
if int(age) <=17 or age<=65:
    billet=(10.10)
else:
    billet=14.10
print("Est ce que ton film est en IMAX?")
IMAX=input()
if IMAX=="oui" :
    billet1 = billet+4.40
elif IMAX=="non":
        billet1 = billet
print("Est ce que tu as droit a une réduc?")
billet2=billet2
réduc= input()	
if réduc=="oui":
    billet2 = billet1//2
elif réduc == "non":
    billet2 = 14.10
print(f"Le prix de ton billet est {billet2}")

    

