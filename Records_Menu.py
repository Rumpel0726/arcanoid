from init_glob_vars import *
from MenuButton import MenuButton
from RecordTable import RecordTable


class Records_Menu:
    def __init__(self):
        self.back_button = MenuButton('Назад', pygame.font.SysFont("areal", 60))
        self.record_table = RecordTable()

    def draw(self):
        self.back_button.draw(100, 600, 140, 40)
        self.record_table.draw()

    def button_hover(self, xy_):
        self.back_button.hover_event(xy_)

    def button_click(self, xy_):
        if self.back_button.get_rect().collidepoint(xy_):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return 'BACK_B'

