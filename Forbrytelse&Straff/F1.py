# leser inn data
prom = float(input("Hvor stor var promillen? "))
motor = input("Var farkosten en motorvogn? (j/n) ").lower()
f = input("Var personen forer av vognen? (j/n) ").lower()
leds = input("Var personen ledsager ved ovekjoring? (j/n) ").lower()
n = input("Var det nodrett? (j/n) ").lower()

# vurderer straffbarhet
if prom > 0.2 and motor == "j" and f == "j" or leds == "j" and n == "n":
    print("Det var straffbar promillekjoring.")
else:
    print("Ikke straffbart, ingen bot.")
