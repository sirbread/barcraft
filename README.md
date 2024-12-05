# barcraft
"real, 3D Minecraft, purely in python" <br>
**This project is based off a _similar_ tutorial to the following link, as the original tutorial is now not availible:** <br>
[Tutorial](http://www.codingwithruss.com/ursina/minecraft-in-python-3d-game-tutorial/) <br>
Side note, the old tutorial did have download links to CC0 assets which is where I obtained the assets for this game. :) <br>

This project is a Minecraft-inspired sandbox game built using the [Ursina Engine](https://www.ursinaengine.org/). The game allows players to explore a generated flat area, place and destroy blocks, and interact with objects like a mini solar system.

## Features

- **Voxel Terrain**: Generate a simple flat world with grass blocks.
- **Block Placement**: Add blocks of different types, including grass, stone, brick, dirt, and solar systems.
- **Block Removal**: Destroy blocks using the left mouse button.
- **Solar System**: Create a solar system block that animates an orbiting planet.
- **First-Person Controlled**
- **Fail-safe**: Teleport back to the starting point if the player falls below the map.
---

## Controls

- **WASD or Arrow Keys**: Move the player.
- **Mouse Movement**: Look around.
- **Left Mouse Button**: Destroy blocks.
- **Right Mouse Button**: Place blocks of the selected type.
- **Number Keys (1-5)**: Switch between block types:
  - `1`: Grass block
  - `2`: Stone block
  - `3`: Brick block
  - `4`: Dirt block
  - `5`: Solar system block
- **ESC**: Exit the game.

### Requirements
- Python 3.11+
- Ursina Engine

### Installation/Running

1. Clone thy repo:
2. Install the Ursina Engine:
    ```bash
    pip install ursina
    ```
3. Ensure all assets are located in the `assets/` folder, including textures, models, and sounds.
4. Run the `main.py` file:
    ```bash
    python main.py
    ```


## Manifest
- README.md:
  This file.

- main.py:
  The main barcraft code.

- assetTest.py:
  A little script to test new models and textures.

- sims.py:
  Methods that control the various simulations in the world. Might change this later as there becomes more simulations.

- assets:
  Folder that contains all of the models, textures and audio files.


## Acknowledgments
- Inspiration from Mojang's *Minecraft*.
