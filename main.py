import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
SPEED = 30
OBSTACLE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects!")

# Player setup
player = pygame.Rect(WIDTH // 2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
obstacles = []

# Game Loop
running = True
score = 0
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - SPEED > 0:
        player.x -= SPEED
    if keys[pygame.K_RIGHT] and player.x + SPEED < WIDTH - PLAYER_WIDTH:
        player.x += SPEED

    # Spawn obstacles
    if random.randint(1, 30) == 1:
        obstacles.append(pygame.Rect(random.randint(0, WIDTH - OBSTACLE_WIDTH), 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    # Move obstacles
    for obstacle in obstacles[:]:
        obstacle.y += OBSTACLE_SPEED
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            score += 1
        if obstacle.colliderect(player):
            running = False  # Game over

    # Draw player and obstacles
    pygame.draw.rect(screen, BLUE, player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)
    
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
