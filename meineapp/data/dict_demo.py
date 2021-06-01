import json

with open ("user_data.json", "r") as open_file:
    personendaten = json.load(open_file)
   
    
# for person in personendaten.values():
#     prename = person["Vorname"]
#     lastname = peron["Nachname"]
#     print(test)
    
    
for person_key, value in personendaten.items():
    print(float(value["Gewicht"])*5)

def personensuche(suche):
    for person in personendaten.values():
        test = person["Vorname"]
        if suche in test:
            print(person["Gewicht"])

suche = input("Wen suchen Sie? ")
    
personensuche(suche)