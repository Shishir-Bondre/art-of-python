from .linked_list import LinkedList


class HashMap(LinkedList):
    """
    Hash map for LRU cache
    """

    def __init__(self, length: int):
        self.__length = length
        self.__values = [0]*length
        super().__init__()

    def _hash_function(self, key: int):
        return self.__length % key

    def set(self, key: int, value: str):
        hash_value = self._hash_function(key)
        node = None if self.__values[hash_value] == 0 else self.__values[hash_value]
        super()._set_node_pointer(node=node)
        self.__values[hash_value] = super().add(value=value)

    def get(self, key):
        hash_value = self._hash_function(key)
        super()._set_node_pointer(node=self.__values[hash_value])
        return super().find()
