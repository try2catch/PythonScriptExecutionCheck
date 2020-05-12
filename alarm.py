from datetime import datetime
from datetime import timedelta


class Alarm:
    def __init__(self, days=0, hours=0, minutes=0, seconds=0):
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_expected_finish_time(self):
        return (datetime.now() + timedelta(days=self.days, hours=self.hours, minutes=self.minutes,
                                           seconds=self.seconds)).strftime('%m-%d-%y %H:%M:%S')

    def run(self):
        expected = self.get_expected_finish_time()
        while True:
            now = datetime.now().strftime('%m-%d-%y %H:%M:%S')
            # print(now, expected)
            if now == expected:
                print('Script execution time is greater than expected.')
                break
