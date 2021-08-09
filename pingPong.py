import pygame, sys,ctypes, random, time, pyautogui
from pygame.locals import *
from ctypes import *

	
pygame.init()

black = (0,0,0)
white = (255, 255 , 255)
red = (255,0,0)
green = (0,255,0)



class GameGUI():



	def __init__(self):
		
		#pygame.init()
		whidth,hight = pyautogui.size()
		


		screen = pygame.display.set_mode((whidth,hight))#,pygame.FULLSCREEN)


		clock = pygame.time.Clock()

		now = time.time()
		future = now + 10

		start_ticks=pygame.time.get_ticks()

		black = (0,0,0)
		white = (255, 255 , 255)

		rectWidth = 10
		rectHight= 100


		borderX = 100
		borderY = 120


		dx = 5
		dy = -5
		x = whidth// 2 -20
		y = hight //2 

		rightScore = 0
		leftScore = 0


		rightRect = hight//2 - rectHight//2
		leftRect = hight//2 - rectHight//2



		font = pygame.font.Font('freesansbold.ttf', 32) 
		text = font.render('PING PONG', True, white, None)
		textRect = text.get_rect()  
		textRect.center = (whidth//2 + 10, hight // 2) 


		scoreFont = pygame.font.Font('freesansbold.ttf', 60)
		score1 = scoreFont.render(str(rightScore), True, white, black) 
		score1Rect = score1.get_rect()  
		score1Rect.center = (borderX, borderY - 50) 

		score2 = scoreFont.render(str(leftScore), True, white, black) 
		score2Rect = score2.get_rect()  
		score2Rect.center = (whidth - borderX, borderY - 50) 
	


		while True:


			r = random.randint(borderY , hight-borderY - 10)

			screen.fill(black)
			#circle = pygame.draw.circle(screen, white,(x, y),50)
			ballRectangle = pygame.draw.rect(screen, white,(x, y,10,10))
			leftRectangle = pygame.draw.rect(screen, white,(borderX + 10, leftRect, rectWidth, rectHight))
			rightRectangle = pygame.draw.rect(screen, white,(whidth-borderX - rectWidth - 10, rightRect, rectWidth, rectHight))
			borderRectangle = pygame.draw.rect(screen , white, (borderX, borderY, whidth-2*borderX, hight-2*borderY),3)


			pygame.draw.line(screen,white,(whidth//2,borderY),(whidth//2,hight-borderY),2)


			x+=dx
			y+=dy

			
			clock.tick(60)


			score1 = scoreFont.render(str(rightScore), True, white, black) 
			score1Rect = score1.get_rect()  
			score1Rect.center = (borderX + 50, borderY - 50)

			score2 = scoreFont.render(str(leftScore), True, white, black) 
			score2Rect = score2.get_rect()  
			score2Rect.center = (whidth - borderX -50, borderY - 50) 



			screen.blit(text, textRect) 

			screen.blit(score1,score1Rect)

			screen.blit(score2,score2Rect)



			keys=pygame.key.get_pressed()



			seconds=(pygame.time.get_ticks()-start_ticks)/1000 
			if seconds > 9:
				
				if dx < 0:
					dx-=1
				if dx > 0:
					dx+=1
				if dy < 0:
					dy-=1
				if dy > 0:
					dy+=1

				start_ticks=pygame.time.get_ticks()


			if keys[K_UP] and rightRect >borderY:
				rightRect -=10
			if keys[K_DOWN] and rightRect <hight - rectHight - borderY:
				rightRect +=10


			if  not aiActivator:
				if (keys[K_z] or keys[K_w]) and leftRect >borderY:
					leftRect -=10
				if keys[K_s] and leftRect <hight - rectHight - borderY:
					leftRect +=10

			else:

				leftRect = self.ai(dx,dy,x,y,whidth,hight,borderY,borderX,rectHight,leftRect)


			if ballRectangle.colliderect(rightRectangle) :
				if y in range(rightRect, rightRect+33) :
				
					x = whidth-borderX - rectWidth - 22
					dx*=-1

					if dy>0:
						dy*=-1

					if dy == 0:
						dy = dx



				elif y in range(rightRect+33, rightRect+66) :
				
					x = whidth-borderX - rectWidth - 22
					dx*=-1
					dy = 0
					

				elif y in range(rightRect+66, rightRect+101) :
				
					x = whidth-borderX - rectWidth - 22
					dx*=-1

					if dy<0:
						dy*=-1

					if dy == 0:
						dy = dx



			if ballRectangle.colliderect(leftRectangle):
				if y in range(leftRect, leftRect+33) :
				
					x = borderX + 22
					dx*=-1

					if dy>0:
						dy*=-1

					if dy == 0:
						dy = dx



				elif y in range(leftRect+33, leftRect+66) :
				
					x = borderX + 22
					dx*=-1
					dy = 0
					

				elif y in range(leftRect+66, leftRect+101) :
				
					x = borderX + 22
					dx*=-1

					if dy<0:
						dy*=-1

					if dy == 0:
						dy = dx


			if y <= borderY or y>=(hight - borderY - 10):
				dy*=-1


			if x <= borderX:
				x = whidth/2
				y = r
				dx = -5
				dy = 5
				dx*=-1
				leftScore +=1


			if x>=whidth - borderX:
				x = whidth/2
				y = r
				dx = 5
				dy = 5
				dx*=-1
				rightScore +=1




			for event in pygame.event.get():
		        	if event.type==QUIT or keys[K_ESCAPE]:
		            		pygame.quit()
		            		sys.exit()




		    
			pygame.display.update()


		screen.destroyAllWindows()


	def ai(self,dx,dy,x,y,whidth,hight,borderY,borderX,rectHight,leftRect):

		local = leftRect

		bounce = False

		xPredict = x
		yPredict = y

		

		if dx<0 and x > borderX and x < whidth//2 :

			while True: 

				yPredict += dy
				xPredict += dx


				if (yPredict <= borderY or yPredict >= hight - borderY) and xPredict >= borderX:
					bounce = True
					break 

				elif xPredict < borderX :

					break
			 

			
			if not bounce:

				if  yPredict + 5 < local  and local > borderY :

					local -= 10


				elif  yPredict + 5 > local+ rectHight  and local  < hight - borderY - rectHight:

					local += 10


			elif borderX <= xPredict <= 290 and dy<0:
				
				if yPredict > local + rectHight and not bounce: 

					local+=10


				elif local > borderY: 

					local-=10


			elif borderX <= xPredict <= 290 and dy>0: 

				if yPredict < local and not bounce : 

					local -=10

				elif local < hight - borderY - rectHight:

					local +=10

		
		else: 

			if local < hight//2 -  rectHight//2  :
				
				local +=   10
			
			elif local  > hight//2 - rectHight//2  :
				
				local -=  10

		

					
		return local




class Interface():
	
	interface = pygame.display.set_mode((500,500))

	

	rectWidth = 165
	rectHight = 50


	x = 263

	dx = 13

	clicked = True 

	global aiActivator 
	aiActivator = False 

	buttonFont = pygame.font.Font('freesansbold.ttf', 18)

	titleFont = pygame.font.Font('freesansbold.ttf',60)




	buttonTextColor = white
	buttonTextColor2 = white

	buttonBorder = 3
	buttonBorder2 = 3

	clock = pygame.time.Clock()
	clock2 = pygame.time.Clock()


	while True:
		
		interface.fill(black)
		
		
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		singlePlayer = pygame.draw.rect(interface, white, (250-rectWidth//2,250-rectHight //2,rectWidth,rectHight), buttonBorder )

		DoublePlayer = pygame.draw.rect(interface, white, (250-rectWidth//2  ,310-rectHight //2,rectWidth,rectHight), buttonBorder2 )


		buttonText = buttonFont.render('SINGLE PLAYER', True, buttonTextColor, None) 
		buttonRect = buttonText.get_rect()  
		buttonRect.center = (250,250)


		buttonText2 = buttonFont.render('DOUBLE PLAYER', True, buttonTextColor2, None) 
		buttonRect2 = buttonText2.get_rect()  
		buttonRect2.center = (250,310)


		titleText = titleFont.render('PING PONG', True, white, None) 
		titleRect = titleText.get_rect()  
		titleRect.center = (250,100)
 

		interface.blit(buttonText,buttonRect)

		interface.blit(buttonText2,buttonRect2)

		interface.blit(titleText,titleRect)


		if  250-rectWidth//2 <mouse[0]< 250+rectWidth//2 and 250-rectHight //2 <mouse[1]< 250+rectHight//2:

			buttonTextColor = black
			buttonBorder = 0
			
			if click[0]==1:
				aiActivator = True
				GameGUI()

		else : 
			buttonTextColor = white
			buttonBorder = 3
		

		if  250-rectWidth//2 <mouse[0]< 250+rectWidth//2 and 310-rectHight //2 <mouse[1]< 310+rectHight//2:

			buttonTextColor2 = black
			buttonBorder2 = 0
			
			if click[0]==1:
				
				GameGUI()

		else : 
			buttonTextColor2 = white
			buttonBorder2 = 3

		

		for event in pygame.event.get():
				if event.type==QUIT:
						pygame.quit()
						sys.exit()

	
		pygame.display.update()
