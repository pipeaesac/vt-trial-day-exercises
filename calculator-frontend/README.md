# 🖥️ Aufgabe 3 – Taschenrechner Frontend

Das Backend läuft bereits. Die Oberfläche ist fertig gestaltet.

**Deine Aufgabe:** Öffne `index.html` und schreibe die Funktion `rechnen()` fertig.

## Starten

```bash
# Im Haupt-Ordner (wo docker-compose.yml liegt):
docker compose up --build
```

Dann: http://localhost:8080

## Was du schreiben musst

Die Funktion `rechnen()` soll:
1. Zahlen und Operator aus dem Formular lesen
2. Per `fetch()` ans Backend schicken
3. Das Ergebnis anzeigen

Die genaue Anleitung steht als Kommentare direkt in `index.html`.

## Backend-URL

```
POST /api/v1/rechnen
```

Du schickst:  `{ "zahl1": 5, "zahl2": 3, "operator": "+" }`
Du bekommst: `{ "ergebnis": 8 }`

## Bonus
- Was passiert bei Division durch 0?
- Was passiert wenn eine Zahl leer ist?