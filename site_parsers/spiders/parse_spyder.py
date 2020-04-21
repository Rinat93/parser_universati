"""
    Основа логики для парсинга ресурсов
"""
import scrapy
import logging
import re
import os
from site_parsers.module.data_analysis import TreeBase
logging.basicConfig(filename="info.log", level=logging.ERROR)


class TaskSpider(scrapy.Spider):
    """
        Основной класс который наследует Spider
    """
    name = 'task'
    urls = ''
    settings_regular = None
    global_regular = None

    def __init__(self, **kwargs):
        # Обязательно должен быть указан параметр url
        if 'url' in kwargs:
            self.urls = kwargs.get('url')
            super().__init__(**kwargs)
        else:
            raise Exception('Не указали параметр поиска - url')

    # Настройки правил регулярных выражении
    def _settings_regular_init(self):
        if self.settings.get('IGNORE_CLASS'):
            # Шаблон регулярного выражения
            regular_template = '(?!.*{})'
            if self.settings.get('TEMPLATE_REGULAR'):
                regular_template = self.settings['TEMPLATE_REGULAR']
            # Создаем необходимый шаблон для регулярного выражения
            self.settings_regular = ''.join(list(map(lambda x: regular_template.format(VARIABLE=x),
                                                     self.settings['IGNORE_CLASS'])))

        """
            Если есть глобальная настройка регулярного выражения то соединяем IGNORE_CLASS 
            и объединяем его с глобальным правилом
        """
        if self.settings.get('GLOBAL_REGULAR_SETTINGS'):
            if not self.settings_regular:
                self.settings_regular = ''
            self.global_regular = self.settings['GLOBAL_REGULAR_SETTINGS'].\
                format(VARIABLE=self.settings_regular)

        if not self.settings.get('TEMPLATE_REGULAR_FILE'):
            raise Exception("Not TEMPLATE_REGULAR_FILE")

    def start_requests(self):
        """ Здесь происходить запрос к странице с указанием каллбэка """
        self._settings_regular_init()
        yield scrapy.Request(url=self.urls, callback=self.parse)

    def save_results(self, result):
        """ Сохранение результата в файл """
        print("Описание")
        print(result)
        # преобразуем ссылку в путь до файла
        path = re.sub(self.settings['TEMPLATE_REGULAR_FILE'], '', self.urls)
        path_to_file = re.sub(r"(\.html)|(\.php)|(\.htm)|(\.shtml)|(\.asp)|(\.aspx)", '.txt', path)
        """
            Если в ссылке нет названия шаблонов то необходимо преобразовать
            последное слово в имя файла
        """
        not_edit = False
        if path_to_file == path:
            not_edit = True
        path_to_file = path_to_file.split('/')
        if not path_to_file[-1]:
            name_file = path_to_file[-2]
            if not not_edit:
                name_file += '.txt'
            del path_to_file[-2]
            path_to_file = './'.join(path_to_file[1:])
            if not os.path.exists(path_to_file):
                os.makedirs(path_to_file, exist_ok=True)
            with open(path_to_file+'/'+name_file, 'w') as files:
                if len(result) > 0:
                    for line in result:
                        files.write(line)

    def parse(self, response):
        """ Очищаем от ненужной информации """

        temp_data = TreeBase()
        for element in response.css("div"):
            temp_data.insert(element.css('p'))

        self.save_results(temp_data.data)
        yield temp_data.data
