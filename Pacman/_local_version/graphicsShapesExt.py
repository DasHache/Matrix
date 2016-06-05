#import Tkinter
from graphics import Graphics, Pos
        
class Shape():

    def __init__(self, canvas, pos):
        self.c = canvas
        self.x = pos[0]
        self.y = pos[1]
        self.color = 'black'
        self.size = 10
        self.items = []
        self.__draw__()

    def __draw__(self):
        x1,y1 = self.x-self.size, self.y-self.size
        x2,y2 = self.x+self.size, self.y+self.size
        l1 = self.c.create_line(x1,y1,x2,y2,fill=self.color)
        l2 = self.c.create_line(x1,y2,x2,y1,fill=self.color)
        self.items.append(l1)
        self.items.append(l2)
        
    def __delete__(self):
        for l in self.items:
            self.c.delete(l)
            
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.__delete__()
        self.__draw__()

    def paint(self, color):
        self.color = color
        self.__draw__()
        
        
class CircleShape(Shape):

    def __init__(self, canvas, pos, rad, color):
        Shape.__init__(self, canvas, pos)
        self.color = color
        self.size = rad
        self.__draw__()

    def __draw__(self):
        x1,y1 = self.x-self.size, self.y-self.size
        x2,y2 = self.x+self.size, self.y+self.size
        i1 = self.c.create_oval(x1,y1,x2,y2,fill=self.color)
        self.items.append(i1)

        
################################################## MAIN ###        

grid_size = 100
rad = 0.5

g = Graphics()
canvas = g.canvas

############################## Circle

x,y,r = Pos(1, 1, rad)
Circle(canvas, (x, y), r, 'yellow')

x,y,r = Pos(1, 2, rad)
Circle(canvas, (x, y), r, 'red')

x,y,r = Pos(1, 4)
rect =   Rect(canvas, (x,y), r, 'blue')


############################## Shape
x,y,r = Pos(3, 3)
s = Shape(canvas, (x,y))
s.move(0,-50)

x,y,r = Pos(5,1)
Shape(canvas, (x,y))


############################## Circle Shape

x,y,r = Pos(3, 1, rad)
circle = CircleShape(canvas, (x,y), r, 'green')
#rect =   RectShape(canvas, (x,y), r, 'blue')
circle.move(0,10)
circle.paint('red')
#rect.paint('red')


