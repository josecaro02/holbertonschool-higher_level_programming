#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, data):
        if type(data) != int:
            raise TypeError('data must be an integer')
        else:
            self.__data = data

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) == Node or value == None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head == None:
            self.__head = Node(value)
        else:
            self.__head.data = Node(value)

    def __repr__(self):
        print(self.__head.data)
        return("")
