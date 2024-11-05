import os
import sys
import shutil
import csv
import random
import argparse

FILENAME = 'Dane.csv'

def generateFiles(miesiace, dni_tygodnia, pory_dnia):
    k = 0
    tydzien = ['pn', 'wt', 'śr', 'czw', 'pt', 'sob', 'niedz']

    for i, miesiac in enumerate(miesiace):
        dni = dni_tygodnia[i].split('-')
        if len(dni) == 2:
            start_index = tydzien.index(dni[0])
            end_index = tydzien.index(dni[1])
            dni = tydzien[start_index:end_index + 1]
        for dzien in dni:
            if k < len(pory_dnia):
                pora = 'rano' if pory_dnia[k] == 'r' else 'wieczór'
            else:
                pora = 'rano'
            k = k + 1
            sciezka = os.path.join(miesiac, dzien, pora)
            os.makedirs(sciezka, exist_ok=True)
            sciezka = os.path.join(miesiac, dzien, pora, FILENAME)

            header = "Model; Wynik; Czas"
            model = random.choice(["A", "B", "C"])
            wynik = random.randint(0, 1000)
            czas = f"{random.randint(0, 1000)}s"

            with open(sciezka, mode="w", encoding="utf-8") as file:
                file.write(f"{header};\n")
                file.write(f"{model} ; {wynik} ; {czas};\n")
            print(f"Utworzono plik: {sciezka}")

# Funkcja tylko do testów
def deleteFiles():
    miesiace = ["styczeń", "luty", "marzec", "kwiecień", "maj",
                "czerwiec", "lipiec", "sierpień", "wrzesień",
                "październik", "listopad", "grudzień"]
    for miesiac in miesiace:
        if os.path.exists(miesiac):
            shutil.rmtree(miesiac)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Skrypt do tworzenia lub odczytu plików.')

    # a) Wybór miesięcy (można wybrać dowolną ilość)
    parser.add_argument('--months', nargs='+', required=True, help='Lista miesięcy (np. styczeń luty)')

    # b) Wybór zakresu dni tygodnia (tyle samo argumentów co w (a) )
    parser.add_argument('--days', nargs='+', required=True, help='Lista zakresów dni tygodnia (np. pn-pt wt-śr)')

    # c) Wybór albo rano albo wieczorem (domyślnie rano)
    parser.add_argument('--pory', nargs='*', help='Lista pór dnia (r lub w). Jeśli nie podano, domyślnie "rano"')

    # d) Wybór opcji tworzenie / odczyt
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--tworzenie', action='store_true', help='Tworzenie plików')
    group.add_argument('-o', '--odczyt', action='store_true', help='Odczyt plików')

    # e) Wybór formatu pliku csv / json
    parser.add_argument('-c', '--csv', action='store_true', help='Użyj formatu CSV')
    parser.add_argument('-j', '--json', action='store_true', help='Użyj formatu JSON')

    args = parser.parse_args()

    miesiace = args.months
    dni_tygodnia = args.days
    pory_dnia = args.pory if args.pory else []

    if len(miesiace) != len(dni_tygodnia):
        print('Liczba miesięcy musi być równa liczbie zakresów dni tygodnia.')
        sys.exit(1)

    generateFiles(miesiace, dni_tygodnia, pory_dnia)
    deleteFiles()


if __name__ == '__main__':
    main()
