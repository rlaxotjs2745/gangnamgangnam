import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver

url_mb = "https://www.megabox.co.kr/theater/time?brchNo=1372"
url_ctmb = "https://www.megabox.co.kr/theater?brchNo=0023"


path = "/Users/tess/Desktop/chromedriver"
driver = webdriver.Chrome(path)
getting = driver.get(url_mb)
code = driver.page_source
soup = BeautifulSoup(code, "html.parser")
lists = soup.find_all("div", {"class": "theater-list"})

for list in lists:
    title = list.find("div", {"class": "theater-tit"}).find("a").text
    house = list.find_all('div', {'class': 'theater-type-box'})
    for j in house:
        theater = j.find('p', {'class': 'theater-name'}).text
        timeseat = j.find_all('div', {'class': 'txt-center'})
        for i in timeseat:
            time = i.find('p', {'class': 'time'}).text
            seat = i.find('p', {'class': 'chair'}).text
            timechair = (time, seat)
            theaters = {theater: timechair}
            movie = {title: theaters}
            print(movie)
driver.quit()
