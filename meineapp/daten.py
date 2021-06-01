import json


def personendaten_speichern(key, vorname, nachname, geschlecht, alter, aktivitaet, groesse, gewicht):
    try:
        with open("data/user_data.json") as open_file:
            datei_inhalt = json.loads(open_file.read())
    except FileNotFoundError:
        datei_inhalt = {}
#hier wird Key als String (definiert in main.py) und die Dict-Struktur definiert
    datei_inhalt[str(key)] = {
                         "Geschlecht": geschlecht,
                         "Alter": alter,
                         "Aktivität": aktivitaet,
                         "Grösse": groesse,
                         "Gewicht": gewicht
                         }

    with open("data/user_data.json", "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

def load():
    file = "data/user_data.json"
    try:
        with open(file) as open_file:
            datei_inhalt = json.loads(open_file.read())
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt

"""def save_file(file, key, name, surname, position, team, age, height, season):
    try:
        with open(file) as open_file:
            content = json.load(open_file)
    except FileNotFoundError:
        content = {}"""

def rezepte_speichern(key2, kategorie, typ, kalorien):
    try:
        with open("data/rezepte.json") as open_file:
            rezepte_inhalt = json.loads(open_file.read())
    except FileNotFoundError:
        rezepte_inhalt = {}
#hier wird Key als String (definiert in main.py) und die Dict-Struktur definiert
    rezepte_inhalt[str(key2)] = {
                         "Kategorie": kategorie,
                         "Typ": typ,
                         "Kalorien": kalorien
                         }

    with open("data/rezepte.json", "w") as open_file:
        json.dump(rezepte_inhalt, open_file, indent=4)