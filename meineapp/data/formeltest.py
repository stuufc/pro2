import random
from random import choice
import time

random.seed(time.time)

dict = {
    "Kaiserschmarrn": {
        "Kalorien": 500,
        "Art": 'vegetarisch'
        },
    "Chilli": {
        "Kalorien": 480,
        "Art": 'fleisch'},
    "Toast": {
        "Kalorien": 600,
        "Art": 'vegetarisch'
        }
    }

gericht = random.choice(list(dict.keys()))
wert = list(dict[gericht].values())
gerichte = random.sample(dict.keys(), k=3)
# werte1 = [dict[g]["Kalorien"] for g in gerichte]

werte1 = []
for g in gerichte:
    werte1.append(dict[g]["Kalorien"])
print(gerichte[0], werte1[0], gerichte, gerichte[0])