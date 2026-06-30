from typing import List

class LinkedList:

    def __init__(self):
        self.ll = []

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.ll):
            return -1
        return self.ll[index]

    def insertHead(self, val: int) -> None:
        self.ll = [val] + self.ll

    def insertTail(self, val: int) -> None:
        self.ll.append(val)

    def remove(self, index: int) -> bool:
        if index < 0 or index >= len(self.ll):
            return False
        self.ll.pop(index)
        return True

    def getValues(self) -> List[int]:
        return self.ll