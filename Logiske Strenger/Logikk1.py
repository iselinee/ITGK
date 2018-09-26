# 1. True
# 2. False
# 3. True
# 4. False
# 5. True

#b.

print("Gi inn a og b, begge heltall i intervall <40,50> eller <70,90>:")
a = int(input("Verdi for a: "))
b = int(input("Verdi for b: "))


if ((a > 70 and a << 90) or ((a > 40 and not a >= 50) and (70 < b < 90) or (b > 40 and b < 50))):
    print("Tallene er begge i gyldige intervall ^u^")
else:
    print("Minst ett av tallene er utenfor et gyldig intervall :(")


#c.

print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
p = int(input("Hvor mange pannekaker ønsker du? "))

if ( 0 > p or p > 10):
    print("Beklager, men det er nok ikke mulig")
else:
    r = 10 - p
    print("Da blir det", p, "på deg og", r, "på meg :D")