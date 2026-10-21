class MyHashSet:

    def __init__(self):
        self.numbers = [False] * 1000001

    def add(self, key: int) -> None:
        self.numbers[key] = True

    def remove(self, key: int) -> None:
        self.numbers[key] = False

    def contains(self, key: int) -> bool:
        return self.numbers[key]