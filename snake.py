import pygame

class Snake:
    def __init__(self, square_size, game_speed):
        self.square_size = square_size
        self.game_speed = game_speed
        self.body = []

    
    def draw(self, screen, size, body_parts, head_color, body_color1, body_color2):
        for part in body_parts:
            if body_parts.index(part) == 0:
                pygame.draw.rect(screen, head_color, [part[0], part[1], size, size])
            elif body_parts.index(part) % 2 == 0:
                pygame.draw.rect(screen, body_color1, [part[0], part[1], size, size])
            else:
                pygame.draw.rect(screen, body_color2, [part[0], part[1], size, size])

    def goes_to_opposite_direction(self, current_x, current_y, new_x, new_y):
        return (current_x == -new_x and current_y == new_y) or (current_y == -new_y and current_x == new_x)
    
    def select_speed(self, key, current_speed_x, current_speed_y):
        new_speed_x, new_speed_y = current_speed_x, current_speed_y   
        if key == pygame.K_DOWN:
            if not self.goes_to_opposite_direction(current_speed_x, current_speed_y, 0, self.square_size):
                new_speed_x, new_speed_y = 0, self.square_size
        elif key == pygame.K_UP:
            if not self.goes_to_opposite_direction(current_speed_x, current_speed_y, 0, -self.square_size):
                new_speed_x, new_speed_y = 0, -self.square_size
        elif key == pygame.K_LEFT:
            if not self.goes_to_opposite_direction(current_speed_x, current_speed_y, -self.square_size, 0):
                new_speed_x, new_speed_y = -self.square_size, 0
        elif key == pygame.K_RIGHT:
            if not self.goes_to_opposite_direction(current_speed_x, current_speed_y, self.square_size, 0):
                new_speed_x, new_speed_y = self.square_size, 0

        return new_speed_x, new_speed_y
    
    def show_score(self, screen, score, color):
        font = pygame.font.SysFont("Helvetica", 40)
        text = font.render(f"Score: {score}", True, color)
        screen.blit(text, [1, 1])
    