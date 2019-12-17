import requests
import os.path

if os.path.isfile('data.csv'):
    print("File exists")
else:
    print("File does not exist, dowloading")
    url = 'http://donnees.ville.montreal.qc.ca/dataset/3e3efad6-9f2f-4cc0-8f1b-92de1ccdb282/resource/c6c5afe8-10be-4539-8eae-93918ea9866e/download/arbres-publics.csv'

    r = requests.get(url, allow_redirects=True)

    open('data.csv', 'wb').write(r.content)
