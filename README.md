# Guess the Number Game

This repository contains two versions of the "Guess the Number" game: a command-line interface (CLI) version and a graphical user interface (GUI) version using Pygame.

## Install

To run the GUI version, you need to install the required dependencies. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## CLI Version

The CLI version of the game is implemented in [cli_guess_number_game.py](cli_guess_number_game.py). In this version, the player guesses a number between 1 and 99 within a specified number of attempts.

### How to Run

```bash
python cli_guess_number_game.py
```

## GUI Version

The GUI version of the game is implemented in [gui_guess_number_game.py](gui_guess_number_game.py) using Pygame. In this version, the player guesses a number between 1 and 99 with visual feedback.

### How to Run

```bash
python gui_guess_number_game.py
```

## Loading Background Music

To enhance the gaming experience, you can add background music to the game. Download the background music from [Pixabay](https://pixabay.com/music/search/number%20game/) and save it in the project directory.

### How to Load Music in Pygame

1. Download the music file from the provided link.
2. Save the music file in the same directory as your game scripts.
3. Add the following code to your `gui_guess_number_game.py` to load and play the music:

```python
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load the background music
pygame.mixer.music.load('background_music.mp3')  # Replace with your music file name

# Play the background music
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
```

## Game Rules

1. The game randomly selects a number between 1 and 99.
2. The player enters their guess.
3. The game provides feedback:
   - "Guess is low" if the guess is lower than the number.
   - "Guess is high" if the guess is higher than the number.
   - "Congrats, you guessed it!" if the guess is correct.
4. In the CLI version, the player has a limited number of attempts to guess the number.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This game was developed by [Halip26](https://halip26.github.io/).