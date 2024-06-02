import math


class Figure:
    """
    Базовий клас для геометричних фігур
    """

    def __init__(self, name):
        """
        Ініціалізація фігури з назвою

        :param name: назва фігури
        """
        self.name = name

    def perimeter(self):
        """
        Обчислення периметра фігури

        :return: периметр фігури
        """
        raise NotImplementedError

    def area(self):
        """
        Обчислення площі фігури

        :return: площа фігури
        """
        raise NotImplementedError


class Rectangle(Figure):
    def __init__(self, x1, y1, x2, y2):
        super().__init__("Прямокутник")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def perimeter(self):
        return 2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1))

    def area(self):
        return abs(self.x2 - self.x1) * abs(self.y2 - self.y1)


class Square(Rectangle):
    def __init__(self, x, y, side):
        super().__init__(x, y, x - side, y + side)
        self.side = side


class Circle(Figure):
    def __init__(self, x, y, radius):
        super().__init__("Коло")
        self.x = x
        self.y = y
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


def parse_input(line):
    """
    Парсинг вхідної строки для створення об'єкта фігури

    :param line: вхідна строка
    :return: об'єкт фігури
        """
    parts = line.split()
    if parts[0] == "Квадрат":
        return Square(float(parts[2]), float(parts[3]), float(parts[5]))
    elif parts[0] == "Прямокутник":
        return Rectangle(
            float(parts[2]), float(parts[3]), float(parts[5]), float(parts[6])
        )
    elif parts[0] == "Коло":
        return Circle(float(parts[2]), float(parts[3]), float(parts[5]))


def main():
    while True:
        print(
            "Формат вводу, наприклад:\nКвадрат Point1 0 0 Point2 1 1 Side 1\nПрямокутник Point1 0 0 Point2 2 3\nКоло Center 0 0 Radius 1")
        print("Введіть дані для геометричної фігури або натисніть Enter для завершення:")
        line = input()
        if not line:
            break
        print("Обробка введених даних...")
        figure = parse_input(line)
        if figure:
            print(
                f"{figure.name} Периметр {figure.perimeter():.2f} Площа {figure.area():.2f}"
            )
        else:
            print("Помилка: невірний формат даних або невідома фігура. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
