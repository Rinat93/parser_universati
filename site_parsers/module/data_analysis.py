'''
    Решено было сделать хранилище данных в бинарном дереве, что-бы более удобно работать с элементами
'''
import re
class TreeBase:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data

    # Добавляем новый элемент в дерево
    def insert(self,data):
        if self.data:
            if len(data) < len(self.data):
                if self.left is None:
                    self.left = TreeBase(data)
                else:
                    self.left.insert(data)
            elif len(data) > len(self.data):
                if self.right is None:
                    self.right = TreeBase(self.data)
                else:
                    self.right.insert(self.data)
                self.data = data
        else:
            self.data = data

    # Для вывода дерева
    def ListTree(self):
        if self.right:
            self.right.ListTree()
        if self.left:
            self.left.ListTree()

    def FormatingData(self):
        self.data = re.sub(r'')
# b = TreeBase()
# for i in [[1,2,3],[4,4,4,4,4,4],[213,5],[2],[4,4,5,1,5,5,6,7]]:
#     b.insert(i)
#
# # print(b.data)
# print(b.ListTree())
# for i in b:
#     print(i)