import flask
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import daten
import json
import kalorienrechner
# import sämtlicher Funktionalitäten und Dateien, die im main.py benötigt werden

app = Flask("meineapp")

# Hier wird die Startseite gerendert, von wo aus auf die anderen Funktionalitäten der Webapp gelinkt wird.
@app.route("/")
def startseite():
    return render_template("index.html")

# Unter diesem Route läuft die Speicherung der Nutzerdaten in das user_data.json
@app.route("/home/", methods=['GET', 'POST'])
def datenspeichern():
    # Die Daten des Webformulars auf home.html werden abgefangen und über die Funktion
    # personendaten_speichern als nested dictionary in user_data.json gespeichert wird.
    if request.method == 'POST':
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        key = f"{vorname} {nachname}" #hier wird der Key für das Dictionary in user_data.json erstellt
        geschlecht = request.form['geschlecht']
        alter = request.form['alter']
        aktivitaet = request.form['aktivitaet']
        groesse = request.form['groesse']
        gewicht = request.form['gewicht']
        daten.personendaten_speichern(key, vorname, nachname, geschlecht, alter, aktivitaet, groesse, gewicht)
        return flask.redirect("/kalorien/")
    # Hier wird definiert, dass nach erfolgreicher Eingabe eines Nutzers auf kalorien.html redirected werden soll.
    # Ohne Betätigung des Formulars wird die Seite home.html gerendert und dargestellt.
    else:
        return render_template("home.html")

# Hier wird das user_data.json ausgelesen und in eine Variable gespeichert. Die Keys werden als
# Nutzerdaten an kalorien.html weitergegeben, damit dort durch die Keys geloopt werden kann.
# Einige Variablen werden als leere Werte vordefiniert, da diese ansonsten nur innerhalb der if-condition "existieren".
@app.route("/kalorien/", methods=['GET', 'POST'])
def datensatz():
    with open("data/user_data.json", "r") as open_file:
        user_data = json.load(open_file)
        user = user_data.keys()
        person = "Null"
        kcal = 0
        menu = []
        # Innerhalb der if-condition wird der im kalorien.html ausgewählte Key als person abgefangen
        # Die entsprechenden Attribute zugehörig zum Key werden dann in Variablen gespeichert und an
        # die entsprechende Funktion weitergegeben. Das Ergebnis dieser Funktion ist in der Variable kcal gespeichert.
        if request.method == "POST":
            person = request.form["personen"]
            gewicht = int(user_data[person]["Gewicht"])
            groesse = int(user_data[person]["Grösse"])
            alter = int(user_data[person]["Alter"])
            aktivitaet = float(user_data[person]["Aktivität"])
            geschlecht = user_data[person]["Geschlecht"]
            kcal = kalorienrechner.kalorien(gewicht, groesse, alter, aktivitaet, geschlecht)
            # Die berechneten Kalorien aus der obigen Funktion werden an die Funktion menu_from_calories
            # weiter gegeben. Gespeichert in der Variable menu wird die entsprechende Info mitgeschickt.
            menu = kalorienrechner.menu_from_calories(kcal)
        return render_template("kalorien.html", nutzerdaten=user, person=person, kalorien=kcal, menu=menu)
    return render_template("kalorien.html")

# Unter diesem Route werden Gerichte in das rezepte.json geschrieben.
# Die Funktionalität ist praktisch gleich wie jene des oberen Routes zur Nutzerdatenerfassung.
# Unterschied: Hier wird nicht redirected, dafür aber ein Bestätigungssatz angezeigt, dass das
# Rezept erfolgreich gespeichert wurde.
@app.route("/rezepte/", methods=['GET', 'POST'])
def rezeptespeichern():
    if request.method == 'POST':
        name = request.form['name']
        key2 = f"{name}" #hier wird der Key für das Dictionary in rezepte.json erstellt
        kategorie = request.form['kategorie']
        typ = request.form['typ']
        kalorien = request.form['kalorien']
        daten.rezepte_speichern(key2, kategorie, typ, kalorien)
        bestaetigung = "Das Rezept " + name + " wurde erfolgreich gespeichert."
        return render_template("rezepte.html", bestaetigung=bestaetigung) #der Satz "bestaetigung" wird hier an das HTML Template weitergegeben
    return render_template("rezepte.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)