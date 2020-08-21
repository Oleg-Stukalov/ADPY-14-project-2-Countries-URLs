import requests
import json

#CONSTANTS
JSON_RAW = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'


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

        #отбираем названия стран
        country_set = set()
        with open('countries.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        #print(type(data), data)
        for element in data:
            #print(element['name']['common'])
            country_set.add(element['name']['common'])
        print(len(country_set), country_set)

            # # создание JSON-отчета
            # temp_dic = {'file_name': likes_list[number], 'size': getsize(f'{likes_list[number]}.jpg')}
            # json_output.append(temp_dic)
            # files_for_upload.append(f'{likes_list[number]}.jpg')
            #




        # сохранение имен стран
        #print(response)



        # for photo_number in range(len(response['response']['items'])):
        #     max_height = []
        #     max_width = []
        #     max_url = []
        #     for max_size in response['response']['items'][photo_number]['sizes']:
        #         max_height.append(max_size['height'])
        #         max_width.append(max_size['width'])
        #         max_url.append(max_size['url'])
        #     photo_url_set.add(max_url[max_width.index(max(max_width))])



    # def yandex_upload(self, files_for_upload):
    #     for file in files_for_upload:
    #         # доп параметры для получения ссылки на загрузку файла
    #         yandex_upload_params = {
    #             'path': f'{"id_VK-"}{id_VK}{"/"}{file}',
    #             'overwrite': 'true'
    #         }
    #         response = requests.get(YANDEX_UPLOAD_URL, params=yandex_upload_params, headers=yandex_oauth_header)
    #         put_url = response.json().get('href')
    #         # открыть файл на БИНАР чтение, передать его в яндекс!
    #         with open(file, 'rb') as f:
    #             data_4upload = f.read()
    #         response_upload = requests.put(put_url, data=data_4upload)






