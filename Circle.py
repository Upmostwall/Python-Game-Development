import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    R = 255
    G = 0
    B = randint(120, 255)

    radius = 120   
    for i in range(20):
        screen.draw.circle(
            (150, 150),   
            radius,       
            (R, G, B)     
        )

        R -= 10
        G += 10

        radius -= 6      

pgzrun.go()
