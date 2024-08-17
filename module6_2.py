class Vehicle:
    __COLOR_VARIANTS = ['black', 'ХАКИ', 'Баклажан']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность движка:  {self.__engine_power}"

    def get_color(self):
        return f"Цвет:  {self.__color}"

    def owner_(self):
        return f'Владелец: {self.owner}'

    def set_color(self, new_color):
        if str.lower(new_color) in list(map(str.lower, Vehicle.__COLOR_VARIANTS)):
            self.__color = new_color
            return self.__color
        else:
            print(f' Нельзя изменить цвет на {new_color}\n')
    def print_info(self):
        print('',vehicle1.get_model(),'\n',vehicle1.get_horsepower(),'\n',vehicle1.get_color(),'\n',vehicle1.owner_())

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Василий',  'Lada седан', 'спелая вишня', 75)

vehicle1.print_info()
print('\n Меняем данные машины и владельца:')
vehicle1.set_color('Pink')
vehicle1.owner = 'Колян'
vehicle1.set_color('Баклажан')
vehicle1.print_info()










