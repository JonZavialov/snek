class boardNode:
  def __init__(self):
    self.direction = "right"
    self.content = ' '

  def getDir(self):
    return self.direction

  def setDir(self,dir):
    self.direction = dir

  def getContent(self):
    return self.content

  def setContent(self,content):
    self.content = content