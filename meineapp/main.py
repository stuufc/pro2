import flask
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import daten
import json
import kalorienrechner
#import preise

app = Flask("meineapp")

def personendaten_laden():
    with open("data/user_data.json") as open_file:
        personendaten = json.load(open_file)
        return personendaten

#@app.route("/hello")
#def home():
    #return render_template('index.html', name="Stefan")

@app.route("/hello/")
@app.route("/hello/<name>") #dynamischer URL wird erstellt, gibt Namen zurück.
def begruessung(name="Wörld"):
    return render_template("index.html", name=name)

@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_login = request.form['login_name']
        #rueckgabe_string = "Hello " + user_login + "!"
        return render_template("login.html", login=user_login)
    else:
        return render_template("login.html")

@app.route("/home/", methods=['GET', 'POST'])
def datenspeichern():
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
    else:
        return render_template("home.html")


@app.route("/kalorien/", methods=['GET', 'POST'])
def datensatz():
    with open("data/user_data.json", "r") as open_file:
        user_data = json.load(open_file)
        user = user_data.keys()
        person = "Null"
        kcal = 0
        if request.method == "POST":
            person = request.form["personen"]
            gewicht = int(user_data[person]["Gewicht"])
            groesse = int(user_data[person]["Grösse"])
            alter = int(user_data[person]["Alter"])
            aktivitaet = float(user_data[person]["Aktivität"])
            geschlecht = user_data[person]["Geschlecht"]
            kcal = kalorienrechner.kalorien(gewicht, groesse, alter, aktivitaet, geschlecht)
        return render_template("kalorien.html", nutzerdaten=user, person=person, kalorien=kcal)
    #personendaten = personendaten_laden()
    return render_template("kalorien.html")

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

@app.route("/registration/")
def registration():
    return render_template("footer.html")

@app.route("/tescht/", methods=['GET', 'POST'])
def testsachen():
    return render_template('kalorien.html')

@app.route("/about")
def about():
    return render_template('header.html')


#from preise import rabatt_berechnen => kann so z.B. Funktionen etc. aus anderen Dateien importieren
"""@app.route("/rabatt/<preis>")
def rabatt(preis):
    preis_mit_rabatt = preis.rabatt(int(preis))

    return "Der neue Preis ist: " + str(preis_mit_rabatt)"""

"""@app.route("/gutschein/<preis>/<gutschein>")
def gutschein(preis, gutschein):
    preis_mit_rabatt = gutscheine.rabatt(preis, gutschein)

    return "Der neue Preis mit Gutschein ist: " + str(preis_mit_rabatt)"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)