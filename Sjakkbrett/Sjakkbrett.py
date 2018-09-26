pos = input("Tast inn posisjon: ").lower()
bokstav = pos[0]
tall = int(pos[1])

if(len(pos) == 2):
    if(((bokstav == "a") or (bokstav == "c") or (bokstav == "e") or (bokstav == "g") or (bokstav == "b") or (bokstav == "d") or (bokstav == "f") or (bokstav == "h")) and (0 < tall < 9)):
        if ((bokstav == "a") or (bokstav == "c") or (bokstav == "e") or (bokstav == "g")):
            if((tall == 1) or (tall == 3) or (tall == 5) or (tall == 7)):
                print("Svart")
            else:
                print("Hvit")
        else:
            if((tall == 1) or (tall == 3) or (tall == 5) or (tall == 7)):
                print("Hvit")
            else:
                print("Svart")
    else:
        print("Feil input.\n Første tegn må være en bokstav mellom A-H eller a-h\n Andre tegn må være et tall mellom 1-8")
else:
    print("Feil input. Du må skrive akkurat to tegn...")