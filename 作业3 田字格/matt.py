import turtle

def draw_grid():
    turtle.speed(10) 
    turtle.penup()  

    turtle.goto(-100, -100)  
    turtle.pendown()  
    for _ in range(4):      
        turtle.forward(200) 
        turtle.left(90)    

    turtle.penup()
    turtle.goto(-100, 0)  
    turtle.pendown()
    turtle.forward(200)    

    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.left(90)          
    turtle.forward(200)   
    
    turtle.penup()
    turtle.goto(-80, -80) 
    turtle.pendown()      
    for _ in range(4):  
     turtle.forward(150) 
     turtle.right(90)
     
    def draw_dashed_line(start_x, start_y, end_x, end_y):
        turtle.penup()
        turtle.goto(start_x, start_y)
        turtle.pendown()
        distance = ((end_x - start_x) ** 2 + (end_y - start_y) ** 2) ** 0.5
        dash_length = 10  
        space_length = 5  
        angle = turtle.towards(end_x, end_y) 
        turtle.setheading(angle)  
        for _ in range(int(distance // (dash_length + space_length))):
            turtle.pendown()
            turtle.forward(dash_length)
            turtle.penup()
            turtle.forward(space_length)
            
        remaining = distance % (dash_length + space_length)
        if remaining > dash_length:
            turtle.pendown()
            turtle.forward(dash_length)
            turtle.penup()
            turtle.forward(remaining - dash_length)
        else:
            turtle.pendown()
            turtle.forward(remaining)

    draw_dashed_line(-100, 100, 100, -100)

    draw_dashed_line(-100, -100, 100, 100)

    turtle.hideturtle()

    turtle.done()

draw_grid()

