import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

stars = []
lines = []

next_star = 0
start_time = 0
total_time = 0
end_time = 0
number_of_stars = 8

def create_stars():
    global start_time
    for count in range(0, number_of_stars):
        star = Actor("star")
        star.pos = (randint(40, WIDTH-40), randint(40, HEIGHT-40)) 
        stars.append(star)
    start_time = time()

def draw():
    global total_time

    screen.blit("background", (0, 0))
    number = 1
    for star in stars:
        star.draw()
        screen.draw.text(
            str(number),
            center = (star.x, star.y + 50),
            fontsize = 30,
            color = "yellow",
            owidth = 1.5,
            ocolor = "black"
        )

        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 255))
    
    if next_star < number_of_stars:
        total_time = time() - start_time
    screen.draw.text(
            str(round(total_time)),
            (10, 10),
            fontsize = 40,
            color = "cyan",
            owidth = 1.5,
            ocolor = "black"
        )
def update():
    pass

def on_mouse_down(pos):
    global next_star, lines

    if next_star < number_of_stars:
        if stars[next_star].collidepoint(pos):
            if next_star > 0:
                lines.append((
                    stars[next_star-1].pos, 
                    stars[next_star].pos
                    ))
            next_star = next_star + 1

    else:
        lines = []
        next_star = 0
        create_stars()

create_stars()
pgzrun.go()