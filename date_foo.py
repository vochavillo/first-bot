

def get_start_of_week(somedate):
    weekday = somedate.isoweekday()
    x = somedate - timedelta(days=weekday)
    return datetime(x.year, x.month, x.day)

def get_end_of_week(somedate):
    a = get_start_of_week(somedate)
    b = a + timedelta(days=7)
    return datetime(b.year, b.month, b.day)


def get_start_of_previous_week(somedate):
    x = somedate - timedelta(days=7)
    return(get_start_of_week(x))


def translate_seattle_time(timestr):
    return dateparser.parse(timestr[0:-6])
