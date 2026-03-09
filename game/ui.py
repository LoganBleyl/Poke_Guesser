import pygame



class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.SysFont('Arial', 24)
        self.font_small = pygame.font.SysFont('Arial', 18)
        self.font_xl = pygame.font.SysFont('Arial', 26)

    def draw(self, state):
        self.screen.fill((255,165,0))
        text = self.font_xl.render("Who's that pokemon?", True, (255, 255, 255))
        rect = text.get_rect(centerx=300, top=20)
        self.screen.blit(text, rect)
        
    
        if state["is_loading"]:
            text = self.font_large.render("Loading...", True, (255, 255, 255))
            rect = text.get_rect(centerx=780, top=300)
            self.screen.blit(text, rect)
            pygame.display.flip()
            return
        
        if state["feedback_message"]:
            text = self.font_small.render(state["feedback_message"], True, (255, 255, 255))
            rect = text.get_rect(centerx=400, top=450)
            self.screen.blit(text, rect)
        
        #loading the pokemon sprite
        rect = state["sprite"].get_rect(center=(400, 280))
        self.screen.blit(state["sprite"], rect)
        #loading the score
        surf = self.font_large.render(f"Score: {state['score']}", True, (255, 255, 255))
        rect = surf.get_rect(centerx=280, top=50)
        #loading the input text & box
        self.screen.blit(surf, rect)
        box_rect = pygame.Rect(200, 490, 400, 44)
        pygame.draw.rect(self.screen, (50, 50, 50), box_rect, border_radius=8)

        surf = self.font_large.render(state["input_text"], True, (255, 255, 255))
        text_rect = surf.get_rect(center=box_rect.center)
        self.screen.blit(surf, text_rect)

        pygame.display.flip()