# ✅ Lösung – Taschenrechner als Web-Service

Das ist die **fertige Referenzlösung** zur Übung in [`../exercise.md`](../exercise.md).
Hier ist alles schon implementiert – gedacht für Betreuer:innen zum Nachschauen und
zum Vergleichen, **nicht** zum Abschreiben 🙂

## Was hier gelöst ist

- `src/rechner.py` – der vollständige Taschenrechner (vier Rechenarten)
- `src/controller.py` – der fertige Endpunkt `/v1/rechnen` (Schritte 2–5 umgesetzt,
  inkl. sauberer Fehlermeldung bei unbekanntem Operator als Bonus)
- `src/templates/index.html` – die Weboberfläche (identisch zur Übung)

## Lösung ausführen

Aus **diesem** Ordner (`solution/`):

```bash
docker build -t rechner-solution .
docker run -d --name rechner-solution -p 5000:5000 rechner-solution
```

Dann **http://localhost:5000/** öffnen und rechnen.

Direkt testen ohne Oberfläche:

```bash
curl -X POST http://localhost:5000/v1/rechnen \
  -H "Content-Type: application/json" \
  -d '{"zahl1": 5, "zahl2": 3, "operator": "+"}'
# -> {"ergebnis":8}
```

Aufräumen:

```bash
docker rm -f rechner-solution
```
