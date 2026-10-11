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
