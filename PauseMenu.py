from init_glob_vars import *
from MenuButton import MenuButton


class PauseMenu:
    def __init__(self):
        self.back_button = MenuButton('Гл. меню', pygame.font.SysFont("areal", 60))
        self.continue_button = MenuButton('Продолжить', pygame.font.SysFont("areal", 60))
        self.font = pygame.font.SysFont("areal", 100)
        self.pause_text = self.font.render('Пауза', True, st.WHITE)

    def draw(self):
        screen.blit(self.pause_text, (540, 210))
        self.back_button.draw(330, 500, 200, 40)
        self.continue_button.draw(700, 500, 200, 40)

    def button_hover(self, xy_):
        self.back_button.hover_event(xy_)
        self.continue_button.hover_event(xy_)

    def button_click(self, xy_):
        if self.back_button.get_rect().collidepoint(xy_):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return 'BACK_B'
        if self.continue_button.get_rect().collidepoint(xy_):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return 'CONT_B'
