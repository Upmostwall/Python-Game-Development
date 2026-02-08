import pgzrun

WIDTH = 640
HEIGHT = 640

CELL_SIZE = 80


maze = [    
    [0,0,1,0,0,0,1,0],  #0 = path, 1 = wall, 2 = goal cell
    [1,0,1,0,1,0,1,0],
    [1,0,0,0,1,0,0,0],
    [1,1,1,0,1,1,1,0],
    [0,0,0,0,0,0,1,0],
    [0,1,1,1,1,0,1,0],
    [0,0,0,0,1,0,0,0],
    [1,1,1,0,1,1,1,2]
]

player_row = 0
player_col = 0

game_won = False

player = Actor("bee")

def draw():
    screen.fill((30, 30, 40)) 

    for i in range(8):
        for j in range(9):
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            rect = Rect((x,y), (CELL_SIZE, CELL_SIZE))

            if maze[i][j] == 1:
                screen.draw.filled_rect(rect, (0, 150, 140))
            
            else:
                screen.draw.filled_rect(rect, (255, 248, 220))
            
            screen.draw.rect(rect, (200, 200, 200))

            if maze[i][j] == 2:
                screen.draw.filled_rect(rect, (255, 215, 0))

                screen.draw.text("GOAL", center = (x+40, y+40), fontsize = 24, color = "black")

    player.pos = (
        player_col * CELL_SIZE + CELL_SIZE //2,
        player_row * CELL_SIZE + CELL_SIZE //2
    )

    player.draw()

    if game_won:
    
        screen.draw.text(
            "You Win!", 
            center = (WIDTH//2, HEIGHT//2), 
            fontsize = 80, 
            color = "lime"
        )


def on_key_down(key):
    global player_row, player_col, game_won

    if game_won:
        return

    new_row = player_row
    new_col = player_col

    if key == keys.UP:
        new_row -= 1
    elif key == keys.DOWN:
        new_row += 1
    elif key == keys.LEFT:
        new_col -= 1
    elif key == keys.RIGHT:
        new_col += 1

    if 0 <= new_row < 8 and 0 <= new_col < 8:
        if maze[new_row][new_col] != 1:
            player_row = new_row
            player_col = new_col

        if maze[player_row][player_col] == 2:
            game_won = True

pgzrun.go()