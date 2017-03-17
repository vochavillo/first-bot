Happy to report that the first bot is up and running for those of you -- and I know that there are many of you -- curious to know how many calls the Seattle Fire Department received since the start of the week, and --wait for it-- how many calls were made last week. Comparisons are nice.

The dataset was downloaded from the Seattle Fire Department's website. Link here:
https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj. The data is updated every five minutes and goes as far back as July 2, 2013. The primary column of interest is the column that lists the dates and times of the individual cases, lumped together under "Datetime." The data was downloaded as a CSV, with the CSV URL being slightly modified. To be more efficient, it was necessary to also use the Socrata API to create a URL for the dataset's CSV file that had a minimum-bound date. This step kept the bot from downloading the entire dataset when only data from two weeks back was needed.

The most onerous part of writing the code for this bot was the data transformation of the dates and times. Using the built-in 'datetime' library, the bot can easily get today's date, without asking for manual input from the user. To get a sense of the transformation necessary, with the current date as a reference, a little counting back was done to calculate the date of the start of the week in which the current date fell. Important in this was deciding what day would mark the start of the week--I decided Sunday. Once the current week's start date was determined, it was just a matter of going back another 7 days to get to the start of the previous week. A function was defined to do a count of the total number of cases within each of the two time periods. The final story reports these two numbers.

The bot itself and the information it spits out isn't exactly breaking new. However, my brother does live in Seattle and maybe he'd care, at least enough to humor me and check out how this bot works and have some quirky information he can share over meals. It's great small talk, morbidity being suspended given that I couldn't confirm which of the 911 calls were actual fires and if any of them were fires which of them resulted in any injury or death. While possible, I didn't find it worth the effort.

My initial thinking was to scrape the Seattle Times' website, filtering stories by mention of "fires," and essentially calling Python's version of our keyboard's "Find" command, using the addresses and call times as keywords. While news stories on fires always include the location of a fire that resulted in injury or death, assuming regional familiarity, the stories often do not include the street address. This meant a comparison of the street address in the CSV data set with the ideal street address that would be found as text in the story would be difficult. This word of matching addresses across two different datasets would also call for some imperfect decision-making about the different ways addresses are represented (e.g. "street," st.", "st", "avenue", "ave." "ave"). Finally, my look into the Seattle Times' archive of stories involves some proficiency with GitHub, seeing as to the news organization's reliance on GitHub to organize their stories.



Description
The number of 911 fire calls made in the last week is provided, alongside a
comparison of the count from the previous week. Also, mention of whether
any of the calls resulted in death will be provided

Arguments
Today's date

Data sources
Seattle Real Time Fire 911 Calls
https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj

# Data transformations

Filters the calls by date
Divides the count between the calls from the last seven days and the calls from the previous week
Counts the number of deaths by looking at the number of times the Seattle Times writes a story in an overlapping period about fires and that mentions death

# Example story

In the last week, there were X calls to the fire department. Here is a map of the locations of those calls.

Of Y of those X calls were confirmed fires and resulted in the death of at least one civilian.

References
