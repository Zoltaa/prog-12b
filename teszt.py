szamok=[]
atlag=0.0

for i in range (5):
    szamok.append(int(input("Kérek számot: ")))

for szam in szamok:
    atlag += szam
atlag = atlag / len(szamok)
    
print(f"Átlag: {atlag}")