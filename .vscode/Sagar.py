import pygame
import random

pygame.init()

# Set up the display
WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the fonts
FONT = pygame.font.SysFont(None, 50)

# Set up the game variables
CELL_SIZE = 20
SPEED = 5
SCORE = 0

# Set up the snake and food
snake = [(WIDTH // 2, HEIGHT // 2)]
dx, dy = CELL_SIZE, 0
food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
        random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

# Set up the game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy != CELL_SIZE:
                dx, dy = 0, -CELL_SIZE
            elif event.key == pygame.K_DOWN and dy != -CELL_SIZE:
                dx, dy = 0, CELL_SIZE
            elif event.key == pygame.K_LEFT and dx != CELL_SIZE:
                dx, dy = -CELL_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx != -CELL_SIZE:
                dx, dy = CELL_SIZE, 0

    # Move the snake
    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)
    snake.pop()

    # Check for collisions
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        game_over = True
    elif head == food:
        food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
        SCORE += 1
    else:
        for body in snake[1:]:
            if head == body:
                game_over = True

    # Draw the screen
    SCREEN.fill(BLACK)
    for x, y in snake:
        pygame.draw.rect(SCREEN, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(SCREEN, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Draw the score
    score_text = FONT.render(f"Score: {SCORE}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(SPEED)

# Quit the game
pygame.quit()