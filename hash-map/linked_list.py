class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:

    def __init__(self):
        self._head = None

    def _set_node_pointer(self, node):
        self._head = node

    def add(self, value):
        new_node = Node()
        new_node.data = value
        if not self._head:
            self._head = new_node
            return self._head

        new_node.next = self._head
        self._head = new_node
        return self._head

    def find(self):
        current = self._head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        return values