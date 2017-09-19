import turtle

def draw_rhombus(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(45)
        some_turtle.forward(100)
        some_turtle.left(135)
        

def draw_line(some_line):
    for i in range(1,2):
        some_line.right(90)
        some_line.forward(300)
    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("Red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(5)
    for x in range(1,37):
        draw_rhombus(brad)
        brad.right(10)
    for i in range(37,38):
        draw_line(brad)
    window.exitonclick()
    
draw_art()
                   
