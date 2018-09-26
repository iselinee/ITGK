dag = int(input("Dager til du skal reise: "))
fullpris = int(440)
discB = int(fullpris/2)
discS = int(fullpris * 0.75)


if (dag <= 14):
    print("Du kan få minipris: 199,-")
    print("Minipris 199,- kan ikke refunderes/endres")

    ref = input("Ønskes dette? (J/N)").lower()

    if ref == "n":
        print("Takk for pengene, god reise!")
    else:
        print("Da tilbyr vi fullpris: 440,-")

else:
    print("Det er for sent for minipris; fullpris: 440,-")
    alder = int(input("Skriv inn din alder: "))
    if alder <= 16:
        print("Prisen på din billett blir", discB)

    elif alder >= 60:
        print("Prisen på din billett blir", discS)

    elif alder >= 18:
        srab = input("Er du militær/student? (J/N) ").lower()
        if (srab == "j") and (alder <= 60):
            print("Prisen på din billett blir", discS)
        else:
            print("Prisen blir 440")