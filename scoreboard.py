# -*- coding: utf-8 -*-
"""
Created on Tue May 24 08:14:01 2022

@author: anujg
"""

from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0,270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f'Score= {self.score}', move=False, align = "center", font=('Arial',24,'normal'))
        
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', move=False, align = "center", font=('Arial',24,'normal'))