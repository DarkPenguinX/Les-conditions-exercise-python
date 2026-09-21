print("Bienvenue dans le programme pour calculer les prix de ton billet de cinéma")
print("Indique ton age")
age=int(input())
if 17>=age>=65:
    billet=(14.10-4)
else:
    billet=14.10
print("Est ce que ton film est en IMAX?")
IMAX=input()
if IMAX=="oui" :
    billet=billet+4.40
else:
    billet=14.10
print("Est ce que tu as droit a une réduc?")
réduc= input()	
if réduc=="oui":
    billet=billet/50
else:
    billet=14.10
    print(f"Le prix de ton billet est {billet}")

    

