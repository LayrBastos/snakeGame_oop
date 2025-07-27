import pygame
from snake import Snake
from food import Food

black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
dark_yellow = (204, 204, 0)
grass_green = (76, 153, 0)

pygame.init()
pygame.display.set_caption("Snake Game")
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

square_size = 20

def play_game():
    snake = Snake(square_size, 15, screen_width, screen_height)
    food = Food(square_size, red)

    food_x, food_y = food.generate(screen_width, screen_height)

    while snake.is_alive:
        screen.fill(grass_green)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                snake.game_over()
            elif event.type == pygame.KEYDOWN:
                snake.speed_x, snake.speed_y = snake.select_speed(event.key, snake.speed_x, snake.speed_y)

        food.draw(screen, food_x, food_y)

        snake.update_position()
        snake.insert_new_head()
        snake.remove_last_segment()
        snake.check_selfcollision()
        snake.check_border_collision(screen_width, screen_height)
        snake.draw(screen, square_size, black, yellow, dark_yellow)
        snake.show_score(screen, snake.size - 1, black)

        pygame.display.update()

        if (snake.x == food_x) and (snake.y == food_y):
            snake.size += 1
            food_x, food_y = food.generate(screen_width, screen_height)
        
        clock.tick(snake.game_speed)

play_game()
