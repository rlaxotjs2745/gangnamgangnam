import requests
import os
from bs4 import BeautifulSoup
from datetime import date
from selenium import webdriver
from mb_gn import megabox
from cgv_gn import cgv

day = str(date.today())
today = day.replace("-", "")

url_cgv = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0056&date={today}&screencodes=&screenratingcode=&regioncode="
url_mb = "https://www.megabox.co.kr/theater/time?brchNo=1372#tab02"
url_ctmb = "https://www.megabox.co.kr/theater?brchNo=0023"

cgv = cgv(url_cgv)
megabox_gn = megabox(url_mb)
megabox_ct = megabox(url_ctmb)
