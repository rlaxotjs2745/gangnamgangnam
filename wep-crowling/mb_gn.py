import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver

url_mb = "https://www.megabox.co.kr/theater/time?brchNo=1372"
url_ctmb = "https://www.megabox.co.kr/theater?brchNo=0023"


def megabox(url):
    path = "/Users/tess/Desktop/chromedriver"
    driver = webdriver.Chrome(path)
    driver.get(url)
    code = driver.page_source
    soup = BeautifulSoup(code, "html.parser")
    lists = soup.find_all("div", {"class": "theater-list"})
    movies = []
    for list in lists:
        title = list.find("div", {"class": "theater-tit"}).find("a").text
        house = list.find_all('div', {'class': 'theater-type-box'})
        d = []
        for j in house:
            theater = j.find('p', {'class': 'theater-name'}).text
            timeseat = j.find_all('div', {'class': 'txt-center'})
            f = []
            for i in timeseat:
                time = i.find('p', {'class': 'time'}).text
                seat = i.find('p', {'class': 'chair'}).text
                timechair = (time, seat)
                f.append(timechair)
            d.append({theater: f})
        movies.append({title: d})
    driver.quit()
    return movies
