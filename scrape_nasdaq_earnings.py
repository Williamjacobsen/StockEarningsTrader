# https://api.nasdaq.com/api/calendar/earnings?date=2023-06-19

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
import pickle
from datetime import datetime
import json

options = Options()
#options.add_argument('--headless')
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(driver, 20)

os.system("cls")

def clickElement(xpath):
    try:
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        element = driver.find_element_by_xpath(xpath)
        element.click()
    except Exception:
        print("\nCould not click element\n")

def locateElement(xpath):
    try:
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        element = element[0].get_attribute('innerHTML')
        element = BeautifulSoup(element, features="lxml")
        element = element.text
        return element
    except Exception: 
        print("\nCould not locate element\n")
        return ""

def send_keysElement(xpath, keys):
    try:
        element = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        element = driver.find_element_by_xpath(xpath)
        element.send_keys(keys)
    except Exception:
        print("\nCould not send keys\n")

class handle_dates():
    def two_digit_date(self, num):
        """Input: '7', Output: '07'"""

        if len(str((num))) < 2:
            return "0" + str(num)
        return num

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

        if month == 1 and days == 1:
            return f"{year - 1}-{12}-{31}"

        new_days = days + add_days
        days_in_month = month_days[self.two_digit_date(date.split('-')[1])]

        if new_days > days_in_month:
            return f"{year}-{self.two_digit_date(month + 1)}-{self.two_digit_date(new_days - days_in_month)}"

        elif 1 > new_days:
            return f"{year}-{self.two_digit_date(month - 1)}-{(month_days[self.two_digit_date(str(month - 1))]) - (-add_days - days)}"

        return f"{year}-{self.two_digit_date(month)}-{self.two_digit_date(new_days)}"

def save_data(result):
    with open("nasdaq_earnings.json", "r") as f:
        data = json.loads(f.read())
        data.append(result)
        f.close()

    with open("nasdaq_earnings.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()

def run():
    date = "2023-06-20"
    while True:
        data = []
        date = handle_dates().add_days_to_date(date, -1)
        driver.get('https://api.nasdaq.com/api/calendar/earnings?date=' + date)
        try:
            for stock in json.loads(locateElement('/html'))['data']['rows']:
                data.append({"date": date, "symbol": stock['symbol'], "marketCap": stock['marketCap']})
            save_data(data)
        except Exception as e:
            pass
        time.sleep(1)

if __name__ == '__main__':
    run()