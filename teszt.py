szamok=[]
atlag=0.0

for i in range (5):
    szamok.append(int(input("Kérek számot: ")))

for szam in szamok:
    atlag += szam
atlag = atlag / len(szamok)
    
print(f"Átlag: {atlag}")

i = 0
while i < len(szamok) and szamok[i] % 2 != 0:
    i += 1

if i < len(szamok):
    print("Van páros szám!")
else:
    print("Nincs páros szám!")
