from init_glob_vars import *


class Brick():
    def __init__(self, color_=st.RED, bonus_=0, strong_=1, display_=1):
        self.color = color_
        self.bonus = bonus_
        self.strong = strong_
        self.disp = display_
        self.x_pos = 0
        self.y_pos = 0
        self.brick_rect = brick_rect_by_pos(self.x_pos, self.y_pos, st.BRICK_W, st.BRICK_H)

    def set_pos(self, x_, y_):
        self.x_pos = x_
        self.y_pos = y_
        self.brick_rect = brick_rect_by_pos(self.x_pos, self.y_pos, st.BRICK_W, st.BRICK_H)

    def set_color(self, color_):
        self.color = color_

    def set_strong(self, strong_):
        self.strong = strong_

    def draw(self):
        pygame.draw.rect(screen, self.color, self.brick_rect)

    def get_rect(self):
        return self.brick_rect

    # Сделаем видимым
    def get_visible(self):
        return self.disp

    # Сделаем невидимым
    def set_unvisible(self):
        self.disp = 0

    # Изменить цвет
    def get_color(self):
        return self.color


# Прямоугольник кирпича по его месту в сетке уровня
def brick_rect_by_pos(x_pos_, y_pos_, w_, h_):
    return pygame.Rect((x_pos_ * (w_ + 4) + 2, y_pos_ * (h_ + 4) + 2, w_, h_))


# Создание кирпича по коду из файла уровня
def make_brick(code_, x_, y_):
    if code_ == 2:
        brick = Brick(st.YELLOW, 1, 2)
    elif code_ == 3:
        brick = Brick(st.ORANGE, 2)
    elif code_ == 4:
        brick = Brick(st.BLUE, 3)
    else:
        brick = Brick(st.RED)
    brick.set_pos(x_, y_)
    return brick


# Цвет кирпича после удара, None - кирпич разбит
def next_brick_color(color_):
    if color_ == st.RED:
        return None
    elif color_ == st.YELLOW:
        return st.RED
    elif color_ == st.ORANGE:
        return st.YELLOW
    elif color_ == st.BLUE:
        return st.YELLOW
    return color_


# Очки за разбитый кирпич
def brick_score(brick_):
    if brick_.bonus == 0:
        return 10
    elif brick_.bonus == 1:
        return 20
    elif brick_.bonus == 2:
        return 40
    return 0
