"""
    Основа логики для парсинга ресурсов
"""
import scrapy
import logging
from site_parsers.module.data_analysis import TreeBase
from site_parsers.module.filesystems import FileSystems

logging.basicConfig(filename="info.log", level=logging.ERROR)


class TaskSpider(scrapy.Spider):
    """
        Основной класс который наследует Spider
    """
    name = 'task'
    urls = ''
    settings_regular = None
    global_regular = None
    file_save = None

    def __init__(self, **kwargs):
        # Обязательно должен быть указан параметр url
        if 'url' in kwargs:
            self.urls = kwargs.get('url')
            super().__init__(**kwargs)
        else:
            raise Exception('Не указали параметр поиска - url')

    # Настройки правил регулярных выражении
    def _settings_regular_init(self):
        if not self.settings.get('TEMPLATE_REGULAR_FILE'):
            raise Exception("Not TEMPLATE_REGULAR_FILE")

    def start_requests(self):
        """ Здесь происходить запрос к странице с указанием каллбэка """
        self._settings_regular_init()

        self.file_save = FileSystems(urls=self.urls, settings=self.settings)

        yield scrapy.Request(url=self.urls, callback=self.parse)

    def parse(self, response: scrapy.selector.SelectorList):
        """ Очищаем от ненужной информации """
        tree_data = TreeBase()
        for element in response.css("body>div"):
            temp = element.css(','.join(self.settings.get('TAGS_ALLOWED')))
            if temp.css('::text') == 0: continue
            tree_data.insert(temp)
        self.file_save.start(tree_data.data)
        yield tree_data.data
