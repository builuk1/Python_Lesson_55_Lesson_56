'''Завдання 1
Створіть клас Circle (Коло). Для даного класу реалізуйте
ряд перевантажених операторів:
■ перевірка на рівність радіусів двох кіл (операція = =);
■ порівняння довжини двох кіл (операції >, <, <=, >=);
■ пропорційна зміна розмірів кола шляхом зміни його
радіусу (операції +, -, +=, -=).'''


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __add__(self, other):
#         result = self.radius + other
#         return result
#
#     def __eq__(self, other):
#         result = self.radius == other.radius
#         return result
#
#     def __str__(self):
#         return f"{self.radius}"
#
#
# c1 = Circle(5)
# c2 = Circle(3)
#
# print(c1 == c2)
# c1 = c1 + 10
# print(c1)
# print(c2)
# c2 = c2 + 10
# print(c2)
#
# class Circle:
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return self.value
#
#     def __add__(self, other):
#         if hasattr(other, 'value'):
#             return self.value + other.value
#         else:
#             return self.value + other
#
#     def __sub__(self, other):
#         if hasattr(other, 'value'):
#             return self.value - other.value
#         else:
#             return self.value - other
#
#     def __mul__(self, other):
#         return self.value * other.value
#
#     def __truediv__(self, other):
#         return self.value / other.value
#
#     def __eq__(self, other):
#         return self.value == other.value
#
#     def __lt__(self, other):
#         return self.value < other.value
#
#     def __le__(self, other):
#         return self.value <= other.value
#
#     def __gt__(self, other):
#         return self.value > other.value
#
#     def __ge__(self, other):
#         return self.value >= other.value
#
#     def __iadd__(self, other):
#         if self.value >= 0:
#             self.value += other
#         else:
#             print("Радіус не може бути збільшений на від'ємне число!")
#         return self
#
#     def __isub__(self, other):
#         if self.value-other>=0:
#             self.value -= other
#         else:
#             print("Радіус не може бути від'ємним!")
#         return self
#
# print(Circle(5)+Circle(5))
# print(Circle(10)-Circle(5))
# print(Circle(5)+int(5))
# print(Circle(5)<=Circle(10))
# print(Circle(5)>Circle(10))
# print(Circle(5)==Circle(5))
# circle=Circle(20)
# circle +=5
# print(circle.value)


# #Приклад качиної типізації
# class Duck:
#     def eat(self):
#         return 'Duck eat'
#
# class Dog:
#     def eat(self):
#         return 'Dog eat'
#
# class Frog:
#     def eat(self):
#         return 'Frog eat'
#
# def food_injector(animal):
#     print(animal.eat())
#
# donald = Duck()
# guffie = Dog()
# pepe = Frog()
#
# # a = int()
#
# food_injector(donald)
# food_injector(guffie)
# food_injector(pepe)
# # food_injector(a)

## CRUD
#
#
# #Приклад перевантаження методів
# class Animal:
#     def eat(self):
#         return 'Animal eat'
#
# class Duck(Animal):
#     def eat(self):
#         return 'Duck eat'
#
# class Dog(Animal):
#     def eat(self):
#         return 'Dog eat'
#
# class Frog(Animal):
#     def eat(self):
#         return 'Frog eat'
#
# def food_injector(animal):
#     print(animal.eat())
#
# donald = Duck()
# guffie = Dog()
# pepe = Frog()
#
# # a = int()
#
# food_injector(donald)
# food_injector(guffie)
# food_injector(pepe)
# # food_injector(a)

#Приклад MRO
class Animal:
    def eat(self):
        return 'Animal eat'

    def show_a(self):
        return 'a'

class Bear(Animal):
    def eat(self):
        return 'Bear eat'
    def show_b(self):
        return 'b'

class Cat(Animal):
    def eat(self):
        return 'Cat eat'
    def show_c(self):
        return 'c'


class Duck(Bear, Cat):
    def eat(self):
        return 'Duck eat'
    def show_d(self):
        return 'd'

class Elephant(Bear):
    def eat(self):
        return 'Elephant eat'
    def show_e(self):
        return 'e'


class Fox(Cat):
    def eat(self):
        return 'Fox eat'
    def show_f(self):
        return 'f'


class Owl(Duck, Elephant, Fox):
    def eat(self):
        return 'Owl eat'
    def show_o(self):
        return 'o'


def food_injector(animal):
    print(animal.eat())

donald = Duck()
