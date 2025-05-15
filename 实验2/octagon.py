import turtle
import random
import time

screen = turtle.Screen()
screen.title("AAA")
screen.bgcolor("black")

p = turtle.Turtle()

p.speed(0)

def draw(sides, color, size = 100):
    t = turtle.Turtle()
    t.speed(5)
    t.color(color)

    angle = 360 / sides
    t.begin_fill()

    for _ in range(sides):
        t.forward(size)
        t.left(angle)
    t.end_fill()

    turtle.done()

draw(8,"red",150)
