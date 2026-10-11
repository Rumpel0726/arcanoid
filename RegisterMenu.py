from init_glob_vars import *
from InputFrame import InputFrame


class RegisterMenu:
    def __init__(self):
        self.name_frame = InputFrame()
        self.name_font = pygame.font.SysFont("areal", 50)
        self.name = ''
        self.name_text = self.name_font.render(self.name, True, st.WHITE)
        self.vvdite_imya = self.name_font.render('Введите имя: ', True, st.WHITE)


    def draw(self):
        #pygame.draw.rect(screen, st.WHITE, pygame.Rect(540, 300, 250, 40)) # Белая рамка
        #pygame.draw.rect(screen, st.BLACK, pygame.Rect(542, 302, 246, 36)) # Белая рамка
        #self.name_text = self.name_font.render(self.name, True, st.WHITE)
        #screen.blit(self.name_text, (542, 302))
        self.name_frame.draw(self.name, 542, 302)
        screen.blit(self.vvdite_imya, (542, 252))

    def add_letter(self, letter):
        self.name += letter

    def del_letter(self):
        if self.name != '':
            self.name = self.name[:-1]
