ukoly = []

def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()

        if nazev == "" or popis == "":
            print("Název ani popis nesmí být prázdné. Zkuste to znovu.")
        else:
            ukoly.append({"nazev": nazev, "popis": popis})
            print("Úkol byl úspěšně přidán.")
            break


def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol['nazev']} – {ukol['popis']}")


def odstranit_ukol():
    if not ukoly:
        print("Nejsou žádné úkoly k odstranění.")
        return

    zobrazit_ukoly()

    try:
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= cislo <= len(ukoly):
            odstraneny = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Takový úkol neexistuje.")
    except ValueError:
        print("Zadejte platné číslo.")

# spuštění programu
hlavni_menu()
