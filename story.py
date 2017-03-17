from fire_foo import current_week_calls, last_week_calls

current_week_count =len(current_week_calls)
last_week_count = len(last_week_calls)

message =
"""
This week there were {current} 911 calls made to the Seattle Fire Department. Last week {previous} calls were made to the department.

Here is a link to a map of that most recent call: {url}.
""".format(current=current_week_count,previous=last_week_count)

print(message)
