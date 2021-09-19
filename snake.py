class snake:
    def __init__(self):
        self.previous = ""
        self.size = 3
        self.acceptableKeys = ['w','a','s','d']
        self.directions = ['up','left','down','right']

    def setSize(self,size):
        self.size = 3

    def setPrevious(self,content):
        self.previous = content

    def getPrevious(self):
        return self.previous

    def parseMove(self,key):
        """parses key press events"""
        try:
            #check for appectable key press
            keyPressed = False
            for posKey in self.acceptableKeys:
                if(key.char == posKey):
                    keyPressed = True
                    break
        except: pass
        
        if(key == self.getPrevious() or not keyPressed):
           return

        self.direction = self.directions[self.acceptableKeys.index(key.char)]
        self.setPrevious(key)