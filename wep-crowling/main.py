import requests
import os
from bs4 import BeautifulSoup

url_mb = "https://www.megabox.co.kr/theater/time?brchNo=1372#tab02"
url_cgv = "http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0056&date=20210206"
url_ctmb = "https://www.megabox.co.kr/theater?brchNo=0023"

response = requests.get(url_mb)
text = BeautifulSoup(response.text, "html.parser")
list = text.find("div", {"class": "inner-wrap pt40"})
print(list)
