import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def get_pokemon(identifier):
    try:
        url = f"{BASE_URL}pokemon/{identifier}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {identifier}: {e}")
        return None

def download_sprite(sprite_url):
    try:
        response = requests.get(sprite_url, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error downloading sprite: {e}")
        return None