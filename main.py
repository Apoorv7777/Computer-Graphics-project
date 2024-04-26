import pygame
import sys

# Initialize pygame
pygame.init()
pygame.display.set_caption("Game Selection")
clock = pygame.time.Clock()

# Set up the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Function to display text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Main game loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked on the buttons
                if game1_button_rect.collidepoint(event.pos):
                    # Run game1.py
                    import game1
                    game1.main()
                elif game2_button_rect.collidepoint(event.pos):
                    # Run game2.py
                    import game2
                    game2.main()

        # Clear the screen
        screen.fill(BLACK)

        # Add background decoration
        pygame.draw.rect(screen, GRAY, pygame.Rect(100, 150, 600, 400))

        # Draw buttons
        game1_button_rect = pygame.Rect(250, 250, 300, 50)
        pygame.draw.rect(screen, WHITE, game1_button_rect)
        draw_text("Play Game 1", font, BLACK, 400, 275)

        game2_button_rect = pygame.Rect(250, 350, 300, 50)
        pygame.draw.rect(screen, WHITE, game2_button_rect)
        draw_text("Play Game 2", font, BLACK, 400, 375)

        # Add title
        draw_text("Game Selection", font, WHITE, WIDTH // 2, 100)

        # Update the display
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()

