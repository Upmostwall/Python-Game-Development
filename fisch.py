import pgzrun
import random

WIDTH =800
HEIGHT = 600

score = 0
game_started = False
game_over = False

player = Actor("harpoon")
player.pos = (WIDTH / 2, HEIGHT - 50)

start_button = Rect((300,250), (200,60))
restart_button = Rect((300,350), (200,60))

bullets = []
plastic_bottles = []
fishes = []

plastic_timer = []
fish_timer = []

def draw():
    screen.clear()
    screen.blit("sea", (0, 0))

    if not game_started:
        screen.draw.text("Fisch Game", center=(WIDTH // 2, 150), fontsize=50, color="white")
        screen.draw.filled_rect(start_button, "darkblue")
        screen.draw.text("START", center=start_button.center, fontsize=40, color="white")
        
        return 
    
    player.draw()
    for bullet in bullets:
        bullet.draw()
    for bottle in plastic_bottles:
        bottle.draw()
    for fish in fishes:
        fish.draw()
    screen.draw.text(f"Score: {score}", (10, 10), color="white")

    if game_over: 
        screen.draw.text("GAME OVER", center = (WIDTH // 2, HEIGHT // 2), fontsize=60, color="white")
        screen.draw.filled_rect(restart_button, "darkgreen")
        screen.draw.text("RESTART", center=restart_button.center, fontsize=35, color="white")

def update():
    global plastic_timer, fish_timer, game_over, score
    if not game_started or game_over:
        return
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

    for bullet in bullets[:]:
        bullet.y -= 7
        if bullet.y < 0:
            bullets.remove(bullet)

    plastic_timer += 1
    if plastic_timer > 80:
        bottle = Actor("plastic_bottle")
        bottle.x = 0
        bottle.y = random.randint(50, HEIGHT - 100)
        bottle.speed = random.randint(1,2)
        plastic_bottles.append(bottle)
        bottle.timer = 0

    fish_timer += 1
    if fish_timer > 100:
        fish = Actor("fish")
        fish.x = 0
        fish.y = random.randint(100, HEIGHT - 200)
        fish.speed = random.randint(1,2)
        fishes.append(fish)
        fish.timer = 0

    for bottle in plastic_bottles[:]:
        bottle.x += bottle.speed
        if bottle.x > WIDTH:
            plastic_bottles.remove(bottle)

    for fish in fishes[:]:
        fish.x += fish.speed
        fish.y += random.choice([-0.5, 0.5])

        if fish.x > WIDTH:
            fishes.remove(fish)

    for bullet in bullets[:]:
        for bottle in plastic_bottles[:]:
            if bullet.colliderect(bottle):
                score += 10
                bullets.remove(bullet)
                plastic_bottles.remove(bottle)
                break

        for fish in fishes[:]:
            if bullet.colliderect(fish):
                score -= 5
                bullets.remove(bullet)
                fishes.remove(fish)
                break       

    if score >= 100:
        game_over = True

def on_key_down(key):
    if game_started and not game_over:
        if key == keys.space:
            bullet = Actor("bullet")
            bullet.pos =  (player.x, player.y - 40)
            bullets.append(bullet)

def on_mouse_down(pos):
    global game_started, game_over, score, plastic_bottles, bullets, fishes
    global plastic_timer, fish_timer
    
    if not game_started and start_button.collidepoint(pos):
        game_started = True
    elif game_over and restart_button.collidepoint(pos):
        game_over = False
        score = 0
        plastic_timer = 0
        fish_timer = 0
        bullets.clear()
        plastic_bottles.clear()
        fishes.clear()
        player.pos = (WIDTH // 2, HEIGHT - 50)

pgzrun.go()

