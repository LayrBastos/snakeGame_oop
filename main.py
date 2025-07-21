import pygame
from snake import Snake
from food import Food
from game_status import game_over

black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
dark_yellow = (204, 204, 0)
grass_green = (76, 153, 0)

pygame.init()
pygame.display.set_caption("Snake Game")
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

square_size = 20

def play_game():
    global game_over
    game_over = False
    snake = Snake(square_size, 15, 1200, 800)
    food = Food(square_size, red)

    food_x, food_y = food.generate(screen_width, screen_height)

    while not game_over:
        screen.fill(grass_green)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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
            food_x, food_y = food.generate()
        
        clock.tick(snake.game_speed)

play_game()
