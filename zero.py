import pgzrun
from random import randint ,choice
#import time

WIDTH = 700
HEIGHT = 500
#переменные, контролирующие движение по горизонтали и вертикали
direction = choice(("right","left"))
direction_vert = choice(("up","down"))
rotation = choice((1,-1))
speedH = randint(0, 5)
speedV =randint(0, 5)

panda = Actor("panda",(WIDTH/2,HEIGHT/2))

def draw():
    screen.fill((0,200,20))
    panda.draw()

def update():
    global direction, direction_vert
    panda.angle += rotation
    #Выбираем направление движения героя
    if panda.right>=WIDTH:
        direction = "left"
    if panda.left <= 0:
        direction = "right"
    if panda.bottom>=HEIGHT:
        direction_vert= "up"
    if panda.top <= 0:
        direction_vert = "down"
    #Двигаемся в зависимости от выбранного направления
    if direction == "left":
        panda.left-=speedH
    else:
        panda.left+=speedH
    if direction_vert == "up":
        panda.top-=speedV
    else:
        panda.top+=speedV
pgzrun.go()