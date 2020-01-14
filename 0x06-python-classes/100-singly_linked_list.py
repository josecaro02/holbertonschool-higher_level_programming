#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
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
        if type(value) == Node or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            new = Node(value, None)
            self.__head = new
        else:
            new = Node(value, None)
            aux = self.__head
            if value < aux.data:
                new.next_node = aux
                self.__head = new
            else:
                while aux.next_node is not None \
                        and aux.next_node.data <= value:
                    aux = aux.next_node
                if aux.next_node is None:
                    aux.next_node = new
                else:
                    new.next_node = aux.next_node
                    aux.next_node = new

    def __repr__(self):
        aux = self.__head
        while aux.next_node is not None:
            print(aux.data)
            aux = aux.next_node
        print("{:d}".format(aux.data), end="")
        return("")
