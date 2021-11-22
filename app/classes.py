import random


class Rooms:
    def __init__(self, room=1, width=11, height=11):
        self.__width = width
        self.__height = height
        self.rooms = self.generate_rooms()
        self.position = self.start_position(room)
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
        rooms = [[random.randint(1, 7) for w in range(self.__width)] for h in range(self.__height)]
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
        room_name = self.rooms[self.position[0]][self.position[1]]
        for i in self.names:
            if room_name in i:
                return i[1]

    def start_position(self, room):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.position = self.__height // 2, self.__width // 2
        counter = 1
        while room != self.rooms[self.position[0]][self.position[1]]:
            for i in range(counter):
                self.change_position(directions[0])
                if room == self.rooms[self.position[0]][self.position[1]]:
                    return self.position[0], self.position[1]
            for i in range(counter):
                self.change_position(directions[1])
                if room == self.rooms[self.position[0]][self.position[1]]:
                    return self.position[0], self.position[1]
            counter += 1
            for i in range(counter):
                self.change_position(directions[2])
                if room == self.rooms[self.position[0]][self.position[1]]:
                    return self.position[0], self.position[1]
            for i in range(counter):
                self.change_position(directions[3])
                if room == self.rooms[self.position[0]][self.position[1]]:
                    return self.position[0], self.position[1]
            counter += 1
        return self.position[0], self.position[1]

    def can_move(self, direction):
        new_pos = (direction[0] + self.position[0], direction[1] + self.position[1])
        if len(self.rooms) > new_pos[0] > -1 and len(self.rooms[0]) > new_pos[1] > -1:
            return new_pos[0], new_pos[1]
        else:
            return False

    def change_position(self, direction):
        if self.can_move(direction):
            self.position = self.can_move(direction)
