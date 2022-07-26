# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:29:59 2022

@author: anujg
"""

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#Create snake body
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
    
screen.update()
    
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
 #Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
   
 #Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        score.game_over()
            
 #Detect collision with tail
    for segments in snake.body[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()
    
    

screen.exitonclick()