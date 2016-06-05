from graphics import Graphics

class PacmanGraphics():

    def __init__(self):
        self.graphics = Graphics()

    def initialize(self, state):
        self.layout = state.layout
        #self.startGraphics() - graphics started by creation of Graphics()
        self.drawObjects()

    def startGraphics(self):
        pass

    def drawObjects(self):
        
        pass
        



################################################## MAIN ###        

if __name__ == '__main__':

    print 'pacmangraphics'
    pg = PacmanGraphics()
    pg.initialize()
    
    print 'done'
