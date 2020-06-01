from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


class Parser:
    def url_request(self, url):
        # получение начальной страницы
        page = urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")
        # Задаем список ссылок
        links = []

        # Выборка ссылок со страницы
        for link in soup.find_all('a'):
            link = link.get('href')
            if link.startswith("http"):
                links.append([link])
            else:
                break
        return links








