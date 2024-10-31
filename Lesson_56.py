# @classmethod

'''
Приймає cls як перший аргумент і може працювати з атрибутами класу.
Викликається через декоратор @classmethod.
'''
#
# class Pen:  # Class клас (креслення, рецепт)
#     model = 'ballpen'  # Поле класу
#     producer = 'BIC'  # Поле класу
#
#     @classmethod
#     def change_model(cls, model):
#         cls.model = model
#
#     def __init__(self, color, width):  # метод ініціалізації \ магічний метод \ метод обʼекту класу
#         self.color = color
#         self.width = width
#         # self.color                   # поле обʼекту класу
#
#     def draw(self):                     # метод обʼекту класу
#         return (f'{self.color} line')
#
# parker = Pen('blue', 2)
# print(parker.draw())
# print(parker.model)
# Pen.change_model('Fountain pen')
# abc = Pen('blue', 2)
# print(abc.draw())
# print(abc.model)
#
# print(parker.model)



class Pen1:  # Class клас (креслення, рецепт)
    model = 'ballpen'  # Поле класу
    producer = 'BIC'  # Поле класу

    @classmethod
    def change_model(cls, model):
        cls.model = model

    def __init__(self, color, width):  # метод ініціалізації \ магічний метод \ метод обʼекту класу
        self.color = color
        self.width = width
        self.model = Pen1.model
        # self.color                   # поле обʼекту класу

    def draw(self):                     # метод обʼекту класу
        return (f'{self.color} line')

parker = Pen1('blue', 2)
print(parker.draw())
print(parker.model)
Pen1.change_model('Fountain pen')
abc = Pen1('blue', 2)
print(abc.draw())
print(abc.model)

print(parker.model)