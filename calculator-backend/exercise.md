# 🧮 Übung: Bring den Taschenrechner ins Web

> 📝 **Nimm dir Notizen!** Du wirst am Ende Fragen zu dieser Übung beantworten.
> Schreib dir auf, was du tust, was du verstehst – und auch, wenn etwas unklar ist.
> Stichwörter reichen völlig aus.

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
| `src/controller.py` | Der Server. **Hier arbeitest du!** | ✅ ja |

---

## Schritt 0 – Server starten und anschauen

Öffne ein Terminal und gehe in den **Hauptordner** (wo `docker-compose.yml` liegt).
Starte beide Container mit:

```powershell
docker compose up --build
```

Öffne nun **http://localhost:8080/** im Browser.

👉 Tippe etwas ein und klicke auf **Berechnen**. Es kommt eine Fehlermeldung –
das ist genau richtig! Den fehlenden Teil baust du gleich.

> **Wichtig – nach jeder Änderung neu starten:**
> Dein Code wird beim Bauen in den Container kopiert. Damit eine Änderung wirkt,
> musst du neu bauen. Dieser Befehl macht beides:
>
> ```powershell
> docker compose up --build
> ```
>
> Danach im Browser einfach neu laden.
> Tipp: Lass das Terminal offen – du brauchst den Befehl nach jedem Schritt wieder.

---

## Schritt 1 – Deinen Taschenrechner einsetzen

Damit der Server deinen Rechner findet, muss er als `src/rechner.py` liegen.

- Hast du deinen Code vom Vormittag? **Kopiere ihn nach `src/rechner.py`.**
- In `src/rechner.py` liegt schon eine fertige Version als Vorlage. Du kannst deine
  eigene benutzen – wichtig ist nur, dass die Funktionen so heissen:
  `addieren`, `subtrahieren`, `multiplizieren`, `dividieren` und jeweils zwei Werte (`a`, `b`) bekommen.

Öffne die Datei und lies sie noch einmal durch. Frag dich:
- Wie heissen die Funktionen genau?
- Was bekommt jede Funktion an Werten herein, was gibt sie zurück?
- Was passiert bei `dividieren`, wenn man durch 0 teilt?

An den Funktionen selbst musst du jetzt **nichts** mehr ändern – du wirst sie gleich nur *aufrufen*.

> 📝 **Notiz-Tipp:** Schreib dir die Funktionsnamen und ihre Parameter auf – am Ende kommen Fragen dazu!

---

## Schritt 2 – Die Funktionen importieren

Öffne `src/controller.py`. Ganz oben gibt es ein `TODO (Schritt 2)`.

Damit du die Funktionen aus `rechner.py` benutzen kannst, musst du sie zuerst
*importieren*. In Python holt man sich Dinge aus einer anderen Datei mit
`from dateiname import funktion1, funktion2`.

💡 **Tipp:** Die Datei heisst `rechner` (ohne `.py`). Importiere alle vier Funktionen,
die du in Schritt 1 gefunden hast.

> Test: Speichere, starte neu (`docker compose up --build`) und schau ins Protokoll:
>
> ```powershell
> docker logs rechner-backend
> ```
>
> Wenn dort **kein** Fehler steht, stimmt dein Import.

> 📝 **Notiz-Tipp:** Schreib dir auf, wie ein `import`-Befehl in Python aufgebaut ist – am Ende kommen Fragen dazu!

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

> 📝 **Notiz-Tipp:** Schreib dir auf, was ein Dictionary ist und wie man darauf zugreift – am Ende kommen Fragen dazu!

---

## Schritt 4 – Die richtige Rechnung auswählen

Jetzt kommt das Herzstück. Je nachdem, welcher `operator` ankommt (`"+"`, `"-"`,
`"*"` oder `"/"`), soll die passende Funktion aus `rechner.py` aufgerufen werden.

💡 **Tipp:** Das ist eine klassische `if` / `elif` / `else`-Entscheidung. Übrigens:
In `rechner.py` gibt es in der `main()`-Funktion **genau so eine Auswahl** schon zu
sehen – die kannst du dir als Vorbild nehmen (aber Tippen statt Kopieren – so lernst du mehr 😉).

Speichere das Ergebnis in einer Variablen, z. B. `ergebnis`.

❓ Überlege: Was soll passieren, wenn jemand einen Operator schickt, den es gar nicht gibt?

> 📝 **Notiz-Tipp:** Schreib dir auf, wie eine `if/elif/else`-Struktur funktioniert – am Ende kommen Fragen dazu!

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

> 📝 **Notiz-Tipp:** Schreib dir auf, was JSON ist und warum Server so antworten – am Ende kommen Fragen dazu!

---

## Schritt 6 – Testen 🎉

1. Speichern, neu starten: `docker compose up --build`
2. Browser auf **http://localhost:8080/** neu laden.
3. Zahlen eingeben, Operator wählen, **Berechnen** klicken → Ergebnis erscheint!

Du kannst den Endpunkt auch direkt testen, ganz ohne Browser:

```powershell
curl -X POST http://localhost:8080/api/v1/rechnen `
  -H "Content-Type: application/json" `
  -d '{"zahl1": 5, "zahl2": 3, "operator": "+"}'
```

Erwartete Antwort: `{"ergebnis": 8}`

> **Steckst du fest?** Logs anschauen:
>
> ```powershell
> docker logs rechner-backend
> ```
>
> Fehlermeldungen verraten dir oft genau die Zeile und das Problem.

---

## 🏆 Bonus-Aufgaben (für die Schnellen)

1. **Division durch 0:** Probiere `10 / 0` über die Oberfläche. Was passiert? Warum?
   (Tipp: Schau in `rechner.py`, was `dividieren` in diesem Fall zurückgibt.)
2. **Ungültiger Operator:** Sorge dafür, dass dein Endpunkt sauber reagiert, wenn der
   Operator unbekannt ist – z. B. mit einer Fehlermeldung statt eines Absturzes.
3. **Fehlende Daten:** Was passiert, wenn `zahl1` gar nicht mitgeschickt wird? Wie
   könnte man das abfangen?
4. **Neue Rechenart:** Füge in `rechner.py` eine Funktion `potenzieren(a, b)` hinzu
   (`a` hoch `b`), baue sie in den Endpunkt ein und ergänze sie in
   `calculator-frontend/index.html` im `<select>`.

Viel Erfolg – und trau dich, Dinge auszuprobieren. Kaputtmachen kannst du nichts! 🚀