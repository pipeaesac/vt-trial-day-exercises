# 🧮 Übung: Bring den Taschenrechner ins Web

Willkommen zum **zweiten Teil**! Heute Früh hast du einen Taschenrechner in Python
gebaut (`rechner.py`). Der läuft bisher nur im Terminal. Jetzt machst du daraus einen
**Web-Service**: eine Internetseite, auf der man rechnen kann.

Die Oberfläche (die Webseite) ist schon fertig. Deinen Taschenrechner vom Vormittag
benutzen wir gleich weiter. **Deine Aufgabe:** Du verbindest beide Teile – über einen
sogenannten *Endpunkt* in Flask.

Keine Sorge, wenn du Flask noch nicht kennst. Du hast ein fertiges Beispiel als Vorlage,
und diese Anleitung führt dich Schritt für Schritt. Du schaffst das zu 90 % allein 💪

---

## Was du am Ende kannst

- verstehen, wie eine Webseite mit einem Server "spricht"
- einen eigenen API-Endpunkt in Flask schreiben
- deinen Code in Docker bauen und testen

---

## Die wichtigsten Dateien

| Datei | Was drin ist | Musst du anfassen? |
|-------|--------------|--------------------|
| `src/rechner.py` | Dein Taschenrechner vom Vormittag (`addieren`, `subtrahieren`, ...) | rein damit 👇 |
| `src/templates/index.html` | Die fertige Weboberfläche | nein |
| `src/controller.py` | Der Server. **Hier arbeitest du!** | ✅ ja |

---

## Schritt 0 – Server starten und anschauen

Baue und starte den Server mit diesen zwei Befehlen:

```bash
docker build -t python-rest .
docker run -d --name rechner -p 5000:5000 python-rest
```

Öffne nun **http://localhost:5000/** im Browser.

👉 Tippe etwas ein und klicke auf **Berechnen**. Es kommt eine Fehlermeldung –
das ist genau richtig! Den fehlenden Teil baust du gleich.

> **Wichtig – nach jeder Änderung neu starten:** Dein Code wird beim Bauen in den
> Container kopiert. Damit eine Änderung wirkt, baust du neu und startest neu.
> Dieser eine Befehl macht beides (das Bauen geht nach dem ersten Mal sehr schnell):
>
> ```bash
> docker rm -f rechner; docker build -t python-rest . && docker run -d --name rechner -p 5000:5000 python-rest
> ```
>
> Danach im Browser einfach neu laden. Tipp: Leg dir diesen Befehl bereit, du
> brauchst ihn nach jedem Schritt.

---

## Schritt 1 – Deinen Taschenrechner einsetzen

Damit der Server deinen Rechner findet, muss er als `src/rechner.py` liegen.

- Hast du deinen Code vom Vormittag? **Kopiere ihn nach `src/rechner.py`.**
- In `src/rechner.py` liegt schon eine fertige Version als Vorlage. Du kannst deine
  eigene benutzen – wichtig ist nur, dass die Funktionen so heißen:
  `addieren`, `subtrahieren`, `multiplizieren`, `dividieren` und jeweils zwei Werte (`a`, `b`) bekommen.

Öffne die Datei und lies sie noch einmal durch. Frag dich:
- Wie heißen die Funktionen genau?
- Was bekommt jede Funktion an Werten herein, was gibt sie zurück?
- Was passiert bei `dividieren`, wenn man durch 0 teilt?

An den Funktionen selbst musst du jetzt **nichts** mehr ändern – du wirst sie gleich nur *aufrufen*.

---

## Schritt 2 – Die Funktionen importieren

Öffne `src/controller.py`. Ganz oben gibt es ein `TODO (Schritt 2)`.

Damit du die Funktionen aus `rechner.py` benutzen kannst, musst du sie zuerst
*importieren*. In Python holt man sich Dinge aus einer anderen Datei mit
`from dateiname import funktion1, funktion2`.

💡 **Tipp:** Die Datei heißt `rechner` (ohne `.py`). Importiere alle vier Funktionen,
die du in Schritt 1 gefunden hast.

> Test: Speichere, starte den Server neu (siehe Befehl in Schritt 0) und schau mit
> `docker logs rechner` ins Protokoll. Wenn dort **kein** Fehler steht, stimmt dein Import.

---

## Schritt 3 – Die Daten aus der Anfrage lesen

Scrolle zu `def rechnen()`. Die Variable `daten` enthält bereits das JSON, das die
Webseite schickt – ein Dictionary in dieser Form:

```python
{ "zahl1": 5, "zahl2": 3, "operator": "+" }
```

Hol dir aus `daten` die drei Werte in drei eigene Variablen (z. B. `zahl1`, `zahl2`, `operator`).

💡 **Tipp:** Auf einen Wert in einem Dictionary greift man mit eckigen Klammern zu,
z. B. `daten["operator"]`. Schau dir an, wie der fertige Endpunkt `postSomeThing()`
weiter oben das mit `content["name"]` macht – dein Vorgehen ist dasselbe.

---

## Schritt 4 – Die richtige Rechnung auswählen

Jetzt kommt das Herzstück. Je nachdem, welcher `operator` ankommt (`"+"`, `"-"`,
`"*"` oder `"/"`), soll die passende Funktion aus `rechner.py` aufgerufen werden.

💡 **Tipp:** Das ist eine klassische `if` / `elif` / `else`-Entscheidung. Übrigens:
In `rechner.py` gibt es in der `main()`-Funktion **genau so eine Auswahl** schon zu
sehen – die kannst du dir als Vorbild nehmen (aber Tippen statt Kopieren – so lernst du mehr 😉).

Speichere das Ergebnis in einer Variablen, z. B. `ergebnis`.

❓ Überlege: Was soll passieren, wenn jemand einen Operator schickt, den es gar nicht gibt?

---

## Schritt 5 – Das Ergebnis zurückgeben

Der Server muss der Webseite antworten – und zwar als JSON. Die Oberfläche erwartet
genau dieses Format:

```json
{ "ergebnis": 8 }
```

💡 **Tipp:** Flask macht aus einem Python-Dictionary mit der Funktion `jsonify(...)`
eine JSON-Antwort. Du hast `jsonify` schon ganz oben importiert. Baue dir ein
Dictionary mit dem Schlüssel `"ergebnis"` und deinem berechneten Wert und gib es
mit `return` zurück.

➡️ Lösche zum Schluss die Platzhalter-Zeile (`return jsonify({"fehler": ...})`),
sonst wird sie statt deiner Antwort ausgeführt.

---

## Schritt 6 – Testen 🎉

1. Datei speichern, Server neu starten (Befehl aus Schritt 0), Browser auf
   **http://localhost:5000/** neu laden.
2. Zahlen eingeben, Operator wählen, **Berechnen** klicken → es sollte ein Ergebnis erscheinen!

Du kannst den Endpunkt auch direkt testen, ganz ohne Oberfläche:

```bash
curl -X POST http://localhost:5000/v1/rechnen \
  -H "Content-Type: application/json" \
  -d '{"zahl1": 5, "zahl2": 3, "operator": "+"}'
```

Erwartete Antwort: `{"ergebnis":8}`

> **Steckst du fest?** Sieh dir das Server-Protokoll mit `docker logs rechner` an
> (oder `docker logs -f rechner`, um live mitzulesen). Fehlermeldungen verraten dir
> oft genau die Zeile und das Problem. Die Zeile `logger.info("Anfrage: %s", daten)`
> zeigt dir außerdem, was bei jeder Anfrage wirklich ankommt.

---

## 🏆 Bonus-Aufgaben (für die Schnellen)

1. **Division durch 0:** Probiere `10 / 0` über die Oberfläche. Was passiert? Warum?
   (Tipp: Schau in `rechner.py`, was `dividieren` in diesem Fall zurückgibt.)
2. **Ungültiger Operator:** Sorge dafür, dass dein Endpunkt sauber reagiert, wenn der
   Operator unbekannt ist – z. B. mit einer Fehlermeldung statt eines Absturzes.
3. **Fehlende Daten:** Was passiert, wenn `zahl1` gar nicht mitgeschickt wird? Wie
   könnte man das abfangen?
4. **Neue Rechenart:** Füge in `rechner.py` eine Funktion `potenzieren(a, b)` hinzu
   (`a` hoch `b`), baue sie in den Endpunkt ein und ergänze sie in der Oberfläche
   (`templates/index.html`, im `<select>`).

Viel Erfolg – und trau dich, Dinge auszuprobieren. Kaputtmachen kannst du nichts! 🚀
