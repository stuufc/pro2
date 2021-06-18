import json

# Die folgende Funktion wird im main.py benutzt um die Nutzerdaten in das
# user_data.json zu speichern.
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


# Gleiche Funktion wie oben, ausser dass hier die Rezepte in das rezepte.json gespeichert werden.
def rezepte_speichern(key2, kategorie, typ, kalorien):
    try:
        with open("data/rezepte.json") as open_file:
            rezepte_inhalt = json.loads(open_file.read())
    except FileNotFoundError:
        rezepte_inhalt = {}
#hier wird Key2 als String (definiert in main.py) und die Dict-Struktur definiert
    rezepte_inhalt[str(key2)] = {
                         "Kategorie": kategorie,
                         "Typ": typ,
                         "Kalorien": kalorien
                         }

    with open("data/rezepte.json", "w") as open_file:
        json.dump(rezepte_inhalt, open_file, indent=4)