# Uruchamianie Pythona z linii poleceń
Na pierwszych zajęciach pojawiło się trochę pytań o to, jak należy uruchamiać programy w pythonie. Z pythonem pracować będziemy z poziomu terminala - poniżej krótka instrukcja.

## Włączanie terminala
#### Windows:
```
Start → Wszystkie programy → Akcesoria → Wiersz poleceń
```
#### macOS
```
Aplikacje → Narzędzia → Terminal
```
#### Linux
Różnie w zależności od dystrybucji, ale pewnie coś w stylu 
```
Aplikacje → Akcesoria → Terminal
```

## Podstawowe komendy
### Przechodzenie pomiędzy folderami
#### Windows, macOS, Linux
```
cd nazwa_folderu
```
np. żeby przejść na pulpit
```
cd Desktop
```
powracanie do katalogu nadrzędnego:
```
cd ..
```
W trakcie wpisywania nazwy folderu można nacisnąć TAB, wtedy terminal automatyczne uzupełnia resztę nazwy lub po wciśnięciu TABa dwa razy wyświetli propozycje folderów, których nazwy zaczynają się tak jak wpisany przez nas fragment nazwy.
### Wyświetlanie aktualnego folderu
#### Windows
```
cd
```
#### macOS, Linux
```
pwd
```
### Wylistowanie zawartości folderu
#### Windows
```
dir
```
#### macOS, Linux
```
ls
```
### Tworzenie folderu
#### Windows, macOS, Linux
```
mkdir nazwa_folderu
```
## Uruchamianie pythona w terminalu
Na zajęciach interpreter pythona będziemy uruchamiać z terminala. Żeby to zrobić, musimy sprawdzić w jaki sposób powinniśmy odwoływać się u siebie do pythona 3.6.
### Sprawdzanie komendy do uruchamiania Pythona
Wpisz w terminalu 
```
python3.6 --version
```
Jeżeli pojawi się wynik w postaci `Python 3.6.x`, oznacza to, że to nazwy `python3.6` powinniśmy używać do uruchamiania pythona na swoim komputerze.
#### Windows
Na Windowsie prawdopodobnie zainstalowany Python będzie dostępny w terminalu pod nazwą `python`.
Żeby to sprawdzić, wpisz
```
python --version
```
Jeżeli pojawi się wynik w postaci `Python 3.6.x`, oznacza to, że to nazwy `python` powinniśmy używać do uruchamiania pythona na swoim komputerze.

Jeżeli dla obu tych nazw pojawia się błąd, napisz do nas maila, chętnie pomożemy ;)

### Uruchamianie skryptu pythonowego
Stwórz plik `test.py` o treści:
```
print('Test!')
```
i zapisz go. Przejdź za pomocą poleceń terminala do folderu z tym plikiem, a następnie uruchom go za pomocą komendy (w zależności od tego co u Ciebie działa):
```
python3.6 test.py
```
lub
```
python test.py
```
Na ekranie powinien pojawić się napis `Test!`, co oznacza, że program działa poprawnie.

### Włączanie interpretera
Żeby włączyć interpreter pythona, użyj odpowiedniej dla siebie komendy, tzn.
```
python3.6
```
lub
```
python
```
W interpreterze można wpisywać komendy w języku python, które są od razu wykonywane. Pamiętajcie, że w interpreterze nie działają terminalowe komendy takie jak `cd`, `ls` itp. Żeby ich używać lub żeby uruchomić cały plik z programem napisanym w pythonie, należy zamknąć interpreter. Żeby zamknąć interpreter naciśnij `Ctrl+Z` na Windowsie lub `Ctrl+D` na Macu lub na Linuksie.
