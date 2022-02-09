from datetime import date

event_start_date = date(2019, 12, 21)
event_end_date = date(2020, 12, 24)
delta = event_end_date - event_start_date
print(delta.days)