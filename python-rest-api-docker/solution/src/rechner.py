def addieren(a, b):
    return a + b


def subtrahieren(a, b):
    return a - b


def multiplizieren(a, b):
    return a * b


def dividieren(a, b):
    if b == 0:
        return "Fehler: Division durch 0"
    return a / b


def main():
    print("Taschenrechner")

    zahl1 = float(input("Erste Zahl: "))
    operator = input("Operator (+, -, *, /): ")
    zahl2 = float(input("Zweite Zahl: "))

    if operator == "+":
        ergebnis = addieren(zahl1, zahl2)
    elif operator == "-":
        ergebnis = subtrahieren(zahl1, zahl2)
    elif operator == "*":
        ergebnis = multiplizieren(zahl1, zahl2)
    elif operator == "/":
        ergebnis = dividieren(zahl1, zahl2)
    else:
        ergebnis = "Ungültiger Operator"

    print("Ergebnis:", ergebnis)


if __name__ == "__main__":
    main()
