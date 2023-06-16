# https://www.slickcharts.com/sp500

"""
['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOGL', 'TSLA', 'GOOG', 'META', 'BRK.B', 'XOM', 'UNH', 'JNJ', 'JPM', 'AVGO', 'V', 'LLY', 'PG', 'MA', 'HD', 'CVX', 'MRK', 'PEP', 'ABBV', 'KO', 'COST', 'PFE', 'WMT', 'ADBE', 'MCD', 'CRM', 'CSCO', 'AMD', 'TMO', 'BAC', 'ACN', 'NFLX', 'ORCL', 'LIN', 'ABT', 'CMCSA', 'DIS', 'TXN', 'WFC', 'DHR', 'VZ', 'INTC', 'NEE', 'PM', 'RTX', 'NKE', 'QCOM', 'BMY', 'HON', 'LOW', 'SPGI', 'UPS', 'CAT', 'COP', 'INTU', 'IBM', 'UNP', 'BA', 'AMAT', 'AMGN', 'MDT', 'SBUX', 'NOW', 'MS', 'GS', 'GE', 'ISRG', 'T', 'PLD', 'DE', 'ELV', 'BLK', 'AXP', 'LMT', 'BKNG', 'MDLZ', 'SYK', 'ADI', 'GILD', 'C', 'TJX', 'ADP', 'AMT', 'MMC', 'VRTX', 'CVS', 'LRCX', 'SCHW', 'REGN', 'CI', 'MO', 'CB', 'ZTS', 'ETN', 'SO', 'BSX', 'FI', 'TMUS', 'MU', 'PGR', 'PYPL', 'BDX', 'EQIX', 'DUK', 'CSX', 'SNPS', 'ITW', 'SLB', 'KLAC', 'AON', 'CME', 'EOG', 'CDNS', 'NOC', 'APD', 'CL', 'ICE', 'TGT', 'WM', 'HCA', 'SHW', 'ATVI', 'FCX', 'CMG', 'HUM', 'ORLY', 'MMM', 'EW', 'F', 'MCK', 'MCO', 'FDX', 'GM', 'PNC', 'MPC', 'NXPI', 'NSC', 'CCI', 'EMR', 'DXCM', 'MAR', 'ROP', 'APH', 'PXD', 'GD', 'GIS', 'MCHP', 'PH', 'MSI', 'FTNT', 'SRE', 'ADSK', 'KMB', 'AZO', 'PSA', 'USB', 'PSX', 'ECL', 'EL', 'AJG', 'MNST', 'JCI', 'D', 'BIIB', 'VLO', 'COF', 'AEP', 'OXY', 'TDG', 'TFC', 'CTAS', 'TEL', 'ANET', 'TT', 'MRNA', 'AIG', 'CTVA', 'PCAR', 'ADM', 'TRV', 'STZ', 'ON', 'EXC', 'IQV', 'MSCI', 'IDXX', 'CARR', 'AFL', 'WELL', 'YUM', 'O', 'HSY', 'HLT', 'NUE', 'HES', 'DOW', 'CPRT', 'SYY', 'WMB', 'ROST', 'OTIS', 'LHX', 'SPG', 'DG', 'ROK', 'PAYX', 'CNC', 'DHI', 'MET', 'CHTR', 'A', 'AME', 'VRSK', 'XEL', 'CSGP', 'AMP', 
'NEM', 'KMI', 'EA', 'CMI', 'PPG', 'GWW', 'ED', 'VICI', 'CTSH', 'FIS', 'BK', 'ILMN', 'DD', 'DVN', 'RMD', 'FAST', 'PRU', 'DFS', 'PEG', 'KR', 'CEG', 'WBD', 'DLR', 'BKR', 'ZBH', 'ALL', 'KEYS', 'RSG', 'MTD', 'ANSS', 'LEN', 'KHC', 'HAL', 'ODFL', 'ABC', 'DLTR', 'WEC', 'GEHC', 'AWK', 'URI', 'EFX', 'IT', 'PCG', 'VMC', 'APTV', 'DAL', 'OKE', 'KDP', 'HPQ', 'XYL', 'GPN', 'AVB', 'ALB', 'PWR', 'MLM', 'WST', 'EIX', 'IR', 'ACGL', 'STT', 'GLW', 'TROW', 'SBAC', 'CBRE', 'FTV', 'EBAY', 'WTW', 'ENPH', 'ES', 'TSCO', 'MPWR', 'CDW', 'ALGN', 
'FANG', 'CHD', 'LYB', 'MKC', 'ULTA', 'EQR', 'WBA', 'WY', 'HIG', 'GPC', 'CAH', 'BAX', 'DTE', 'TTWO', 'HPE', 'AEE', 'STE', 'FE', 'RCL', 'MTB', 'ETR', 'DRI', 'DOV', 'VRSN', 'LH', 'FICO', 'IFF', 'LUV', 'PODD', 'PPL', 'INVH', 'LVS', 'HOLX', 'OMC', 'ARE', 'EXR', 'CTRA', 'FSLR', 'CLX', 'RJF', 'EXPD', 'TDY', 'VTR', 'BR', 'WAB', 'CNP', 'COO', 'FITB', 'NVR', 'MAA', 'FLT', 'CMS', 'SWKS', 'UAL', 'STLD', 'TER', 'NDAQ', 'BALL', 'K', 'RF', 'HWM', 'ATO', 'CAG', 'PHM', 'IRM', 'PFG', 'LW', 'GRMN', 'TYL', 'SJM', 'EXPE', 'TRGP', 'MOH', 
'NTAP', 'FDS', 'CINF', 'CCL', 'WAT', 'IPG', 'IEX', 'PAYC', 'NTRS', 'HBAN', 'AMCR', 'BRO', 'SEDG', 'DGX', 'BBY', 'PTC', 'ESS', 'J', 'SYF', 'CBOE', 'RVTY', 'AKAM', 'MRO', 'SNA', 'JBHT', 'ZBRA', 'BG', 'TSN', 'EQT', 'MGM', 'AES', 'LKQ', 'TXT', 'AVY', 'EVRG', 'POOL', 'RE', 'AXON', 'LNT', 'CF', 'CFG', 'UDR', 'FMC', 'SWK', 'WDC', 'TRMB', 'KMX', 'EPAM', 'STX', 'TAP', 'NDSN', 'HST', 'MAS', 'MTCH', 'CPT', 'LYV', 'PKG', 'ETSY', 'MOS', 'HRL', 'VTRS', 'TECH', 'KIM', 'JKHY', 'BF.B', 'CE', 'WRB', 'TFX', 'IP', 'INCY', 'BWA', 'PEAK', 'L', 'LDOS', 'CHRW', 'APA', 'NI', 'DPZ', 'WYNN', 'AAL', 'CRL', 'GEN', 'TPR', 'CZR', 'QRVO', 'MKTX', 'ALLE', 'JNPR', 'HSIC', 'CDAY', 'PNR', 'FOXA', 'EMN', 'GL', 'ROL', 'REG', 'UHS', 'KEY', 'CPB', 'PNW', 'BBWI', 'AOS', 'FFIV', 'HII', 'PARA', 'XRAY', 'NRG', 'NCLH', 'WHR', 'BIO', 'HAS', 'RHI', 'BEN', 'BXP', 'CTLT', 'IVZ', 'NWSA', 'GNRC', 'WRK', 'FRT', 'AIZ', 'VFC', 'ALK', 'DXC', 'SEE', 'CMA', 'DVA', 'OGN', 'MHK', 'RL', 'FOX', 'AAP', 'ZION', 'LNC', 'NWL', 'NWS', 'DISH']
"""

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

options = Options()
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

def run():
    driver.get('https://www.slickcharts.com/sp500')
    symbols = []
    for i in range(1, 504):
        symbols.append(locateElement(f'/html/body/div[2]/div[3]/div[1]/div/div/table/tbody/tr[{i}]/td[3]/a'))
    print(str(symbols))

if __name__ == '__main__':
    run()

