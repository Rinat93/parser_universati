# Руководство
    Запустить парсер
        scrapy crawl task -a url=URL_SITE
    Все правила для фильтрации данных находятся в:
        site_parsers/custom_settings.py
        
# Настройки

TEMPLATE_REGULAR_FILE - регулярное выражение для преобразование ссылки в имя/путь файла

TAGS_ALLOWED - Допустимые теги

LINE_MAX_LENGTH - Максимальная длинна строки