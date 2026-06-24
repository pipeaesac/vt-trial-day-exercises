# ======================================================
# rechner.py – Dein Taschenrechner vom Vormittag
#
# Kopiere deinen Code hierher!
# Die Funktionen müssen genau so heissen:
#   addieren(a, b)
#   subtrahieren(a, b)
#   multiplizieren(a, b)
#   dividieren(a, b)
# ======================================================

def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b

def multiplizieren(a, b):
    return a * b

def dividieren(a, b):
    if b == 0:
        return "Fehler: Division durch 0!"
    return a / b