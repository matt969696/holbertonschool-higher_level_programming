#!/usr/bin/python3
"""
Singly linked list Module
Define 2 classes :
    Node : node of a singly linked list
    SinglyLinkedList : singly linked list
"""


class Node:
    """
    Node : simple implementation of a node
    """
    def __init__(self, data, next_node=None):
        """
        Node Init : initialize a node

        Attributes:
        data (int): node value
        next:node (Node) : next node or None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for data attribute of Node object
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for data attribute of Node object
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter for next_node attribute of Node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for next_node attribute of Node object
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    SinglyLinkedList : simple implementation of linked list
    """
    def __init__(self):
        """
        List init : initialize a single linked list

        Attributes:
        head (node) : head of the list
        """
        self.__head = None

    def __str__(self):
        """
        List print : print the entire list in stdout
        """
        out = ""
        cur = self.__head
        while cur is not None:
            out = out + str(cur.data)
            cur = cur.next_node
            if cur is not None:
                out = out + '\n'
        return out

    def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted
        position in the list (increasing order)
        """
        cur = self.__head

        if cur is None or cur.data > value:
            newnode = Node(value, cur)
            self.__head = newnode
        else:
            while cur is not None and cur.data < value:
                temp = cur
                cur = cur.next_node
            newnode = Node(value, cur)
            temp.next_node = newnode
