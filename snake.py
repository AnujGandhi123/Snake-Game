# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:29:20 2022

@author: anujg
"""
from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        
        self.body = [Turtle() for i in range(3)]
        self.create_snake()
        self.head = self.body[0]
        
    def move(self):
        for obj_number in range(len(self.body)-1,0,-1):
            new_x = self.body[obj_number - 1].xcor()
            new_y = self.body[obj_number - 1].ycor()
            self.body[obj_number].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)
        
    def create_snake(self):
        X=0
        Y=0
        for obj in self.body:
            self.add_segment(X,Y,obj)
            X=X-20
            
    def add_segment(self,X,Y,obj):
        obj.pu()
        obj.shape("square")
        obj.color("white")
        obj.goto(X,Y)
    
    def extend(self): 
        #add new seg to snake
        position = self.body[-1].position()
        self.body.append(Turtle())
        self.add_segment(position[0], position[1],self.body[-1])
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)