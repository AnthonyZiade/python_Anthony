import pgzrun

WIDTH = 1600
HEIGHT = 900

kobe = Actor("kobe")
kobe.pos = (WIDTH/5, HEIGHT/2)
speed = 1 # nombre de pixels par update

ring = Actor("ring")
ring.pos = (WIDTH/1.1, HEIGHT/3)
vy_a = 7 # vitesse verticale du ring

ball = Actor("ball")
ball.pos = (WIDTH/4, HEIGHT/2) # point initial
ball.speed_x = 0 # vitesse du ballon au point initial

inst = Actor("inst") # instructions 
inst.pos = (WIDTH/2, HEIGHT/7.5) 

p_text = ""
a_text = ""

def update():
    global vy_a
    if (ring.y < 0 or ring.y > HEIGHT):
        vy_a = -vy_a
    ring.y += vy_a
    
    ball.x += ball.speed_x

    if (ball.x > WIDTH): # si le ballon se rend au bord de l'ecran, il va retourner au point initial
        ball.pos = (WIDTH/4, HEIGHT/2) # point initial
        ball.speed_x = 0 # vitesse du ballon au point initial
        
def draw():
    screen.fill("white") # cause un arriere plan blanc
    kobe.draw()
    ring.draw()
    ball.draw()
    inst.draw()
    screen.draw.text(p_text, (10,10), color = "Purple")
    screen.draw.text(a_text, (10,30), color = "Gold")

def on_mouse_move(pos):
    global p_text, a_text
    p_text = "Position: " + str(pos)
    kobe.angle = kobe.angle_to(pos)
    a_text = "Angle: " + str(round(kobe.angle))
    wrap = str(pos).split(' ', 1)[1] # cela fait que "wrap" est definie par la valeur "y" seulement du position de la souris
    wrap = wrap[:-1]
    if (ball.speed_x == 0):
        ball.y = int(wrap)
    
def on_mouse_down():
    ball.speed_x = 10 # quand la souris est clicker, la ball va bouger
    
pgzrun.go()