import main
from dateutil import parser
import unittest

"""
Change Data according to your current time for testing in method: Test_case1 and Test_case2...


Test_case1:
    CALL U2 India 13:00:00 14:30:00
    CALL U2 India 15:00:00 16:30:00
    
Test_Case2:
    Email - U1 - India - 18:00:00 18:30:00 Tuesday and Thursday

"""


class Simple(unittest.TestCase):

    def test_case1(self):
        # Testing If the
        # current time is between start time and end time

        # Change data according to time for testing.
        Data_List = ["CALL U2 India 13:00:00 14:30:00", "CALL U2 India 15:00:00 16:30:00",
                     "Email - U1 - India - 15:30:00 18:30:00 Tuesday and Thursday"]
        StartDay = ''
        Test_Result = []
        for data in Data_List:
            input = data.lstrip(' ').replace('-', '')
            User_Input_List = [i for i in input.split()]
            if len(User_Input_List) == 5:
                # Split the user input.
                Task_Type, User, Country, StartTime, EndTime = User_Input_List
            else:
                Task_Type, User, Country, StartTime, EndTime, StartDay, _, EndDay = User_Input_List
            StartTime, EndTime = parser.parse(StartTime), parser.parse(EndTime)
            result = main.Check_Task(Country, StartTime, EndTime, StartDay)
            Test_Result.append(result)
        self.assertListEqual(Test_Result, [False, False, True])

    def test_case2(self):
        # Testing next time when the task would
        # be picked up
        StartDay = ''

        # Change data according to time for testing.
        input = "Email - U1 - India - 18:00:00 18:30:00 Tuesday and Thursday".lstrip(' ').replace('-', '')
        User_Input_List = [i for i in input.split()]
        if len(User_Input_List) == 5:
            # Split the user input.
            Task_Type, User, Country, StartTime, EndTime = User_Input_List
        else:
            Task_Type, User, Country, StartTime, EndTime, StartDay, _, EndDay = User_Input_List
        StartTime, EndTime = parser.parse(StartTime), parser.parse(EndTime)
        result = main.Check_Task(Country, StartTime, EndTime, StartDay)
        if len(User_Input_List) > 5:
            self.assertEqual(result, f'Current datetime: {StartDay} {StartTime.strftime("%H"":""%M"":""%S")}')


if __name__ == "__main__":
    unittest.main()
