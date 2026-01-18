import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    R = 255
    G = 0
    B = randint(120, 255)

    width = WIDTH
    height = HEIGHT-200
    for i in range(20):
        rect = Rect((0,0),(width,height))
        rect.center = 150, 150
        screen.draw.rect(rect, (R, G, B))

        R -= 10
        G += 10

        width -= 10
        height += 10

pgzrun.go()