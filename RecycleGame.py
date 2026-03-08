import pgzrun
import random

font_options = (255,255,255)

WIDTH = 1000
HEIGHT = 800

CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

CENTER = (CENTER_X, CENTER_Y)

FINAL_LEVEL = 6
START_SPEED = 10

ITEMS = ["chips", "bottle", "battery", "paper"]

game_over = False
game_complete = False
current_level = 1

items = []
animations = []

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bg1", (0, 0))

    if game_over:
        display_message("Game Over!", "Try Again!")
    elif game_complete:
        display_message("Congratulations!", "You completed the game!")
    else:
        for item in items:
            item.draw()

def update():
    global items

    if len(items) == 0:
        items = make_items(current_level)

def make_items(no_of_extra_items):
    items_to_create = get_option_to_create(no_of_extra_items)
    new_items = create_items(items_to_create)

    layout_items(new_items)
    animate_items(new_items)

    return new_items

def get_option_to_create(no_of_extra_items):
    items_to_create = ["paper"]

    for i in range(0, no_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option + ".png")
        new_items.append(item)
    return new_items

def layout_items(items_layout):
    gaps = len(items_layout) + 1
    gapsize = WIDTH / gaps
    random.shuffle(items_layout)

    for index, item in enumerate(items_layout):
        new_xpos = (index + 1) * gapsize
        item.x = new_xpos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor = ("center", "bottom")

        animation = animate(item, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items, current_level

    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animations(animations_stop):
    for animation in animations_stop:
        if animation.running:
            animation.stop()

def display_message(heading, subheading):
    screen.draw.text(
        heading, center=CENTER, fontsize=60, color="white"
        )
    screen.draw.text(
        subheading, center=(CENTER_X, CENTER_Y + 30), color="white")
    
pgzrun.go()