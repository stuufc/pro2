import json

with open ("data/user_data.json", "r") as open_file:
    personendaten = json.load(open_file)
    print(personendaten)

for person in personendaten:
    print(person)


def kalorien_mann(gewicht, groesse, alter, aktivitaet):
    grundumsatz_mann = 66.47 + (13.7 * gewicht) + (5 * groesse) - (6.8 * alter)
    erhaltungskal_mann = grundumsatz_mann * aktivitaet
    return erhaltungskal_mann

def kalorien_frau(gewicht, groesse, alter, aktivitaet):
    grundumsatz_frau = 655.1 + (9.6 * gewicht) + (1.8 * groesse) - (4.7 * alter)
    erhaltungskal_frau = grundumsatz_frau + aktivitaet
    return erhaltungskal_frau

def kalorien(gewicht, groesse, alter, aktivitaet, geschlecht):
    grundumsatz_mann = 66.47 + (13.7 * gewicht) + (5 * groesse) - (6.8 * alter)
    grundumsatz_frau = 65.51 + (9.6 * gewicht) + (1.8 * groesse) - (4.7 * alter)
    if geschlecht == "m":
        erhaltungskalorien = grundumsatz_mann * aktivitaet
    else:
        erhaltungskalorien = grundumsatz_frau * aktivitaet
    return erhaltungskalorien


"""
Grundumsatz:
Mann: Grundumsatz= 66,47 + (13,7 x Körpergewicht [kg]) + (5 x Körpergröße [cm]) – (6,8 x Alter [Jahre])
Frau: Grundumsatz= 655,1 + (9,6 x Körpergewicht [kg]) + (1,8 x Körpergröße [cm]) – (4,7 x Alter [Jahre])

Erhaltungskalorien = Grundumsatz x PAL-Wert

PAL-Index:
1 - ausschliesslicht sitzende/liegende Aktivität: 1,2
2 - aussschliesslich sitzende Tätigkeiten (Bürojob) mit wenig körperlicher Aktivität in der Freizeit: 1,4 - 1,5
3 - überwiegend sitzende Tätigkeit. Z.T. gehende oder stehend mit moderatem Sportpensum in der Freizeit: 1,6 - 1,7
4 - überwiegend gehende/stehende Tätigkeit und moderates Sportpensum 1.8 - 1.9
5 - körperlich anstrengender Beruf mit zusätzlich viel Aktivitäten in der Freizeit 2.0-2.4

Quelle: https://smartgains.de/kalorien-berechnen/
"""