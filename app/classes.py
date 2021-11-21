import random


class Rooms:
    def __init__(self, room, width=10, height=10):
        self.__width = width
        self.__height = height
        self.start_room = room
        self.position = self.start_position()
        self.rooms = self.generate_rooms()
        self.names = [(1, 'Спальня'),
                      (2, 'Холл'),
                      (3, 'Кухня'),
                      (4, 'Подвал'),
                      (5, 'Коридор'),
                      (6, 'Гостевая'),
                      (7, 'Зал')]
        self.directions = [((-1, 0), 'Север'),
                           ((1, 0), 'Юг'),
                           ((0, -1), 'Запад'),
                           ((0, 1), 'Восток')]

    def generate_rooms(self) -> object:
        rooms = [[random.randint(1, 7) for _ in range(self.__width)] for _ in range(self.__height)]
        # формируем стены (обозначение - 0)
        for i in range(self.__width):
            rooms[0][i] = 0
            rooms[self.__height - 1][i] = 0
        for i in range(self.__height):
            rooms[i][0] = 0
            rooms[i][self.__width - 1] = 0
            # формируем выходы с каждой стороны (обозначение - -1)
        rooms[0][random.randint(1, self.__width - 2)] = -1
        rooms[self.__height - 1][random.randint(1, self.__width - 2)] = -1
        rooms[random.randint(1, self.__height - 2)][0] = -1
        rooms[random.randint(1, self.__height - 2)][self.__width - 1] = -1
        return rooms

    def get_name(self):
        room = self.rooms[self.position[0]][self.position[1]]
        for i in self.names:
            if room in i:
                return i[1]

    def start_position(self):  # дописать обход по часовой стрелке
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while self.start_room != self.rooms[self.position[0]][self.position[1]]:
            self.change_position(self, directions[i])
        return (self.position[0], self.position[1])

    def can_move(self, direction):
        new_pos = (direction[0] + self.position[0], direction[1] + self.position[1])
        if self.__height > new_pos[0] > -1 and self.__width > new_pos[1] > -1:
            return new_pos[0], new_pos[1]
        else:
            return False

    def change_position(self, direction):
        if self.can_move(direction):
            self.position = self.can_move(direction)
