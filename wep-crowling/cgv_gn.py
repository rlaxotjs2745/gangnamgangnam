import requests
import os
from bs4 import BeautifulSoup
from datetime import date

day = str(date.today())
today = day.replace("-", "")

url = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0056&date={today}&screencodes=&screenratingcode=&regioncode="
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
information = soup.find_all('div', {'class': 'col-times'})
moviess = []
for m in information:
    text = m.find_all('strong')
    tim = m.find_all("div", {"class": "info-timetable"})
    for i in text:
        j = i.text
        title = j.replace("\r\n", "").strip()
    for u in tim:
        y = u.find_all("li")
        for t in y:
            time = t.find("em").text
            seat = t.find("span", {"class": "txt-lightblue"})
            try:
                seat = seat.text
            except:
                seat = "좌석없음"
            timeseat = (time, seat)
            movies = {title: []}
            movies[title] = timeseat
            moviess.append(movies)
print(moviess)
