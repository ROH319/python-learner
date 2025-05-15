import turtle


def koch(t, order, size, speed, color):
    t.speed(speed)
    t.pencolor(color)
    if order == 0:
        t.forward(size)
    else:
        koch(t, order - 1, size / 3, speed, color)
        t.left(60)
        koch(t, order - 1, size / 3, speed, color)
        t.right(120)
        koch(t, order - 1, size / 3, speed, color)
        t.left(60)
        koch(t, order - 1, size / 3, speed, color)


def draw_koch_snowflake(order, size, speed, color, is_reverse=False):
    t = turtle.Turtle()
    screen = turtle.Screen()
    if is_reverse:
        t.right(180)
    for _ in range(3):
        koch(t, order, size, speed, color)
        t.right(120)
    screen.exitonclick()


# 正向绘制雪花
#draw_koch_snowflake(order=3, size=300, speed=3, color="blue", is_reverse=False)

# 反向绘制雪花
draw_koch_snowflake(order=3, size=300, speed=3, color="red", is_reverse=True)
