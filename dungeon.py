import pygame, random

pygame.init()

# Screen settings
screen = pygame.display.set_mode([600, 600])

# Define colors (for the example)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Room layout (1 is a wall, 0 is empty space)
room_1 = [
    1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 1, 1, 1, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
]


room_2 = [
    1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
]

room_3 = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
]

over_world = [
    "empty", room_2, "empty", "empty",
    "empty", room_1, room_3, "empty",
    "empty", "empty", "empty", "empty",
    "empty", "empty", "empty", "empty",
]






#Overworld Position
over_world_position = 5



# Set starting room
current_room = over_world[over_world_position]

player_pos = [2, 2]

# Size of the tile
tile_size = 50

# Load images
wall_tile = pygame.transform.scale(pygame.image.load("dungeon_wall.png"), (tile_size, tile_size))
player_image = pygame.transform.scale(pygame.image.load("player.png"), (tile_size, tile_size))

# Padding Constants
x_padding = 50
y_padding = 50


goblin = {"image":pygame.image.load("goblin.png")}

enemies_global = []

enemies_global.append({"room":room_1,"x":3,"y":3, "enemy":goblin})


AI_Timer_Delay = 5000
AI_Ticks = pygame.time.get_ticks()




def collision_detection(pos):
    pos_index = pos[0] + pos[1] * 10
    return current_room[pos_index] == 1




# Render enemies in the current room
def render_enemies():
    for enemy in enemies_global:
        if enemy["room"] == current_room:  # Only render enemies in the current room
            enemy_pixel_x = enemy["x"] * tile_size + x_padding
            enemy_pixel_y = enemy["y"] * tile_size + y_padding
            screen.blit(enemy["enemy"]["image"], (enemy_pixel_x, enemy_pixel_y))



def check_exit_direction(pos):
    """Check if player has exited the map, and return the direction."""
    if pos[0] < 1:
        return "west"
    elif pos[0] > 8:
        return "east"
    elif pos[1] < 1:
        return "north"
    elif pos[1] > 7:
        return "south"
    return None


# Render the room layout
def render_map():
    for i in range(len(current_room)):
        x = (i % 10) * tile_size  # Calculate x position (10 tiles per row)
        y = (i // 10) * tile_size  # Calculate y position (next row every 10 tiles)

        if current_room[i] == 1:
            screen.blit(wall_tile, (x + x_padding, y + y_padding))

    player_pixel_x = player_pos[0] * tile_size + x_padding
    player_pixel_y = player_pos[1] * tile_size + y_padding
    screen.blit(player_image, (player_pixel_x, player_pixel_y))


def screen_transition(direction):
    global over_world_position, current_room, over_world

    if direction == "north":
        over_world_position -= 4
    elif direction == "south":
        over_world_position += 4
    elif direction == "west":
        over_world_position -= 1
    elif direction =="east":
        over_world_position += 1

    current_room = over_world[over_world_position]

def enemy_ai():
    for enemy in enemies_global:
        if enemy['room'] == current_room:
            enemy_x = enemy['x']
            enemy_y = enemy['y']

            enemy_x += random.randint(-1,1)
            enemy_y += random.randint(-1,1)

            if collision_detection((enemy_x,enemy_y)) != True:
                enemy['x'] = enemy_x
                enemy['y'] = enemy_y





def check_mouse_collision_detection(pos):
    x = int(pos[0] / 50) - 1
    y = int(pos[1] / 50) - 1

    for enemy in enemies_global:
        print("----------------")
        print(x)
        print(y)
        print("----------------")
        print(enemy['x'])
        print(enemy['y'])
        print("----------------")
        if enemy['room'] == current_room:
            if x == enemy['x']:
                if y == enemy['y']:
                    print("enemy")


# Main game loop
running = True
while running:
    screen.fill(BLACK)  # Fill background with black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            check_mouse_collision_detection(mouse_pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_pos[1] -= 1
                if collision_detection(player_pos):
                    player_pos[1] += 1
            elif event.key == pygame.K_a:
                player_pos[0] -= 1
                if collision_detection(player_pos):
                    player_pos[0] += 1
            elif event.key == pygame.K_s:
                player_pos[1] += 1
                if collision_detection(player_pos):
                    player_pos[1] -= 1
            elif event.key == pygame.K_d:
                player_pos[0] += 1
                if collision_detection(player_pos):
                    player_pos[0] -= 1

    # Check if the player has left the map
    exit_direction = check_exit_direction(player_pos)
    if exit_direction:
        print(f"Exited the room towards the {exit_direction}.")
        # You can reset the player's position or load a new room here

        # Example of resetting the player to the opposite side when exiting
        if exit_direction == "west":
            player_pos[0] = 7  # Move to the opposite edge
            screen_transition("west")
        elif exit_direction == "east":
            player_pos[0] = 1
            screen_transition("east")
        elif exit_direction == "north":
            player_pos[1] = 7
            screen_transition("north")
        elif exit_direction == "south":
            player_pos[1] = 1
            screen_transition("south")




    if pygame.time.get_ticks() - AI_Ticks == 1000:
        #enemy_ai()
        AI_Ticks = pygame.time.get_ticks()



    # Render the map
    render_map()
    render_enemies()

    pygame.display.flip()  # Update the screen

pygame.quit()
