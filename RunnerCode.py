import pygame
import math
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/Player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/Player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("UltimatePygameIntro-main/graphics/Player/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("UltimatePygameIntro-main/audio/jump.mp3")
        self.jump_sound.set_volume(0.1)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('UltimatePygameIntro-main\graphics/fly\Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('UltimatePygameIntro-main\graphics/fly\Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load("UltimatePygameIntro-main/graphics/Snail/Snail1.png").convert_alpha()
            snail_2 = pygame.image.load("UltimatePygameIntro-main/graphics/Snail/Snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))

    def animation_state(self):
       self.animation_index += 0.1
       if self.animation_index >= len(self.frames): self.animation_index = 0
       self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()





def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score = math.floor(current_time/1000)
    score_surf = test_font.render((f"Score: {score}"), False, (64,64,64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surf, obstacle_rect)
            else: screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for  obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect): return False
    return True

def collisions_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]





pygame.init()
screen = pygame.display.set_mode((800, 400))
game_active = True
start_time = 0
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("UltimatePygameIntro-main/font/Pixeltype.ttf", 50)

sky_surf = pygame.image.load('UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surf = pygame.image.load('UltimatePygameIntro-main/graphics/ground.png').convert()
music = pygame.mixer.Sound("UltimatePygameIntro-main/audio/music.wav")
music.set_volume(0.2)
music.play(loops=-1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

#Snail
snail_frame_1 = pygame.image.load("UltimatePygameIntro-main/graphics/Snail/Snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("UltimatePygameIntro-main/graphics/Snail/Snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surf = snail_frames[snail_index]

#Fly
fly_frame_1 = pygame.image.load('UltimatePygameIntro-main\graphics/fly\Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('UltimatePygameIntro-main\graphics/fly\Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0
fly_surf = fly_frames[fly_index]


obstacle_rect_list = []


player_walk_1 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/Player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/Player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("UltimatePygameIntro-main/graphics/Player/jump.png").convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_grav = 0

# Intro Screen
player_stand = pygame.image.load("UltimatePygameIntro-main/graphics/Player/Player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center=(400,200))
title_surf = test_font.render("Runner", False, "#ffffff")
title_rect = title_surf.get_rect(center=(400,50))
inst_surf = test_font.render("Press Space to Start", False, '#ffffff')
inst_rect = inst_surf.get_rect(center=(400, 350))
score = 0

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_grav = -20

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))
            if event.type == snail_animation_timer:
                if snail_index == 0: snail_index = 1
                else: snail_index = 0
                snail_surf = snail_frames[snail_index]

            if event.type == fly_animation_timer:
                if fly_index == 0: fly_index = 1
                else: fly_index = 0
                fly_surf = fly_frames[fly_index]

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        score = display_score()

        # Player
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collisions_sprite()

    else:
        screen.fill((94, 129, 162))
        screen.blit(title_surf, title_rect)
        player_stand_rect = player_stand.get_rect(center=(400,200))
        screen.blit(player_stand, player_stand_rect)
        start_time = pygame.time.get_ticks()
        score_msg = test_font.render(f"Score = {math.floor(score/1000)}", False, "#ffffff")
        score_rect = score_msg.get_rect(center=(400,350))
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_grav = 0
        if not score == 0: screen.blit(score_msg, score_rect)
        else: screen.blit(inst_surf, inst_rect)


    pygame.display.update()
    clock.tick(60)
