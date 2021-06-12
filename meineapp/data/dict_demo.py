import json
import random

with open ("user_data.json", "r") as open_file:
    personendaten = json.load(open_file)
   
    
# for person in personendaten.values():
#     prename = person["Vorname"]
#     lastname = peron["Nachname"]
#     print(test)
    
    
# for person_key, value in personendaten.items():
#     print(float(value["Gewicht"])*5)
# 
# def personensuche(suche):
#     for person in personendaten.values():
#         test = person["Vorname"]
#         if suche in test:
#             print(person["Gewicht"])
# 
# suche = input("Wen suchen Sie? ")
#     
# personensuche(suche)

# for i in personendaten:
#     print(personendaten.get(i))
#     for m in personendaten.values():
#         print(personendaten.values())
    
# for k, v in personendaten.items():
#     print("Key " + str(k))
#     for x, y in v.items():
#         gewicht = personendaten[k]["Gewicht"]
#         groesse = personendaten[k]["Grösse"]
#         alter = personendaten[k]["Alter"]
#         aktivitaet = personendaten[k]["Aktivität"]
#         #print(x, "->", y)
#         print("Gewicht: ", gewicht, "Grösse: ", groesse, "Alter: ", alter, "Aktivität: ", aktivitaet)
#         
# print(personendaten["Stefan Banzer"]["Gewicht"])

# def kalorien(gewicht, groesse, alter, aktivitaet, geschlecht):
#     grundumsatz_mann = 66.47 + (13.7 * gewicht) + (5 * groesse) - (6.8 * alter)
#     grundumsatz_frau = 655.1 + (9.6 * gewicht) + (1.8 * groesse) - (4.7 * alter)
#     if geschlecht == "m":
#         erhaltungskalorien_mann = grundumsatz_mann * aktivitaet
#         return erhaltungskalorien_mann
#     elif geschlecht == "w":
#         erhaltungskalorien_frau = grundumsatz_frau * aktivitaet
#         return erhaltungskalorien_frau
#     return kalorien
#     
# kalorien(78, 176, 38, 1.7, 'm')
# print(str(kalorien))
#GUTER CODE UNTEN
# personendaten = list(personendaten)
# value = random.sample(personendaten, k=3)
# 
# print(value)
# 
# for person in personendaten:
#     for x, y in person.items():
#         print(x, "->", y)

# personen = random.sample(personendaten.keys(), k=10)
personen = personendaten.keys()
#value = list(personendaten[person]).values()
values = [personendaten[person] for person in personen]
for p, v in zip(personen, values):
    print(p, "->", v)
