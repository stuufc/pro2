from flask import Flask
from flask import render_template
from flask import request
import daten
import kalorienrechner
#import preise

app = Flask("meineapp")

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
        key = f"{vorname} {nachname}"
        geschlecht = request.form['geschlecht']
        alter = request.form['alter']
        aktivitaet = request.form['aktivitaet']
        groesse = request.form['groesse']
        gewicht = request.form['gewicht']
        daten.personendaten_speichern(key, vorname, nachname, geschlecht, alter, aktivitaet, groesse, gewicht)
        return "test erfolgreich"
    return render_template("home.html")

@app.route("/registration/")
def registration():
    return render_template("footer.html")
@app.route("/tescht")
def test():
    return "succes"

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