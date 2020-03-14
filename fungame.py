import pygame
import sys
import random

pygame.init()

# position and s(255,0,0)ize

WIDTH = 900
HEIGHT = 700

RED = (255,0,0)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BACKGROUND_COLOR = (0, 0, 0)

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size),0]
enemy_list = [enemy_pos]

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# for and if

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
	if score < 20:
		SPEED = 6
	elif score < 40:
		SPEED = 7
	elif score < 60:
		SPEED = 8
	elif score < 80:
		SPEED = 10
	elif score < 100:
		SPEED = 11
	elif score < 120:
		SPEED = 12
	elif score < 150:
		SPEED = 13
	elif score < 170:
		SPEED = 13
	elif score < 200:
		SPEED = 15
	elif score < 220:
		SPEED = 17
	elif score < 240:
		SPEED = 19
	elif score < 265:
		SPEED = 15	



	else:
		SPEED = 20
	return SPEED


def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.3:  
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED
		else:
			enemy_list.pop(idx)
			score += 1
	return score
	


def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False





def detect_collision(player_pos, enemy_pos):
		p_x = player_pos[0]
		p_y = player_pos[1]

		e_x = enemy_pos[0]
		e_y = enemy_pos[1]

		if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
			if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
				return True
		return False

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
         
         # key switch

			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT:
				x -= player_size
				if x<0:
					x = 0
			elif event.key == pygame.K_RIGHT:
				x += player_size
				if x+player_size > WIDTH:
					x = (WIDTH-player_size)
		
		
			# elif event.key == pygame.K_UP:
				# y -= 5
			# elif event.key == pygame.K_DOWN:
				# y += 5
				


			player_pos = [x,y]
			
	screen.fill(BACKGROUND_COLOR)

 	# update position of enemy
	# if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
	#	enemy_pos[1] += SPEED
	# else:
	#	enemy_pos[0] = random.randint(0, WIDTH-enemy_size)
	#	enemy_pos[1] = 0



	
	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	SPEED = set_level(score, SPEED)
	
	text = "Score:" + str(score)
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH-200,HEIGHT-40))


	if collision_check(enemy_list, player_pos):
		game_over = True
		print ("Game over!\n Score:" , score)
		break

	draw_enemies(enemy_list)
	pygame.draw.rect(screen, WHITE, (player_pos[0],player_pos[1],player_size,player_size))

	clock.tick(30)

	pygame.display.update()


