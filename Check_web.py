import os
import requests


def gen_get_files(dir):
    for d in os.listdir(dir):
        yield os.path.join(dir, d)


def gen_get_file_lines(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            yield line.replace('\n', '')


def check_webpage(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False


try:
    os.mkdir(r"C:\Users\Mikołaj\Desktop\PYT")
except:
    pass

with open(r"C:\Users\Mikołaj\Desktop\PYT\pl.txt", 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.nie-ma-takiego-adresu.pl/\n')
    f.write('http://www.demotywatory.pl')

with open(r"C:\Users\Mikołaj\Desktop\PYT\com.txt", 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

for file in gen_get_files(r"C:\Users\Mikołaj\Desktop\PYT"):
    for line in gen_get_file_lines(file):
        print("{} - {} - {}".format(file, line, check_webpage(line)))