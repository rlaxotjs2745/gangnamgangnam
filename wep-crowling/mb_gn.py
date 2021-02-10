import requests
import os
from bs4 import BeautifulSoup
from datetime import date

url_mb = "https://www.megabox.co.kr/theater/time?brchNo=1372#tab02"

response = requests.get(url_mb)
text = BeautifulSoup(response.text, "html.parser")
list = text.find("div", {"class": "inner-wrap pt40"})
print(text)
