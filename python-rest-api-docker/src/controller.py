from flask import Flask, request, jsonify, render_template
import logging

# TODO (Schritt 2): Importiere hier die Funktionen aus rechner.py,
#                   damit du sie weiter unten benutzen kannst.
# from rechner import ...

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def index():
    # Liefert die Taschenrechner-Oberflaeche (templates/index.html) aus.
    return render_template("index.html")


# --- Beispiel-Endpunkt (schon fertig) -------------------------------------
# Schau ihn dir genau an: So liest man Daten aus einer Anfrage und gibt
# etwas zurueck. Dein Rechner-Endpunkt funktioniert sehr aehnlich!
@app.route("/v1/api", methods=["POST"])
def postSomeThing():
    content = request.json
    name = content["name"]
    logger.info("name: %s", name)
    return "Hello %s" % name


# --- DEINE AUFGABE --------------------------------------------------------
# Hier soll der Taschenrechner-Endpunkt entstehen.
# Die Weboberflaeche schickt dir per POST ein JSON wie dieses:
#     { "zahl1": 5, "zahl2": 3, "operator": "+" }
# und erwartet als Antwort ein JSON wie dieses:
#     { "ergebnis": 8 }
@app.route("/v1/rechnen", methods=["POST"])
def rechnen():
    daten = request.json
    logger.info("Anfrage: %s", daten)

    # TODO (Schritt 3): Lies zahl1, zahl2 und operator aus 'daten'.
    # TODO (Schritt 4): Rufe je nach operator die passende Funktion aus rechner.py auf.
    # TODO (Schritt 5): Gib das Ergebnis als JSON zurueck -> { "ergebnis": ... }

    # Platzhalter, damit die App startet. Ersetze ihn durch deine Loesung.
    return jsonify({"fehler": "Endpunkt noch nicht implementiert (siehe exercise.md)"}), 501
