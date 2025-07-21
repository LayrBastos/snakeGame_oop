import pygame


class Snake:
    def __init__(self, square_size, game_speed, screen_width, screen_height):
        self.square_size = square_size
        self.game_speed = game_speed
        self.body = []
        self.size = 1
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed_x = square_size
        self.speed_y = 0
        self.is_alive = True

    
    def draw(self, screen, size, head_color, body_color1, body_color2):
        for part in self.body:
            if self.body.index(part) == 0:
                pygame.draw.rect(screen, head_color, [part[0], part[1], size, size])
            elif self.body.index(part) % 2 == 0:
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
    

    def update_position(self):
        self.x += self.speed_x
        self.y += self.speed_y


    def insert_new_head(self):
        self.body.insert(0, [self.x, self.y])


    def remove_last_segment(self):
        if len(self.body) > self.size:
            self.body.pop()


    def check_selfcollision(self):
        for part in self.body[1:]:
            if part == [self.x, self.y]:
                self.game_over()


    def check_border_collision(self, screen_width, screen_height):
        if (self.x < 0) or (self.x >= screen_width) or (self.y < 0) or (self.y >= screen_height):
            self.game_over()

    
    def show_score(self, screen, score, color):
        font = pygame.font.SysFont("Helvetica", 40)
        text = font.render(f"Score: {score}", True, color)
        screen.blit(text, [1, 1])

    
    def game_over(self):
        self.is_alive = False
    