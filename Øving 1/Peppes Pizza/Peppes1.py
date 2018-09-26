pizza = 750
studentrabatt = 0.20
tips = 0.08

totalt = (pizza * (1-studentrabatt) + (pizza*tips))

print("Total pris: ", totalt)
deltok = int(input("Hvor mange deltok på middagen? "))
each = float(totalt / deltok)

print("Ettersom dere var ", deltok , " personer, så må hver person betale ", each , " kr.")

