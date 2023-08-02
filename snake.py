import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Warna RGB
WHITE = (248, 247, 243) 
GREEN = (21, 71, 52) 
RED = (169, 29, 54)

# Ukuran blok ular dan makanan
BLOCK_SIZE = 20

# Membuat layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Johan S")

# Kelas Ular
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (0, 0)
    
    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = ((x + dx * BLOCK_SIZE) % SCREEN_WIDTH, (y + dy * BLOCK_SIZE) % SCREEN_HEIGHT)
        
        # Periksa tabrakan dengan tubuh ular sendiri
        if new_head in self.body:
            return False
        
        self.body = [new_head] + self.body[:-1]
        return True
    
    def grow(self):
        x, y = self.body[-1]
        dx, dy = self.direction
        new_tail = ((x - dx * BLOCK_SIZE) % SCREEN_WIDTH, (y - dy * BLOCK_SIZE) % SCREEN_HEIGHT)
        self.body.append(new_tail)
    
    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

# Kelas Makanan
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()
    
    def spawn(self):
        self.position = (random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                         random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
    
    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

# Fungsi utama
def main():
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        if not snake.move():
            # Jika ular menabrak dirinya sendiri, game berakhir
            pygame.quit()
            return
        
        if snake.body[0] == food.position:
            snake.grow()
            food.spawn()

        screen.fill(WHITE)
        snake.draw()
        food.draw()
        pygame.display.flip()

        clock.tick(8)  # Kecepatan ular

if __name__ == "__main__":
    main()
