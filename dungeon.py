import pygame, random, math

pygame.init()

# Screen settings
screen = pygame.display.set_mode([600, 600])

# Define colors (for the example)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Room layout (1 is a wall, 0 is empty space)
room_1 = [
    1, 1, 2, 1, 1, 1, 1, 1, 1, 1,
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
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
]

room_4 = [
    1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1, 1, 2, 1, 1,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1, 1, 0, 1, 1,
]

room_5 = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 0, 0, 0, 0, 0, 0, 1,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
    0, 0, 1, 1, 1, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
]

over_world = [
    "empty", room_2, "empty", "empty",
    "empty", room_1, room_3, "empty",
    "empty", room_5, room_4, "empty",
    "empty", "empty", "empty", "empty",
]






#Overworld Position
over_world_position = 5



# Set starting room
current_room = over_world[over_world_position]

player_pos = [2, 2]


Sword = {"Attack": 3}

player_stats = {"HP":0,"Strength":random.randint(3,18),"Dexterity":random.randint(3,18),"Intelligence":random.randint(3,18), "Inventory":[], "Equipped Weapon": None, "skills":[]}

player_stats['HP'] = player_stats['Strength'] * 3

# Size of the tile
tile_size = 50

# Load images
wall_tile = pygame.transform.scale(pygame.image.load("dungeon_wall.png"), (tile_size, tile_size))
player_image = pygame.transform.scale(pygame.image.load("player.png"), (tile_size, tile_size))
key_image = pygame.transform.scale(pygame.image.load("key.png"), (tile_size, tile_size))
sword_image = pygame.transform.scale(pygame.image.load("sword.png"), (tile_size, tile_size))
sword_image_m = pygame.transform.scale(pygame.image.load("sword_mithril.png"), (tile_size, tile_size))

# Padding Constants
x_padding = 50
y_padding = 50


goblin = {"name":"Goblin","image":pygame.image.load("goblin.png"), 'health':20}

wright = {"name":"Wright","image":pygame.image.load("wright.png"),'health':60}

enemies_global = []

enemies_global.append({"room":room_1,"x":3,"y":3, "stats":goblin})
enemies_global.append({"room":room_3,"x":3,"y":3, "stats":wright})
enemies_global.append({"room":room_5,"x":3,"y":3, "stats":goblin})
enemies_global.append({"room":room_5,"x":5,"y":5, "stats":goblin})
enemies_global.append({"room":room_5,"x":2,"y":5, "stats":goblin})

door_tile = pygame.image.load("door.png")


key = {"type":"key","image":key_image,"name":"key"}

doors = [{'room':room_1,"x":2,"y":0,"locked":True,"check":18,"key":key},{'room':room_4,"x":7,"y":5,"locked":True,"check":18,"key":None}]

AI_Timer_Delay = 5000
AI_Ticks = pygame.time.get_ticks()
Enemy_Collision_Ticks = pygame.time.get_ticks()

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 36)  # You can change the font size if needed

sword = {"type":"weapon","image":sword_image,"name":"sword", "attack":5}
sword_m = {"type":"weapon","image":sword_image_m, "name":"mithril sword","attack":20}

meat = {"name":"Meat","type":"Food", "Value":3,"image":pygame.transform.scale(pygame.image.load("meat.png"), (tile_size, tile_size))}

items = []
items.append({'room':room_1,"x":6,"y":1,"stats":key, "name":"Key"})
items.append({"room":room_1,"x":7,"y":1,"stats":sword,"name":"sword"})
items.append({"room":room_2,"x":4,"y":3,"stats":sword_m,"name":"mithril sword"})

selected_item_index = 0  # Index for currently selected item



sword_sound_effect = pygame.mixer.Sound("Sword_Effect.mp3")
goblin_death_sound_effect = pygame.mixer.Sound("Goblin_Death.mp3")
unlock_sound_effect = pygame.mixer.Sound("Door_Sound_Effect.mp3")

# Function to render player stats
def render_player_stats():
    stats_surface = font.render(f"HP: {player_stats['HP']} | STR: {player_stats['Strength']} | DEX: {player_stats['Dexterity']} | INT: {player_stats['Intelligence']}", True, WHITE)
    screen.blit(stats_surface, (100, 550))  # Display near the bottom of the screen




def check_door(door):
    return door['locked']

def unlock_door(door):
    if player_stats['Dexterity'] >= door['check']:
        door['locked'] = False
        #ADD logic to play sound effect here
        pygame.mixer.Sound.play(unlock_sound_effect)

    if door['key'] in player_stats['Inventory']:
        door['locked'] = False
        pygame.mixer.Sound.play(unlock_sound_effect)

def collision_detection(pos):
    pos_index = pos[0] + pos[1] * 10

    if current_room[pos_index] == 1:
        return True
    elif current_room[pos_index] == 2:
        for door in doors:
            if door['x'] == pos[0] and door['y'] == pos[1] and current_room == door['room']:
                return check_door(door)





def random_loot(enemy):
    if enemy['stats']['name'] == "Goblin":
        if random.randint(1,100) < 100:
            print(enemy['x'])
            items.append({'room':current_room,"x":enemy['x']+random.randint(-1,1),"y":enemy['y']+random.randint(-1,1),"name":"Meat", "stats":meat})





def is_in_melee_range(player_x, player_y, enemy_x, enemy_y):
    # Check if the player is within 1 tile of the enemy (manhattan distance <= 1)
    return abs(player_x - enemy_x) <= 1 and abs(player_y - enemy_y) <= 1


def attack(player_x, player_y, enemy):
    # Get enemy's position
    enemy_x = enemy['x']
    enemy_y = enemy['y']


    if is_in_melee_range(player_x, player_y, enemy_x, enemy_y):
        damage = random.randint(1, round(player_stats['Strength'] / 3 )) + round(player_stats["Strength"] / 4)
        if player_stats['Equipped Weapon'] != None:
            damage += player_stats['Equipped Weapon']['attack']
        enemy['stats']['health'] -= damage
        
        if enemy['stats']['health'] <= 0:
            enemies_global.remove(enemy)
            pygame.mixer.Sound.play(goblin_death_sound_effect)
            random_loot(enemy)
        print(f"Attacked enemy! Enemy's health is now {enemy['stats']['health']}")
        pygame.mixer.Sound.play(sword_sound_effect)
    else:
        print("Enemy is out of melee range!")


# Render enemies in the current room
def render_enemies():
    for enemy in enemies_global:
        if enemy["room"] == current_room:  # Only render enemies in the current room
            enemy_pixel_x = enemy["x"] * tile_size + x_padding
            enemy_pixel_y = enemy["y"] * tile_size + y_padding
            screen.blit(enemy["stats"]["image"], (enemy_pixel_x, enemy_pixel_y))



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
        elif current_room[i] == 2:
            screen.blit(door_tile, (x + x_padding, y + y_padding))


    player_pixel_x = player_pos[0] * tile_size + x_padding
    player_pixel_y = player_pos[1] * tile_size + y_padding
    screen.blit(player_image, (player_pixel_x, player_pixel_y))


def render_items():
    for item in items:
        if item['room'] == current_room:
            item_x = item['x'] * tile_size + x_padding
            item_y = item['y'] * tile_size + y_padding
            screen.blit(item['stats']['image'],(item_x,item_y))



def render_inventory():
    font = pygame.font.Font(None, 30)
    font_2 = pygame.font.Font(None, 25)
    screen.fill(BLACK)

    # Define the inventory rectangle properties
    inventory_rect = pygame.Rect(50, 50, 400, 400)  # Position and size of the inventory box

    # Draw the white border around the inventory rectangle
    pygame.draw.rect(screen, WHITE, inventory_rect, 3)  # Draw border (3 pixels wide)

    # Render inventory items with images
    for index, item in enumerate(player_stats['Inventory']):
        text_color = WHITE if index != selected_item_index else (255, 255, 0)  # Highlight selected item
        text = font.render(item["name"], True, text_color)
        screen.blit(text, (100, 120 + index * 40))

        # Render the item image to the left of the text
        item_image = item.get("image")  # Assuming each item has an 'image' attribute
        if item_image:
            # Blit the item image next to the text
            screen.blit(item_image, (300, 100 + index * 40))

    # Define position for equipped weapon display
    equipped_weapon_x = inventory_rect.right + 20  # Position to the right of the inventory
    equipped_weapon_y = 60  # Start below the top of the inventory box

    # Render equipped weapon title
    equipped_weapon_title = font_2.render("Weapon", True, WHITE)
    screen.blit(equipped_weapon_title, (equipped_weapon_x, equipped_weapon_y))

    # Render the name of the currently equipped weapon
    equipped_weapon = player_stats['Equipped Weapon']
    equipped_weapon_name = equipped_weapon['name'] if equipped_weapon else "None"
    equipped_weapon_text = font_2.render(equipped_weapon_name, True, WHITE)
    screen.blit(equipped_weapon_text, (equipped_weapon_x, equipped_weapon_y + 30))  # Draw below the title

    # Render the equipped weapon image
    if equipped_weapon and "image" in equipped_weapon:  # Check if the equipped weapon has an image
        screen.blit(equipped_weapon["image"], (equipped_weapon_x, equipped_weapon_y + 60))  # Draw below the text




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

            # enemy_x += random.randint(-1,1)
            # enemy_y += random.randint(-1,1)

            if enemy_x < player_pos[0]:
                enemy_x +=1
            elif enemy_x > player_pos[0]:
                enemy_x -=1

            if enemy_y < player_pos[1]:
                enemy_y +=1
            elif enemy_y > player_pos[1]:
                enemy_y -=1



            if collision_detection((enemy_x,enemy_y)) != True:
                enemy['x'] = enemy_x
                enemy['y'] = enemy_y


def check_mouse_collision_detection(pos):
    x = int(pos[0] / 50) - 1
    y = int(pos[1] / 50) - 1

    for enemy in enemies_global:
        if enemy['room'] == current_room:
            if x == enemy['x']:
                if y == enemy['y']:
                    attack(player_pos[0], player_pos[1], enemy)

    for door in doors:
        if door['room'] == current_room:
            if x == door['x']:
                if y == door['y']:
                    if is_in_melee_range(player_pos[0],player_pos[1],door['x'],door['y']):
                        unlock_door(door)
    
    for item in items:
        if item['room'] == current_room:
            if x == item['x']:
                if y == item['y']: 
                    if is_in_melee_range(player_pos[0],player_pos[1],item['x'],item['y']):
                        player_stats['Inventory'].append(item['stats'])
                        items.remove(item)



def check_enemy_collisions():
    for enemy in enemies_global:
        if enemy['room'] == current_room:
            if enemy['x'] == player_pos[0] and enemy['y'] == player_pos[1]:
                if enemy['stats'] == goblin:
                    player_stats['HP'] -= random.randint(3,5)
                if enemy['stats'] == wright:
                    player_stats['HP'] -= random.randint(10,15)







def render_game_over():
    font = pygame.font.Font(None, 74)  # Create a font object for game over text
    text = font.render("Game Over", True, WHITE)  # Render the text
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    
    restart_text = font.render("Press R to Restart", True, WHITE)  # Render restart instruction
    restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    
    exit_text = font.render("Press Q to Quit", True, WHITE)  # Render quit instruction
    exit_rect = exit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
    
    screen.fill(BLACK)  # Fill the screen with black
    screen.blit(text, text_rect)  # Draw game over text
    screen.blit(restart_text, restart_rect)  # Draw restart text
    screen.blit(exit_text, exit_rect)  # Draw exit text
    pygame.display.flip()  # Update the display

    # Event loop for game over state
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    game_over = False  # Exit the game over loop
                    reset_game()  # Reset game state here
                elif event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    quit()

def reset_game():
    global player_pos, current_room, over_world_position, enemies_global, player_stats

    player_pos = [2, 2]
    over_world_position = 5
    player_stats = {"HP":0,"Strength":random.randint(3,18),"Dexterity":random.randint(3,18),"Intelligence":random.randint(3,18), "Inventory":[], "Equipped Weapon":None}
    player_stats['HP'] = player_stats['Strength'] * 3
    current_room = over_world[over_world_position]
    enemies_global = []  # Reset enemies as needed
    enemies_global.append({"room": room_1, "x": 3, "y": 3, "stats": goblin})
    enemies_global.append({"room":room_3,"x":3,"y":3, "stats":wright})
    doors = [{'room':room_1,"x":2,"y":0,"locked":True,"check":18,"key":key}]
    items = []
    items.append({'room':room_1,"x":6,"y":1,"stats":key,"name":"key"})






# Main game loop
running = True

render_inventory_bool = False

while running:
    screen.fill(BLACK)  # Fill background with black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            check_mouse_collision_detection(mouse_pos)

        if event.type == pygame.KEYDOWN:
            if render_inventory_bool == False :
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
                elif event.key == pygame.K_TAB:
                    render_inventory_bool = not render_inventory_bool
            else:
                if event.key == pygame.K_w:
                    selected_item_index -= 1
                elif event.key == pygame.K_s:
                    selected_item_index += 1
                elif event.key == pygame.K_RETURN:
                    if player_stats['Inventory'][selected_item_index]['type'] == "weapon":
                        player_stats['Equipped Weapon'] = player_stats['Inventory'][selected_item_index]
                    if player_stats['Inventory'][selected_item_index]['type'] == "Food":
                        print('test')
                        player_stats['HP'] += player_stats['Inventory'][selected_item_index]['Value']
                        player_stats['Inventory'].remove(player_stats['Inventory'][selected_item_index])
                elif event.key == pygame.K_TAB:
                    render_inventory_bool = not render_inventory_bool


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



    # if pygame.time.get_ticks() - Enemy_Collision_Ticks == 100:
    #     print('test')
    #     check_enemy_collisions()
    #     Enemy_Collision_Ticks = pygame.time.get_ticks()

    if pygame.time.get_ticks() - AI_Ticks >= 1000:
        enemy_ai()
        check_enemy_collisions()
        AI_Ticks = pygame.time.get_ticks()



    # Render the map
    if player_stats['HP'] >= 0:
        if pygame.time.get_ticks() - Enemy_Collision_Ticks >= 500:
            check_enemy_collisions()
            Enemy_Collision_Ticks = pygame.time.get_ticks()
        if render_inventory_bool == False:
            render_map()
            render_enemies()
            render_items()
        else:
            render_inventory()
        render_player_stats()
    else:
        render_game_over()

    pygame.display.flip()  # Update the screen

pygame.quit()

