import pgzrun
from random import randint

TITLE = "Good Shot Game"

WIDTH = 500
HEIGHT = 500

message = ""

alien = Actor("alien")

def draw():
    screen.clear()
    screen.fill(color = (128,0,0))
    screen.draw.text("Game over", center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color="white")
    alien.draw()
    
    alien.draw()
    screen.draw.text(message, center = (400,200), fontsize = 25, color = "white")

def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot!"
        place_alien()
    else:
        message = "You Missed! Try Again."

place_alien()
pgzrun.go()

