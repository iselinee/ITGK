import math

radius = float(input("Radius: "))
hoyde = float(input("Høyde: "))
omkrets = math.tau * radius
areal_sylinder = omkrets * hoyde + 2 * math.pi * radius ** 2
areal_sirkel = math.pi * radius ** 2

print("Har en sirkel med radius ", radius , "som er grunnflate i en sylinder med høyde", hoyde)
print("Omkrets av sirkelen:", round(omkrets,1))  # tau er det samme som 2 pi
print("Areal av sirkelen:", round(areal_sirkel,1))
print("Areal av sylinderen:", round(areal_sylinder,1))