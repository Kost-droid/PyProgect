import requests
from bs4 import BeautifulSoup
response = requests.get('https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level13.lecture07')
soup = BeautifulSoup (response.text, 'html.parser')
print (response.status_code)
print(soup)
