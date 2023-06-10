# PYTRIS™ Copyright (c) 2017 Jason Kim All Rights Reserved.

import pygame
import operator
from random import *
from pygame.locals import *
import numpy as np

RIGHT = 0
LEFT = 1
ROTATE_RIGHT = 2
ROTATE_LEFT = 3
TELEPORT = 4
HOLD = 5
SPEED_DOWN = 6

class tetrimino:
########################################### I
    mino_map = [
        [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0]
            ],
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0]
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]
            ]
        ],
    ########################################### J
        [
            [
                [2, 0, 0, 0],
                [2, 2, 2, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 2, 2, 0],
                [0, 2, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [2, 2, 2, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 2, 0, 0],
                [0, 2, 0, 0],
                [2, 2, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
    ########################################### L
        [
            [
                [0, 0, 3, 0],
                [3, 3, 3, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 3, 0, 0],
                [0, 3, 0, 0],
                [0, 3, 3, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [3, 3, 3, 0],
                [3, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [3, 3, 0, 0],
                [0, 3, 0, 0],
                [0, 3, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
    ########################################### O
        [
            [
                [0, 4, 4, 0],
                [0, 4, 4, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 4, 4, 0],
                [0, 4, 4, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 4, 4, 0],
                [0, 4, 4, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 4, 4, 0],
                [0, 4, 4, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
    ########################################### S
        [
            [
                [0, 5, 5, 0],
                [5, 5, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 5, 0, 0],
                [0, 5, 5, 0],
                [0, 0, 5, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [0, 5, 5, 0],
                [5, 5, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [5, 0, 0, 0],
                [5, 5, 0, 0],
                [0, 5, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
    ########################################### T
        [
            [
                [0, 6, 0, 0],
                [6, 6, 6, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 6, 0, 0],
                [0, 6, 6, 0],
                [0, 6, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [6, 6, 6, 0],
                [0, 6, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 6, 0, 0],
                [6, 6, 0, 0],
                [0, 6, 0, 0],
                [0, 0, 0, 0]
            ]
        ],
    ########################################### Z
        [
            [
                [7, 7, 0, 0],
                [0, 7, 7, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 7, 0],
                [0, 7, 7, 0],
                [0, 7, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0],
                [7, 7, 0, 0],
                [0, 7, 7, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 7, 0, 0],
                [7, 7, 0, 0],
                [7, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        ]
    ]

class variables_ui:
    def __init__(self):
        # Fonts
        font_path = "./envs/assets/fonts/OpenSans-Light.ttf"
        font_path_b = "./envs/assets/fonts/OpenSans-Bold.ttf"
        font_path_i = "./envs/assets/fonts/Inconsolata/Inconsolata.otf"

        self.h1 = pygame.font.Font(font_path, 50)
        self.h2 = pygame.font.Font(font_path, 30)
        self.h4 = pygame.font.Font(font_path, 20)
        self.h5 = pygame.font.Font(font_path, 13)
        self.h6 = pygame.font.Font(font_path, 10)

        self.h1_b = pygame.font.Font(font_path_b, 50)
        self.h2_b = pygame.font.Font(font_path_b, 30)

        self.h2_i = pygame.font.Font(font_path_i, 30)
        self.h5_i = pygame.font.Font(font_path_i, 13)

        # Sounds
        self.click_sound = pygame.mixer.Sound("./envs/assets/sounds/SFX_ButtonUp.wav")
        self.move_sound = pygame.mixer.Sound("./envs/assets/sounds/SFX_PieceMoveLR.wav")
        self.drop_sound = pygame.mixer.Sound("./envs/assets/sounds/SFX_PieceHardDrop.wav")
        self.single_sound = pygame.mixer.Sound("./envs/assets/sounds/SFX_SpecialLineClearSingle.wav")
        self.double_sound = pygame.mixer.Sound("./envs/assets/sounds/SFX_SpecialLineClearDouble.wav")
        self.triple_sound = pygame.mixer.Sound("./envs/assets/sounds/SFX_SpecialLineClearTriple.wav")
        self.tetris_sound = pygame.mixer.Sound("./envs/assets/sounds/SFX_SpecialTetris.wav")


        # Background colors
        self.black = (10, 10, 10) #rgb(10, 10, 10)
        self.white = (255, 255, 255) #rgb(255, 255, 255)
        self.grey_1 = (26, 26, 26) #rgb(26, 26, 26)
        self.grey_2 = (35, 35, 35) #rgb(35, 35, 35)
        self.grey_3 = (55, 55, 55) #rgb(55, 55, 55)

        # Tetrimino colors
        self.cyan = (69, 206, 204) #rgb(69, 206, 204) # I
        self.blue = (64, 111, 249) #rgb(64, 111, 249) # J
        self.orange = (253, 189, 53) #rgb(253, 189, 53) # L
        self.yellow = (246, 227, 90) #rgb(246, 227, 90) # O
        self.green = (98, 190, 68) #rgb(98, 190, 68) # S
        self.pink = (242, 64, 235) #rgb(242, 64, 235) # T
        self.red = (225, 13, 27) #rgb(225, 13, 27) # Z


        self.t_color = [self.grey_2, self.cyan, self.blue, self.orange, self.yellow, self.green, self.pink, self.red, self.grey_3]

class Tetris():

    def __init__(self):
        # Define
        self.block_size = 17 # Height, width of single block
        self.width = 10 # Board width
        self.height = 20 # Board height
        self.framerate = 30 # Bigger -> Slower

        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((300, 374))
        pygame.time.set_timer(pygame.USEREVENT, self.framerate * 10)
        pygame.display.set_caption("PYTRIS™")

        self.ui_variables = variables_ui()

         # Initial values
        self.blink = False
        self.start = True
        self.pause = False
        self.done = False
        self.game_over = False

        self.score = 0
        self.level = 1
        self.goal = self.level * 5
        self.bottom_count = 0
        self.hardrop = False

        self.dx, self.dy = 3, 0 # Minos location status
        self.rotation = 0 # Minos self.rotation status

        self.mino = randint(1, 7) # Current mino
        self.next_mino = randint(1, 7) # Next mino

        self.hold = False # Hold status
        self.hold_mino = -1 # Holded mino

        self.name_location = 0
        self.name = [65, 65, 65]

        with open('./envs/leaderboard.txt') as f:
            lines = f.readlines()
        lines = [line.rstrip('\n') for line in open('./envs/leaderboard.txt')]

        self.leaders = {'AAA': 0, 'BBB': 0, 'CCC': 0}
        for i in lines:
            self.leaders[i.split(' ')[0]] = int(i.split(' ')[1])
        self.leaders = sorted(self.leaders.items(), key=operator.itemgetter(1), reverse=True)

        self.matrix = [[0 for y in range(self.height + 1)] for x in range(self.width)] # Board self.matrix

        ###########################################################
        # Loop Start
        ###########################################################

    def run(self):
        while not self.done:
            self.view()

        pygame.quit()
   
    # Draw block
    def draw_block(self, x, y, color):
        pygame.draw.rect(
            self.screen,
            color,
            Rect(x, y, self.block_size, self.block_size)
        )
        pygame.draw.rect(
            self.screen,
            self.ui_variables.grey_1,
            Rect(x, y, self.block_size, self.block_size),
            1
        )

    # Draw game screen
    def draw_board(self, next, hold, score, level, goal):
        self.screen.fill(self.ui_variables.grey_1)

        # Draw sidebar
        pygame.draw.rect(
            self.screen,
            self.ui_variables.white,
            Rect(204, 0, 96, 374)
        )

        # Draw next mino
        grid_n = tetrimino.mino_map[next - 1][0]

        for i in range(4):
            for j in range(4):
                dx = 220 + self.block_size * j
                dy = 140 + self.block_size * i
                if grid_n[i][j] != 0:
                    pygame.draw.rect(
                        self.screen,
                        self.ui_variables.t_color[grid_n[i][j]],
                        Rect(dx, dy, self.block_size, self.block_size)
                    )

        # Draw hold mino
        grid_h = tetrimino.mino_map[self.hold - 1][0]

        if self.hold_mino != -1:
            for i in range(4):
                for j in range(4):
                    dx = 220 + self.block_size * j
                    dy = 50 + self.block_size * i
                    if grid_h[i][j] != 0:
                        pygame.draw.rect(
                            self.screen,
                            self.ui_variables.t_color[grid_h[i][j]],
                            Rect(dx, dy, self.block_size, self.block_size)
                        )

        # Set max score
        if self.score > 999999:
            self.score = 999999

        # Draw texts
        text_hold = self.ui_variables.h5.render("HOLD", 1, self.ui_variables.black)
        text_next = self.ui_variables.h5.render("NEXT", 1, self.ui_variables.black)
        text_score = self.ui_variables.h5.render("SCORE", 1, self.ui_variables.black)
        score_value = self.ui_variables.h4.render(str(self.score), 1, self.ui_variables.black)
        text_level = self.ui_variables.h5.render("LEVEL", 1, self.ui_variables.black)
        self.level_value = self.ui_variables.h4.render(str(self.level), 1, self.ui_variables.black)
        text_goal = self.ui_variables.h5.render("GOAL", 1, self.ui_variables.black)
        self.goal_value = self.ui_variables.h4.render(str(self.goal), 1, self.ui_variables.black)

        # Place texts
        self.screen.blit(text_hold, (215, 14))
        self.screen.blit(text_next, (215, 104))
        self.screen.blit(text_score, (215, 194))
        self.screen.blit(score_value, (220, 210))
        self.screen.blit(text_level, (215, 254))
        self.screen.blit(self.level_value, (220, 270))
        self.screen.blit(text_goal, (215, 314))
        self.screen.blit(self.goal_value, (220, 330))

        # Draw board
        for x in range(self.width):
            for y in range(self.height):
                dx = 17 + self.block_size * x
                dy = 17 + self.block_size * y
                self.draw_block(dx, dy, self.ui_variables.t_color[self.matrix[x][y + 1]])

    # Draw a tetrimino
    def draw_mino(self, x, y, mino, r):
        grid = tetrimino.mino_map[mino - 1][r]

        tx, ty = x, y
        while not self.is_bottom(tx, ty, mino, r):
            ty += 1

        # Draw ghost
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    self.matrix[tx + j][ty + i] = 8

        # Draw mino
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    self.matrix[x + j][y + i] = grid[i][j]

    # Erase a tetrimino
    def erase_mino(self, x, y, mino, r):
        grid = tetrimino.mino_map[mino - 1][r]

        # Erase ghost
        for j in range(21):
            for i in range(10):
                if self.matrix[i][j] == 8:
                    self.matrix[i][j] = 0

        # Erase mino
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    self.matrix[x + j][y + i] = 0

    # Returns true if mino is at bottom
    def is_bottom(self, x, y, mino, r):
        grid = tetrimino.mino_map[mino - 1][r]

        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    if (y + i + 1) > 20:
                        return True
                    elif self.matrix[x + j][y + i + 1] != 0 and self.matrix[x + j][y + i + 1] != 8:
                        return True

        return False

    # Returns true if mino is at the left edge
    def is_leftedge(self, x, y, mino, r):
        grid = tetrimino.mino_map[mino - 1][r]

        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    if (x + j - 1) < 0:
                        return True
                    elif self.matrix[x + j - 1][y + i] != 0:
                        return True

        return False

    # Returns true if mino is at the right edge
    def is_rightedge(self, x, y, mino, r):
        grid = tetrimino.mino_map[mino - 1][r]

        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    if (x + j + 1) > 9:
                        return True
                    elif self.matrix[x + j + 1][y + i] != 0:
                        return True

        return False

    # Returns true if turning right is possible
    def is_turnable_r(self, x, y, mino, r):
        if r != 3:
            grid = tetrimino.mino_map[mino - 1][r + 1]
        else:
            grid = tetrimino.mino_map[mino - 1][0]

        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    if (x + j) < 0 or (x + j) > 9 or (y + i) < 0 or (y + i) > 20:
                        return False
                    elif self.matrix[x + j][y + i] != 0:
                        return False

        return True

    # Returns true if turning left is possible
    def is_turnable_l(self, x, y, mino, r):
        if r != 0:
            grid = tetrimino.mino_map[mino - 1][r - 1]
        else:
            grid = tetrimino.mino_map[mino - 1][3]

        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    if (x + j) < 0 or (x + j) > 9 or (y + i) < 0 or (y + i) > 20:
                        return False
                    elif self.matrix[x + j][y + i] != 0:
                        return False

        return True

    # Returns true if new block is drawable
    def is_stackable(self, mino):
        grid = tetrimino.mino_map[mino - 1][0]

        for i in range(4):
            for j in range(4):
                #print(grid[i][j], self.matrix[3 + j][i])
                if grid[i][j] != 0 and self.matrix[3 + j][i] != 0:
                    return False

        return True

    def teleport(self):
        self.ui_variables.drop_sound.play()
        while not self.is_bottom(self.dx, self.dy, self.mino, self.rotation):
            self.dy += 1
        self.hardrop = True
        pygame.time.set_timer(pygame.USEREVENT, 1)
        self.draw_mino(self.dx, self.dy, self.mino, self.rotation)
        self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)

    def hold_press(self):
            if self.hold == False:
                self.ui_variables.move_sound.play()
                if self.hold_mino == -1:
                    self.hold_mino =self.mino
                    self.mino = self.next_mino
                    self.next_mino = randint(1, 7)
                else:
                    self.hold_mino,self.mino =self.mino, self.hold_mino
                self.dx, self.dy = 3, 0
                self.rotation = 0
                self.hold = True
            self.draw_mino(self.dx, self.dy,self.mino, self.rotation)
            self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)

    def turn_right(self):
        if self.is_turnable_r(self.dx, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.rotation += 1
        # Kick
        elif self.is_turnable_r(self.dx, self.dy - 1,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dy -= 1
            self.rotation += 1
        elif self.is_turnable_r(self.dx + 1, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx += 1
            self.rotation += 1
        elif self.is_turnable_r(self.dx - 1, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx -= 1
            self.rotation += 1
        elif self.is_turnable_r(self.dx, self.dy - 2,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dy -= 2
            self.rotation += 1
        elif self.is_turnable_r(self.dx + 2, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx += 2
            self.rotation += 1
        elif self.is_turnable_r(self.dx - 2, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx -= 2
            self.rotation += 1
        if self.rotation == 4:
            self.rotation = 0
        self.draw_mino(self.dx, self.dy,self.mino, self.rotation)
        self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)

    def turn_left(self):
        if self.is_turnable_l(self.dx, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.rotation -= 1
        # Kick
        elif self.is_turnable_l(self.dx, self.dy - 1,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dy -= 1
            self.rotation -= 1
        elif self.is_turnable_l(self.dx + 1, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx += 1
            self.rotation -= 1
        elif self.is_turnable_l(self.dx - 1, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx -= 1
            self.rotation -= 1
        elif self.is_turnable_l(self.dx, self.dy - 2,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dy -= 2
            self.rotation += 1
        elif self.is_turnable_l(self.dx + 2, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx += 2
            self.rotation += 1
        elif self.is_turnable_l(self.dx - 2, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx -= 2
        if self.rotation == -1:
            self.rotation = 3
        self.draw_mino(self.dx, self.dy, self.mino, self.rotation)
        self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)

    def move_right(self):
        if not self.is_rightedge(self.dx, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx += 1
        self.draw_mino(self.dx, self.dy,self.mino, self.rotation)
        self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)

    def move_left(self):
        if not self.is_leftedge(self.dx, self.dy,self.mino, self.rotation):
            self.ui_variables.move_sound.play()
            self.dx -= 1
            self.draw_mino(self.dx, self.dy,self.mino, self.rotation)
            self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)

    def speed_down(self):
        pygame.time.set_timer(pygame.USEREVENT, self.framerate * 1)

    def action(self, action):
        if action == RIGHT: #Droite
            self.move_right()
            
        elif action == LEFT: #Gauche
            self.move_left()
        
        elif action == ROTATE_RIGHT: #
            self.turn_right()
        
        elif action == ROTATE_LEFT:
            self.turn_left()
        
        elif action == TELEPORT:
            self.teleport()
        
        elif action == HOLD:
            self.hold_press()

        elif action == SPEED_DOWN:
            self.speed_down()

    def evaluate(self):
        return self.score

    def is_done(self):
        return self.game_over

    def observe(self):
        # matrix
        # Level
        # Next piece
        # Holding piece

        matrix = self.matrix
        # Chaque élément de la matrice est entre différent de 0 est 1
        matrix = [[1 if x > 0 else 0 for x in y] for y in matrix]
        
        # On ajoute sur la matrice la piece courante
        
        # On récupère la matrice de la pièce courante
        mino_matrix = tetrimino().mino_map[self.mino-1][self.rotation]
        # On remplace les numéros par des 2
        mino_matrix = [[2 if x > 0 else 0 for x in y] for y in mino_matrix]

        # On ajoute à la matrice générale la matrice de la pièce courante
        for i in range(len(mino_matrix)):
            for j in range(len(mino_matrix[i])):
                if mino_matrix[i][j] == 2:
                    matrix[self.dx+j][self.dy+i] = mino_matrix[i][j]

        # On "aplatit" la matrice
        matrix = [item for sublist in matrix for item in sublist]

        next_mino = self.next_mino -1
        
        hold_mino = self.hold_mino
        if hold_mino > 0:
            hold_mino = hold_mino - 1
        
        # On crée le np concaténé général
        return np.array(matrix + [self.level] + [next_mino] + [hold_mino])

    def view(self):
        # Pause screen
        if self.pause:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.done = True
                elif event.type == USEREVENT:
                    pygame.time.set_timer(pygame.USEREVENT, 300)
                    self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)

                    pause_text = self.ui_variables.h2_b.render("PAUSED", 1, self.ui_variables.white)
                    pause_start = self.ui_variables.h5.render("Press esc to continue", 1, self.ui_variables.white)

                    self.screen.blit(pause_text, (43, 100))
                    if self.blink:
                        self.screen.blit(pause_start, (40, 160))
                        self.blink = False
                    else:
                        self.blink = True
                    pygame.display.update()
                elif event.type == KEYDOWN:
                    self.erase_mino(self.dx, self.dy, self.mino, self.rotation)
                    if event.key == K_ESCAPE:
                        self.pause = False
                        self.ui_variables.click_sound.play()
                        pygame.time.set_timer(pygame.USEREVENT, 1)

        # Game screen
        elif self.start:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.done = True
                elif event.type == USEREVENT:
                    # Set speed
                    if not self.game_over:
                        keys_pressed = pygame.key.get_pressed()
                        if keys_pressed[K_DOWN]:
                            self.speed_down()
                        else:
                            pygame.time.set_timer(pygame.USEREVENT, self.framerate * 10)

                    # Draw a mino
                    self.draw_mino(self.dx, self.dy, self.mino, self.rotation)
                    self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)

                    # Erase a mino
                    if not self.game_over:
                        self.erase_mino(self.dx, self.dy, self.mino, self.rotation)

                    # Move mino down
                    if not self.is_bottom(self.dx, self.dy, self.mino, self.rotation):
                        self.dy += 1

                    # Create new mino
                    else:
                        if self.hardrop or self.bottom_count == 6:
                            self.hardrop = False
                            self.bottom_count = 0
                            self.score += 10 * self.level
                            self.draw_mino(self.dx, self.dy,self.mino, self.rotation)
                            self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)
                            if self.is_stackable(self.next_mino):
                                self.mino = self.next_mino
                                self.next_mino = randint(1, 7)
                                self.dx, self.dy = 3, 0
                                self.rotation = 0
                                self.hold = False
                            else:
                                self.start = False
                                self.game_over = True
                                pygame.time.set_timer(pygame.USEREVENT, 1)
                        else:
                            self.bottom_count += 1

                    # Erase line
                    erase_count = 0
                    for j in range(21):
                        is_full = True
                        for i in range(10):
                            if self.matrix[i][j] == 0:
                                is_full = False
                        if is_full:
                            erase_count += 1
                            k = j
                            while k > 0:
                                for i in range(10):
                                    self.matrix[i][k] = self.matrix[i][k - 1]
                                k -= 1
                    if erase_count == 1:
                        self.ui_variables.single_sound.play()
                        self.score += 50 * self.level
                    elif erase_count == 2:
                        self.ui_variables.double_sound.play()
                        self.score += 150 * self.level
                    elif erase_count == 3:
                        self.ui_variables.triple_sound.play()
                        self.score += 350 * self.level
                    elif erase_count == 4:
                        self.ui_variables.tetris_sound.play()
                        self.score += 1000 * self.level

                    # Increase self.level
                    self.goal -= erase_count
                    if self.goal < 1 and self.level < 15:
                        self.level += 1
                        self.goal += self.level * 5
                        self.framerate = int(self.framerate * 0.8)

                elif event.type == KEYDOWN:
                    self.erase_mino(self.dx, self.dy, self.mino, self.rotation)
                    if event.key == K_ESCAPE:
                        self.ui_variables.click_sound.play()
                        self.pause = True
                    # Hard drop
                    elif event.key == K_SPACE:
                        self.teleport()
                    # Hold
                    elif event.key == K_LSHIFT or event.key == K_c:
                        self.hold_press()
                        
                    # Turn right
                    elif event.key == K_UP or event.key == K_x:
                        self.turn_right()
                    # Turn left
                    elif event.key == K_z or event.key == K_LCTRL:
                        self.turn_left()
                    # Move left
                    elif event.key == K_LEFT:
                        self.move_left()
                    # Move right
                    elif event.key == K_RIGHT:
                        self.move_right()

            pygame.display.update()

        # Game over screen
        elif self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.done = True
                elif event.type == USEREVENT:
                    pygame.time.set_timer(pygame.USEREVENT, 300)
                    over_text_1 = self.ui_variables.h2_b.render("GAME", 1, self.ui_variables.white)
                    over_text_2 = self.ui_variables.h2_b.render("OVER", 1, self.ui_variables.white)
                    over_start = self.ui_variables.h5.render("Press return to continue", 1, self.ui_variables.white)

                    self.draw_board(self.next_mino, self.hold_mino, self.score, self.level, self.goal)
                    self.screen.blit(over_text_1, (58, 75))
                    self.screen.blit(over_text_2, (62, 105))

                    self.name_1 = self.ui_variables.h2_i.render(chr(self.name[0]), 1, self.ui_variables.white)
                    self.name_2 = self.ui_variables.h2_i.render(chr(self.name[1]), 1, self.ui_variables.white)
                    self.name_3 = self.ui_variables.h2_i.render(chr(self.name[2]), 1, self.ui_variables.white)

                    underbar_1 = self.ui_variables.h2.render("_", 1, self.ui_variables.white)
                    underbar_2 = self.ui_variables.h2.render("_", 1, self.ui_variables.white)
                    underbar_3 = self.ui_variables.h2.render("_", 1, self.ui_variables.white)

                    self.screen.blit(self.name_1, (65, 147))
                    self.screen.blit(self.name_2, (95, 147))
                    self.screen.blit(self.name_3, (125, 147))

                    if self.blink:
                        self.screen.blit(over_start, (32, 195))
                        self.blink = False
                    else:
                        if self.name_location == 0:
                            self.screen.blit(underbar_1, (65, 145))
                        elif self.name_location == 1:
                            self.screen.blit(underbar_2, (95, 145))
                        elif self.name_location == 2:
                            self.screen.blit(underbar_3, (125, 145))
                        self.blink = True

                    pygame.display.update()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.ui_variables.click_sound.play()

                        outfile = open('leaderboard.txt','a')
                        outfile.write(chr(self.name[0]) + chr(self.name[1]) + chr(self.name[2]) + ' ' + str(self.score) + '\n')
                        outfile.close()

                        self.game_over = False
                        self.hold = False
                        self.dx, self.dy = 3, 0
                        self.rotation = 0
                        self.mino = randint(1, 7)
                        self.next_mino = randint(1, 7)
                        self.hold_mino = -1
                        self.framerate = 30
                        self.score = 0
                        self.score = 0
                        self.level = 1
                        self.goal = self.level * 5
                        self.bottom_count = 0
                        self.hardrop = False
                        self.name_location = 0
                        self.name = [65, 65, 65]
                        self.matrix = [[0 for y in range(self.height + 1)] for x in range(self.width)]

                        with open('leaderboard.txt') as f:
                            lines = f.readlines()
                        lines = [line.rstrip('\n') for line in open('leaderboard.txt')]

                        self.leaders = {'AAA': 0, 'BBB': 0, 'CCC': 0}
                        for i in lines:
                            self.leaders[i.split(' ')[0]] = int(i.split(' ')[1])
                        self.leaders = sorted(self.leaders.items(), key=operator.itemgetter(1), reverse=True)

                        pygame.time.set_timer(pygame.USEREVENT, 1)
                    elif event.key == K_RIGHT:
                        if self.name_location != 2:
                            self.name_location += 1
                        else:
                            self.name_location = 0
                        pygame.time.set_timer(pygame.USEREVENT, 1)
                    elif event.key == K_LEFT:
                        if self.name_location != 0:
                            self.name_location -= 1
                        else:
                            self.name_location = 2
                        pygame.time.set_timer(pygame.USEREVENT, 1)
                    elif event.key == K_UP:
                        self.ui_variables.click_sound.play()
                        if self.name[self.name_location] != 90:
                            self.name[self.name_location] += 1
                        else:
                            self.name[self.name_location] = 65
                        pygame.time.set_timer(pygame.USEREVENT, 1)
                    elif event.key == K_DOWN:
                        self.ui_variables.click_sound.play()
                        if self.name[self.name_location] != 65:
                            self.name[self.name_location] -= 1
                        else:
                            self.name[self.name_location] = 90
                        pygame.time.set_timer(pygame.USEREVENT, 1)

        # Start screen
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.done = True
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.ui_variables.click_sound.play()
                        self.start = True

            # pygame.time.set_timer(pygame.USEREVENT, 300)
            self.screen.fill(self.ui_variables.white)
            pygame.draw.rect(
                self.screen,
                self.ui_variables.grey_1,
                Rect(0, 187, 300, 187)
            )

            title = self.ui_variables.h1.render("PYTRIS™", 1, self.ui_variables.grey_1)
            title_start = self.ui_variables.h5.render("Press space to start", 1, self.ui_variables.white)
            title_info = self.ui_variables.h6.render("Copyright (c) 2017 Jason Kim All Rights Reserved.", 1, self.ui_variables.white)

            leader_1 = self.ui_variables.h5_i.render('1st ' + self.leaders[0][0] + ' ' + str(self.leaders[0][1]), 1, self.ui_variables.grey_1)
            leader_2 = self.ui_variables.h5_i.render('2nd ' + self.leaders[1][0] + ' ' + str(self.leaders[1][1]), 1, self.ui_variables.grey_1)
            leader_3 = self.ui_variables.h5_i.render('3rd ' + self.leaders[2][0] + ' ' + str(self.leaders[2][1]), 1, self.ui_variables.grey_1)

            if self.blink:
                self.screen.blit(title_start, (92, 195))
                self.blink = False
            else:
                self.blink = True

            self.screen.blit(title, (65, 120))
            self.screen.blit(title_info, (40, 335))

            self.screen.blit(leader_1, (10, 10))
            self.screen.blit(leader_2, (10, 23))
            self.screen.blit(leader_3, (10, 36))

            if not self.start:
                pygame.display.update()
                self.clock.tick(3)


   

if __name__ == '__main__':
    t = Tetris()
    t.run()


