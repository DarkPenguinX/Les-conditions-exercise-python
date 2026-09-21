print("hello, in wich year were you born?")
year= int(input())
age= 2026-year
print(f"A la fin de l'anée 2026 tu auras",{age})
if int(age<12):
    print("tu es un enfant")
elif 17>age>12:
    print("Tu es un adolecent")
else:
    print("Tu es un adulte")