import datetime

class handle_dates():
    def two_digit_date(self, num):
        """Input: '7', Output: '07'"""

        if len(str((num))) < 2:
            return "0" + str(num)
        return str(num)

    def convert_date(self, date):
        """Input: 'Jul 27, 2021', Output: '2021-7-27'"""

        date = date.replace(",", "")
        year = self.two_digit_date(date[-4:])
        months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = self.two_digit_date(months.index(date[:3]))
        day = self.two_digit_date(date[4:6])
        return str(year) + '-' + str(month) + '-' + str(day)

    def is_leap_year(self, year):
        return year % 4 == 0

    def add_days_to_date(self, date, add_days = 0):
        """adds days to date (only within a month)"""

        days = int(date.split('-')[2])
        month = int(date.split('-')[1])
        year = int(date.split('-')[0])

        month_days = {
            "01": 31,
            "02": 29 if self.is_leap_year(year) else 28,
            "03": 31,
            "04": 30,
            "05": 31,
            "06": 30,
            "07": 31,
            "08": 31,
            "09": 30,
            "10": 31,
            "11": 30,
            "12": 31
        }

        while add_days != 0:
            if add_days < 0:
                days -= 1
            else:
                days += 1

            if days > month_days[self.two_digit_date(month)]:
                if month != 12:
                    month += 1
                else:
                    month = 1
                    year += 1
                days = 1
            elif days < 1:
                if month != 1:
                    month -= 1
                else:
                    month = 12
                    year -= 1
                days = month_days[self.two_digit_date(month)]
            
            if datetime.datetime(year, month, days).weekday() < 4:
                if add_days > 0:
                    add_days -= 1
                else:
                    add_days += 1

        return f"{year}-{self.two_digit_date(month)}-{self.two_digit_date(days)}"


handle_dates().add_days_to_date('2023-05-06', -600)

