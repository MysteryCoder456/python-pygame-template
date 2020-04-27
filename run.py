import pygame
from game.main import Game


def main():
	game = Game(1024, 720, "PygameTemplate")
	game.start()

	while game.running:
		game.clock.tick(game.FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.running = False

		game.logic()
		game.render(game.win)
		
		
if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
