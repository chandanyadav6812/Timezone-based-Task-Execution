# import libraries
from datetime import datetime
import pytz
from dateutil import parser


# Time Zone according to country....
Country_TimeZone = {'India': 'Asia/Calcutta', 'USA': 'America/New_York', 'Aus': 'Australia/Perth'}


def Check_Task(country, starttime, endtime, startday):
    try:
        time_zone = Country_TimeZone.get(country, None)
        if time_zone:
            TimeZone = pytz.timezone(time_zone)

        # get current time according timezone...
        CurrentTime = parser.parse(datetime.now(TimeZone).strftime("%H"":""%M"":""%S"))

        # Check if starttime is greater then current time..
        if CurrentTime < starttime:

            # StartDay is not None then return with Current time with Day...
            # Else return Current Time...
            if startday != '':
                # f - string formatting...
                return f'Current datetime: {startday} {starttime.strftime("%H"":""%M"":""%S")}'
            else:
                return f'Current time: {starttime.strftime("%H"":""%M"":""%S")}'
        else:

            # Return True if current time between starttime and endtime...
            if endtime > CurrentTime > starttime:
                return True
            else:
                return False

    except Exception:
        return "Please enter valid country Name..."


def main(user_input):
    # Split the user input and remove '-' with ''
    User_Input = user_input.lstrip(' ').replace('-', '')

    # Convert the user input into list
    User_Input_List = [i for i in User_Input.split()]
    StartDay = ''
    EndDay = ''
    try:
        if len(User_Input_List) == 5:
            # Split the user input.
            Task_Type, User, Country, StartTime, EndTime = User_Input_List
        else:
            Task_Type, User, Country, StartTime, EndTime, StartDay, _, EndDay = User_Input_List

        StartTime, EndTime = parser.parse(StartTime), parser.parse(EndTime)
        result = Check_Task(Country, StartTime, EndTime, StartDay)
        print(result)

        # To stop Screen
        input()

    except Exception:
        print('Please make sure use space between the input...')


if __name__ == "__main__":
    # Take input from user...
    user_input = input()
    main(user_input)
