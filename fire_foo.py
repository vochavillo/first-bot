import requests
from os.path import exists
import csv
from datetime import datetime, timedelta
from dateutil import parser as dateparser

from datefoo import *





def make_seattle_data_url(startdate, enddate):
    # https://dev.socrata.com/docs/queries/where.html
    # https://dev.socrata.com/docs/queries/query.html
    return "http://theurlcall."



######## delete this later
DATA_URL = 'https://data.seattle.gov/api/views/kzjm-xkqj/rows.csv?accessType=DOWNLOAD'
DATA_FILENAME = 'data/seattle911.csv'
def save_data(txt):
    with open(DATA_FILENAME, 'w') as f:
        f.write(txt)
###########

# change to get_data(startdate, enddate)
def get_data():
#    url = make_seattle_data_url(startdate, enddate)
    if not exists(DATA_FILENAME):
        resp = requests.get(DATA_URL)
        txt = resp.text
        save_data(txt)
    else:
        with open(DATA_FILENAME, 'r') as f:
            txt = f.read()

    lines = txt.splitlines()
    return list(csv.DictReader(lines))



def get_calls_for_week_of(somedate):
    records = get_data()

    firstday = get_start_of_week(somedate)
    lastday = get_end_of_week(somedate)

    weekcalls = []

    for row in records:
        if row['Datetime']:
            try:
                calltime = translate_seattle_time(row['Datetime'])
            except ValueError:
                pass
            else:
                if calltime > firstday and calltime < lastday:
                    weekcalls.append(row)

    return weekcalls





def current_week_calls():
    return  get_calls_for_week_of(datetime.now())


def last_week_calls():
    d = get_start_of_previous_week(datetime.now())
    return get_calls_for_week_of(d)





























