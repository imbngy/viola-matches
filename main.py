from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd
from tqdm import tqdm

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

website = "https://www.adamchoi.co.uk/overs/detailed"

driver = webdriver.Chrome(options=options)
driver.get(website)

all_matches_btn = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')

all_matches_btn.click()

dropdown = Select(driver.find_element(By.ID, 'country')).select_by_visible_text('Italy')

WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.TAG_NAME, 'tr'))

matches = driver.find_elements(By.XPATH,'//*[@id="page-wrapper"]/div/div[4]/div[5]/detailed-team/div/div/div[2]/div/div/div[2]/table/tbody/tr')

date = []
home_team = []
score = []
away_team = []

with tqdm(total=len(matches)) as pbar:
    for match in matches:
        date.append(match.find_element(By.XPATH,'./td[1]').text)
        home_team.append(match.find_element(By.XPATH,'./td[2]').text)
        score.append(match.find_element(By.XPATH,'./td[3]').text)
        away_team.append(match.find_element(By.XPATH,'./td[4]').text)
        pbar.update(1)



driver.quit()

df = pd.DataFrame({'Date':date,'Home Team':home_team,'Score':score,'Away Team':away_team})

df.to_csv('matches.csv',index=False)

print('#######   Job done.   #######')

