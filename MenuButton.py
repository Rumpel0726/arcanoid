from init_glob_vars import *


class MenuButton:
    def __init__(self, button_text_, font_):
        self.btn_text = button_text_
        self.font_btn = pygame.font.SysFont("areal", 60)
        self.font_btn = font_
        self.button_text = self.font_btn.render(self.btn_text, True, st.WHITE)
        self.btn_rect = pygame.Rect(0, 0, 0, 0)
        self.hover_mode = 'NONE'

    def draw(self, x_, y_, w_, h_):
        self.btn_rect = pygame.Rect(x_, y_, w_, h_)
        pygame.draw.rect(screen, st.BLACK, pygame.Rect(x_, y_, w_, h_))
        screen.blit(self.button_text, (x_, y_))

    def hover(self): # - Изменяет цвет кнопки
        self.button_text = self.font_btn.render(self.btn_text, True, st.GREY)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        self.hover_mode = 'HOVER'

    def un_hover(self): # - Изменяет цвет кнопки
        if self.hover_mode == 'HOVER':
            self.button_text = self.font_btn.render(self.btn_text, True, st.WHITE)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.hover_mode = 'UN_HOVER'

    def get_rect(self):
        return self.btn_rect

    def hover_event(self, xy_):
        if self.get_rect().collidepoint(xy_):
            self.hover()
            return
        else:
            self.un_hover()
