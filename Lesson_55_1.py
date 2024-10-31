# @staticmethod

'''
Використовується для методів, які логічно пов'язані з класом, але не використовують його атрибути.
Викликається через декоратор @staticmethod.
'''


class Pen:  # Class клас (креслення, рецепт)
    model = 'ballpen'  # Поле класу
    producer = 'BIC'  # Поле класу

    @staticmethod
    def pen_strong(lenght, strenght):
        if lenght > strenght:
            return 'Broken'
        else:
            return 'Passed'

    def __init__(self, color, width):  # метод ініціалізації \ магічний метод \ метод обʼекту класу
        self.color = color
        self.width = width
        # self.color                   # поле обʼекту класу

    def draw(self):  # метод обʼекту класу
        return (f'{self.color} line')


parker = Pen('blue', 2)
print(parker.draw())

print(parker.pen_strong(2, 3))
print(Pen.pen_strong(2, 3))
