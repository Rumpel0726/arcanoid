import pygame
import ast
import settings as st
import random as rn

# Set up the drawing window
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
bonus_plus = pygame.image.load('data/bonus_plus.png')
bonus_minus = pygame.image.load('data/bonus_minus.png')
bonus_circle = pygame.image.load('data/bonus_circle.png')
gl_rocket_width = st.RACKET_W
