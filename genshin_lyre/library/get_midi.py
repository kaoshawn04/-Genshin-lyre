import os

import requests
import requests_html

from bs4 import BeautifulSoup
from requests_html import HTMLSession


PYPPETEER_CHROMIUM_REVISION = "1263111"
os.environ["PYPPETEER_CHROMIUM_REVISION"] = PYPPETEER_CHROMIUM_REVISION

API_KEY = "BZ51A86BLM"


def download_midi(url):
    base_url = f"https://msdl.nanomidi.net/musescore/midi"
    payload = {
        "url": url,
        "api_key": API_KEY
    }

    response = requests.get(url=base_url, params=payload).json()
    print(response)
    download_url = response["download_url"]
    name = response["score_title"]

    response = requests.get(url=download_url, stream=True)

    with open(f"./assets/sheet/midi/{name}.mid", "wb") as midi_file:
        for chunk in response.raw:
            midi_file.write(chunk)
        

def get_url(query):
    url = f"https://musescore.com/sheetmusic?text={query}"
    
    with HTMLSession() as session:
        response = session.get(url=url)
        
    response.html.render()
    
    soup = BeautifulSoup(response.html.html, "html.parser")
    scores = soup.find_all("article", class_="c9ju0 J5IQp mX2qa")
    
    for score in scores:
        instrument = score.find("div", class_="C4LKv DIiWA").a.div.get_text()
        url = score.find("div", class_="EzJvq").a["href"]
        info = score.find("div", class_="KYeND Mu94Z WJGhZ").get_text()
        info = info.split("•")
        
        if instrument == "Solo Piano":
            print(info[-2])
        
    #return scores


download_midi(url="https://musescore.com/user/38744404/scores/7093474")