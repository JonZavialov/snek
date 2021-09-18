class board:
    def __init__(self, size):
        self.dimensions = size
    
    def render(self):
        """renders the board with the provided dimensions"""
        #top
        self.renderHoriz()
        #sides
        self.renderVert()
        #bottom
        self.renderHoriz()

    def renderHoriz(self):
        """renders horizontal border with the provided dimensions"""
        print('+-', end='')
        for i in range (self.dimensions):
            print('--', end='')
        print('-+')

    def renderVert(self):
        """renders vertical border with the provided dimensions"""
        for i in range (self.dimensions):
            print('| ', end='')
            for f in range (self.dimensions):
                print('  ', end='')
            print(' |')