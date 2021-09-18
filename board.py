class board:
    def render(dimensions):
        """renders the board with the provided dimensions"""
        def renderHoriz(dimensions):
            """renders horizontal border with the provided dimensions"""
            print('+-', end='')
            for i in range (dimensions):
                print('--', end='')
            print('-+')

        def renderVert(dimensions):
            """renders vertical border with the provided dimensions"""
            for i in range (dimensions):
                print('| ', end='')
                for f in range (dimensions):
                    print('  ', end='')
                print(' |')
        
        #top
        renderHoriz(dimensions)
        #sides
        renderVert(dimensions)
        #bottom
        renderHoriz(dimensions)