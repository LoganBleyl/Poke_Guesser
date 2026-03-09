import pygame
from game.game_manager import GameManager
from game.ui import UI




def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Who's That Pokémon?")
    clock = pygame.time.Clock()
    game_manager = GameManager()
    ui = UI(screen)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                game_manager.handle_event(event)
        game_manager.update()
        state = game_manager.get_state()
        ui.draw(state)
        clock.tick(60)
       
       

if __name__ == "__main__":
    main()
