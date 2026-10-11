from init_glob_vars import *


class Racket:
    def __init__(self):
        self.racket = pygame.Rect(0, 0, st.RACKET_W, st.RACKET_H)

    def draw(self, x_, y_, w_):
        pygame.draw.rect(screen, st.GREEN, self.set_rect(x_, y_, w_, st.RACKET_H))

    def set_rect(self, x_, y_, w_, h_):
        self.racket.x = x_
        self.racket.y = y_
        self.racket.width = w_
        self.racket.height = h_
        return self.racket

    def get_rect(self):
        return self.racket


# Новая позиция рокетки по нажатым стрелкам
def move_racket(pos_x_, left_, right_, speed_, width_, field_w_):
    new_x = pos_x_
    if left_ and new_x > 0:
        new_x -= speed_
    if right_ and new_x < field_w_ - width_:
        new_x += speed_
    return new_x
