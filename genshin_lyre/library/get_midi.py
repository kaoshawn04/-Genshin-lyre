import requests
from bs4 import BeautifulSoup


url = "https://musescore.com/sheetmusic?text=%E5%8D%83%E6%9C%AC%E6%AB%BB"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
a = soup.select_one("body > div.js-page.react-container > div > section > section > main > div.G0g4K > section > article:nth-child(1) > div.dhaTG.J5IQp > div.EzJvq > a")


with open("response.txt", "w", encoding = "utf-8") as file:
    file.write(response.text)