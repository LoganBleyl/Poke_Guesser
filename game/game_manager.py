from game.poke_manager import PokeManager
from game.input_handler import InputHandler
import pygame


class GameManager:
    def __init__(self):
        self.pokemon = PokeManager()
        self.input = InputHandler()
        self.score = 0
        self.feedback_timer = 0
        self.feedback_message = ""
        self.revealed = False
        self.pokemon.load_pokemon()
    
    def update(self):
        if self.feedback_timer > 0:
            self.feedback_timer -= 1
            if self.feedback_timer <= 0:
                self.feedback_message = ""
    
    def handle_event(self, event):
        if self.revealed:
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                self.revealed = False
                self.feedback_message = ""
                self.feedback_timer = 0
                self.input.clear()
                self.pokemon.load_pokemon()
            return
        else:
            handled_event = self.input.handle_event(event)
            if handled_event is not None:
                self._check_guess(handled_event)
    
    def _check_guess(self, guess):
        if guess.lower() == self.pokemon.poke_name:
            self.score += 1
            self.revealed = True
            self.feedback_message = "Correct!"
        else:
            self.feedback_message = "Wrong!"
            self.feedback_timer = 90

    def get_state(self):
        sprite = None
        if self.pokemon.ready:
            sprite = self.pokemon.poke_image if self.revealed else self.pokemon.silhouette
        return {
            "sprite": sprite,
            "score": self.score,
            "feedback_message": self.feedback_message,
            "revealed": self.revealed,
            "is_loading": self.pokemon.is_loading,
            "poke_name": self.pokemon.poke_name,
            "input_text": self.input.current_text
            }