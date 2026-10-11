from init_glob_vars import *
from MenuButton import MenuButton


class MainMenu:
    def __init__(self):
        self.font_caption = pygame.font.SysFont("areal", 100)
        self.caption = self.font_caption.render('А Р К А Н О И Д', True, st.RED)
        self.play_button = MenuButton('Играть', pygame.font.SysFont("areal", 60))
        self.settings_button = MenuButton('Настройки', pygame.font.SysFont("areal", 60))
        self.record_button = MenuButton('Рекорды', pygame.font.SysFont("areal", 60))
        self.change_user = MenuButton('Сменить пользователя', pygame.font.SysFont("areal", 60))
        self.exit_button = MenuButton('Выйти', pygame.font.SysFont("areal", 60))

    def draw(self):
        screen.blit(self.caption, (360, 100))
        self.play_button.draw(100, 200, 140, 40)
        self.settings_button.draw(100, 300, 220, 40)
        self.record_button.draw(100, 400, 200, 40)
        self.change_user.draw(100, 500, 400, 40)
        self.exit_button.draw(100, 600, 140, 40)

    def button_hover(self, xy_):
        self.play_button.hover_event(xy_)
        self.settings_button.hover_event(xy_)
        self.record_button.hover_event(xy_)
        self.change_user.hover_event(xy_)
        self.exit_button.hover_event(xy_)

    def button_click(self, xy_):
        if self.play_button.get_rect().collidepoint(xy_):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return 'PLAY_B'
        elif self.settings_button.get_rect().collidepoint(xy_):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            print(1)
            return 'SET_B'
        elif self.record_button.get_rect().collidepoint(xy_):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return 'REC_B'
        elif self.change_user.get_rect().collidepoint(xy_):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return 'REG_B'
        elif self.exit_button.get_rect().collidepoint(xy_):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return 'EXIT_B'
        else:
            return False


