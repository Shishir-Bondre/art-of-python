class Node:

    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.__head = None

    def _add(self, value):
        node = Node()
        node.data = value
        if not self.__head:
            self.__head = node
            return
        node.next = self.__head
        self.__head = node

    def _find(self, value):
        current = self.__head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def _remove_node_for_value(self, value):
        previous = self.__head
        current = self.__head
        while current:
            if current.data == value:
                previous.next = current.next
                del current
                return True
            previous = current
            current = current.next
        return False

    def _remove_last(self):
        current = self.__head
        if not self.__head:
            return False

        if not current.next:
            self.__head = None
            del current
            return True

        while current.next.next:
            current = current.next

        node_to_be_deleted = current.next
        current.next = None
        del node_to_be_deleted
        return True

    def _traverse(self):
        values = []
        if not self.__head:
            return values

        current = self.__head
        while current:
            values.append(current.data)
            current = current.next
        return values
