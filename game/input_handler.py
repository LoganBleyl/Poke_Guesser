import pygame

class InputHandler:
    def __init__(self):
        self.current_text = ""

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.current_text = self.current_text[:-1]
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                text = self.current_text
                self.current_text = ""
                return text
            else:
                if event.unicode.isprintable():
                    self.current_text += event.unicode
        return None
    
    def clear(self):
        self.current_text = ""