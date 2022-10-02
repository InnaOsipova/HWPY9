#Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

import pygame
import sys

def vin (some_list, simbol):
    if some_list [0][0] == some_list[0][1] == some_list[0][2]== simbol \
        or some_list [1][0] == some_list[1][1] == some_list[1][2]== simbol \
        or some_list [2][0] == some_list[2][1] == some_list[2][2]== simbol :
                v = True
                
            
    elif some_list [0][0] == some_list[1][0] == some_list[2][0]== simbol \
        or some_list [0][1] == some_list[1][1] == some_list[2][1]== simbol \
        or some_list [0][2] == some_list[1][2] == some_list[2][2]== simbol :
                v = True
                
    elif some_list [0][0] == some_list[1][1] == some_list[2][2]== simbol or some_list[2][0] == some_list[1][1] == some_list[0][2]==simbol:
                v = True
                
    else:
        v = False
        
    return v

pygame.init()

size = (190, 190)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Крестики нолики")
width = height = 50
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (30, 1, 200)
font = pygame.font.SysFont('microsofttaile', 32)
follow_player1 = font.render('X', 1, red, white)
follow_player2 = font.render('O', 1, green, white)
player = 1
margin = 10
mas = [[0]*3 for i in range(3)]
victory = False
step =0


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            
            column = x_mouse//(margin+width)
            row = y_mouse// (margin+height)
            
            if player == 1 and mas [row][column] == 0:
                mas [row][column] = 1
                x_p = column*width+(column+1)*margin
                y_p = row*height+(row+1)*margin
                screen.blit(follow_player1, (x_p, y_p))
                victory = vin(mas, player)
                if victory == True:
                    s1 = (356, 28)
                    screen1 = pygame.display.set_mode(s1)
                    font1 = pygame.font.SysFont('gisha', 35)
                    screen1.blit(font1.render('Победил игрок, играющий Х ', 1, red, white), (0, 0))
                step +=1
                player =2
                
            elif player == 2 and mas [row][column] == 0:
                mas [row][column] = 2
                x_p = column*width+(column+1)*margin
                y_p = row*height+(row+1)*margin
                screen.blit(follow_player2, (x_p, y_p))
                victory = vin (mas, player)
                if victory == True:
                    s2 = (467, 40)
                    screen2 = pygame.display.set_mode(s2)
                    font2 = pygame.font.SysFont('trebuchetms', 35)
                    screen2.blit(font2.render('Победил игрок, играющий О ', 1, green, white), (0, 0))
                step +=1
                player =1
                
        elif step == 8:
                s3 = (220, 28)
                screen3 = pygame.display.set_mode(s3)
                font3 = pygame.font.SysFont('jasmineupc', 35)
                screen3.blit(font3.render('Нет победителей  ', 1, yellow, white), (0, 0))
        
            
    pygame.display.update()
