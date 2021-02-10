import requests
import os
from bs4 import BeautifulSoup
from datetime import date

day = str(date.today())
today = day.replace("-", "")

url_cgv = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0056&date={today}&screencodes=&screenratingcode=&regioncode="

response = requests.get(url_cgv)
soup = BeautifulSoup(response.text, "html.parser")
information = soup.find_all('div', {'class': 'col-times'})

moviess = []
for movie in information:
    text = movie.find_all('strong')
    for i in text:
        j = i.text
        title = j.replace("\r\n", "").strip()
    tim = movie.find_all("div", {"class": "info-timetable"})
    for u in tim:
        y = u.find_all("li")
        for t in y:
            time = t.find("em").text
            seat = t.find("span", {"class": "txt-lightblue"})
            if seat == None:
                seat = "<span>좌석없음</span>"
            seat = seat.text
            timeseat = (time, seat)
            movies = {title: timeseat}
            moviess.append(movies)
print(moviess)
