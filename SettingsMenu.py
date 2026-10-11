from init_glob_vars import *
from MenuButton import MenuButton
import settings as st
import time


class SettingsMenu:
    def __init__(self):
        self.font = pygame.font.SysFont("areal", 60)
        self.up_dawn_font = pygame.font.SysFont("areal", 60, bold=True)
        self.paddle_size_text = self.font.render('Размер рокетки: ', True, st.WHITE)
        self.paddle_sens_text = self.font.render('Скорость рокетки: ', True, st.WHITE)
        self.ball_size_text = self.font.render('Размер мячика: ', True, st.WHITE)
        self.ball_speed_text = self.font.render('Скорость мячика: ', True, st.WHITE)
        self.banus_speed_text = self.font.render('Скорость бонуса: ', True, st.WHITE)
        self.save_text = self.font.render('Изменения применины', True, st.YELLOW)
        self.paddle_size = self.font.render(str(st.RACKET_W), True, st.YELLOW)
        self.paddle_sens = self.font.render(str(st.RACKET_SPEED), True, st.YELLOW)
        self.ball_size = self.font.render(str(st.BALL_RADIUS), True, st.YELLOW)
        self.ball_speed = self.font.render(str(st.BALL_SPEED), True, st.YELLOW)
        self.banus_speed = self.font.render(str(st.BONUS_SPEED), True, st.YELLOW)

        self.paddle_size_up_button = MenuButton('>', self.up_dawn_font)
        self.paddle_size_dawn_button = MenuButton('<', self.up_dawn_font)
        self.paddle_sens_up_button = MenuButton('>', self.up_dawn_font)
        self.paddle_sens_dawn_button = MenuButton('<', self.up_dawn_font)
        self.ball_size_up_button = MenuButton('>', self.up_dawn_font)
        self.ball_size_dawn_button = MenuButton('<', self.up_dawn_font)
        self.ball_speed_up_button = MenuButton('>', self.up_dawn_font)
        self.ball_speed_dawn_button = MenuButton('<', self.up_dawn_font)
        self.banus_speed_up_button = MenuButton('>', self.up_dawn_font)
        self.banus_speed_dawn_button = MenuButton('<', self.up_dawn_font)

        self.back_button = MenuButton('Назад', self.font)
        self.save_button = MenuButton('Сохранить', self.font)
        self.is_save = 0

    def draw(self):
        screen.blit(self.paddle_size_text, (100, 100))
        screen.blit(self.paddle_sens_text, (100, 200))
        screen.blit(self.ball_size_text, (100, 300))
        screen.blit(self.ball_speed_text, (100, 400))
        screen.blit(self.banus_speed_text, (100, 500))
        self.paddle_size = self.font.render(str(st.RACKET_W), True, st.YELLOW)
        self.paddle_sens = self.font.render(str(st.RACKET_SPEED), True, st.YELLOW)
        self.ball_size = self.font.render(str(st.BALL_RADIUS), True, st.YELLOW)
        self.ball_speed = self.font.render(str(st.BALL_SPEED), True, st.YELLOW)
        self.banus_speed = self.font.render(str(st.BONUS_SPEED), True, st.YELLOW)
        screen.blit(self.paddle_size, (550, 100))
        screen.blit(self.paddle_sens, (550, 200))
        screen.blit(self.ball_size, (550, 300))
        screen.blit(self.ball_speed, (550, 400))
        screen.blit(self.banus_speed, (550, 500))

        self.paddle_size_up_button.draw(700, 100, 20, 40)
        self.paddle_size_dawn_button.draw(650, 100, 20, 40)
        self.paddle_sens_up_button.draw(700, 200, 20, 40)
        self.paddle_sens_dawn_button.draw(650, 200, 20, 40)
        self.ball_size_up_button.draw(700, 300, 20, 40)
        self.ball_size_dawn_button.draw(650, 300, 20, 40)
        self.ball_speed_up_button.draw(700, 400, 20, 40)
        self.ball_speed_dawn_button.draw(650, 400, 20, 40)
        self.banus_speed_up_button.draw(700, 500, 20, 40)
        self.banus_speed_dawn_button.draw(650, 500, 20, 40)
        #screen.blit(self.save_text, (700, 600))
        self.back_button.draw(100, 600, 140, 40)
        self.save_button.draw(450, 600, 140, 40)

        if self.is_save > 0:
            screen.blit(self.save_text, (700, 600))
            self.is_save -= 1
            #time.sleep(2)
            #self.is_save = 0


    def button_hover(self, xy_):
        self.back_button.hover_event(xy_)
        self.paddle_size_up_button.hover_event(xy_)
        self.paddle_size_dawn_button.hover_event(xy_)
        self.paddle_sens_up_button.hover_event(xy_)
        self.paddle_sens_dawn_button.hover_event(xy_)
        self.ball_size_up_button.hover_event(xy_)
        self.ball_size_dawn_button.hover_event(xy_)
        self.ball_speed_up_button.hover_event(xy_)
        self.ball_speed_dawn_button.hover_event(xy_)
        self.banus_speed_up_button.hover_event(xy_)
        self.banus_speed_dawn_button.hover_event(xy_)
        self.save_button.hover_event(xy_)

    def button_click(self, xy_):
        if self.back_button.get_rect().collidepoint(xy_):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return 'BACK_B'
        elif self.save_button.get_rect().collidepoint(xy_):
            self.is_save = 120
            return 'SAVE_B'
        elif self.paddle_size_up_button.get_rect().collidepoint(xy_):
            st.RACKET_W += 1
            return 'UP_DAWN'
        elif self.paddle_size_dawn_button.get_rect().collidepoint(xy_):
            if (st.RACKET_W - 1) > 0:
                st.RACKET_W -= 1
            return 'UP_DAWN'
        elif self.paddle_sens_up_button.get_rect().collidepoint(xy_):
            st.RACKET_SPEED += 1
            return 'UP_DAWN'
        elif self.paddle_sens_dawn_button.get_rect().collidepoint(xy_):
            if (st.RACKET_SPEED - 1) > 0:
                st.RACKET_SPEED -= 1
            return 'UP_DAWN'
        elif self.ball_size_up_button.get_rect().collidepoint(xy_):
            st.BALL_RADIUS += 1
            return 'UP_DAWN'
        elif self.ball_size_dawn_button.get_rect().collidepoint(xy_):
            if (st.BALL_RADIUS - 1) > 0:
                st.BALL_RADIUS -= 1
            return 'UP_DAWN'
        elif self.ball_speed_up_button.get_rect().collidepoint(xy_):
            st.BALL_SPEED += 1
            return 'UP_DAWN'
        elif self.ball_speed_dawn_button.get_rect().collidepoint(xy_):
            if (st.BALL_SPEED - 1) > 0:
                st.BALL_SPEED -= 1
            return 'UP_DAWN'
        elif self.banus_speed_up_button.get_rect().collidepoint(xy_):
            st.BONUS_SPEED += 1
            return 'UP_DAWN'
        elif self.banus_speed_dawn_button.get_rect().collidepoint(xy_):
            if (st.BONUS_SPEED - 1) > 0:
                st.BONUS_SPEED -= 1
            return 'UP_DAWN'


