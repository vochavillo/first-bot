# my first bot


hello




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

# Data transformations

Filters the calls by date
Divides the count between the calls from the last seven days and the calls from the previous week
Counts the number of deaths by looking at the number of times the Seattle Times writes a story in an overlapping period about fires and that mentions death

# Example story

In the last week, there were X calls to the fire department. Here is a map of the locations of those calls.

Of Y of those X calls were confirmed fires and resulted in the death of at least one civilian.

References
