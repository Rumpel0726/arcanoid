from init_glob_vars import *
from Racket import Racket, move_racket
from Bonus import is_bonus_caught, apply_bonus
from Ball import Ball
from Brick import Brick
from Level import Level, is_level_win, load_levels, make_level_bricks
from MainMenu import MainMenu
from GameMenu import GameMenu
from RegisterMenu import RegisterMenu
from DB import DB
from PauseMenu import PauseMenu
from Records_Menu import Records_Menu
from SettingsMenu import SettingsMenu
from LoseMenu import LoseMenu
from WinMenu import WinMenu

pygame.init()


# Главный Класс - игра
class Game:
    pos_x = 500
    pos_y = 650

    def __init__(self, levels_):
        self.levels = levels_
        self.racket = Racket()
        self.ball = Ball()
        self.level = Level()
        self.main_menu = MainMenu()
        self.register_menu = RegisterMenu()
        self.pause_menu = PauseMenu()
        self.records_menu = Records_Menu()
        self.settings_menu = SettingsMenu()
        self.win_menu = WinMenu()

        self.racket_eng = 10
        self.score = 0
        self.level_num = 0
        self.user_name = ''
        self.db = DB()
        self.level_bricks = make_level_bricks(self.levels[self.level_num])
        self.brick = Brick()
        self.game_menu = GameMenu(self.level_num + 1, self.score)
        self.lose_menu = LoseMenu()
        self.bonus_list = []
        self.settings_status = ''
        self.pause_status = ''
        self.menu_status = ''
        self.lost_status = ''
        self.win_status = ''
        self.f_run = 'REG'
        # 2 REG
        # 1 M_MENU
        # 0 LOST
        # 1 GAME

        self.mouse_click_pos = (0, 0)
        self.start_hscore = 0

    def set_game(self):
        self.racket = Racket()
        self.ball = Ball()
        self.level = Level()
        self.level_bricks = make_level_bricks(self.levels[self.level_num])
        self.brick = Brick()
        self.game_menu = GameMenu(self.level_num + 1, self.score)
        self.game_menu.hscore = self.start_hscore
        self.bonus_list = []
        self.pos_x = 500
        self.user_name = self.register_menu.name
        self.game_menu.set_name(self.user_name)
        self.start_hscore = self.db.get_hscore(self.user_name)
        self.game_menu.hscore = self.start_hscore
        self.racket_eng = 10

    def start(self, rocket_width_):
        # Run until the user asks to quit
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.f_run == 'EXIT':
                    self.db.close_db()
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.f_run == 'PAUSE':
                            self.f_run = 'GAME'
                        elif self.f_run == 'GAME':
                            self.f_run = 'PAUSE'
                        # начнем игру заново
                        if self.f_run == 'LOST':
                            self.set_game()
                            rocket_width_ = st.RACKET_W
                    elif self.f_run == 'REG':
                        if event.key == 8: # Удаление символов в поле ввода имени
                            self.register_menu.del_letter()
                        elif event.key == 13: # Ввод имени
                            #print(self.user_name)
                            if self.register_menu.name != '':
                                self.user_name = self.register_menu.name
                                self.db.add_data(self.user_name)
                                self.game_menu.set_name(self.user_name)
                                self.start_hscore = self.db.get_hscore(self.user_name)
                                self.game_menu.hscore = self.start_hscore
                                self.f_run = 'M_MENU'
                        elif len(self.register_menu.name) < 11: # Лимит длины имени
                            self.register_menu.add_letter(event.unicode)
                elif event.type == pygame.MOUSEBUTTONUP: # Сохраняем позицию миши в момент клика
                    self.mouse_click_pos = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            # Fill the background with white
            screen.fill(st.BLACK)

            if self.f_run == 'PAUSE':
                self.pause_menu.draw()
                self.pause_status = self.pause_menu.button_click(self.mouse_click_pos)
                self.pause_menu.button_hover(pygame.mouse.get_pos())
                if self.pause_status == 'BACK_B':
                    self.f_run = 'M_MENU'
                    self.mouse_click_pos = (0, 0)
                    self.set_game()
                    rocket_width_ = st.RACKET_W
                elif self.pause_status == 'CONT_B':
                    self.f_run = 'GAME'
                    self.mouse_click_pos = (0, 0)

            if self.f_run == 'REC':
                self.records_menu.draw()
                self.records_menu.button_hover(pygame.mouse.get_pos())
                if self.records_menu.button_click(self.mouse_click_pos) == 'BACK_B':
                    self.f_run = 'M_MENU'
                    self.mouse_click_pos = (0, 0)

            if self.f_run == 'SET':
                self.settings_menu.draw()
                self.settings_menu.button_hover(pygame.mouse.get_pos())
                self.settings_status = self.settings_menu.button_click(self.mouse_click_pos)
                if self.settings_status == 'BACK_B':
                    self.f_run = 'M_MENU'
                    self.mouse_click_pos = (0, 0)
                elif self.settings_status == 'UP_DAWN':
                    self.mouse_click_pos = (0, 0)
                elif self.settings_status == 'SAVE_B':
                    self.mouse_click_pos = (0, 0)
                    self.set_game()
                    rocket_width_ = st.RACKET_W

            if self.f_run == 'REG':
                self.register_menu.draw()

            if self.f_run == 'M_MENU': # Режим - главное меню
                self.main_menu.draw()
                self.main_menu.button_hover(pygame.mouse.get_pos())
                self.menu_status = self.main_menu.button_click(self.mouse_click_pos)
                self.level_num = 0
                self.score = 0
                self.level_bricks = make_level_bricks(self.levels[self.level_num])
                self.game_menu.score = 0
                if self.menu_status == 'PLAY_B':
                    self.f_run = 'GAME'
                    self.mouse_click_pos = (0, 0)
                if self.menu_status == 'REC_B':
                    self.f_run = 'REC'
                    self.mouse_click_pos = (0, 0)
                if self.menu_status == 'REG_B':
                    self.f_run = 'REG'
                    self.mouse_click_pos = (0, 0)
                if self.menu_status == 'SET_B':
                    self.f_run = 'SET'
                    self.mouse_click_pos = (0, 0)
                if self.menu_status == 'EXIT_B':
                    self.f_run = 'EXIT'
                    self.mouse_click_pos = (0, 0)

            if self.f_run == 'LOST': # Режим - экран пригрыша
                self.lose_menu.draw()
                self.lose_menu.button_hover(pygame.mouse.get_pos())
                self.lost_status = self.lose_menu.button_click(self.mouse_click_pos)
                self.level_num = 0
                self.score = 0
                if self.lost_status == 'BACK_B':
                    self.f_run = 'M_MENU'
                    self.mouse_click_pos = (0, 0)
                    self.set_game()
                    rocket_width_ = st.RACKET_W
                elif self.lost_status == 'CONT_B':
                    self.f_run = 'GAME'
                    self.mouse_click_pos = (0, 0)
                    self.set_game()
                    rocket_width_ = st.RACKET_W

            if self.f_run == 'WIN': # Режим - экран победы
                self.win_menu.draw()
                self.win_menu.button_hover(pygame.mouse.get_pos())
                self.win_status = self.win_menu.button_click(self.mouse_click_pos)
                if self.win_status == 'WBACK_B':
                    self.f_run = 'M_MENU'
                    self.mouse_click_pos = (0, 0)
                    self.level_num += 1
                    self.set_game()
                    rocket_width_ = st.RACKET_W
                elif self.win_status == 'WCONT_B':
                    self.f_run = 'GAME'
                    self.mouse_click_pos = (0, 0)
                    self.level_num += 1
                    self.set_game()
                    rocket_width_ = st.RACKET_W

            if self.f_run == 'GAME': # Режим - игра запущена
                pygame.draw.line(screen, st.GREY, (1080, 0), (1080, 720), 4)
                self.score = self.game_menu.get_score()
                self.game_menu.draw(self.level_num + 1, self.score)

                # Передвижение рокетки
                self.pos_x = move_racket(self.pos_x, keys[pygame.K_LEFT], keys[pygame.K_RIGHT], st.RACKET_SPEED, rocket_width_, st.DEFINITION[0])


                # Draw a solid blue circle in the center
                #pygame.draw.rect(screen, st.GREEN, pygame.Rect(pos_x, pos_y, 135, 22))
                self.racket.draw(self.pos_x, self.pos_y, rocket_width_)
                # Нарисуем шарик
                ball_status, score, self.bonus_list = self.ball.draw(self.racket, self.bonus_list, self.level_bricks, self.racket_eng)
                self.game_menu.set_score(score)
                if ball_status == 0:
                    self.f_run = 'LOST'
                if is_level_win(self.level_bricks):
                    self.f_run = 'WIN'
                    self.score = self.game_menu.get_score()
                self.level.draw(self.level_bricks)
                for i in range(len(self.bonus_list)): # проверка косания с бонусом
                    self.bonus_list[i].draw()
                    self.bonus_list[i].move()
                    if is_bonus_caught(self.racket.get_rect(), self.bonus_list[i]):
                        self.bonus_list[i].visible = 0
                        rocket_width_, self.racket_eng, self.ball.no_colis = apply_bonus(self.bonus_list[i].bonus_type, rocket_width_, self.racket_eng, self.ball.no_colis)
                if self.score > self.game_menu.hscore:
                    self.game_menu.hscore = self.score
                    self.db.set_hscore(self.user_name, self.game_menu.hscore)

            clock.tick(st.FPS)

            # Flip the display
            pygame.display.flip()


def start_game():
    levels = load_levels('data/levels.txt')
    game = Game(levels)
    game.start(gl_rocket_width)
    pygame.quit()


# Start game
start_game()
