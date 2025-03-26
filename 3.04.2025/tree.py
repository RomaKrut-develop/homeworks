# In the world of blind men, one-eyed man is king...

from colorama import Style, Back, Fore

class Node:
    def __init__(self, key):
        self.left = None  # Левый дочерний узел (изначально None)
        self.right = None # Правый дочерний узел (изначально None)
        self.value = key  # Значение узла

class BinaryTree:
    def __init__(self):
        self.root = None # Инициализация дерева с пустым корнем
    
    def insert(self, key): # Метод для вставки элемента в бинарное дерево
        # Если дерево пустое, создаем корень с данным значением
        if self.root is None:
            self.root = Node(key)
        else:
            # Если дерево не пустое, вызываем рекурсивный метод вставки узлов
            self.__insert_rec(self.root, key) 
    
    def __insert_rec(self, node, key): # Рекурсивный метод для вставки элемента
        # Если ключ меньше текущего узла, вставляем в левое поддерево
        if key < node.value:
            # Если левый дочерний узел пуст, создаем новый узел
            if node.left is None:
                node.left = Node(key)
            else:
                # Иначе продолжаем рекурсивный поиск для левого поддерева
                self.__insert_rec(node.left, key)
        
        else:
            # Если ключ больше или равен текущему узлу, вставляем в правое поддерево
            if node.right is None:
                node.right = Node(key)
            else:
                # Иначе продолжаем рекурсивный поиск для правого поддерева
                self.__insert_rec(node.right, key)
    
    def inorder_traversal(self):
        # Обход дерева в порядке in-order (Левое поддерево, узел, правое поддерево)
        result = []
        self.__inorder_rec(self.root, result)
        return result

    def __inorder_rec(self, node, result):
        if node: # Проверяем, существует ли узел
            self.__inorder_rec(node.left, result) # Обходим левое дерево
            result.append(node.value) # Добавляем значение узла в результат
            self.__inorder_rec(node.right, result) # Обходим правое дерево

    def search(self, key):
        # Метод для поиска элемента в дереве
        return self.__search(self.root, key)
    
    def __search(self, node, key): # Рекурсивная функция для поиска элемента
        if node is None:
            return False # Если значение узла будет None, возвращаем False
        
        if node.value == key: # Если ключ был найден, возвращаем True
            return True
        elif key < node.value: # Мы обходим левую часть дерева
            return self.__search(node.left, key) 
        else: # Ищем в правой части дерева
            return self.__search(node.right, key)
        
    def is_empty(self): return self.root is None # Метод для проверки, пусто ли дерево

    def find_min(self):
        if self.is_empty(): return None
        return self.__find_min(self.root)

    def __find_min(self, node):
        while node.left: # Цикл, работает пока есть левые значения
            node = node.left # Присваиваем при каждой итерации левую часть
        return node.value

    def find_max(self):
        if self.is_empty():return None
        return self.__find_max(self.root)
    
    def __find_max(self,node):
        while node.right:
            node = node.right
        return node.value
    
bt = BinaryTree()
elements = [10, 20, 5, 3, 7, 15]

for el in elements:
    bt.insert(el)

bt.inorder_traversal()
bt.search(15)

bt.find_min()