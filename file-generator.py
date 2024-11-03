import os
import sys
import shutil

def generateFiles(miesiace, dni_tygodnia, pory_dnia):
    k = 0
    tydzien = ['pn', 'wt', 'śr', 'czw', 'pt', 'sob', 'niedz']

    for i, miesiac in enumerate(miesiace):
        dni = dni_tygodnia[i].split('-')
        if (len(dni) == 2):
            start_index = tydzien.index(dni[0])
            end_index = tydzien.index(dni[1])
            dni = tydzien[start_index:end_index + 1]
        for dzien in dni:
            if (k < len(pory_dnia)):
                pora = 'rano' if pory_dnia[k] == 'r' else 'wieczór'
            else: pora = 'rano'
            k = k + 1
            sciezka = os.path.join(miesiac, dzien, pora)
            os.makedirs(sciezka, exist_ok=True)
            print(f"Utworzono katalog: {sciezka}")

#funkcja tylko do testów
def deleteFiles():
    miesiace = ["styczeń", "luty", "marzec", "kwiecień", "maj",
                "czerwiec", "lipiec", "sierpień", "wrzesień",
                "październik", "listopad", "grudzień"]
    for miesiac in miesiace:
        if os.path.exists(miesiac):
            shutil.rmtree(miesiac)

def main():
    generateFiles(["styczeń", "luty", "kwiecień"], ["pn-wt", "pt", "sb"], ["r","w",'r','r'])
    deleteFiles()

main()