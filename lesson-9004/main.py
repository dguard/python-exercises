
class Vehicle:
    # 'ff9900', '9ade00', '009100', 'ba00ff'
    __COLOR_VARIANTS = ('orange', 'lime', 'green', 'purple')

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            pass
        else:
            print(f"Нельзя сменить цвет на {new_color}.")
        self.__color = new_color

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


if __name__ == "__main__":
    # Текущие цвета __COLOR_VARIANTS = ['orange', 'lime', 'green', 'purple']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'orange')

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('pink')
    vehicle1.set_color('lime')

    vehicle1.owner = 'Alex'

    # Проверяем что поменялось
    vehicle1.print_info()
