import os


def get_file():
    while True:
        filename = input("Podaj sciezke dostepu do pliku: \n")
        if os.path.isfile(filename):
            return open(filename, 'r')


def append_to_file(path_file: str):
    file = open(os.getcwd() + '\\' + path_file, 'a')
    file.write(line)
    file.close()


def delete_file_if_exists(path_file:str):
    if os.path.exists(path_file):
        os.remove(path_file)


file_pl = 'webs_pl.txt'
file_other = 'webs_other.txt'
main_file = get_file()
delete_file_if_exists(file_pl)
delete_file_if_exists(file_other)

for line in main_file:
    if line.replace('\n', '').endswith('.pl'):
        append_to_file(file_pl)
    else:
        append_to_file(file_other)

main_file.close()

# C:\Users\Mikołaj\repositories\nauka-python\plik.txt
