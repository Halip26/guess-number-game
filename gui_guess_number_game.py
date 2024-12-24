import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (4, 204, 17)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

# Fonts
font = pygame.font.Font(None, 36)

# Random number
number = random.randint(1, 99)

# Game variables
input_text = ""
instruction_message = "Guess a number between 1 and 99: "
result_message = ""
result_color = BLACK
game_over = False


# Main game loop
def main():
    global input_text, result_message, result_color, game_over, number

    while True:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_RETURN:
                    if input_text.isdigit():
                        guess = int(input_text)
                        if guess < number:
                            result_message = "Guess is low"
                            result_color = ORANGE  # Set color to orange
                        elif guess > number:
                            result_message = "Guess is high"
                            result_color = RED  # Set color to red
                        else:
                            result_message = "Congrats, you guessed it!"
                            result_color = GREEN  # Set color to green
                            game_over = True
                        input_text = ""
                    else:
                        result_message = "Please enter a valid number"
                        result_color = BLACK
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < 3:
                        input_text += event.unicode

        # Render the instruction message
        instruction_surface = font.render(instruction_message, True, BLACK)
        screen.blit(
            instruction_surface, (WIDTH // 2 - instruction_surface.get_width() // 2, 50)
        )

        # Draw the input box
        pygame.draw.rect(screen, BLACK, (150, 150, 300, 50), 2)

        # Render the input text
        input_surface = font.render(input_text, True, BLACK)
        screen.blit(input_surface, (160, 160))

        # Render the result message (below the input box)
        result_surface = font.render(result_message, True, result_color)
        screen.blit(result_surface, (150, 220))

        # Update the display
        pygame.display.flip()


# Run the game
main()
