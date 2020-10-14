import pygame,sys,random
from pygame import font
import pkg_resources.py2_warn




def restart_game():
	global x,y
	ball.center=(500, 300)
	player.y=235
	opponent.y=235
	x=0
	y=0

def player_animation():
	global player_speed
	player.y+=player_speed

	#set player boundary
	if player.top<=0:
		player.top=0
	if player.bottom>=600:
		player.bottom=600

def ball_animation():
	global ball_speed_x, ball_speed_y
	ball.x+=ball_speed_x
	ball.y+=ball_speed_y

	if ball.top<=0 or ball.bottom>=600:
		ball_speed_y*=-1

	if ball.colliderect(player) or ball.colliderect(opponent):
		hit.play()
		ball_speed_x*=-1

def opponent_animation():
	opponent_speed=2
	if opponent.top<=ball.y:
		opponent.top+=opponent_speed
	if opponent.bottom>=ball.y:
		opponent.bottom-=opponent_speed

def player_2():
	global opponent_speed
	opponent.y+=opponent_speed

	#set player boundary
	if opponent.top<=0:
		opponent.top=0
	if opponent.bottom>=600:
		opponent.bottom=600



def ball_restart():
	global ball_speed_x, ball_speed_y
#restarting ball initial position
	ball.center=(500, 300)
	ball_speed_x*=random.choice((-1, 1))
	ball_speed_y*=random.choice((-1, 1))


pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Ping Pong")

#background color
bg_color=(0,0,0)
grey=(200,200,200)

#Game objects 
ball = pygame.Rect(485, 285, 30, 30)
player = pygame.Rect(980, 235, 10, 140)
opponent = pygame.Rect(10, 235, 10, 140)

#defining speeds
ball_speed_x=2*random.choice((-1,1))
ball_speed_y=2*random.choice((-1,1))
player_speed=0
opponent_speed=0

#Image
img_screen = screen
img_image=pygame.image.load("ping3.png")
img_image=pygame.transform.scale(img_image, (500, 400))
img_rect=img_image.get_rect()
img_screen_rect=screen.get_rect()
img_rect.top=img_screen_rect.top+100
img_rect.centerx=img_screen_rect.centerx

#Sounds
hit = pygame.mixer.Sound('hit2.wav')
click = pygame.mixer.Sound('hit.wav')
applause = pygame.mixer.Sound('applause.wav')





#start game
play_screen =screen
play_screen_rect=screen.get_rect()
play_width=200
play_height=50
play_color=(200,200,200)
play_text_color=(0,0,0)
play_font=pygame.font.SysFont('comicsans', 40, True)
play_rect=pygame.Rect(0,0, play_width, play_height)
play_rect.center = play_screen_rect.center
play_msg_image=play_font.render("Play Game", True, play_text_color, play_color)
play_msg_image_rect=play_msg_image.get_rect()
play_msg_image_rect.center=play_rect.center

player1_screen =screen
player1_screen_rect=screen.get_rect()
player1_width=250
player1_height=50
player1_color=(200,200,200)
player1_text_color=(0,0,0)
player1_font=pygame.font.SysFont('comicsans', 40, True)
player1_rect=pygame.Rect(0,0, player1_width, player1_height)
player1_rect.center = player1_screen_rect.center
player1_msg_image=player1_font.render("Player 1 Wins!!", True, player1_text_color, player1_color)
player1_msg_image_rect=player1_msg_image.get_rect()
player1_msg_image_rect.center=player1_rect.center

player2_screen =screen
player2_screen_rect=screen.get_rect()
player2_width=250
player2_height=50
player2_color=(200,200,200)
player2_text_color=(0,0,0)
player2_font=pygame.font.SysFont('comicsans', 40, True)
player2_rect=pygame.Rect(0,0, player2_width, player2_height)
player2_rect.center = player2_screen_rect.center
player2_msg_image=player2_font.render("Player 2 Wins!!", True, player2_text_color, player2_color)
player2_msg_image_rect=player2_msg_image.get_rect()
player2_msg_image_rect.center=player2_rect.center


#Quit Game
quit_screen =screen
quit_screen_rect=screen.get_rect()
quit_width=100
quit_height=30
quit_color=(200,200,200)
quit_text_color=(0,0,0)
quit_font=pygame.font.SysFont('comicsans', 35, True)
quit_rect=pygame.Rect(400,0, quit_width, quit_height)
quit_rect.centerx = quit_screen_rect.centerx
quit_rect.top=quit_screen_rect.top+550
quit_msg_image=quit_font.render("Quit", True, quit_text_color, quit_color)
quit_msg_image_rect=quit_msg_image.get_rect()
quit_msg_image_rect.center=quit_rect.center

menu_screen = screen
menu_screen_rect= screen.get_rect()
menu_width=100
menu_height = 30
menu_color=(200,200,200)
menu_text_color=(0,0,0)
menu_font=pygame.font.SysFont('comicsans', 30, True)
menu_rect=pygame.Rect(400, 0, menu_width, menu_height)
menu_rect.top=menu_screen_rect.top
menu_rect.centerx=menu_screen_rect.centerx-100
menu_msg_image=menu_font.render("Menu", True, menu_text_color, menu_color)
menu_msg_image_rect=menu_msg_image.get_rect()
menu_msg_image_rect.top=menu_rect.top+5
menu_msg_image_rect.center=menu_rect.center

#Pause Game
pause_screen = screen
pause_screen_rect= screen.get_rect()
pause_width=80
pause_height = 30
pause_color=(200,200,200)
pause_text_color=(0,0,0)
pause_font=pygame.font.SysFont('comicsans', 30, True)
pause_rect=pygame.Rect(250, 0, pause_width, pause_height)
pause_rect.top=pause_screen_rect.top
pause_rect.centerx=pause_screen_rect.centerx+100
pause_msg_image=pause_font.render("Pause", True, pause_text_color, pause_color)
pause_msg_image_rect=pause_msg_image.get_rect()
pause_msg_image_rect.top=pause_rect.top+5
pause_msg_image_rect.centerx=pause_rect.centerx

#Restart Game
restart_screen = screen
restart_screen_rect= screen.get_rect()
restart_width=100
restart_height = 30
restart_color=(200,200,200)
restart_text_color=(0,0,0)
restart_font=pygame.font.SysFont('comicsans', 30, True)
restart_rect=pygame.Rect(250, 0, restart_width, restart_height)
restart_rect.top=restart_screen_rect.top
restart_rect.centerx=restart_screen_rect.centerx+200
restart_msg_image=restart_font.render("Restart", True, pause_text_color, pause_color)
restart_msg_image_rect=restart_msg_image.get_rect()
restart_msg_image_rect.top=restart_rect.top+5
restart_msg_image_rect.centerx=restart_rect.centerx

#Single player
single_screen = screen
single_screen_rect= screen.get_rect()
single_width=250
single_height = 40
single_color=(200,200,200)
single_text_color=(0,0,0)
single_font=pygame.font.SysFont('comicsans', 40, True)
single_rect=pygame.Rect(250, 0, single_width, single_height)
single_rect.top=single_screen_rect.top+450
single_rect.centerx=single_screen_rect.centerx
single_msg_image=single_font.render("Single Player", True, single_text_color, single_color)
single_msg_image_rect=single_msg_image.get_rect()
single_msg_image_rect.top=single_rect.top+5
single_msg_image_rect.centerx=single_rect.centerx

#Multiplayer
multi_screen = screen
multi_screen_rect= screen.get_rect()
multi_width=250
multi_height = 40
multi_color=(200,200,200)
multi_text_color=(0,0,0)
multi_font=pygame.font.SysFont('comicsans', 40, True)
multi_rect=pygame.Rect(250, 0, multi_width, multi_height)
multi_rect.top=multi_screen_rect.top+500
multi_rect.centerx=multi_screen_rect.centerx
multi_msg_image=multi_font.render("Multi Player", True, multi_text_color, multi_color)
multi_msg_image_rect=multi_msg_image.get_rect()
multi_msg_image_rect.top=multi_rect.top+5
multi_msg_image_rect.centerx=multi_rect.centerx



single_game=False
multi_game=False
x=0
y=0
player_font=pygame.font.SysFont('comicsans', 30, True)
opponent_font=pygame.font.SysFont('comicsans', 30, True)
image_font=pygame.font.SysFont('comicsans', 70, True)

help1="To move player 1:"
help2="'a' for upward movement"
help3="'z' for downward movement"
help4="To move player 2:"
help5="'arrow Up' for upward movement"
help6="'arrow Down' for downward movement"

help_font=pygame.font.SysFont('comicsans', 25, True)

#Copyright
Copyright1="EMMY GAMES"
Copyright2="Copyright © 2020"
Copyright_font=pygame.font.SysFont('arial', 28, True)


game_stats=False
game_screen=False



#main event
while True:
	pygame.time.delay(0)
	for event in pygame.event.get():
		if event == pygame.QUIT:
			sys.exit()
			pygame.quit()
		
		#moving the player
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed-=2
			if event.key == pygame.K_DOWN:
				player_speed+=2
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed=0
			if event.key == pygame.K_DOWN:
				player_speed=0

		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y=pygame.mouse.get_pos()
			if menu_rect.collidepoint(mouse_x, mouse_y):
				click.play()
				applaud=False
				single_game=False
				multi_game=False
				restart_game()
				game_stats=False

		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y=pygame.mouse.get_pos()
			if quit_rect.collidepoint(mouse_x, mouse_y):
				applaud=False
				click.play()
				sys.exit()
				pygame.quit()


		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y=pygame.mouse.get_pos()
			if play_rect.collidepoint(mouse_x, mouse_y):
				applaud=False
				click.play()
				game_stats=True
				game_screen=True

		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y=pygame.mouse.get_pos()
			if pause_rect.collidepoint(mouse_x, mouse_y):
				applaud=False
				click.play()
				game_stats=False
				game_screen=False

		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y=pygame.mouse.get_pos()
			if restart_rect.collidepoint(mouse_x, mouse_y):
				applaud=False
				click.play()
				applaud=False
				restart_game()
				game_stats=False
				game_screen=False

		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y=pygame.mouse.get_pos()
			if single_rect.collidepoint(mouse_x, mouse_y):
				applaud=False
				click.play()
				single_game=True
				game_screen=False

		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y=pygame.mouse.get_pos()
			if multi_rect.collidepoint(mouse_x, mouse_y):
				applaud=False
				click.play()
				multi_game=True
				game_screen=False


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				opponent_speed-=2
			if event.key == pygame.K_z:
				opponent_speed+=2
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				opponent_speed=0
			if event.key == pygame.K_z:
				opponent_speed=0

		

	if game_stats:
		ball_animation()
		player_animation()
		if single_game:
			opponent_animation()
		elif multi_game:
			player_2()
		
		if ball.left<=0:
			y+=1
			ball_restart()
		if ball.right>=1000:
			x+=1
			ball_restart()
		applaud=False

	#Play screen
	play_screen.fill(play_color, play_rect)
	play_screen.blit(play_msg_image, play_msg_image_rect)
	
	#Draw the screen
	screen.fill(bg_color)

	#Show option screen
	if single_game==False and multi_game==False:
		single_screen.fill(single_color, single_rect)
		single_screen.blit(single_msg_image, single_msg_image_rect)

		#Multiplayer screen
		multi_screen.fill(multi_color, multi_rect)
		multi_screen.blit(multi_msg_image, multi_msg_image_rect)

		#Quit game
		quit_screen.fill(quit_color, quit_rect)
		quit_screen.blit(quit_msg_image, quit_msg_image_rect)

		image_text=image_font.render("PING PONG", 1, (200,200,200))
		screen.blit(image_text, (350, 20))
		img_screen.blit(img_image, img_rect)

		image_text=image_font.render("PING PONG", 1, (200,200,200))
		screen.blit(image_text, (350, 20))

		help_text1=help_font.render(help1, 1, (200,200,200))
		help_text2=help_font.render(help2, 1, (200,200,200))
		help_text3=help_font.render(help3, 1, (200,200,200))
		help_text4=help_font.render(help4, 1, (200,200,200))
		help_text5=help_font.render(help5, 1, (200,200,200))
		help_text6=help_font.render(help6, 1, (200,200,200))
		screen.blit(help_text1, (0,0))
		screen.blit(help_text2, (0,20))
		screen.blit(help_text3, (0,40))
		screen.blit(help_text4, (0,60))
		screen.blit(help_text5, (0,80))
		screen.blit(help_text6, (0,100))

		Copyright_text1=Copyright_font.render(Copyright1, 1, (200,200,200))
		Copyright_text2=Copyright_font.render(Copyright2, 1, (200,200,200))
		screen.blit(Copyright_text1, (700,500))
		screen.blit(Copyright_text2, (700,530))
		applaud=False


		





	


	if single_game or multi_game:
		pygame.draw.rect(screen, (255,0,0), player)
		pygame.draw.rect(screen, (0,0,255), opponent)
		pygame.draw.ellipse(screen, (255,255,255), ball)
		pygame.draw.aaline(screen, grey, (500, 0), (500, 600))
		player_text=player_font.render("Player 1: " + str(x), 1, (200,200,200))
		opponent_text=opponent_font.render("Player 2: " + str(y), 1, (200,200,200))
		screen.blit(player_text, (30, 0))
		screen.blit(opponent_text, (850, 0))
		applaud=False




		if game_screen==False:
			play_screen.fill(play_color, play_rect)
			play_screen.blit(play_msg_image, play_msg_image_rect)
			applaud=False

		menu_screen.fill(menu_color, menu_rect)
		menu_screen.blit(menu_msg_image, menu_msg_image_rect)

		pause_screen.fill(pause_color, pause_rect)
		pause_screen.blit(pause_msg_image, pause_msg_image_rect)

		restart_screen.fill(restart_color, restart_rect)
		restart_screen.blit(restart_msg_image, restart_msg_image_rect)

		if x==11:
			game_stats=False
			applaud=True
			player1_screen.fill(player1_color, player1_rect)
			player1_screen.blit(player1_msg_image, player1_msg_image_rect)
			game_screen=True

		if y==11:
			game_stats=False
			applaud=True
			player2_screen.fill(player2_color, player2_rect)
			player2_screen.blit(player2_msg_image, player2_msg_image_rect)
			game_screen=False

		if applaud:
			applause.play()



	

	pygame.display.flip()

