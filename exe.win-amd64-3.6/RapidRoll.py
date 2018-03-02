import pygame
import random
import time

pygame.init()

dis_width = 600
dis_height = 600
dis_background = (0,255,128)
ball_color = (255,0,0)
rect_color = (128,0,255)
score_color = (0,128,128)
button_color = (36,38,123)
hover = (51,138,21)

ball = pygame.image.load("ball.png")
startball = pygame.image.load("ball1.png")
die = pygame.mixer.Sound('die.wav')
menu = pygame.mixer.Sound('menu.wav')
pygame.mixer.music.load('play.wav')

game_display = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Rapid Roll')
clock = pygame.time.Clock()

def MainMenu():
	pygame.mixer.Sound.play(menu)
	game_display.fill(score_color)
	game_display.blit(startball,(250,150))
	font = pygame.font.SysFont("comicsansms",100)
	text = font.render("Rapid Roll",True,button_color)
	game_display.blit(text,(80,250))
	namefont = pygame.font.SysFont("comicsansms",15)
	nametext = namefont.render("Credit: Md Tomal Hossain",True,button_color)
	game_display.blit(nametext,(400,570))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		Button("Play >>",450,500,80,60,button_color,game_loop)
		Button("Quit",50,500,80,60,button_color,quitGame)
		pygame.display.update()
		clock.tick(15)

def Circle(x,y):
	game_display.blit(ball,(x,y))

def CreateObject(x,y,color):
	pygame.draw.rect(game_display,color,[x,y,100,10])

def ScoreBoard(count):
	font = pygame.font.SysFont("comicsansms",20)
	text = font.render("Score: "+str(count),True,score_color)
	game_display.blit(text,(0,0))

def Lives(life):
	font = pygame.font.SysFont("comicsansms",20)
	text = font.render("Lives: "+str(life),True,score_color)
	game_display.blit(text,(500,0))

def quitGame():
	pygame.quit()
	quit()

def Button(msg,x,y,w,h,color,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x<mouse[0]<x+w and y<mouse[1]<y+h:
		pygame.draw.rect(game_display,hover,(x,y,w,h))
		if click[0]==1 and action!= None:
			action()
	else:
		pygame.draw.rect(game_display,color,(x,y,w,h))
	font = pygame.font.SysFont("comicsansms",20)
	text = font.render(msg,True,dis_background)
	game_display.blit(text,(x+(w/5),y+(h/4)))

def GameOver():
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(menu)
	font = pygame.font.SysFont("comicsansms",80)
	text = font.render("Game Over",True,score_color)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		game_display.blit(text,(100,200))

		Button("Quit",150,300,80,60,button_color,quitGame)
		Button("Play Again",350,300,150,60,button_color,game_loop)
		pygame.display.update()
		clock.tick(15)

def game_loop():

	pygame.mixer.Sound.stop(menu)
	pygame.mixer.music.play(-1)
	circle_x = 250
	circle_y = 50
	x_change = 0
	y_change = 0

	rect_x1 = random.randrange(0,100)
	rect_x2 = random.randrange(0,100)
	rect_x3 = random.randrange(200,300)
	rect_x4 = random.randrange(200,300)
	rect_x5 = random.randrange(400,500)
	rect_x6 = random.randrange(400,500)

	rect_y1 = 610
	rect_y2 = 800
	rect_y3 = 680
	rect_y4 = 900
	rect_y5 = 750
	rect_y6 = 1000

	count = 0
	life = 3
	exit=False
	
	while not exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					x_change = 5
				if event.key == pygame.K_LEFT:
					x_change = -5
			if event.type == pygame.KEYUP:
				x_change = 0
		
		if count < 20:
			y_change = 2
		if count >= 20 and count < 50:
			y_change = 3
		if count >= 50 and count < 80:
			y_change = 4
		if count >= 80 and count < 120:
			y_change = 5
		if count >= 120 and count < 160:
			y_change = 6
		if count >=160 and count < 200:
			y_change = 7
		if count >=200 and count < 300:
			y_change = 8
		if count >=300:
			y_change = 10

		if (circle_x>5 and x_change==-5)  or  (circle_x<565 and x_change==5):
			circle_x+=x_change

		if(circle_y<0 or circle_y>600):
			pygame.mixer.Sound.play(die)
			life = life - 1
			circle_y = 100
			circle_x = 250
			time.sleep(1)
		if(rect_y1<0):
			rect_y1 = 605
			rect_x1 = random.randrange(0,100)
			count+=1
		if(rect_y2<0):
			rect_y2 = 605
			rect_x2 = random.randrange(0,100)
			count+=1
		if(rect_y3<0):
			rect_y3 = 605
			rect_x3 = random.randrange(200,300)
			count+=1
		if(rect_y4<0):
			rect_y4 = 605
			rect_x4 = random.randrange(200,300)
			count+=1
		if(rect_y5<0):
			rect_y5 = 605
			rect_x5 = random.randrange(400,500)
			count+=1
		if(rect_y6<0):
			rect_y6 = 605
			rect_x6 = random.randrange(400,500)
			count+=1
		
		rect_y1 -=y_change
		rect_y2 -=y_change
		rect_y3 -=y_change
		rect_y4 -=y_change
		rect_y5 -=y_change
		rect_y6 -=y_change


		if(circle_x+25>=rect_x1 and circle_x+5<=rect_x1+100 and rect_y1-circle_y<=30 and rect_y1-circle_y>15):
			circle_y -= y_change
		elif(circle_x+25>=rect_x2 and circle_x+5<=rect_x2+100 and rect_y2-circle_y<=30 and rect_y2-circle_y>15):
			circle_y -= y_change
		elif(circle_x+25>=rect_x3 and circle_x+5<=rect_x3+100 and rect_y3-circle_y<=30 and rect_y3-circle_y>15):
			circle_y -= y_change
		elif(circle_x+25>=rect_x4 and circle_x+5<=rect_x4+100 and rect_y4-circle_y<=30 and rect_y4-circle_y>15):
			circle_y -= y_change
		elif(circle_x+25>=rect_x5 and circle_x+5<=rect_x5+100 and rect_y5-circle_y<=30 and rect_y5-circle_y>15):
			circle_y -= y_change
		elif(circle_x+25>=rect_x6 and circle_x+5<=rect_x6+100 and rect_y6-circle_y<=30 and rect_y6-circle_y>15):
			circle_y -= y_change
		else:
			circle_y += y_change
		
		
		game_display.fill(dis_background)
		
		Circle(circle_x,circle_y)
		
		CreateObject(rect_x1,rect_y1,rect_color)
		CreateObject(rect_x2,rect_y2,rect_color)
		CreateObject(rect_x3,rect_y3,rect_color)
		CreateObject(rect_x4,rect_y4,rect_color)
		CreateObject(rect_x5,rect_y5,rect_color)
		CreateObject(rect_x6,rect_y6,rect_color)
		
		Lives(life)
		ScoreBoard(count)
		if life == 0:
		       GameOver()
		pygame.display.update()
		clock.tick(60)
MainMenu()
pygame.quit()
quit()
