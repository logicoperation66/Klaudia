import glob

### Use glob to find input all .txt files to variable

files = glob.glob("Zalecenia/*.txt")
n = 1

### Printing list of files with some text to be sure what excersise is inside.
for file in files:
    __file = open(file, 'r')
    print(f"Zalecenie nr.{n} \n{__file.read(50)}...\n")
    n += 1

prompt = "Podaj numer zalecenia które chcesz dodać do pliku głownego :"
prompt2 = "Podaj nazwę dla pliku końcowego (pamiętaj aby dodać rozszerzenie) :"

final_filename = str(input(prompt2))

### Used while in while... I'm sure there is better way to solve that but
# already is too late for my brain to think about it.... It works..

## I should add a function to check if the recommendation number exists.
# For example if I have 3 recomendation and i chose 4 i get err..
# THIS NEED  TO BE DONE BETTER.
while True:
    while True:
        try:
            choice = int(input('Podaj liczbę :'))
        except ValueError:
            print('Podałeś niewłaściwe dane. Wpisz liczbę naturalną.')
        else:
            break
    if choice == 0:
        print(f"Tworzenie pliku o nazwie {final_filename} gotowe.")
        break
    else:
        path = files[choice - 1]
        text = open(path, 'r')
        f = open(final_filename, '+a')
        f.writelines(f"\n...\n{text.read()}")
        print(f"Dodałeś zalecenie o nr.{choice}, Jeśli chcesz zakończyć wpisz 0")



