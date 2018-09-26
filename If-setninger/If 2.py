epler = int(input("Hvor mange epler har du? "))
barn = int(input("Hvor mange barn passer du på? "))

if epler > 0:
    print("Da blir det", epler//barn , "epler til hvert barn, \nog", epler%barn, "epler til overs til deg selv.")

print("Takk for i dag!")