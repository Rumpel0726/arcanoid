from init_glob_vars import *


class Bonus():
    def __init__(self):
        self.visible = 0
        self.x_pos = 0
        self.y_pos = 0
        self.bonus_type = "plus"

    def draw(self):
        if self.visible == 1:
            # pygame.draw.rect(screen, st.BLUE, pygame.Rect(self.x_pos, self.y_pos, st.BONUS_W, st.BONUS_H))
            if self.bonus_type == "plus":
                screen.blit(bonus_plus, (self.x_pos, self.y_pos))
            elif self.bonus_type == "minus":
                screen.blit(bonus_minus, (self.x_pos, self.y_pos))
            elif self.bonus_type == "circle":
                screen.blit(bonus_circle, (self.x_pos, self.y_pos))
            self.y_pos += st.BONUS_SPEED
            if self.y_pos == st.HEIGHT:
                self.visible = 0

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, 35, 35)


# Тип бонуса из разбитого кирпича, '' - бонуса нет
# rnd1_ и rnd2_ - случайные числа 0 или 1
def choose_bonus_type(brick_, rnd1_, rnd2_):
    if brick_.bonus == 1:
        if rnd1_ == 0:
            return "plus"
        elif rnd2_ == 1:
            return "minus"
        return "plus"
    elif brick_.bonus == 2:
        return "plus"
    elif brick_.bonus == 3:
        return "circle"
    return ''


# Создание бонуса
def make_bonus(bonus_type_, x_, y_):
    bonus = Bonus()
    bonus.bonus_type = bonus_type_
    bonus.visible = 1
    bonus.x_pos = x_
    bonus.y_pos = y_
    return bonus
