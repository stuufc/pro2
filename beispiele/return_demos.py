"""def xprint(satz, anzahl):
    viele_saetze = satz * anzahl
    return viele_saetze

satz = "Hello World!"

ergebins_der_funktion = xprint(satz, 3)

noch_ein_ergebnis = xprint(ergebins_der_funktion, 5)
print(noch_ein_ergebnis)"""

def gerade(zahl_1=1):
    if zahl_1 % 2 == 0:
        return str(zahl_1) + " ist gerade"
    else:
        return str(zahl_1) + " ist ungerade"

erste_zahl = 5

ergebnis = gerade(erste_zahl)
print(ergebnis)


