import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)


try:
    if os.path.exists(tmpfile_path):
      os.remove(tmpfile_path)
      save_url_to_file(url,tmpfile_path)
      shutil.copy(tmpfile_path,tmpfile)
except Exception as e:
    print("Error \n {}".format(e))
else:
    print("URL downloaded successfully {}".format(file))
finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
        print("Final removal of the file {}".format(tmpfile_path))
    print("Done")


