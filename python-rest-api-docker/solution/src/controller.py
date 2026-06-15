from flask import Flask, request, jsonify, render_template
import logging

from rechner import addieren, subtrahieren, multiplizieren, dividieren

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    # Liefert die Taschenrechner-Oberflaeche (templates/index.html) aus.
    return render_template("index.html")


# --- Beispiel-Endpunkt (war von Anfang an da) -----------------------------
@app.route("/v1/api", methods=["POST"])
def postSomeThing():
    content = request.json
    name = content["name"]
    logger.info("name: %s", name)
    return "Hello %s" % name


# --- Geloester Rechner-Endpunkt -------------------------------------------
# Die Weboberflaeche schickt: { "zahl1": 5, "zahl2": 3, "operator": "+" }
# und erwartet zurueck:       { "ergebnis": 8 }
@app.route("/v1/rechnen", methods=["POST"])
def rechnen():
    daten = request.json
    logger.info("Anfrage: %s", daten)

    # Schritt 3: Werte aus der Anfrage lesen.
    zahl1 = daten["zahl1"]
    zahl2 = daten["zahl2"]
    operator = daten["operator"]
    # Schritt 4: Passende Funktion aus rechner.py aufrufen.
    if operator == "+":
        ergebnis = addieren(zahl1, zahl2)
    elif operator == "-":
        ergebnis = subtrahieren(zahl1, zahl2)
    elif operator == "*":
        ergebnis = multiplizieren(zahl1, zahl2)
    elif operator == "/":
        ergebnis = dividieren(zahl1, zahl2)
    else:
        # Bonus: unbekannter Operator -> saubere Fehlermeldung statt Absturz.
        return jsonify({"fehler": "Unbekannter Operator: %s" % operator}), 400

    # Schritt 5: Ergebnis als JSON zurueckgeben.
    return jsonify({"ergebnis": ergebnis})
