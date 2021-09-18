class snake:
    def __init__(self):
        self.previous = ""  

    def setPrevious(self,content):
        self.previous = content

    def getPrevious(self):
        return self.previous

    def move(self,key):
       if(key == self.getPrevious()):
           return
       
       self.setPrevious(key)