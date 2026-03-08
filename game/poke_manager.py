import threading
import os
import random

import pygame
from api.pokeapi_client import get_pokemon, download_sprite
from utils.silhouette import create_silhouette

MAX_POKEMON = 898
CACHE_DIR = os.path.join("cache", "downloaded_sprites")

class PokeManager:
    def __init__(self):
        self.poke_name = None
        self.poke_index = None
        self.silhouette = None
        self.poke_image = None
        self._load_thread = None
        self.is_loading = True

    def load_pokemon(self):
        self.is_loading = True
        self.poke_name = None
        self.silhouette = None
        self.poke_image = None
        self._load_thread = threading.Thread(target=self._load_worker, daemon=True)
        self._load_thread.start()
        
    def _load_worker(self):
        self.poke_index = random.randint(1, MAX_POKEMON)
        pokemon_data = get_pokemon(self.poke_index)
        
        if not pokemon_data:
            print(f"Failed to load data for Pokémon #{self.poke_index}")
            self.is_loading = False
            return
        
        self.poke_name = pokemon_data["name"].lower()
        sprite_url = pokemon_data["sprites"]["front_default"]
        
        if not sprite_url:
            print(f"No sprite available for Pokémon #{self.poke_index}")
            self.is_loading = False
            return
        
        save_path = os.path.join(CACHE_DIR, f"{self.poke_index}.png")
        
        if download_sprite(sprite_url, save_path):
            self.silhouette = create_silhouette(save_path)
            self.poke_image = pygame.image.load(save_path).convert_alpha()
        else:
            print(f"Failed to download sprite for Pokémon #{self.poke_index}")
        
        self.is_loading = False
    
    @property
    def ready(self):
        return not self.is_loading and self.silhouette is not None