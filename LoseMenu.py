from init_glob_vars import *
from MenuButton import MenuButton


class LoseMenu:
    def __init__(self):
        self.font = pygame.font.SysFont("areal", 100)
        self.game_over_text = self.font.render('ВЫ ПРОИГРАЛИ', True, st.RED)
        self.back_button = MenuButton('Гл. меню', pygame.font.SysFont("areal", 60))
        self.continue_button = MenuButton('Продолжить', pygame.font.SysFont("areal", 60))

    def draw(self):
        screen.blit(self.game_over_text, (360, 340))
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
