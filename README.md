# 🎮 Pokéguesser

> *Who's That Pokémon?* — A Python guessing game built with Pygame and the PokéAPI.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![PokéAPI](https://img.shields.io/badge/Data-PokéAPI-red)

---

## About

Pokéguesser is a single-player guessing game inspired by the classic *"Who's That Pokémon?"* segments from the animated series. A random Pokémon is fetched live from the [PokéAPI](https://pokeapi.co/), converted into a black silhouette, and displayed on screen. Your job is to guess its name.

Guess correctly and the Pokémon is revealed. Keep going and watch your score grow.

Built as a first mid-level Python project to practise:
- REST API integration with live data fetching
- Image manipulation with Pillow
- Multi-threaded background loading
- Pygame game loop architecture
- Clean multi-file project structure

---

## How to Play

1. **A silhouette appears** — a random Pokémon is fetched and displayed as a black shape.
2. **Type your guess** into the input box at the bottom of the screen.
3. **Press Enter** to submit your guess.
   - ✅ Correct — the Pokémon is revealed and you gain a point. Press Enter to load the next one.
   - ❌ Wrong — try again. The input box clears automatically.
4. **Press Space** at any time to reveal the answer and skip to the next Pokémon (no point awarded).

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/pokeguesser.git
cd pokeguesser

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install pygame requests pillow
```

### Run the game

```bash
python main.py
```

> **Note:** The first run will download Pokémon sprites from the PokéAPI. Sprites are cached locally in `cache/downloaded_sprites/` so subsequent runs load instantly.

---

## Built With

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/) — game window, rendering, and input
- [Requests](https://requests.readthedocs.io/) — HTTP calls to the PokéAPI
- [Pillow](https://pillow.readthedocs.io/) — silhouette image generation
- [PokéAPI](https://pokeapi.co/) — live Pokémon data and sprites

---

*First 898 Pokémon supported (Generations 1–8).*
