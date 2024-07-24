def add_time(start, duration, start_day=''):
    start_hour, start_minute = map(int, start.split()[0].split(':'))
    start_period = start.split()[1]
    duration_hours, duration_minutes = map(int, duration.split(':'))

    end_minute = start_minute + duration_minutes
    additional_hours = end_minute // 60
    end_minute %= 60
    end_hour = start_hour + duration_hours + additional_hours

    if start_period == 'PM':
        end_hour += 12

    additional_days = end_hour // 24
    end_hour %= 24

    end_period = 'AM' if end_hour < 12 else 'PM'
    end_hour = end_hour if end_hour <= 12 else end_hour - 12
    if end_hour == 0:
        end_hour = 12

    formatted_time = f'{end_hour}:{end_minute:02} {end_period}'

    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_day_of_week = ''
    days_later = ''
    if start_day:
        current_weekday = day_of_week.index(start_day.capitalize())
        new_weekday_index = (current_weekday + additional_days) % 7
        new_day_of_week = day_of_week[new_weekday_index]

        if additional_days == 1:
            days_later = '(next day)'
        elif additional_days > 1:
            days_later = f'({additional_days} days later)'

    if new_day_of_week:
        print(f"{formatted_time}, {new_day_of_week} {days_later}")
    else:
        print(f"{formatted_time} {days_later}")


add_time('8:16 PM', '466:02', 'tuesday')
