import requests
import os
from bs4 import BeautifulSoup
from datetime import date

day = str(date.today())
today = day.replace("-", "")


def cgv(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    information = soup.find_all('div', {'class': 'col-times'})
    movies = []
    for m in information:
        text = m.find_all('strong')
        time_seat = m.find_all("div", {"class": "info-timetable"})
        for i in text:
            j = i.text
            title = j.replace("\r\n", "").strip()
        for u in time_seat:
            y = u.find_all("li")
            timeseats = []
            for t in y:
                time = t.find("em").text
                seat = t.find("span", {"class": "txt-lightblue"})
                try:
                    seat = seat.text
                except:
                    seat = "좌석없음"
                timeseat = (time, seat)
                timeseats.append(timeseat)
        movies.append({title: timeseats})
    return movies
