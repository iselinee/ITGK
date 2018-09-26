print("Vennligst gi inn et flyttall med minst 5 siffer både før og etter .")

tall1 = float(input("Hva er tallet ditt? "))

konv1 = int(tall1)
avrund = round(tall1)
avrund1 = round(tall1,2)
avrund2 = round(tall1,4)
avrund3 = round(konv1,-3)
konv2 = float(konv1)


print("Konvertert til helttall med int(): ", konv1)

print("Avrundet til nærmeste helttall: ", avrund)
print("Avrundet til 2 desimaler: ", avrund1)
print("Avrundet til 4 desimaler: ", avrund2)
print("Avrundet til nærmeste tusen: ", avrund3)
print("Heltall fra int() konvertert tilbake til flyttall: ", konv2)
