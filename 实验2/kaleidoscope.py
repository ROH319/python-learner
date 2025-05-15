import turtle
import random
import time

screen = turtle.Screen()
screen.title("AAA")
screen.bgcolor("black")

p = turtle.Turtle()

p.speed(0)
colors = ["red","orange","yellow","green","blue","purple"]


# for i in range(100):
#    r = random.random()
#    g = random.random()
#    b = random.random()
#    p.pencolor(r,g,b)
#    p.forward(i*2)
#    p.right(144)

def draw_petal():
    for _ in range(2):
        p.circle(100,60)
        p.left(120)

for i in range(360):
    p.color(colors[i%6])
    draw_petal()
    p.left(10)

#turtle.done()
    
