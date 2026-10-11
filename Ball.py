from init_glob_vars import *
import random as rn
from Bonus import make_bonus
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

    def draw(self, rocket_rect, bonus_list, game_menu, f_run, level_bricks, racket_eng):
        old_x = self.ball.x
        self.ball = move_ball(self.ball, self.ball_speed, self.dx, self.dy)
        if is_ball_lost(self.ball):
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
                    brick_rect = level_bricks[i].get_rect()
                    if level_bricks[i].bonus == 1:
                        bonus_type = "plus"
                        if rn.randint(0, 1) == 0:
                            bonus_type = "plus"
                        elif rn.randint(0, 1) == 1:
                            bonus_type = "minus"
                        bonus_list.append(make_bonus(bonus_type, brick_rect.x, brick_rect.y))
                    elif level_bricks[i].bonus == 2:
                        bonus_list.append(make_bonus("plus", brick_rect.x, brick_rect.y))
                    elif level_bricks[i].bonus == 3:
                        bonus_list.append(make_bonus("circle", brick_rect.x, brick_rect.y))
                elif level_bricks[i].get_color() == st.YELLOW:
                    level_bricks[i].set_color(st.RED)
                elif level_bricks[i].get_color() == st.ORANGE:
                    level_bricks[i].set_color(st.YELLOW)
                elif level_bricks[i].get_color() == st.BLUE:
                    level_bricks[i].set_color(st.YELLOW)


        # Условие отражения с правой и левой стеной
        self.dx = bounce_side_wall(self.ball, self.ball_radius, st.HEIGHT, self.dx)
        # Условие отражения с верхней стеной
        if is_top_wall_hit(self.ball, self.ball_radius):
            self.no_colis = False
            self.dy = -self.dy
        # Условие отражения c рокеткой
        self.dx, self.dy = bounce_racket(self.ball, old_x, self.dx, self.dy, rocket_rect.get_rect(), racket_eng)
        pygame.draw.circle(screen, pygame.Color('white'), self.ball.center, self.ball_radius)
        return 1


# Сдвиг мячика на один кадр, возвращает новый прямоугольник
def move_ball(ball_, speed_, dx_, dy_):
    new_ball = ball_.copy()
    new_ball.x += speed_ * dx_
    new_ball.y += speed_ * dy_
    return new_ball


# Мячик упал ниже экрана
def is_ball_lost(ball_):
    return ball_.y > 720


# Отражение от правой и левой стены
def bounce_side_wall(ball_, radius_, field_w_, dx_):
    if ball_.centerx < radius_ or ball_.centerx > field_w_ - radius_:
        return -dx_
    return dx_


# Мячик долетел до верхней стены
def is_top_wall_hit(ball_, radius_):
    return ball_.centery < radius_


# Отражение от рокетки
# Если мячик попал в край рокетки и летит к этому краю, то меняется и направление по X
def bounce_racket(ball_, old_x_, dx_, dy_, racket_rect_, racket_eng_):
    if racket_rect_.y > 600 and ball_.colliderect(racket_rect_) and dy_ > 0:
        racket_center = racket_rect_.x + racket_rect_.width / 2
        if ball_.x > racket_center + racket_eng_: # правый край
            if old_x_ > ball_.x:
                dx_ = -dx_
        elif ball_.x < racket_center - racket_eng_: # левый край
            if old_x_ < ball_.x:
                dx_ = -dx_
        dy_ = -dy_
    return dx_, dy_
