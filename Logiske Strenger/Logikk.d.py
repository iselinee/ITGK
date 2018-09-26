print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
p = int(input("Hvor mange pannekaker ønsker du? "))
s = input("Er du glad i pannekaker? (j/n) ").lower()

if s == 'j':
    elsker_pannekaker = True
else:
    elsker_pannekaker = False

if ((0 > p or p > 10) or s != 'j'):
    print("Beklager, men det er nok ikke mulig")
else:
    r = 10-p
    print("Da blir det",p,"på deg og",r,"på meg :D")