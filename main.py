import sys

import pygame
from asteroid import Asteroid
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from asteroidfield import AsteroidField
from shot import Shot




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide_with(player):
                log_event("player_hit")
                print ("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                #print (f"Checking collision between asteroid at {asteroid.position} with radius {asteroid.radius} and shot at {shot.position} with radius {shot.radius}")
                if asteroid.collide_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill() 

                   
            
 
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        # print(f"Delta time: {dt}")



if __name__ == "__main__":
    main()

 

