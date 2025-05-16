from datetime import datetime
import pytz

# List of timezones you want to display
timezones = [
    'US/Eastern',
    'US/Central',
    'US/Mountain',
    'US/Pacific',
    'Europe/London',
    'Europe/Berlin',
    'Asia/Kolkata',
    'Asia/Tokyo',
    'Australia/Sydney'
]

print("Current Time in Different Timezones:\n")

for zone in timezones:
    tz = pytz.timezone(zone)
    time_in_zone = datetime.now(tz)
    print(f"{zone:20s} : {time_in_zone.strftime('%Y-%m-%d %H:%M:%S')}")
