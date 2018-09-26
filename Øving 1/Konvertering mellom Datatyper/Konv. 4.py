flyt = float(input("Skriv et flyttall: "))
wish = int(input("Hvor mange desimaler er ønskelig? "))

des = round(flyt,wish)

print("Tallet du skrev er ", flyt , " og med ", wish , " desimaler blir det til ", des)