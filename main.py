# import libraries
from datetime import datetime
import pytz
from dateutil import parser

"""
    Test Cases:
        CALL U2 India 13:00:00 14:30:00
        CALL U2 India 15:00:00 16:30:00
        Email - U1 - India - 15:30:00 18:30:00 Tuesday and Thursday
        
    

"""

# Time Zone according to country...
Country_TimeZone = {'India': 'Asia/Calcutta', 'USA': 'America/New_York', 'Aus': 'Australia/Perth'}


def Check_Task(country, starttime, endtime, startday):
    try:
        time_zone = Country_TimeZone.get(country, None)
        if time_zone:
            TimeZone = pytz.timezone(time_zone)
        CurrentTime = parser.parse(datetime.now(TimeZone).strftime("%H"":""%M"":""%S"))
        if CurrentTime < starttime:
            if startday != '':
                return f'Current datetime: {startday} {starttime.strftime("%H"":""%M"":""%S")}'
            else:
                return f'Current time: {starttime.strftime("%H"":""%M"":""%S")}'
        else:
            if endtime > CurrentTime > starttime:
                return True
            else:
                return False
    except Exception:
        return "Please enter valid country Name..."


# For manual testing...
# def main():
#     while True:
#         # Take input from user.
#         User_Input = input().lstrip(' ').replace('-', '')
#
#         # Convert the user input into list
#         User_Input_List = [i for i in User_Input.split()]
#         StartDay = ''
#         EndDay = ''
#         try:
#             if len(User_Input_List) == 5:
#                 # Split the user input.
#                 Task_Type, User, Country, StartTime, EndTime = User_Input_List
#             else:
#                 Task_Type, User, Country, StartTime, EndTime, StartDay, _, EndDay = User_Input_List
#
#             StartTime, EndTime = parser.parse(StartTime), parser.parse(EndTime)
#             result = Check_Task(Country, StartTime, EndTime, StartDay)
#             print(result)
#             Repeat_task_or_not = input("To continue please enter or to exit type (E) and enter..")
#             if Repeat_task_or_not == '':
#                 continue
#             elif Repeat_task_or_not == 'E':
#                 break
#             else:
#                 print('Choose wrong option restart app..')
#         except Exception:
#             print('Please make sure use space between the input...')
