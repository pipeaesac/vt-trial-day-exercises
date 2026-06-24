from flask import Flask, request, jsonify
import logging

from rechner import addieren, subtrahieren, multiplizieren, dividieren

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/v1/api", methods=["POST"])
def postSomeThing():
    content = request.json
    name = content["name"]
    logger.info("name: %s", name)
    return "Hello %s" % name


@app.route("/v1/rechnen", methods=["POST"])
def rechnen():
    daten = request.json
    logger.info("Anfrage: %s", daten)

    zahl1    = daten["zahl1"]
    zahl2    = daten["zahl2"]
    operator = daten["operator"]

    if operator == "+":
        ergebnis = addieren(zahl1, zahl2)
    elif operator == "-":
        ergebnis = subtrahieren(zahl1, zahl2)
    elif operator == "*":
        ergebnis = multiplizieren(zahl1, zahl2)
    elif operator == "/":
        ergebnis = dividieren(zahl1, zahl2)
    else:
        return jsonify({"fehler": "Unbekannter Operator: " + operator}), 400

    # dividieren() gibt einen String zurück bei Division durch 0
    if isinstance(ergebnis, str):
        return jsonify({"fehler": ergebnis}), 400

    return jsonify({"ergebnis": ergebnis})