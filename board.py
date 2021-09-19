class board:
    def __init__(self, sizeX, sizeY):
        self.board = """"""
        self.X = sizeX
        self.Y = sizeY
        self.arr = []

        for y in range (sizeY):
            arr = []
            for x in range (sizeX):
                arr.append(' ')
            self.arr.append(arr)

        board.setBoard(self)

    def render(self):
        print(self.getBoard())

    def setBoard(self):
        """sets the board"""
        self.clearBoard()
        #top
        self.setHoriz()
        #sides
        self.setVert()
        #bottom
        self.setHoriz()

    def setHoriz(self):
        """sets horizontal border"""
        self.board +=  '+'
        for i in range (self.X):
            self.board += '-'
        self.board += '+\n'

    def setVert(self):
        """sets vertical border"""
        for y in range (self.Y):
            self.board += '|'
            for x in range (self.X):
                self.board += self.arr[y][x]
            self.board += '|\n'

    def clearBoard(self):
        self.board = """"""

    def getBoard(self):
        return self.board

    def setBoardPos(self,x,y,content):
        self.arr[y][x] = content
        self.setBoard()

    def getBoardPos(self,x,y):
        return self.arr[y][x]