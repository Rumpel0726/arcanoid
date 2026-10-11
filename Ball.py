from init_glob_vars import *
import random as rn
from Bonus import Bonus
from Brick import brick_score


# Класс - мячик
class Ball():
    def __init__(self):
        self.ball_radius = st.BALL_RADIUS
        self.ball_speed = st.BALL_SPEED
        self.ball_rect = int(self.ball_radius * 2 ** 0.5)
        self.ball = pygame.Rect(550, 600, self.ball_radius, self.ball_radius)
        self.no_colis = False
        self.dx = -1
        self.dy = -1
        self.old_x = 0

    def draw(self, rocket_rect, bonus_list, game_menu, f_run, level_bricks, racket_eng):
        self.old_x = self.ball.x
        self.ball.x += self.ball_speed * self.dx
        self.ball.y += self.ball_speed * self.dy
        if self.ball.y > 720:
            return 0
        # Условие отражения с кирпичем
        for i in range(len(level_bricks)):
            if self.ball.colliderect(level_bricks[i].get_rect()) and level_bricks[i].get_visible() == 1 and (self.dy > 0 or self.dy < 0 or self.dx > 0 or self.dx < 0):
                if not self.no_colis:
                    self.dy = -self.dy
                if level_bricks[i].get_color() == st.RED:
                    level_bricks[i].set_unvisible()
                    game_menu.set_score(brick_score(level_bricks[i]))
                    # Создание бонуса
                    if level_bricks[i].bonus == 1:
                        bonus = Bonus()
                        if rn.randint(0, 1) == 0:
                            bonus.bonus_type = "plus"
                        elif rn.randint(0, 1) == 1:
                            bonus.bonus_type = "minus"
                        bonus.visible = 1
                        bonus.x_pos = level_bricks[i].get_rect().x
                        bonus.y_pos = level_bricks[i].get_rect().y
                        bonus_list.append(bonus)
                    elif level_bricks[i].bonus == 2:
                        bonus = Bonus()
                        bonus.bonus_type = "plus"
                        bonus.visible = 1
                        bonus.x_pos = level_bricks[i].get_rect().x
                        bonus.y_pos = level_bricks[i].get_rect().y
                        bonus_list.append(bonus)
                    elif level_bricks[i].bonus == 3:
                        bonus = Bonus()
                        bonus.bonus_type = "circle"
                        bonus.visible = 1
                        bonus.x_pos = level_bricks[i].get_rect().x
                        bonus.y_pos = level_bricks[i].get_rect().y
                        bonus_list.append(bonus)
                elif level_bricks[i].get_color() == st.YELLOW:
                    level_bricks[i].set_color(st.RED)
                elif level_bricks[i].get_color() == st.ORANGE:
                    level_bricks[i].set_color(st.YELLOW)
                elif level_bricks[i].get_color() == st.BLUE:
                    level_bricks[i].set_color(st.YELLOW)


        # Условие отражения с правой и левой стеной
        if self.ball.centerx < self.ball_radius or self.ball.centerx > st.HEIGHT - self.ball_radius:
            self.dx = -self.dx
        # Условие отражения с верхней стеной
        if self.ball.centery < self.ball_radius:
            self.no_colis = False
            self.dy = -self.dy
        # Условие отражения c рокеткой
        if rocket_rect.get_rect().y > 600:
            if self.ball.colliderect(rocket_rect.get_rect()) and self.dy > 0:
                #print(racket_eng)

                if self.ball.x > rocket_rect.get_rect().x+(rocket_rect.get_rect().width/2) + racket_eng:
                    self.dy = -self.dy
                    if self.old_x > self.ball.x:
                        self.dx = -self.dx
                else:
                    if self.ball.x < rocket_rect.get_rect().x+(rocket_rect.get_rect().width/2) - racket_eng:
                        self.dy = -self.dy
                        if self.old_x < self.ball.x:
                            self.dx = -self.dx
                    else:
                        self.dy = -self.dy
        pygame.draw.circle(screen, pygame.Color('white'), self.ball.center, self.ball_radius)
        return 1
