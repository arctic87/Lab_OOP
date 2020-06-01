from html_parser import Parser

#начальная страница
url = 'http://news.google.com/'

#собираем данные с сайта
list1 = Parser.url_reguest(None, url)
list2 = Parser.url_reguest(None, url)

#находим новые ссылки путем вычитания второго списка из первого
search_different = list(set(list1)-set(list2))
#выводим новые ссылки
print(search_different)

print(list1[5])
#выводим данные со второго уровня сайтов
list_level2 = Parser.url_reguest(None, list1[5])
print(list_level2)
