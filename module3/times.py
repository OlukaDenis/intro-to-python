# Midnight: 12:00 AM - 1:00 AM (00:00 - 01:00)
# Late Night: 1:00 AM - 5:00 AM (01:00 - 05:00)
# Dawn: 5:00 AM - 7:00 AM (05:00 - 07:00)
# Morning: 7:00 AM - 12:00 PM (07:00 - 12:00)
# Afternoon: 12:00 PM - 5:00 PM (12:00 - 17:00)
# Evening: 5:00 PM - 9:00 PM (17:00 - 21:00)
# Night: 9:00 PM - 12:00 AM (21:00 - 00:00)

counter = 2;
counter += 2 # counter = counter + 2

print('Enter the current hour in 24 hr format: ')
hour = input()

if hour.isdigit():
    formatted_hour = int(hour)
    if formatted_hour >= 0 and formatted_hour <= 1:
        print('Midnight')
    elif formatted_hour > 1 and formatted_hour <= 5:
        print('Late night')
    elif formatted_hour > 5 and formatted_hour <= 7:
        print('Dawn')
    elif formatted_hour > 7 and formatted_hour <= 12:
        print('Morning')
    elif formatted_hour > 12 and formatted_hour <= 17:
        print('Afternoon')    
    elif formatted_hour > 17 and formatted_hour <= 21:
        print('Evening')  
    else:
        print('Night')     
else:
    print('Hours must be digits!!')
