navn = input("Skriv ditt navn: ")
alder = int(input("Hei, " + navn + ", hvor gammel er du? "))
prog = int(input("Hvor gammel var du da du begynte å programmere? "))

kodeAar = str(alder - prog)
print("Da har du programmert i ",kodeAar, "år")

gøy = str(input("Synes du de " + kodeAar + " årene har vært gøy? "))
print("Takk for svar, ",navn, "!")

