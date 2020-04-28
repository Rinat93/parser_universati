# Какие классы стоит отсеивать
# IGNORE_CLASS = ['sidebar','banner','ads','footer','nav','js','script']
# # Шаблон регулярного выражения для каждого элемента DOM
# TEMPLATE_REGULAR = '(?!.*{VARIABLE})'

# Шаблон для разбора URL в путь до файла
TEMPLATE_REGULAR_FILE = r"^((https:\/\/)|(www\.)|(http:\/\/)|(www\.))|(\/)$"

TAGS_ALLOWED = ['p', 'h1','h2','h3','span']

LINE_MAX_LENGTH = 80

# Глобальный шаблон регулярного выражения
# GLOBAL_REGULAR_SETTINGS = r'^({VARIABLE}.*)$'