class board:
    def __init__(self, sizeX, sizeY):
        self.board = """"""
        self.X = sizeX
        self.Y = sizeY
    
    def render(self):
        """renders the board"""
        #top
        self.setHoriz()
        #sides
        self.setVert()
        #bottom
        self.setHoriz()
        
        print(self.getBoard())

    def setHoriz(self):
        """renders horizontal border"""
        self.board +=  '+'
        for i in range (self.X):
            self.board += '-'
        self.board += '+\n' 

    def setVert(self):
        """renders vertical border"""
        for i in range (self.Y):
            self.board += '|'
            for f in range (self.X):
                self.board += ' '
            self.board += '|\n'

    def getBoard(self):
        return self.board