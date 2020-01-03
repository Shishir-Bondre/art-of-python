from .linked_list import LinkedList


class Lru(LinkedList):

    def __init__(self):
        self.__lru_size = None
        self.__current_size = 0
        super().__init__()

    def set_lru_size(self, size: int):
        self.__lru_size = size

    def get_lru_size(self):
        return self.__lru_size

    def get(self, element):
        if super()._find(value=element):
            super()._remove_node_for_value(value=element)
            super()._add(value=element)
            return True
        return False

    def set(self, element):

        if self.__current_size == self.__lru_size:
            super()._remove_last()
            super()._add(value=element)
        else:
            super()._add(value=element)
            self.__current_size += 1

    def see_cached_elements(self):
        return super()._traverse()
