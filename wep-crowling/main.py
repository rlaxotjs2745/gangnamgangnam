import requests
import os
from bs4 import BeautifulSoup
from cgv_gn import cgv(url)
from mb_gn import mb(url)
from datetime import date
from selenium import webdriver

day = str(date.today())
today = day.replace("-", "")

url_cgv = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0056&date={today}&screencodes=&screenratingcode=&regioncode="
url_mb = "https://www.megabox.co.kr/theater/time?brchNo=1372#tab02"
url_ctmb = "https://www.megabox.co.kr/theater?brchNo=0023"
