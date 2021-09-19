class game:
    def __init__(self,snake,board):
        self.board = board
        self.snake = snake

    def genSnake(self):
        x = self.snake.getX()
        y = self.snake.getY()
        
        for i in range (self.snake.getLength()):
            self.board.setBoardPos(x, y, "*")
            x -= 1