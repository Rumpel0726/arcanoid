from init_glob_vars import *
from MenuButton import MenuButton


class InputFrame:
    def __init__(self):
        self.font = pygame.font.SysFont("areal", 50)
        self.text = ''

    def draw(self, text_, x_, y_):
        pygame.draw.rect(screen, st.WHITE, pygame.Rect(x_ - 2, y_ - 2, 250, 40))
        pygame.draw.rect(screen, st.BLACK, pygame.Rect(x_, y_, 246, 36))
        self.text = self.font.render(text_, True, st.WHITE)
        screen.blit(self.text, (x_, y_))

