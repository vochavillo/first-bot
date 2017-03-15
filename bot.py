import requests
from os.path import exists
import csv


DATA_URL = 'https://data.seattle.gov/api/views/kzjm-xkqj/rows.csv?accessType=DOWNLOAD'
DATA_FILENAME = 'data/seattle911.csv'


def save_data(txt):
    with open(DATA_FILENAME, 'w') as f:
        f.write(txt)



def get_data():
    if not exists(DATA_FILENAME):
        resp = requests.get(DATA_URL)
        txt = resp.text
        save_data(txt)
    else:
        with open(DATA_FILENAME, 'r') as f:
            txt = f.read()

    lines = txt.splitlines()
    return list(csv.DictReader(lines))


