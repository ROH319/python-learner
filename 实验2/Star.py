import turtle
import random

screen = turtle.Screen()
screen.title("AAA")
screen.bgcolor("black")

p = turtle.Turtle()

p.speed(0)


for i in range(100):
    r = random.random()
    g = random.random()
    b = random.random()
    p.pencolor(r,g,b)
    p.forward(i*2)
    p.right(144)
