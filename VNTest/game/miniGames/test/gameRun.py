import pygame
import os

file_path = 'C:\RenPy\VNTest\game\miniGames\test'
game_folder = os.path.dirname(file_path)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))