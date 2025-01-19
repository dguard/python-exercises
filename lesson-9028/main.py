import math


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=True):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (r >= 0 and r <= 255) and (g >= 0 and g <= 255) \
            and (b >= 0 and b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        if self.sides_count == len(sides) \
            and all(map(lambda x: x > 0, sides)):
            return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


    def set_sides(self, sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color, filled=True):
        super().__init__(sides, color, filled)
        self.__radius = self._Figure__sides[0]

    def get_square(self):
        sides = self._Figure__sides
        return math.pi * math.pow(sides[0], 2)



class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self._Figure__sides
        half_perimeter = 0.5 * (sides[0] + sides[1] + sides[2])
        S = math.sqrt(half_perimeter * (half_perimeter - sides[0]) \
          * (half_perimeter - sides[1]) \
          * (half_perimeter - sides[2])
          )
        return S


class Cube(Figure):
    sides_count = 12

    def __init__(self, sides, color, filled=True):
        super().__init__(sides, color, filled)
        self._Figure__sides = [self._Figure__sides[0] for _ in range(1, self.sides_count+1)]

    def get_volume(self):
        volume = 1
        for i in range(0, 3):
            volume *= self._Figure__sides[i]
        return volume

if __name__ == '__main__':
    circle1 = Circle([10], (200, 200, 100))  # (Цвет, стороны)
    cube1 = Cube( [6], (222, 35, 130))
    Circle([10, 15, 6], (200, 200, 100))

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())

    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides([5, 3, 12, 4, 5])  # Не изменится
    print(cube1.get_sides())

    circle1.set_sides([15])  # Изменится
    print(circle1.get_sides())

    print(circle1.get_square())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    triangle1 = Triangle([10, 15, 6], (200, 200, 100))
    print(triangle1.get_square())