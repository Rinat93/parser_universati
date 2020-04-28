import re
import textwrap
import os
import scrapy


class FileSystems:
    text: str
    urls: str

    def __init__(self, urls: str, width_str: int = 80, settings: dict = None):
        self.settings = settings
        self.urls = urls
        if not settings:
            raise Exception("Нет объекта настроек!")

    def start(self, html: scrapy.selector.SelectorList):
        """
            Запуск сохранение результата парсинга в файл
        """
        self.text = self.reformat(html)
        self.save()

    def reformat(self, html: scrapy.selector.SelectorList):
        """ Форматируем текст """
        res = ''.join(html.extract())

        for txt in html.css('a,h1,h2,h3'):
            # Форматируем ссылки
            if txt.attrib.get('href'):
                res = res.replace(''.join(txt.extract()),"{}[{}]".format(txt.css('::text').get(),
                                                                    txt.attrib['href']))
            else:
                # Форматируем абзацы
                res = res.replace(''.join(txt.extract()), "***{}***".format(txt.css('::text').get()))

        res = scrapy.selector.Selector(text=res).css('::text').getall()
        return textwrap.fill(''.join(res), width=self.settings.get('LINE_MAX_LENGTH', 80)).replace('***', '\n\n')

    def save(self):
        path = re.sub(self.settings['TEMPLATE_REGULAR_FILE'], '', self.urls)
        path_to_file = re.sub(r"(\.html)|(\.php)|(\.htm)|(\.shtml)|(\.asp)|(\.aspx)", '.txt', path)

        """
            Если в ссылке нет названия шаблонов то необходимо преобразовать
            последное слово в имя файла
        """
        if path == path_to_file:
            path_to_file += '.txt'
        name_file = path_to_file.split('/')[-1]
        path_to_file = './sites/{}'.format('/'.join(path_to_file.split('/')[:-1]))
        if not os.path.exists(path_to_file):
            os.makedirs(path_to_file, exist_ok=True)
        with open('{}/{}'.format(path_to_file,name_file), 'w') as files:
            if len(self.text) > 0:
                files.write(self.text)