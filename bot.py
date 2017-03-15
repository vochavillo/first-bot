import datetime


def get_data():

#how do you get data saved on your desktop?
datafile =
def get_fires(fname):
    thefile = open(fname, 'r')
    contents = thefile.read()
    thefile.close()
    txt = contents.text
    lines = txt.splitlines
    fires = list(csv.DictReader(lines))

    sortedfires = sorted(fires, key=foo_fires, reverse=True)

#foo_fires sorts fires by date
def foo_fires(firelist):
    firelist['Datetime']
    #do I have to reformat the values in the Datetime column?

def make_fire_locator(fire):
    base_url = 'https://maps.googleapis.com/maps/api/staticmap?'
    MAP_SIZE = '800x400'
    coordinate_pairs = []
    my_params = {'size': MAP_SIZE, 'markers': coordinate_pairs}
    fires = get_fires()
    coordinate_pairs = ["%s,%s" % (f['latitude'], f['longitude']) for f in fire]
    preq = requests.PreparedRequest()
    preq.prepare_url(base_url, {'size': MAP_SIZE, 'markers': coordinate_pairs})
    my_url = preq.url
    return my_url

def current_week_fire_count(current_date):
    #start of the week is Sunday; how do you go back to Sunday if it's say Friday
    fires = get_fires()
    currentday = datetime.datetime.strptime(current_date, '%m/%d/%Y').weekday()
    #check syntax, should return day of week as integer
    count = 0
    if currentday == 0:
        #then subtract a whole week
        startdate = current_date - 7
        enddate = current_date - 7
    else:
        #if it's wednesday, then go back to monday
        difference = currentday - 0
        startdate = current_date - difference
        enddate = current_date

        for f in fires:
            if (fires['Datetime'] >= startdate) and (fires['Datetime'] <= enddate):
                count += 1
    return count



        #go back that many days to begin the week



def previous_week_fire_count():



Description
The number of 911 fire calls made in the last week is provided, alongside a
comparison of the count from the previous week. Also, mention of whether
any of the calls resulted in death will be provided

Arguments
Today's date

Data sources
Seattle Real Time Fire 911 Calls
https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj

Google Maps Static API
https://developers.google.com/maps/documentation/static-maps/intro

Seattle Times GitHub
https://github.com/seattletimes

Data transformations
Filters the calls by date
Divides the count between the calls from the last seven days and the calls from the previous week
Counts the number of deaths by looking at the number of times the Seattle Times writes a story in an overlapping period about fires and that mentions death

Example story
In the last week, there were X calls to the fire department. Here is a map of the locations of those calls.

Of Y of those X calls were confirmed fires and resulted in the death of at least one civilian.

References
