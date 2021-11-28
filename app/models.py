import random
from threading import Lock


class RoomsMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Rooms(metaclass=RoomsMeta):
    def __init__(self, width=10, height=10):
        self.__width = width
        self.__height = height
        self.rooms = self.generate_rooms()
        self.position = self.start_position()
        self.message = "Добро пожаловать"
        self.names = [
            (1, "Спальня"),
            (2, "Холл"),
            (3, "Кухня"),
            (4, "Подвал"),
            (5, "Коридор"),
            (6, "Гостевая"),
            (7, "Зал"),
            (-1, "Выход"),
        ]
        self.directions = [
            "Север",
            "Юг",
            "Запад",
            "Восток",
        ]

    def generate_rooms(self) -> object:
        """создание комнат"""
        rooms = [
            [random.randint(0, 7) for _ in range(self.__width)]
            for _ in range(self.__height)
        ]
        """ формируем стены (обозначение - 0) """
        for i in range(self.__width):
            rooms[0][i] = 0
            rooms[self.__height - 1][i] = 0
        for i in range(self.__height):
            rooms[i][0] = 0
            rooms[i][self.__width - 1] = 0
        """ формируем выходы с каждой стороны (обозначение - -1) """
        rooms[0][random.randint(1, self.__width - 2)] = -1
        rooms[self.__height - 1][random.randint(1, self.__width - 2)] = -1
        rooms[random.randint(1, self.__height - 2)][0] = -1
        rooms[random.randint(1, self.__height - 2)][self.__width - 1] = -1
        return rooms

    def get_name(self):
        room_pos = self.rooms[self.position[0]][self.position[1]]
        for i in self.names:
            if room_pos in i:
                return i[1]

    def start_position(self):
        """определение стартовой позиции от средней точки в пространстве"""
        self.position = self.__height // 2, self.__width // 2
        while self.rooms[self.position[0]][self.position[1]] == 0:
            self.change_position(random.choice(self.directions))
        return self.position

    def can_move(self, direction):
        directions = {
            "Север": (-1, 0),
            "Юг": (1, 0),
            "Запад": (0, -1),
            "Восток": (0, 1),
        }
        step = directions[direction]
        """проверка возможности движения"""
        new_pos = (step[0] + self.position[0], step[1] + self.position[1])
        if self.__height < new_pos[0] or self.__width < new_pos[1]:
            return False
        elif self.rooms[new_pos[0]][new_pos[1]] == 0:
            return False
        else:
            return new_pos[0], new_pos[1]

    def change_position(self, direction):
        if self.can_move(direction):
            self.position = self.can_move(direction)
            if self.rooms[self.position[0]][self.position[1]] == -1:
                self.message = f"Поздравляем, вы вышли на улицу!"
            else:
                self.message = f"Вы переместились на {direction}"
        else:
            self.message = "Вы не можете туда идти"
