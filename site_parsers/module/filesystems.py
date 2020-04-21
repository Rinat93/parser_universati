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
        conf = []
        # formats = textwrap.fill

        # Форматируем тег <a>
        for txt in html.css('a'):
            if txt.attrib.get('href'):
                conf.append([''.join(txt.extract()),"{}[{}]".format(txt.css('::text').get(), txt.attrib['href'])])

        # Форматируем заголовки
        for head in html.css('h1,h2,h3'):
            conf.append([''.join(head.extract()), "***{}***".format(head.css('::text').get())])


        # print(conf)
        for rep in conf:
            res = res.replace(rep[0],rep[1])

        html = scrapy.selector.Selector(text=res)


        # Форматируем абзацы
        for abz in html.css('p'):
            for tags in self.settings.get('TAGS_ALLOWED'):
                res=res.replace(''.join(abz.get()),abz.get().replace('<{}>'.format(tags),'<{}>***'.format(tags)))

        print(res)
        res = scrapy.selector.Selector(text=res).css('::text').getall()

        # print(res)
        return textwrap.fill(''.join(res), width=self.settings.get('LINE_MAX_LENGTH', 80)).replace('***','\n\n')

    def save(self):
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
            path_to_file = './sites/{}'.format('/'.join(path_to_file[1:]))
            if not os.path.exists(path_to_file):
                os.makedirs(path_to_file, exist_ok=True)
            with open(path_to_file + '/' + name_file, 'w') as files:
                if len(self.text) > 0:
                    files.write(self.text)