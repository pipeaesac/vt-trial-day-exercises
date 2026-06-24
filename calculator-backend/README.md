# ⚙️ Aufgabe 1 – Taschenrechner Backend

Hier baust du den Server-Teil des Taschenrechners mit Python und Flask.

Die Anleitung Schritt für Schritt findest du in `exercise.md`.

---

## Starten

Im **Hauptordner** (wo `docker-compose.yml` liegt):

```powershell
docker compose up --build
```

Dann: **http://localhost:8080**

Nach jeder Änderung einfach denselben Befehl nochmal ausführen.

---

## Dateien

| Datei | Was |
|-------|-----|
| `src/rechner.py` | Dein Taschenrechner vom Vormittag – kopiere deinen Code hierher |
| `src/controller.py` | Der Flask-Server – **hier arbeitest du** |

---

## Logs anschauen

Wenn etwas nicht klappt:

```powershell
docker logs rechner-backend
```

---

## Testen ohne Browser

```powershell
curl -X POST http://localhost:8080/api/v1/rechnen `
  -H "Content-Type: application/json" `
  -d '{"zahl1": 5, "zahl2": 3, "operator": "+"}'
```

Erwartete Antwort: `{"ergebnis": 8}`