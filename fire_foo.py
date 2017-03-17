import requests
from os.path import exists
import csv
from datetime import datetime, timedelta
from dateutil import parser as dateparser
from datefoo import *

def make_seattle_data_url(startdate, enddate):
    base_url = 'https://soda.demo.socrata.com/resource/kzjm-xkqj/rows.csv?$where='
    url_string = 'Datetime >={start}&Datetime <={end}'.format(start=startdate,end=enddate)
    url = base_url + url_string + '0000' #for some reason the timezone tag isn't working so manually adding timezone

    return url

def get_data():
    startdate = get_start_of_previous_week (datetime.now())
    enddate = datetime.now()

    strstartdate = datetime.strftime(startdate, "%m/%d%y %H:%M:%S %p %z")
    strenddate = datetime.strftime(enddate, "%m/%d%y %H:%M:%S %p %z")

    DATA_URL = make_seattle_data_url(strstartdate, strenddate)
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
