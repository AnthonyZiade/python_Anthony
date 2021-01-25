import pgzrun

WIDTH = 1600
HEIGHT = 900

hoop = Actor("hoop")
hoop.pos = (800, 100)
speed = 0

line = Actor("line")
line.pos = (800, 400)
speed = 0

kdjumper = Actor("kdjumper")
kdjumper.pos = (1400, 200)
speed = 0

bball = Actor("bball")
bball.pos = (1400, 150)
speed = 0

p_text = ""


class Tony:
    def __init__(self):
        self.speed_x = 0
        self.speed_y = 0
    @property
    def speed_x(self):
        return self._speed_x
    @speed_x.setter
    def speed_x(self,value):
        self._speed_x = value
    @property
    def speed_y(self):
        return self._speed_y
    @speed_y.setter
    def speed_y(self,value):
        self._speed_y = value

D = Tony()

def draw():
    screen.fill("white")
    line.draw()
    hoop.draw()
    kdjumper.draw()
    bball.draw()
    screen.draw.text(p_text, (10,10), color = "Black")
    
def on_mouse_move(pos):
    global p_text
    p_text = "Position: " + str(pos)

def on_mouse_down(pos):
    x, y = pos
    if D.speed_x == 0:
        D.speed_x = (x - bball.x)/75
        D.speed_y = (y - bball.y)/75
    

def update():
    bball.x += D.speed_x
    bball.y += D.speed_y
    
    
    if bball.x > WIDTH or bball.x < 0:
        D.speed_x = 0
        D.speed_y = 0
    if bball.y > HEIGHT or bball.y < 0:
        D.speed_y = 0
        D.speed_x = 0


pgzrun.go()
