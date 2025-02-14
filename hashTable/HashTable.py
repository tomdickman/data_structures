from typing import Union
import hashlib

class HashTable:
    datamap: list[list[Union[str, int]]]

    def __init__(self, size = 7):
        self.datamap = [None] * size

    def print(self):
        for i, v in enumerate(self.datamap):
            print(i, ': ', v)

    def __hash(self, value: str):
        buffer = value.encode('utf-8')
        hashedValue = hashlib.sha256(buffer).hexdigest()
        index = int(hashedValue, 16) % len(self.datamap)
        print(hashedValue)
        print(value, '->', index)
        return index

    def set(self, key, value):
        index = self.__hash(key)

        if not self.datamap[index]:
            self.datamap[index] = []

        self.datamap[index].append([ key, value ])

        return self

    def get(self, key):
        index = self.__hash(key)

        if not self.datamap[index]:
            return None
        for i in range(len(self.datamap[index])):
            if self.datamap[index][i][0] == key:
                return self.datamap[index][i][1]

        return None

    def keys(self):
        keyList = []

        for slot in self.datamap:
            if slot:
                for item in slot:
                    keyList.append(item[0])

        return keyList
