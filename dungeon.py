import pygame, random, math
from rooms import *
from pygame import *
from crt_shader import Graphic_engine
from settings import *
from goblin import Goblin

pygame.init()

# Screen settings
#screen = pygame.display.set_mode([600, 600])


screen = pygame.Surface(VIRTUAL_RES).convert((255, 65282, 16711681, 0))
# you need to give your display OPENGL flag to blit screen using OPENGL
pygame.display.set_mode(REAL_RES, DOUBLEBUF|OPENGL)
# init shader class
crt_shader =  Graphic_engine(screen)

# Define colors (for the example)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)





over_world_width = 4

over_world = [
    "empty", room_2, "empty", "empty",
    "empty", room_1, room_3, "empty",
    "empty", room_5, room_4, "empty",
    "empty", room_7, room_6, "empty",
]

over_world_width = 5

over_world = [
    "empty", "empty", "empty", "empty", "empty",
    "empty", "empty", "empty", "empty", "empty",
    "empty", "empty", "empty", "empty", "empty",
    "empty", town,   forest_2, "empty", "empty",
    
     start, forest_1, forest_3,"empty","empty",
]







#Overworld Position
over_world_position = 20



# Set starting room
current_room = over_world[over_world_position]

player_pos = [2, 7]


Sword = {"Attack": 3}

player_stats = {"HP":0, "MHP":0, "Strength":random.randint(3,18),"Dexterity":random.randint(3,18),"Intelligence":random.randint(3,18), "Gold":25, "Inventory":[], "Equipped Weapon": None, "skills":{}, "exp":0}

player_stats['HP'] = player_stats['Strength'] * 3
player_stats['MHP'] = player_stats['HP']

# Size of the tile
tile_size = 50

# Load images
wall_tile = pygame.transform.scale(pygame.image.load("dungeon_wall.png"), (tile_size, tile_size))
building_tile = pygame.transform.scale(pygame.image.load("building.png"),(tile_size,tile_size))
inn_tile = pygame.transform.scale(pygame.image.load("Inn_Shop.png"), (tile_size, tile_size))
tree_tile = pygame.transform.scale(pygame.image.load("tree.png"),(tile_size,tile_size))
player_image = pygame.transform.scale(pygame.image.load("player.png"), (tile_size, tile_size))
key_image = pygame.transform.scale(pygame.image.load("key.png"), (tile_size, tile_size))
sword_image = pygame.transform.scale(pygame.image.load("sword.png"), (tile_size, tile_size))
sword_image_m = pygame.transform.scale(pygame.image.load("sword_mithril.png"), (tile_size, tile_size))
sword_image_r = pygame.transform.scale(pygame.image.load("sword_rune.png"), (tile_size, tile_size))
bolt_image = pygame.transform.scale(pygame.image.load("bolt.png"),(tile_size, tile_size))
magic_bolt_image = pygame.transform.scale(pygame.image.load("magic_bolt.png"),(tile_size, tile_size))


# Padding Constants
x_padding = 50
y_padding = 50


# goblin = {"name":"Goblin","image":pygame.image.load("goblin.png"), 'health':30, 'max_health':30, "exp":10}
# goblin_2 = {"name":"Goblin","image":pygame.image.load("goblin.png"), 'health':30, 'max_health':30, "exp":10}
# wright = {"name":"Wright","image":pygame.image.load("wright.png"),'health':60,  'max_health':60, "exp":30}

enemies_global = []

#Enemy Examples
enemies_global.append({"room":forest_2,"x":3,"y":3, "stats":Goblin(), "dead":False, "respawn":1})
enemies_global.append({"room":forest_2,"x":4,"y":1, "stats":Goblin(), "dead":False, "respawn":1})
enemies_global.append({"room":forest_2,"x":5,"y":5, "stats":Goblin(), "dead":False, "respawn":1})

door_tile = pygame.image.load("door.png")


#key = {"type":"key","image":key_image,"name":"key"}
#key_2 = {"type":"key","image":key_image,"name":"key_2"}

doors = []
#doors = [{'room':room_1,"x":2,"y":0,"locked":True,"check":18,"key":key},{'room':room_4,"x":7,"y":5,"locked":True,"check":18,"key":key_2}]

AI_Timer_Delay = 5000
AI_Ticks = pygame.time.get_ticks()
Projectile_Ticks = pygame.time.get_ticks()
Enemy_Collision_Ticks = pygame.time.get_ticks()

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 36)  # You can change the font size if needed

sword = {"type":"weapon","image":sword_image,"name":"sword", "attack":5}
sword_m = {"type":"weapon","image":sword_image_m, "name":"Mithril Sword","attack":10}
sword_r = {"type":"weapon","image":sword_image_r, "name":"Rune Sword","attack":25}

meat = {"name":"Meat","type":"Food", "Value":3,"image":pygame.transform.scale(pygame.image.load("meat.png"), (tile_size, tile_size))}


items = []

#items.append({'room':room_1,"x":6,"y":1,"stats":key, "name":"Key"})
#items.append({"room":room_1,"x":7,"y":1,"stats":sword,"name":"sword"})
items.append({"room":forest_1,"x":4,"y":3,"stats":sword_m,"name":"Mithril Sword"})
items.append({"room":forest_3,"x":4,"y":3,"stats":sword_r,"name":"Rune Sword"})
#items.append({"room":room_5,"x":5,"y":3,"stats":key_2, "name":"Great Key"})

selected_item_index = 0  # Index for currently selected item




sword_sound_effect = pygame.mixer.Sound("Sword_Effect.mp3")
goblin_death_sound_effect = pygame.mixer.Sound("Goblin_Death.mp3")
unlock_sound_effect = pygame.mixer.Sound("Door_Sound_Effect.mp3")
punch_sound_effect = pygame.mixer.Sound("punch_sound_effect.mp3")

pygame.mixer.music.load("Background_music.mp3")

projectiles = []

dialog = ""

# Inn menu options
inn_options = ["Sleep (10 gold)", "Rumors","Leave"]

current_day = 0
DAY_TICKS = 0

def handle_projectiles():
    for i in projectiles:
        current_x = i['x']
        current_y = i['y']

        target_x = i['target_x']
        target_y = i['target_y']



        if current_y < target_y:
            current_y += 1
        elif current_y > target_y:
            current_y -= 1


        if current_x < target_x:
            current_x += 1
        elif current_x > target_x:
            current_x -= 1




        i['x'] = current_x
        i['y'] = current_y


        projectile_pixel_x = i["x"] * tile_size + x_padding
        projectile_pixel_y = i["y"] * tile_size + y_padding




        screen.blit(i['image'], (projectile_pixel_x, projectile_pixel_y))





def render_projectiles():
    for i in projectiles:
        projectile_pixel_x = i["x"] * tile_size + x_padding
        projectile_pixel_y = i["y"] * tile_size + y_padding

        screen.blit(i['image'],(projectile_pixel_x,projectile_pixel_y))





def day_pass():
    global current_day, current_room, enemies_global

    current_day += 1
    for enemy in enemies_global:
        if 'respawn' in enemy:
            respawn_rate = enemy['respawn']
            if current_room != enemy['room'] and enemy['stats'].health <= 0:
                enemy['stats'].health = enemy['stats'].max_health
                enemy['dead'] = False

# Function to render player stats
def render_player_stats():
    stats_surface = font.render(f"HP: {player_stats['HP']} | STR: {player_stats['Strength']} | DEX: {player_stats['Dexterity']} | INT: {player_stats['Intelligence']}", True, WHITE)
    screen.blit(stats_surface, (100, 550))  # Display near the bottom of the screen


def building_logic_inn():
    global render_building_window_bool_inn
    if inn_options[selected_item_index] == "Leave":
        render_building_window_bool_inn = False
    elif inn_options[selected_item_index] == "Sleep (10 gold)":
        if player_stats['Gold'] >= 10:
            sleep()

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

    if current_room[pos_index] in [1, 3, 4, 5]:
        return True
    elif current_room[pos_index] == 2:
        for door in doors:
            if door['x'] == pos[0] and door['y'] == pos[1] and current_room == door['room']:
                return check_door(door)

    for enemy in enemies_global:
        if enemy['room'] == current_room:
            if enemy['x'] == pos[0] and enemy['y'] == pos[1] and enemy['dead'] == False:
                return True


def sleep():
    global render_building_window_bool_inn

    render_building_window_bool_inn = False

    player_stats['Gold'] -= 10
    player_stats['HP'] = player_stats['MHP']

def random_loot(enemy):
    if enemy['stats'].name == "Goblin":
        player_stats['exp'] += enemy['stats'].exp
        if random.randint(1,100) < 100:
            print(enemy['x'])
            items.append({'room':current_room,"x":enemy['x']+random.randint(-1,1),"y":enemy['y']+random.randint(-1,1),"name":"Meat", "stats":meat})



def check_projectiles():
    # Iterate through the list of projectiles
    for projectile in projectiles:
        # Get the current position of the projectile
        projectile_x = projectile['x']
        projectile_y = projectile['y']

        # Check for collision with the player
        player_x = player_pos[0]
        player_y = player_pos[1]

        if projectile_x == player_x and projectile_y == player_y and projectile['source'] != "player":
            # If there's a collision with the player, apply damage or any other effect
            player_stats['HP'] -= projectile['damage']
            print("Player hit! Health: ", player_stats['HP'])
            # Remove the projectile if it hits the player
            projectiles.remove(projectile)
            continue

        # Check for collision with enemies
        for enemy in enemies_global:
            enemy_x = enemy['x']
            enemy_y = enemy['y']

            if projectile_x == enemy_x and projectile_y == enemy_y and projectile['source'] != "enemy":
                # If there's a collision with an enemy, apply damage or effect
                enemy['stats']['health'] -= projectile['damage']
                print(f"Enemy hit! Enemy Health: {enemy['stats']['health']}")
                # Remove the projectile if it hits an enemy
                projectiles.remove(projectile)
                # if enemy['stats']['health'] <= 0:
                #     enemies_global.remove(enemy)
                break  # Exit enemy loop, projectile is destroyed
        if projectile_x == projectile['target_x'] and projectile_y == projectile['target_y']:
            if projectile in projectiles: projectiles.remove(projectile)



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
        enemy['stats'].health -= damage
        
        if enemy['stats'].health <= 0 and enemy['dead'] != True:
            # enemies_global.remove(enemy)
            enemy['dead'] = True
            pygame.mixer.Sound.play(goblin_death_sound_effect)
            random_loot(enemy)
        print(f"Attacked enemy! Enemy's health is now {enemy['stats'].health}")
        if player_stats['Equipped Weapon'] != None:
            pygame.mixer.Sound.play(sword_sound_effect)
        else:
            pygame.mixer.Sound.play(punch_sound_effect)

    else:
        print("Enemy is out of melee range!")


# Render enemies in the current room
def render_enemies():
    for enemy in enemies_global:
        if enemy["room"] == current_room and enemy['dead'] == False:  # Only render enemies in the current room
            enemy_pixel_x = enemy["x"] * tile_size + x_padding
            enemy_pixel_y = enemy["y"] * tile_size + y_padding
            screen.blit(enemy["stats"].image, (enemy_pixel_x, enemy_pixel_y))



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
        elif current_room[i] == 3:
            screen.blit(tree_tile, (x + x_padding, y + y_padding))
        elif current_room[i] == 4:
            screen.blit(building_tile,(x + x_padding, y + y_padding))
        elif current_room[i] == 5:
            screen.blit(inn_tile,(x + x_padding, y + y_padding))




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

    exp_text = "EXP: " + str(player_stats['exp'])
    exp_text_render = font_2.render(exp_text, True, WHITE)
    screen.blit(exp_text_render,(equipped_weapon_x, equipped_weapon_y + 120))



def screen_transition(direction):
    global over_world_position, current_room, over_world, over_world_width

    if direction == "north":
        over_world_position -= over_world_width
    elif direction == "south":
        over_world_position += over_world_width
    elif direction == "west":
        over_world_position -= 1
    elif direction =="east":
        over_world_position += 1

    current_room = over_world[over_world_position]

def enemy_ai():
    for enemy in enemies_global:
        if enemy['room'] == current_room and enemy['dead'] == False:
            enemy_x = enemy['x']
            enemy_y = enemy['y']

            # enemy_x += random.randint(-1,1)
            # enemy_y += random.randint(-1,1)

            if enemy['stats'].name == "wright":
                decision = random.randint(1,10)
                if(decision < 5):
                    projectiles.append({"x":enemy['x'],"y":enemy['y'], "target_x":player_pos[0], "target_y":player_pos[1], "image":magic_bolt_image, "damage":5,"source":"enemy"})
                else:
                    if enemy_x < player_pos[0]:
                        enemy_x +=1
                    elif enemy_x > player_pos[0]:
                        enemy_x -=1

                    if enemy_y < player_pos[1]:
                        enemy_y +=1
                    elif enemy_y > player_pos[1]:
                        enemy_y -=1
            else:
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
    global dialog, in_dialog,render_building_window_bool_inn

    x = int(pos[0] / 50) - 1
    y = int(pos[1] / 50) - 1

    index = x + y * 10 
    if current_room[index] == 3 and is_in_melee_range(player_pos[0],player_pos[1],x,y):
        dialog = "Its a tree"
        in_dialog = True
    elif current_room[index] == 5 and is_in_melee_range(player_pos[0],player_pos[1],x,y):
        render_building_window_bool_inn = True

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



def create_projectile(pos):
    x = int(pos[0] / 50) - 1
    y = int(pos[1] / 50) - 1

    spawn_x = player_pos[0]
    spawn_y = player_pos[1]

    projectiles.append({"x":spawn_x,"y":spawn_y, "target_x":x, "target_y":y, "image":bolt_image, "damage":5,"source":"player"})

def check_enemy_collisions():
    for enemy in enemies_global:
        if enemy['room'] == current_room and enemy['dead'] == False:
            if enemy['x'] == player_pos[0] and enemy['y'] == player_pos[1]:
                if enemy['stats'].name == "Goblin":
                    player_stats['HP'] -= random.randint(3,5)



def render_building_window():
    font = pygame.font.Font(None, 30)
    font_2 = pygame.font.Font(None, 25)
    screen.fill(BLACK)

    # Define the inn menu rectangle properties
    inn_rect = pygame.Rect(50, 50, 400, 300)  # Position and size of the inn menu box

    # Draw the white border around the inn rectangle
    pygame.draw.rect(screen, WHITE, inn_rect, 3)  # Draw border (3 pixels wide)

    
    # Render inn options
    for index, option in enumerate(inn_options):
        text_color = WHITE if index != selected_item_index else (255, 255, 0)  # Highlight selected option
        text = font.render(option, True, text_color)
        screen.blit(text, (100, 100 + index * 40))

    # Display player stats or additional info if desired
    gold_text = f"Gold: {player_stats['Gold']}"  # Assuming player_stats has a 'Gold' attribute
    gold_render = font_2.render(gold_text, True, WHITE)
    screen.blit(gold_render, (inn_rect.x + 20, inn_rect.bottom + 20))  # Position below the inn menu

def render_dialog_window(dialog):
    
    dialog_width = REAL_RES[0] - 40  # Width of the dialog
    dialog_height = 100  # Height of the dialog
    dialog_x = (REAL_RES[0] - dialog_width) // 2  # Center horizontally
    dialog_y = REAL_RES[1] - dialog_height - 20  # Position at the bottom with some padding

    # Draw the dialog window background (black) and border (white)
    dialog_rect = pygame.Rect(dialog_x, dialog_y, dialog_width, dialog_height)
    pygame.draw.rect(screen, BLACK, dialog_rect)  # Background
    pygame.draw.rect(screen, WHITE, dialog_rect, 3)  # Border with thickness of 3

    # Render the text
    font = pygame.font.Font(None, 36)  # Use a default font and set the size
    text_surface = font.render(dialog, True, WHITE)  # Render the text in white
    text_rect = text_surface.get_rect(center=dialog_rect.center)  # Center the text in the dialog

    # Blit the text onto the dialog
    screen.blit(text_surface, text_rect)


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

    crt_shader()
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
render_building_window_bool_inn = False
in_dialog = False

pygame.mixer.music.play()


while running:
    screen.fill(BLACK)  # Fill background with black

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            in_dialog = False
            render_building_window_bool_inn = False 
            mouse_pos = pygame.mouse.get_pos()
            check_mouse_collision_detection(mouse_pos)
        elif pygame.mouse.get_pressed()[2]:
            mouse_pos = pygame.mouse.get_pos()
            create_projectile(mouse_pos)

        if event.type == pygame.KEYDOWN:
            in_dialog = False
            if render_inventory_bool == False:
                if render_building_window_bool_inn == False:
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
                        selected_item_index -=1 
                    elif event.key == pygame.K_s:
                        selected_item_index +=1
                    elif event.key == pygame.K_TAB:
                        render_building_window_bool_inn = False
                    elif event.key == pygame.K_RETURN:
                        building_logic_inn()

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


    if pygame.time.get_ticks() - Projectile_Ticks >= 150:
        handle_projectiles()
        Projectile_Ticks = pygame.time.get_ticks()
    if pygame.time.get_ticks() - DAY_TICKS >= 10000:
        day_pass()
        DAY_TICKS = pygame.time.get_ticks()

    # Render the map
    if player_stats['HP'] >= 0:
        if pygame.time.get_ticks() - Enemy_Collision_Ticks >= 1000:
            check_enemy_collisions()
            Enemy_Collision_Ticks = pygame.time.get_ticks()

        if render_inventory_bool == False:
            if render_building_window_bool_inn == False:
                render_map()
                render_enemies()
                render_items()
                render_projectiles()
                check_projectiles()
            else:
                render_building_window()
        else:
            render_inventory()


        if in_dialog:
            render_dialog_window(dialog)
        else:
            render_player_stats()
    else:
        render_game_over()

    #pygame.display.flip()  # Update the screen
    crt_shader()
pygame.quit()

