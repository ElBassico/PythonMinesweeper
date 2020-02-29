class Grid:

    def __init__(self, width, length, amount_of_bombs):
        self.width = width
        self.height = height
        self.amount_of_bombs = amount_of_bombs
    
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

    def create_grid(width, length):
        row = []
        column = []
        for x in range(0,10):
            column = []
            for y in range(0,10):
                column.append(0)
            row.append(column)
