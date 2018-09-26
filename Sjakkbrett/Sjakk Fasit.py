pos = input("Posisjon:")
if len(pos) == 2:
    ch = pos[0]
    if ('A' <= ch <='H' or 'a' <= ch 'h') and '1' <= pos[1] <= '8':
        #input OK
        tall = int(pos[1])
        if (ord(ch) + tall) % 2 == 0:
            print("Svart")
        else:
            print("Hvit")
    else:
        print("Feil input.")
        print("Første tegn må være en bokstav mellom A-H eller a-h")
        print("Andre tegn må være et tall mellom 1-8")
else:
    print("Feil lengde på input, skal være 2 tegn.")