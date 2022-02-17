#turtle 모듈 이용한 미니게임

import turtle
import random

scr = turtle.Screen()
scr.setup(700 , 700)
scr.title("Snake Game!")
scr.bgcolor("lightcyan")

b = turtle.Turtle()
b.color("red")
b.shape("turtle")
b.penup()
b.goto(-300, -300)
b.pendown()
for x in range(4):
      b.ht()
      b.forward(600)
      b.left(90)
t = turtle.Turtle()
t.color("navy")
t.shape("turtle")
t.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("gray")
food.penup()

food.ht()
food.goto(-100, 100)
food.st()


def left():
      t.setheading(180)

def right():
      t.setheading(0)

def up():
      t.setheading(90)

def down():
      t.setheading(270)
scr.onkey(left,"Left")
scr.onkey(right,"Right")
scr.onkey(up,"Up")
scr.onkey(down,"Down")
scr.listen()
score = 0
speed = 1
while True:
      t.forward(speed)
      if t.xcor() <= -300 or t.xcor() >= 300:
            t.right(180)
      if t.ycor() <= -300 or t.ycor() >= 300:
            t.right(180)
      if -10 < t.xcor() - food.xcor() < 10 and -10 < t.ycor() - food.ycor() < 10:
            food.ht()
            food.goto(random.randint(-300,300),random.randint(-300,300))
            food.st()
            score += 10
            speed = 1+score/20
            t.write(score)
            
