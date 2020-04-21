"""
    Решено было сделать хранилище данных в бинарном дереве, что-бы более удобно
        работать с элементами
"""


class TreeBase:
    """
        Инициализируем наше дерево
    """

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """ Добавляем новый элемент в дерево """
        if self.data:
            if len(data.css('::text')) < len(self.data.css('::text')):
                if self.left is None:
                    self.left = TreeBase(data)
                else:
                    self.left.insert(data)
            elif len(data.css('::text')) > len(self.data.css('::text')):
                if self.right is None:
                    self.right = TreeBase(self.data)
                else:
                    self.right.insert(self.data)
                self.data = data
        else:
            self.data = data

    def list_tree(self):
        """ Для вывода дерева """
        if self.right:
            print(self.right.list_tree())
        if self.left:
            print(self.left.list_tree())
