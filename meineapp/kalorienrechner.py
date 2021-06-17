import json
import random

with open ("data/user_data.json", "r") as open_file:
    personendaten = json.load(open_file)
    print(personendaten)

for person in personendaten:
    print(person)

# Mit dieser Funktion werden die Kalorien anhand der übermittelten Attribute ausgerechnet
def kalorien(gewicht, groesse, alter, aktivitaet, geschlecht):
    grundumsatz_mann = 66.47 + (13.7 * gewicht) + (5 * groesse) - (6.8 * alter)
    grundumsatz_frau = 65.51 + (9.6 * gewicht) + (1.8 * groesse) - (4.7 * alter)
    if geschlecht == "m":
        erhaltungskalorien = grundumsatz_mann * aktivitaet
    else:
        erhaltungskalorien = grundumsatz_frau * aktivitaet
    return erhaltungskalorien

# Diese Funktion wird weiter unten verwendet um die Gerichte in die Kategorien breakfast,
# lunch, dinner, snack einzuteilen.
def get_category(dishes, category):
    dish_cat = []
    for dish in dishes.keys():
        if dishes[dish]["Kategorie"] == category:
            # Jedes Element in der dish_cat Liste ist eine Liste, in der
            # das erste Element der Name des Gerichts ist und das zweite Element
            # das Key-value-Paar aus dem rezepte.json.
            dish_cat.append([dish, dishes[dish]])
    return dish_cat


# Mit dieser Funktion werden alle dishes mit zu vielen Kalorien enfernt
# und in die Liste dish_removed geschrieben
def remove_dishes(dishes, max_calories):
    dish_removed = []
    for dish in dishes:
        if int(dish[1]["Kalorien"]) <= max_calories:
            dish_removed.append(dish)
    return dish_removed

# Diese Funktion wird letztlich im main.py verwendet um passende Gerichte darzustellen
# Die Variable calories wird im main.py an die Funktion mitgegeben und entspricht den errechneten
# Kalorien, die eine Person als Tagesbedarf benötigt.
def menu_from_calories(calories):
    # Hier wird definiert wie viel die einzelne Mahlzeit prozentual vom gesamten
    # Kalorienbedarf ausmachen darf
    breakfast_percent = 0.2
    lunch_percent = 0.4
    dinner_percent = 0.3
    snack_percent = 0.1

    # Hier wird die maximal erlaubte Kalorienanzahl pro Kategorie errechnet
    breakfast_cal = breakfast_percent * calories
    lunch_cal = lunch_percent * calories
    dinner_cal = dinner_percent * calories
    snack_cal = snack_percent * calories

    # Hier werden alle Dishes ausgelesen (bzw. der Inhalt des rezepte.json)
    dishes = []
    with open("data/rezepte.json", "r") as open_file:
        dishes = json.load(open_file)

    # Hier wird mit Hilfe der oben definierten get_category Funktion die verschiedenen
    # Kategorien von dishes in die jeweiligen Variablen gespeichert
    breakfast = get_category(dishes, "breakfast")
    lunch = get_category(dishes, "lunch")
    dinner = get_category(dishes, "dinner")
    snack = get_category(dishes, "snack")

    # Hier werden die dishes gesucht, die in die jeweilige Kalorien-range passen
    # es werden die jeweiligen Werte an die remove_dishes Funktion, welche oben definiert wurde
    # weiter gegeben und die passenden Gerichte werden in eine neue, aufgeräumte Liste geschrieben
    breakfast = remove_dishes(breakfast, breakfast_cal)
    lunch = remove_dishes(lunch, lunch_cal)
    dinner = remove_dishes(dinner, dinner_cal)
    snack = remove_dishes(snack, snack_cal)

    # Hier werden zufällig Gerichte aus der Liste mit passenden Gerichten ausgewählt
    # Ich verwende random.sample statt random.choice, das so keine Duplikate ausgegeben werden
    # wobei sich das mit k=1 sowieso erübrigt hätte. Mit den if-conditions stelle ich sicher,
    # dass nur ein Wert angezeigt wird, wenn sich ein passendes Element in der Liste befindet.
    br = None
    lu = None
    di = None
    sn = None
    if len(breakfast) > 0:
        br = random.sample(breakfast, k=1)
    if len(lunch) > 0:
        lu = random.sample(lunch, k=1)
    if len(dinner) > 0:
        di = random.sample(dinner, k=1)
    if len(snack) > 0:
        sn = random.sample(snack, k=1)

    return [br, lu, di, sn]


# Hier unten ist der Ursprung zur Funktion zur Quellenberechnung inklusive Quellenangabe

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