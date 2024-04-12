from math import sqrt
"""Задание №1"""
def number(numbers: list):
    return list(set(numbers))

number([1,2,3,4,5,5,4,3,2,1])


"""Задание №2"""
def numbers(min: int, max: int):
    return [numlist for numlist in range(min, max)]


numbers(1,10)


"""Задание №3"""
class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%s,%s)"%(self.x, self.y)

    def changes(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, x: int, y: int):
        self.x = self.x + x
        self.y = self.y + y

    def calculation_distance(self, x: int, y: int):
        return sqrt((self.x - self.y)**2+(x - y)**2)
