# -*- coding:utf-8 -*-

import time as time_lib
import requests
from bs4 import BeautifulSoup
import pywhatkit
import os
import webbrowser

def get_latest_earthquake_data():
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table")
    if table:
        earthquake_rows = table.find_all("tr")[1:]
        latest_earthquake_row = earthquake_rows[0]
        columns = latest_earthquake_row.find_all("td")
        date = columns[0].text
        magnitude = columns[5].text
        depth = columns[3].text
        location = columns[6].text
        earthquake_info = f" >>>>>>>>>>>>>>>Yeni deprem olcumu yapildi! Tarih: {date}, Siddet: {magnitude}, Derinlik: {depth}, Yer: {location} "
        return earthquake_info
    
previous_data = None

while True:
    earthquake_data = get_latest_earthquake_data()
    if earthquake_data != previous_data:
        print(earthquake_data)
        previous_data = earthquake_data
        webbrowser.open('https://google.com/', new=2)
        pywhatkit.sendwhatmsg_to_group_instantly("BxorFLiL13C4qGbdEz6Zr2", get_latest_earthquake_data())
        time_lib.sleep(5)
        os.system("taskkill /f /im msedge.exe")


    time_lib.sleep(60) # Verileri her 60 saniyede tekrar kontrol et

