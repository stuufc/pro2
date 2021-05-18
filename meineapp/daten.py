import json


def personendaten_speichern(key, vorname, nachname, geschlecht, alter, aktivitaet, groesse, gewicht):
    try:
        with open("data/user_data.json") as open_file:
            datei_inhalt = json.loads(open_file.read())
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = {"Vorname": vorname,
                         "Nachame": nachname,
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