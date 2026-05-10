import pgzrun
import random

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.color = color

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y *= -1

balls = []

for i in range(10):
    radius = random.randint(20, 50)
    
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT - radius)
    
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    speed_x = random.choice([-5, -4, -3, 3, 4, 5])
    speed_y = random.choice([-5, -4, -3, 3, 4, 5])
    
    ball = Ball(x,y,radius, color, speed_x, speed_y)
    balls.append(ball)

def draw():
    screen.clear()
    screen.fill("black")
    for ball in balls:
        ball.draw()

def update():
    for ball in balls:
        ball.move() 

pgzrun.go()