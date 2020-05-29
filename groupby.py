import os
import itertools


def scantree(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry
        


listing = scantree(r"C:\Users\Mikołaj\Desktop")
for l in listing:
    print("Dir" if l.is_dir() else "File",l.path)

listing = sorted(listing,key=lambda x: x.is_dir())

for is_dir,elements in itertools.groupby(listing,key=lambda x:x.is_dir()):
    print("Dir" if l.is_dir() else "File",l.path)
    
