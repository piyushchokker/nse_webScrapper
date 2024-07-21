from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
import undetected_chromedriver as uc


def table():

    driver = uc.Chrome()
    driver.get("https://www.nseindia.com/get-quotes/derivatives?symbol=NIFTY&instrument=Index%20Futures")
    time.sleep(15)

    element=driver.find_element(By.XPATH,"""/html/body/div[11]/div[1]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div/table""").get_attribute('outerHTML')
    soup=BeautifulSoup(element,'lxml')

    table=soup.find('table')
    driver.quit()

    return table

titles=['Instrument Type', 'Expiry Date', 'Option', 'Strike', 'Open', 'High', 'Low', 'Close', 'Prev.Close', 'Last ', 'chng', '%Chng', 'Volume(Contracts)', 'Value(₹ Lakhs)']


df=pd.DataFrame(columns=titles)

while True:
    rows=table().find_all("tr")

    for i in rows[1:]:
        data=i.find_all("td")
        
        row=[tr.text for tr in data[1:]]
        
        l=len(df)
        df.loc[l]=row
    df.to_csv("nse_index_option.csv",index=False)

    time.sleep(40)

    
