from bs4 import BeautifulSoup
import requests
import re

class Parser:
    def url_reguest(self, request):
        url = requests.get(request)
        
        #используем фреймворк
        soup = BeautifulSoup(url.text, "html.parser")
        links = []
        
        #ищем ссылки с заданными параметрами
        for link in soup.findAll('a'):
            link = link.get('href')
            if link.startswith('http'):
                links.append(link)

        return links


