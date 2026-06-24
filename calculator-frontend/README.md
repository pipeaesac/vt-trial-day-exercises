# 🧮 Aufgabe 3 – Taschenrechner Frontend

Das Backend läuft bereits. Die Webseite ist fertig gestaltet.

**Deine Aufgabe:** Öffne `index.html` und schreibe die Funktion `rechnen()` im `<script>`-Block fertig.

---

## Was du schreiben musst

Die Funktion soll:

1. Die zwei Zahlen und den Operator aus dem Formular lesen
2. Sie per `fetch()` ans Backend schicken
3. Das Ergebnis im Ergebnis-Kasten anzeigen

Die genaue Anleitung steht als Kommentare direkt im Code.

---

## Backend-URL

```
POST /api/v1/rechnen
```

**Du schickst:**
```json
{ "zahl1": 5, "zahl2": 3, "operator": "+" }
```

**Du bekommst zurück:**
```json
{ "ergebnis": 8 }
```

---

## Testen

```bash
docker compose up --build
```

Dann: http://localhost:8080/taschenrechner/

---

## Bonus

- Was passiert bei Division durch 0? Zeige eine sinnvolle Fehlermeldung.
- Was passiert wenn eine Zahl leer ist? Fange das ab.