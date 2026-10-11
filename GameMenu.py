from init_glob_vars import *


class GameMenu:
    def __init__(self, level_num_, score_):
        self.score = score_
        self.font = pygame.font.SysFont("areal", 35)
        self.username = 'none'
        self.hscore = 0
        self.name_text = self.font.render('Имя: ', True, st.WHITE)
        self.level_text = self.font.render('Уровень: ', True, st.WHITE)
        self.score_text = self.font.render('Очки: ', True, st.WHITE)
        self.high_score_text = self.font.render('Рекорд очков: ', True, st.WHITE)
        self.name = self.font.render(self.username, True, st.WHITE)
        self.level_num_text = self.font.render(str(level_num_), True, st.WHITE)
        self.score_num_text = self.font.render(str(score_), True, st.WHITE)
        self.high_score_num_text = self.font.render(str(self.hscore), True, st.WHITE)

    def draw(self, level_num_, score_): # Вывод статистики игрока
        self.score = score_
        self.name = self.font.render(self.username, True, st.WHITE)
        self.level_num_text = self.font.render(str(level_num_), True, st.WHITE)
        self.score_num_text = self.font.render(str(score_), True, st.WHITE)
        self.high_score_num_text = self.font.render(str(self.hscore), True, st.WHITE)
        screen.blit(self.name_text, (1100, 10))
        screen.blit(self.name, (1100, 55))
        screen.blit(self.level_text, (1100, 100))
        screen.blit(self.level_num_text, (1100, 145))
        screen.blit(self.score_text, (1100, 190))
        screen.blit(self.score_num_text, (1100, 235))
        screen.blit(self.high_score_text, (1100, 280))
        screen.blit(self.high_score_num_text, (1100, 325))

    def set_score(self, sc):
        self.score = self.score + sc
        #print(self.score)

    def get_score(self):
        return self.score

    def set_name(self, nm):
        self.username = nm
