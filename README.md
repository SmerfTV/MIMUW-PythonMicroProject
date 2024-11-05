## Funkcje

- **Generowanie Plików CSV:** Tworzy pliki CSV z losowymi danymi w strukturze katalogów bazującej na podanych miesiącach, dniach tygodnia i porach dnia.
- **Odczyt Plików CSV:** Odczytuje pliki CSV i sumuje wartości z kolumny `Czas` dla wszystkich rekordów, gdzie w kolumnie `Model` znajduje się wartość `"A"`.


## Instalacja

1. **Sklonuj Repozytorium:**

   ```bash
   git clone https://github.com/twoje-repozytorium/skrypt-csv.git
   cd skrypt-csv
   ```

2. **Upewnij się, że masz zainstalowany Python:**

   Sprawdź wersję Pythona za pomocą:

   ```bash
   python --version
   ```

   Jeśli nie masz Pythona, pobierz go z [oficjalnej strony](https://www.python.org/downloads/).

## Użycie

Skrypt jest uruchamiany z poziomu wiersza poleceń i przyjmuje kilka argumentów, które pozwalają na dostosowanie jego działania.

### Składnia

```bash
python skrypt.py --months <miesiące> --days <dni_tygodnia> [--pory <pory_dnia>] [-t | -o]
```

### Argumenty

- `--months`: **(Wymagane)** Lista miesięcy, dla których mają być tworzone lub odczytywane pliki CSV.

  **Przykład:** `--months styczeń luty`

- `--days`: **(Wymagane)** Lista zakresów dni tygodnia odpowiadających poszczególnym miesiącom. Każdy zakres powinien być w formacie `start-end`, gdzie `start` i `end` to skróty dni tygodnia (`pn`, `wt`, `śr`, `czw`, `pt`, `sob`, `niedz`).

  **Przykład:** `--days pn-wt pt`

- `--pory`: **(Opcjonalne)** Lista pór dnia (`r` dla rano, `w` dla wieczór). Jeśli nie podano, domyślnie przypisywana jest pora `"rano"`.

  **Przykład:** `--pory r w`

- `-t`, `--tworzenie`: **(Opcjonalne)** Opcja tworzenia plików CSV zgodnie z podanymi parametrami.

  **Przykład:** `-t` lub `--tworzenie`

- `-o`, `--odczyt`: **(Opcjonalne)** Opcja odczytu plików CSV i sumowania wartości z kolumny `Czas` dla `Model` = "A".

  **Przykład:** `-o` lub `--odczyt`


## Autorzy

- **Michał Stradczuk**
- **Antoni Cichoń**

- **Wsparcie:**
  - W przypadku pytań lub problemów, prosimy o otwarcie [issue](https://github.com/twoje-repozytorium/skrypt-csv/issues) w repozytorium.

---

*Dziękujemy za korzystanie z naszego skryptu!*
