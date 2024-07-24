
from datetime import datetime, timedelta, date

def add_time(start, duration, start_day = ''): #add starting weekday parameter
    start_format = '%I:%M %p'
    duration_format = '%H:%M'
    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    str_1 = ''
    str_2 = ''
    new_day_of_week = ''
    start_time = datetime.strptime(start, start_format)

    if start_day:
        current_weekday = start_time.weekday() # monday is 0, sunday is 6
        target_weekday = day_of_week.index(start_day.capitalize())
        days_difference = (target_weekday - current_weekday) % 7
        start_time += timedelta(days = days_difference)


    duration_hours, duration_minutes = map(int, duration.split(':'))
    duration_delta = timedelta(hours=duration_hours, minutes=duration_minutes)

    new_time = start_time + duration_delta

    if new_time.date() == (start_time + timedelta(days=1)).date():
        str_2 = '(next day)'
    elif start_time.date() != new_time.date():
        days_difference = (new_time - start_time).days + 1
        str_2 = f"({days_difference} days later)"

    if new_time.date() == (start_time.date):
        str_1 = f'{start_day}'
    else:
        days_difference = (new_time - start_time).days
        #str_1 =
    if start_day:
        new_day_of_week = day_of_week[new_time.weekday()]
    formatted_time = new_time.strftime('%I:%M %p').lstrip('0')
    print(new_time.strftime(formatted_time), str_2, new_day_of_week)

add_time('11:00 PM', '28:10')



