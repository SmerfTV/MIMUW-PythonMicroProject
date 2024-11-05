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
            k += 1
            sciezka = os.path.join(miesiac, dzien, pora)
            os.makedirs(sciezka, exist_ok=True)
            sciezka_pliku = os.path.join(sciezka, FILENAME)

            if os.path.isfile(sciezka_pliku):
                print(f"Plik już istnieje, więc nie zostanie utworzony:\n{sciezka_pliku}")
            else:
                try:
                    zapisz_csv(sciezka_pliku)
                    print(f"Utworzono plik CSV: {sciezka_pliku}")
                except Exception as e:
                    print(f"Nie udało się utworzyć pliku {sciezka_pliku}: {e}")

def zapisz_csv(sciezka_pliku):
    """
    Zapisuje dane do pliku CSV zgodnie z wymaganiami.
    Pierwsza linia to nagłówek, druga linia to losowe dane.
    """
    header = ["Model", "Wynik", "Czas"]
    model = random.choice(["A", "B", "C"])
    wynik = random.randint(0, 1000)
    czas = f"{random.randint(0, 1000)}s"

    with open(sciezka_pliku, mode="w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerow([model, wynik, czas])

def readFiles(miesiace, dni_tygodnia, pory_dnia):
    k = 0
    tydzien = ['pn', 'wt', 'śr', 'czw', 'pt', 'sob', 'niedz']
    suma_czas = 0

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
            k += 1
            sciezka_pliku = os.path.join(miesiac, dzien, pora, FILENAME)

            if os.path.exists(sciezka_pliku):
                try:
                    with open(sciezka_pliku, mode="r", encoding="utf-8") as file:
                        reader = csv.DictReader(file, delimiter=';')
                        for row in reader:
                            if row.get("Model") == "A":
                                czas_str = row.get("Czas", "0s").rstrip('s')
                                try:
                                    czas = int(czas_str)
                                    suma_czas += czas
                                except ValueError:
                                    print(f"Błędny format czasu w pliku {sciezka_pliku}: {row.get('Czas')}")
                except Exception as e:
                    print(f"Nie udało się odczytać pliku {sciezka_pliku}: {e}")
            else:
                print(f"Plik CSV nie istnieje: {sciezka_pliku}")

    print(f"Suma czasu dla Model A: {suma_czas}s")

# Funkcja tylko do testów
def deleteFiles():
    miesiace = ["styczeń", "luty", "marzec", "kwiecień", "maj",
                "czerwiec", "lipiec", "sierpień", "wrzesień",
                "październik", "listopad", "grudzień"]
    for miesiac in miesiace:
        if os.path.exists(miesiac):
            try:
                shutil.rmtree(miesiac)
                print(f"Usunięto katalog: {miesiac}")
            except Exception as e:
                print(f"Nie udało się usunąć katalogu {miesiac}: {e}")
    print("Wszystkie katalogi i pliki zostały usunięte.")

def main():
    parser = argparse.ArgumentParser(description='Skrypt do tworzenia lub odczytu plików CSV.')

    # a) Wybór miesięcy (można wybrać dowolną ilość)
    parser.add_argument('--months', nargs='+', required=True, help='Lista miesięcy (np. styczeń luty)')

    # b) Wybór zakresu dni tygodnia (tyle samo argumentów co w (a) )
    parser.add_argument('--days', nargs='+', required=True, help='Lista zakresów dni tygodnia (np. pn-pt wt-śr)')

    # c) Wybór albo rano albo wieczorem (domyślnie rano)
    parser.add_argument('--pory', nargs='*', help='Lista pór dnia (r lub w). Jeśli nie podano, domyślnie "rano"')

    # d) Wybór opcji tworzenie / odczyt
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--tworzenie', action='store_true', help='Tworzenie plików CSV')
    group.add_argument('-o', '--odczyt', action='store_true', help='Odczyt plików CSV')

    # e) Opcja usuwania plików
    parser.add_argument('--delete', action='store_true', help='Usuń wszystkie utworzone katalogi i pliki')

    args = parser.parse_args()

    miesiace = args.months
    dni_tygodnia = args.days
    pory_dnia = args.pory if args.pory else []

    if len(miesiace) != len(dni_tygodnia):
        print('Liczba miesięcy musi być równa liczbie zakresów dni tygodnia.')
        sys.exit(1)

    if args.delete:
        deleteFiles()
        sys.exit(0)

    if args.tworzenie:
        generateFiles(miesiace, dni_tygodnia, pory_dnia)
    elif args.odczyt:
        readFiles(miesiace, dni_tygodnia, pory_dnia)

if __name__ == '__main__':
    main()
