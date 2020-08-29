import requests
import json

#CONSTANTS
JSON_RAW = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
WIKI_URL = 'https://ru.wikipedia.org/wiki/'
CU_FILE = 'country_url.json'


country_list = []
wiki_list = []
#stop_counter = 0

class CountryURL:
    """
    CountryURL is a class that gets the country name from JSON open source file (https://github.com/mledoze/countries/blob/master/countries.json) and
    searches for Wiki URL, saves it in local JSON set
    """

    def __init__(self, url=JSON_RAW):
        self.stop_counter = 1
        response = requests.get(url)
        print('Список стран будем брать отсюда:', url)
        # print(response, response.content)
        # print('***', response.json())

        # сохраняю локальную копию файла
        with open('countries.json', 'w', encoding='utf-8') as f:
            data = response.json()
            #print('***', type(response.json()), response.json()) #list!!!!
            json.dump(data, f, ensure_ascii=False, indent=4)

        # отбираю названия стран
        with open('countries.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            #print(type(data), data)
            for element in data:
                #print(element['name']['common'])
                country_list.append(element['name']['common'])
            #print(len(country_list), country_list)
        #return country_list

    def __iter__(self):
        pass
        return self

    def __next__(self):
        # генерирую страницы Вики
        for element in country_list:
            wiki_list.append(f'{WIKI_URL}{element}')
        #print(wiki_list)

        # "склеиваю" полный словарь страна-ссылка
        country_url = {}
        for number in range(len(country_list)):
            # print(country_list[number])
            # print(wiki_list[number])
            # print()
            country_url[country_list[number]] = wiki_list[number]
        # print(len(country_url), country_url)

        # сохранение результата в файл
        with open(CU_FILE, 'w', encoding='utf-8') as f:
            json.dump(country_url, f, ensure_ascii=False, indent=4)
        print('Список стран со ссылками Википедии успешно сохранен в локальный файл:', CU_FILE)

        #условие выхода из бесконечного цикла
        #global stop_counter
        self.stop_counter += 1
        if  self.stop_counter == len(country_list):
            raise StopIteration









