from turtle import Turtle,Screen
import time
MOVING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments=[]
        self.create()

    def create(self):
        for position in MOVING_POSITIONS:
            new_segment = Turtle()
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.color("white")
            new_segment.shape("square")
            self.segments.append(new_segment)
    def move(self):
        for segment in range(len(self.segments)-1,0,-1):
             new_x = (self.segments[segment-1]).xcor()
             new_y = (self.segments[segment-1]).ycor()
             self.segments[segment].goto(new_x,new_y)
        self.segments[0].forward(20)
    def right(self):
        self.segments[0].setheading(0)
    def left(self):
        self.segments[0].setheading(180)
    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def grow(self):
        time.sleep(0.0005)
        new_segment = Turtle()
        new_segment.speed("fastest")
        new_segment.penup()
        x = self.segments[len(self.segments)-1].xcor()
        y = self.segments[len(self.segments)-1].ycor()
        new_segment.goto(x, y)
        new_segment.color("white")
        new_segment.shape("square")
        self.segments.append(new_segment)
