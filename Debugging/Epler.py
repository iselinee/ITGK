print("Dette er et program for å teste din sjenerøsitet.")

har_epler = int(input("Hvor mange epler har du? "))


if har_epler <= 0:
    print("Æsj, det sier du bare for å slippe å gi noe!")

else :
    gir_epler = int(input("Hvor mange kan du gi til meg? "))
    if gir_epler < har_epler / 2 :
        print("Du beholder det meste for deg selv...")
    else:
        print("Takk, det var snilt!")

        # Oppgave B, gramatisk korrekt
        if(har_epler - gir_epler == 1):
            print("Du har nå", har_epler - gir_epler, "eple igjen.")

        elif(har_epler - gir_epler) < 0:
            print("Du har nå 0 epler igjen. Gi meg de", abs(har_epler - gir_epler), "neste gang vi møtes.")

        else:
            print("Du har nå", har_epler - gir_epler, "epler igjen.")