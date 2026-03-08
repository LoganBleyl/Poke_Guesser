import requests
import os

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

def download_sprite(url, save_path):
    if os.path.exists(save_path):
        return True

    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error downloading sprite: {e}")
        return False
