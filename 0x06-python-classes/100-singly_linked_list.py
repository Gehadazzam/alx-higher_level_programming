#!/usr/bin/python3
"""
creat new class
named Node
"""


class Node:
    """define attributes"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
creat new class
named SinglyLinkedList
"""


class SinglyLinkedList:
    """define attributes"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        list = []
        new = self.__head
        while new:
            list.append(str(new.data))
            new = new.next_node
        return "\n".join(list)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new = self.__head
            while new.next_node and new.next_node.data < value:
                new = new.next_node
            new_node.next_node = new.next_node
            new.next_node = new_node
