import matplotlib.pyplot as plt
from math import pi
from math import sqrt
import random

class Circle:
    def __init__(self, x = 0, y = 0, r = 5):
        self.x = x
        self.y = y
        self.r = r

    def change_r(self, dr):
        if self.r + dr > 0:
            self.r += dr
        else:
            self.r = 0
    def change_x0(self, x0):
        self.x = x0
    def change_y0(self, y0):
        self.y = y0
        
    def square(self):
        return pi*(self.r**2)
    def inside(self, x, y):
        if (self.x - x)**2 + (self.y - y)**2 <= self.r**2:
            return True
        else:
            return False
    
    def show(self):
        figure, axes = plt.subplots()
        Drawing_colored_circle = plt.Circle(( self.x , self.y ), self.r, fill = False, color='blue')
         
        axes.set_aspect( 1 )
        axes.add_artist( Drawing_colored_circle )
        plt.title( 'Circle' )
        plt.xlim(self.x - self.r - 2, self.x + self.r + 2)
        plt.ylim(self.y - self.r - 2, self.y + self.r + 2)
        
        
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        axes.plot((0.98), (0), ls="", marker=">", ms=10, color="k", transform=axes.get_yaxis_transform(), clip_on = True)
        axes.plot(0, 0.98, ls="", marker="^", ms=10, color="k", transform=axes.get_xaxis_transform(), clip_on = True)
        plt.scatter(self.x, self.y, s = 1, color='black')
        plt.show()
    pass


a = Circle(3, 3, 1)
# b = Circle(int(input()), int(input()))
b = Circle(-3, -3, 1)

# radius = int(input())
# coordinate_x = int(input())
# coordinate_y = int(input())

# a.change_r(radius)
# a.change_x0(coordinate_x)
# a.change_y0(coordinate_y)



# случайно выбирается направление движения
# одна окружность может двигаться х + 1, у + 1 или одновременно
# вторая может двигаться на +-2 по горизонтали и по вертикали



n = 0 
while sqrt((b.x - a.x)**2 + (b.y - a.y)**2) > a.r + b.r:
    print(sqrt((b.x - a.x)**2 + (b.y - a.y)**2))
    for i in [random.choice(['x', 'y', 'xy'])]:        #c = xy
        if i == 'x':
            dx = int(random.choice(['-1', '1']))
            a.change_x0(a.x + dx)
            print(i, dx, a.x)
        elif i == 'y':
            dy = int(random.choice(['-1', '1']))
            a.change_y0(a.y + dy)
            print(i, dy, a.y)
        elif i == 'xy':
            dx = int(random.choice(['-1', '1']))
            dy = int(random.choice(['-1', '1']))
            a.change_x0(a.x + dx)
            a.change_y0(a.y + dy)
            print(i, dx, a.x, dy, a.y)
    if (a.x - b.x) > 0 and (a.y - b.y) > 0:
        if abs(a.x - b.x) > abs(a.y - b.y):
            b.change_y0(b.y + 2)
        else:
            b.change_x0(b.x + 2)
    elif (a.x - b.x) < 0 and (a.y - b.y) > 0:
        if abs(a.x - b.x) > abs(a.y - b.y):
            b.change_y0(b.y + 2)
        else:
            b.change_x0(b.x - 2)
    elif (a.x - b.x) < 0 and (a.y - b.y) < 0:
        if abs(a.x - b.x) > abs(a.y - b.y):
            b.change_y0(b.y - 2)
        else:
            b.change_x0(b.x - 2)
    elif (a.x - b.x) > 0 and (a.y - b.y) < 0:
        if abs(a.x - b.x) > abs(a.y - b.y):
            b.change_y0(b.y - 2)
        else:
            b.change_x0(b.x + 2)
    elif (a.x - b.x) == 0:
        if a.y > b.y: 
            b.change_y0(b.y + 2)
        else:
            b.change_y0(b.y - 2)
    elif (a.y - b.y) == 0:
        if a.x > b.x: 
            b.change_x0(b.x + 2)
        else:
            b.change_x0(b.x - 2)
    n +=1
    
    figure, axes = plt.subplots()
    Drawing_colored_circle_1 = plt.Circle(( a.x , a.y ), a.r, fill = False, color='blue')
    Drawing_colored_circle_2 = plt.Circle(( b.x , b.y ), b.r, fill = False, color='red')
     
    axes.set_aspect( 1 )
    axes.add_artist( Drawing_colored_circle_1 )
    axes.add_artist( Drawing_colored_circle_2 )
    plt.title( 'Circles are moving' )
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    
    
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    axes.plot((0.98), (0), ls="", marker=">", ms=10, color="k", transform=axes.get_yaxis_transform(), clip_on = True)
    axes.plot(0, 0.98, ls="", marker="^", ms=10, color="k", transform=axes.get_xaxis_transform(), clip_on = True)
    plt.scatter(a.x, a.y, s = 1, color='blue')
    plt.scatter(b.x, b.y, s = 1, color='red')
    plt.show()

print(n, a.x, a.y, sqrt((b.x - a.x)**2 + (b.y - a.y)**2))
# (x1, y1), (x2, y2)
#  0   0      2, 3
# (x1 - x2)  (y1 - y2)