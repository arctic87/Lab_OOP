from html_parser import Parser

list1 = Parser.url_reguest(None, "http://google.com")
list2 = Parser.url_reguest(None, "http://google.com")

search_different = list(set(list1)-set(list2))

print(search_different)

print(list1[5])
list_level2 = Parser.url_reguest(None, list1[5])
print(list_level2)
