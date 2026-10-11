from init_glob_vars import *
import random as rn
from Bonus import make_bonus, choose_bonus_type
from Brick import brick_score, next_brick_color
from lists import add_element_last


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

    # Движение мячика на один кадр
    # Возвращает: 0 - мячик упал / 1, очки за кадр, новый список бонусов
    def move(self, racket_, bonus_list, level_bricks, racket_eng):
        old_x = self.ball.x
        self.ball = move_ball(self.ball, self.ball_speed, self.dx, self.dy)
        if is_ball_lost(self.ball):
            return 0, 0, bonus_list
        score = 0
        # Условие отражения с кирпичем
        for i in range(len(level_bricks)):
            if self.ball.colliderect(level_bricks[i].get_rect()) and level_bricks[i].get_visible() == 1:
                if not self.no_colis:
                    self.dy = -self.dy
                new_color = next_brick_color(level_bricks[i].get_color())
                if new_color is None: # кирпич разбит
                    level_bricks[i].set_unvisible()
                    score += brick_score(level_bricks[i])
                    # Создание бонуса
                    bonus_type = choose_bonus_type(level_bricks[i], rn.randint(0, 1), rn.randint(0, 1))
                    if bonus_type != '':
                        brick_rect = level_bricks[i].get_rect()
                        bonus_list = add_element_last(bonus_list, make_bonus(bonus_type, brick_rect.x, brick_rect.y))
                else:
                    level_bricks[i].set_color(new_color)

        # Условие отражения с правой и левой стеной
        self.dx = bounce_side_wall(self.ball, self.ball_radius, st.HEIGHT, self.dx)
        # Условие отражения с верхней стеной
        if is_top_wall_hit(self.ball, self.ball_radius):
            self.no_colis = False
            self.dy = -self.dy
        # Условие отражения c рокеткой
        self.dx, self.dy = bounce_racket(self.ball, old_x, self.dx, self.dy, racket_.get_rect(), racket_eng)
        return 1, score, bonus_list

    def draw(self):
        pygame.draw.circle(screen, pygame.Color('white'), self.ball.center, self.ball_radius)


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
