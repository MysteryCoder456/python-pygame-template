from win import *
import pygame


def start():
  	# initialize all your variables here
  	global x, y, radius
  	x = 0
  	y = 0
  	radius = 20
	
	
def logic():
	# write all the code that invloves logic here
	x = pygame.mouse.get_pos()[0]
	y = pygame.mouse.get_pos()[1]
	
	
def render():
	# write all your code for render in this function between "w.fill(background)" and "pygame.display.update()"
	w.fill(background)
	
	# (255, 255, 255) stands for white in RGB values
	pygame.draw.ellipse(w, (255, 255, 255), (x, y, radius * 2, radius * 2))
	
	pygame.display.update()
	
	
# !!! - DO NOT MODIFY THE BELOW CODE IN ANYWAY - !!!


def main():
	global running
	
	start()
	
	while running:
		# clock.tick() takes parameter than specifies the fps that you game should run at
		clock.tick(60)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				
		logic()
		render()
		
		
if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
