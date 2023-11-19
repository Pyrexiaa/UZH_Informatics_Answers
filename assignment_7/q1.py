class MagicDrawingBoard:
    def __init__(self, x, y):
        if x < 1 or y < 1:
            raise Warning("Invalid board size provided")
        self.width = x
        self.height = y
        self.board = [[0 for _ in range(x)] for _ in range(y)]

    def pixel(self, coordinate):
        x, y = coordinate
        if not 0 <= x < self.width or not 0 <= y < self.height:
            raise Warning("Pixel coordinates out of bounds")
        self.board[y][x] = 1

    def rect(self, top_left, bottom_right):
        x1, y1 = top_left
        x2, y2 = bottom_right
        if x2 <= x1 or y2 <= y1 or not (0 < x2 <= self.width) or not (0 < y2 <= self.height) or not (0 <= x1 < self.width) or not (0 <= y1 < self.height):
            raise Warning("Invalid rectangle coordinates")

        for y in range(y1, y2):
            for x in range(x1, x2):
                self.board[y][x] = 1

    def img(self):
        return '\n'.join(''.join(str(pixel) for pixel in row) for row in self.board)
    
    def reset(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

# Uncomment the following code to start using your implementation
db = MagicDrawingBoard(5,2) # instantiation of a specific size
db.pixel((0,1)) # draw at one coordinate
db.rect((0,0), (1,2)) # draw a rectangle
img = db.img() # return the drawn image 
print(img)
