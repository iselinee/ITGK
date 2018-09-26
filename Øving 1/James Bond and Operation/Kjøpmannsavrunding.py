desi = float(input("Gi et desimaltall: "))
kutt = int(input("Antall desimaler til avrunding: "))

faktor = 10 ** kutt
resultat = int(tall * faktor + 0.5)
print("Avrundet til", d, "desimaler: ", resultat)

if kutt <= 0: #Skal ende med helttall
    resultat = int(resultat)
print("Avrundet til", kutt, "desimaler:", resultat)







