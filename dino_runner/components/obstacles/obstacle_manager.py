import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import *


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        self.image_obstacles = [Cactus(), Bird(),]
        if len(self.obstacles) == 0:
           
                self.obstacles.append(self.image_obstacles[random.randint(0,1)])# aleatorio aparecer a imagem
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up or game.player.type == JUMP_TYPE:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1 
                    DEATH_SOUND.play()
                    break
                else:   
                      if game.player.type == HAMMER_TYPE:
                          self.obstacles.remove(obstacle)
                                         
                      if game.player.type == SHIELD_TYPE:
                         continue
                                                                                         
    def reset_obstacles(self):
        self.obstacles = []  

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
               
      