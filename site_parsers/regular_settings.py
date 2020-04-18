# Какие классы стоит отсеивать
IGNORE_CLASS = ['sidebar','banner','ads','footer','nav']
# Шаблон регулярного выражения для каждого элемента DOM
TEMPLATE_REGULAR = '(?!.*{VARIABLE})'

# Шаблон для разбора URL в путь до файла
TEMPLATE_REGULAR_FILE = r"^((https:\/\/)(www\.)|(http:\/\/)|(www\.))"
# Глобальный шаблон регулярного выражения
GLOBAL_REGULAR_SETTINGS = r'^({VARIABLE}.*)$'