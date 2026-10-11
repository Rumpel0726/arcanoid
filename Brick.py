from init_glob_vars import *


class Brick():
    def __init__(self, color_=st.RED, bonus_=0, strong_=1, display_=1):
        self.color = color_
        self.bonus = bonus_
        self.strong = strong_
        self.disp = display_
        self.x_pos = 0
        self.y_pos = 0
        self.brick_rect = pygame.Rect((self.x_pos * (st.BRICK_W + 4) + 2, self.y_pos * (st.BRICK_H + 4) + 2, st.BRICK_W, st.BRICK_H))

    def set_pos(self, x_, y_):
        self.x_pos = x_
        self.y_pos = y_

    def set_color(self, color_):
        self.color = color_

    def set_strong(self, strong_):
        self.strong = strong_

    def draw(self):
        self.brick_rect = pygame.Rect((self.x_pos * (st.BRICK_W + 4) + 2, self.y_pos * (st.BRICK_H + 4) + 2, st.BRICK_W, st.BRICK_H))
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


# Очки за разбитый кирпич
def brick_score(brick_):
    if brick_.bonus == 0:
        return 10
    elif brick_.bonus == 1:
        return 20
    elif brick_.bonus == 2:
        return 40
    return 0
