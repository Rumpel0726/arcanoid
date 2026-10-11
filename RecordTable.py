from init_glob_vars import *
from DB import DB


class RecordTable:
    def __init__(self):
        self.db = DB()
        self.rec_arr = self.db.get_data()
        self.font = pygame.font.SysFont("areal", 60)
        self.dis_width = 1200
        self.column_space = 20
        self.i = 0
        self.messg = self.font.render(f'Игроки               Очки', True, st.RED)

    def draw(self):
        self.rec_arr = self.db.get_data()
        self.i = 0
        screen.blit(self.messg, [self.dis_width / 2, (700 / 4) + 5 - 100])
        for row in self.rec_arr:
            column1 = self.font.render('{:>3}'.format(row[0]), True, st.YELLOW)
            column2 = self.font.render('{:30}'.format(row[1]), True, st.YELLOW)
            screen.blit(column1, [self.dis_width / 2,                     ((700 / 4) + self.i + 5) - 50])
            screen.blit(column2, [self.dis_width / 2 + self.column_space, ((700 / 4) + self.i + 5) - 50])

            self.i += 45

