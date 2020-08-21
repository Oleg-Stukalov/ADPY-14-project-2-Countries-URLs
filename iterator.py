import requests
import json

#CONSTANTS
JSON_RAW = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
WIKI_URL = 'https://ru.wikipedia.org/wiki/'


class CountryURL:
    """
    CountryURL is a class that gets the country name from JSON open source file (https://github.com/mledoze/countries/blob/master/countries.json) and
    searches for Wiki URL, saves it in local JSON set
    """

    def __init__(self):
        pass

    def get_request(self, url=JSON_RAW):
        response = requests.get(url)
        print('Список стран будем брать отсюда:', url)
        #print(response, response.content)
        #print('***', response.json())
        return response.json()

    def get_country(self):
        response = self.get_request()
        #сохранение локальной копии файла
        with open('countries.json', 'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)

        #отбираю названия стран
        with open('countries.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        #print(type(data), data)
        country_list = []
        for element in data:
            #print(element['name']['common'])
            country_list.append(element['name']['common'])
        #print(len(country_list), country_list)

        #генерирую страницы Вики
        wiki_list = []
        for element in country_list:
            wiki_list.append(f'{WIKI_URL}{element}')
        #print(wiki_list)

        #склеиваю полный словарь страна-ссылка
        country_url = {}
        for number in range(len(country_list)):
            # print(country_list[number])
            # print(wiki_list[number])
            # print()
            country_url[country_list[number]] = wiki_list[number]
        # print(len(country_url), country_url)

        # сохранение локальной копии файла
        with open('country_url.json', 'w', encoding='utf-8') as f:
            json.dump(country_url, f, ensure_ascii=False, indent=4)
        print('Список стран со ссылками Википедии успешно сохранен в локальный файл: country_url.json')






