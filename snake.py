class snake:
    def __init__(self):
        self.previous = ""
        self.size = 3
        self.acceptableKeys = ['w','a','s','d']

    def setSize(self,size):
        self.size = 3

    def setPrevious(self,content):
        self.previous = content

    def getPrevious(self):
        return self.previous

    def parseMove(self,key):
        #todo: check if one of the accpetble keys is pressed
        if(key == self.getPrevious()):
           return
        print(key.char)
        self.setPrevious(key)