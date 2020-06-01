from html_parser import Parser

# начальная страница
url = 'http://google.com/'

# получение списка ссылок из класса Parser
links = Parser.url_request(None, url)

# показываем ссылки
print("Ссылки с ресурса", url)
for link in links:
    print(" ->", link[0])

    # получение списка ссылок второго уровня
    links_2 = Parser.url_request(None, link[0])
    for link2 in links_2:
        print("второй уровень ->", link2[0])




