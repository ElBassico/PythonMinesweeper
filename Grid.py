import random

class Grid:

    def __init__(self, width = 0, length = 0, amount_of_bombs = 0):
        self._width = self.check_width(width)
        self._length = self.check_length(length)
        self._grid = self.create_grid()
        self._amount_of_bombs = self.check_amount_of_bombs(amount_of_bombs)
    
    def check_width(self, width):
        if width < 10:
            width = 10
        elif width > 25:
            width = 25
        return width
    
    def check_length(self, length):
        if length < 10:
            length = 10
        elif length > 25:
            length = 25
        return length

    def check_amount_of_bombs(self, amount_of_bombs):
        if (self._width * self._length) / 6 > amount_of_bombs:
            amount_of_bombs = round((self._width * self._length) / 6)
        return amount_of_bombs

    def create_grid(self):
        row = []
        column = []
        for x in range(0, self._width):
            column = []
            for y in range(0, self._length):
                column.append(0)
            row.append(column)
        return row
        
    def determine_bomb_positions(self):
        position = []
        while not len(position) == self._amount_of_bombs: 
            new_position = random.randint(0, self._length * self._width - 1)
            if len(position) == 0:
                position.append(new_position)
                continue
            counter = 0
            for y in position:
                counter = counter + 1
                if y == new_position:
                    break
                if counter == len(position):
                    position.append(new_position)
                    break
        return position

    def add_bombs_to_grid(self, bomb_position):
        bomb_position.sort()
        x = self._length
        y = 0
        counter  = 0
        while bomb_position[len(bomb_position) - 1] >= x - self._length:
            if counter == len(bomb_position):
                break
            for p in bomb_position[counter:len(bomb_position)]:
                p = p - y * self._length
                if p < self._length:
                    self._grid[y][p] = 1
                    counter += 1
                else:
                    x += self._length
                    y += 1
                    break


veld = Grid(5,5,10)
bombs = veld.determine_bomb_positions()
print(bombs)
veld.add_bombs_to_grid(bombs)
print(veld._grid)