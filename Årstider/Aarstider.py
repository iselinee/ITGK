# Lager et program som ut i fra dato, kan gi svar på hvilken aarstid det er

# Lager input for ønskelig dag og mnd
mnd = str(input("Måned: ")).lower()
dag = int(input("Dag: "))


# Lager en if-setning for vår, da den varer fra 20.mars til 20.juni
if ((mnd == "mars" and dag >= 20) or (mnd == "april") or (mnd == "mai") or (mnd == "juni" and dag < 21)):
    print("Vår")

# Lager samme for sommer, 21. juni til 21.september
elif ((mnd == "juni" and dag >= 21) or (mnd == "juli") or (mnd == "august") or (mnd == "september" and dag < 22)):
    print("Sommer")

# Lager samme for høst, 22. september til 20. desember
elif ((mnd == "september" and dag >= 22) or (mnd == "oktober") or (mnd == "november") or (mnd == "desember" and dag < 21)):
    print("Høst")

# Til slutt er vinteren fra 21.desember til 19.mars
elif ((mnd == "desember" and dag >= 21) or (mnd == "januar") or (mnd == "februar") or (mnd == "mars" and dag < 20)):
    print("Vinter")

# hvis du skriver noe annet enn de 12 mnd
else:
    print("Wrong input")