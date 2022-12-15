from math import sin, cos, tan, degrees, radians, asin, pi, sqrt, acos
#Body:
# O - počáteční bod
# B - Cíl
# C - Bod kam musíme směřovat abychom doletěli do B (cíle)

#Úhly:
# Všechny úhly se vztahují k přímce N (sever) která definuje 0 stupňů
# W - Úhel ze kterého vane vítr
# KZ - Kurz (úhel pod kterým musíme letět abychom dorazili do cíle B)
# TU - Traťový úhel (úhel kde se od nás (N) nachází cíl B)
# US - Úhel snosu (rozdíl úhlů TU a KZ)
# E - Úhel, který svírají prodloužená TR a vítr
# E s čarou - Úhel vypočítaný jako 180 - E
# F - Úhel trojúhelníku, který svýrá PVR a vítr
# UV - Úhel pod kterým vítr fouká na trať

#Délky a síly:
# PVR - Pravá vzdušná rychlost (Vzdálenost mezi námi O a C / rychlost letadla)
# TR - Traťová rychlost (Rychlost jak se pohybujeme po přímé trati z O k B)
# V - Rychlost větru
# S - Vzdálenost od nás O do cíle B

#Čas:
# t - Doba než letadlo doletí do cíle B

print ("Co znáš? Vše uváděj v základních jednotkách a kurzy jako úhly (kurz 080 jako 80).")
print ("W - Úhel ze kterého vane vítr")
print ("PVR - Pravá vzdušná rychlost (Vzdálenost mezi námi O a C / rychlost letadla)")
print ("TU - Traťový úhel (úhel/kurz kde se od nás (N) nachází cíl B)")
print ("V - Rychlost větru")
print ("S - Rychlost letounu")
print ("KZ - Kurz (úhel) pod kterým letět abychom dorazili do cíle):")
print ("TR - Traťová rychlost (rychlost jak se pohybujeme po přímé trati z O k B):")

odpoved = str(input("Piš jen výše uvedené zkratky a dělej mezi nimi pomlčky a podle pořadí výše např. PVR-TU-V. "))

if odpoved == "PVR-TU-KZ-TR":
    PVR = int(input("Zadej PVR = "))
    TU = int(input("Zadej TU = "))
    KZ = int(input("Zadej KZ = "))
    TR = int(input("Zadej TR = "))

    US = TU - KZ
    print ("Úhel snosu je",US,"°")

    USr = US * (pi/180)
    V = sqrt(PVR**2 + TR**2 - (2*PVR*TR*cos(USr)))
    print ("Rychlost větru je",V,"kilometrů v hodině.")

    KZr = KZ * (pi/180)
    EsCarourA = (V**2 + TR**2 - PVR**2) / (2 * V * TR)
    EsCarour = cos(EsCarourA)
    EsCarou = degrees(EsCarour)
    print ("Úhel E s čarou je", EsCarou, "°")
    F = 180 - EsCarou - US
    print ("Úhel F je", F, "°")
    UV = F - KZ
    print ("Úhel pod kterým vítr fouká na trať je",UV,"°")

    W = 360 - UV
    print ("Úhel ze kterého vane vítr je",W,"°")

elif odpoved == "W-PVR-TU-V-S":
    W = int(input("Zadej W = "))
    PVR = int(input("Zadej PVR = "))
    TU = int(input("Zadej TU = "))
    V = int(input("Zadej V = "))
    S = int(input("Zadej S = "))

    UV = 90 - (TU-90) + W
    print ("Vítr fouká na trať pod úhlem", UV, "°")

    UVr = UV *  (pi/180)
    USr = asin((V/PVR)*sin(UVr))
    US = degrees(USr)
    print ("Úhel snosu US je", US, "°")

    TUr = TU * (pi/180)
    KZr = TUr - USr
    KZ = degrees(KZr)
    print ("Kurz je ",KZ,"°")

    Wr = W * (pi/180)
    KZrminusWr = KZr - Wr
    TR = (PVR/sin(UVr)) * sin(abs(KZrminusWr))
    print ("Traťová rychlost je ",TR," km/h.")

    th = (S/TR)
    tm = (S/TR)*60
    print ("Doba doletu do cíle je",th," hodin respektive",tm,"minut.")


elif odpoved == "W-PVR-TU-V":
    W = int(input("Zadej W = "))
    PVR = int(input("Zadej PVR = "))
    TU = int(input("Zadej TU = "))
    V = int(input("Zadej V = "))
    S = 1

    UV = 90 - (TU-90) + W
    print ("Vítr fouká na trať pod úhlem", UV, "°")

    UVr = UV *  (pi/180)
    USr = asin((V/PVR)*sin(UVr))
    US = degrees(USr)
    print ("Úhel snosu US je", US, "°")

    TUr = TU * (pi/180)
    KZr = TUr - USr
    KZ = degrees(KZr)
    print ("Kurz je ",KZ,"°")

    Wr = W * (pi/180)
    KZrminusWr = KZr - Wr
    TR = (PVR/sin(UVr)) * sin(abs(KZrminusWr))
    print ("Traťová rychlost je ",TR," km/h.")

    th = (S/TR)
    tm = (S/TR)*60
    print ("Doba doletu do cíle je",th," hodin respektive",tm,"minut.")

else:
    print ("Zadal jsi špatné údaje.")
