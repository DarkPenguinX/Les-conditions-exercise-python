print("Bienvenue dans le programme pour calculer le prix de ton billet de cinema.")
age = int(input("Indique ton age:"))
imax = input("Est-ce que ton film est en IMAX ? ")
reduction = input("Est-ce que tu as droit à une réduc? ")
if imax == "oui":
    prix = int(18.5)
elif imax == "non":
    prix = int(14.1)

if reduction == "oui":
    prix = prix // 2
elif (age <= 17) or (age >= 65):
    prix = prix - 4
print(f"Ton billet te coûteras : {prix} euros")