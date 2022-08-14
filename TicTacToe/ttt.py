# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:11:35 2022

@author: Lili
"""

import numpy as np
import pygame
import math
#CIRCLE = pygame.image.load('circle.png')
#CROSS = pygame.image.load('x.png')
################Colors#############
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
#####################DIMENSIONS#################
ROWS = 3
COLUMNS = 3

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
CIRCLE = pygame.image.load('circle.png')
CROSS = pygame.image.load('x.png')

def mark(row, col, player):
    board[row][col] = player
board = np.zeros((ROWS,COLUMNS))

#check to see if chosen square is empty or not
def is_valid_mark(row,col):
    return board[row][col]== 0

#no zero, then, the board is full
def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 0 :
                return False
    return True

def draw_board():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] ==1:
                #import image to window with blit. takes 2 arguments, first image, 2nd is the tupple with x, y position.
                window.blit(CIRCLE,((c*200)+50,(r*200)+50))
            elif board[r][c]==2:
                window.blit(CROSS,((c*200)+50,(r*200)+50))
    pygame.display.update()
                
            

def draw_lines():
    #The window we want to draw the color in, the color, the starting position, the end position and the width of the line.
    pygame.draw.line(window, BLACK,(200,0),(200,600),10)
    pygame.draw.line(window, BLACK,(400,0),(400,600),10)
    pygame.draw.line(window, BLACK,(0,200),(600,200),10)
    pygame.draw.line(window, BLACK,(0,400),(600,400),10)


def is_winning_move(player):
    #horizontal check
    if player == 1:
        #announcement = "Player 1 Won"
        winning_color=BLUE
    else:
        #announcement = "Player 2 Won"
        winning_color=RED
    for r in range(ROWS):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
           # print(announcement)
           #CREATE A HORIZONTAL LINE
           pygame.draw.line(window, winning_color, (10,(r*200) + 100), (WIDTH-10, (r*200) + 100), 10)
           return True
    for c in range(COLUMNS):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            #print(announcement)
            pygame.draw.line(window, winning_color, ((c*200) + 100, 10), ((c*200) + 100, HEIGHT-10), 10)
            return True
        #check diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        #print(announcement)
        #negative diagonal win
         pygame.draw.line(window, winning_color,(10, 10) , (590,590), 10)
         return True    
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
         #print(announcement)
         #bottom left to top right crner
         pygame.draw.line(window, winning_color, (590, 10), (10, 590), 10)
         return True   

board=np.zeros((ROWS,COLUMNS))

game_over = False

Turn = 0

#initialize pygame
pygame.init()

window = pygame.display.set_mode(SIZE)
#title
pygame.display.set_caption("tic tac toe")
window.fill(WHITE)
draw_lines()
pygame.display.update()
pygame.time.wait(2000)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type ==pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            
                          
            if Turn % 2 == 0:
                #player 1
                #row = int(input("Player 1: Choose row number (0-2): "))
                #second element in the tuple
                row = math.floor(event.pos[1]/200)
                col = math.floor(event.pos[0]/200)
                #col = int(input("Player 1: Choose column number (0-2): "))
                if is_valid_mark(row,col):
                    mark(row, col, 1)
                    if is_winning_move(1):
                        game_over=True
                else:
                    Turn -=1
            else:        
                #player 2
                row = math.floor(event.pos[1]/200)
                col = math.floor(event.pos[0]/200)
                if is_valid_mark(row,col):
                    mark(row, col, 2)
                    if is_winning_move(2):
                        game_over=True
                else:
                    Turn -=1
                    
        #player 1's turn even, player 2's turn is odd.
            Turn +=1
            print(board)
            draw_board()
    if is_board_full():
        game_over=True
    if game_over==True:
        print("Game Over")
        #delay of 2000 miliseconds before next round starts.
        pygame.time.wait(2000)
        #reset board
        board.fill(0)
        #fill window with white color
        window.fill(WHITE)
        #draw the lines and board
        draw_lines()
        draw_board()
        #reset game over to false, so game can begin again.
        game_over=False
        pygame.display.update()
        