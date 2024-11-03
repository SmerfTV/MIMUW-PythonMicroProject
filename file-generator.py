import os
import sys
import shutil

def generateFiles(miesiace, dni_tygodnia, pory_dnia):
    k = 0
    for i, miesiac in enumerate(miesiace):
        dni = dni_tygodnia[i] if i < len(dni_tygodnia) else dni_tygodnia[-1]
        for j, dzien in enumerate(dni.split('-')):
            if (k < len(pory_dnia)):
                pora = 'rano' if pory_dnia[k] == 'r' else 'wieczorem'
            else:
                pora = 'wieczorem'
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