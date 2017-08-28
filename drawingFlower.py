import turtle

def draw_petal(turtle):
    for i in range(1, 37):
        for j in range(2):
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            turtle.right(120)
        turtle.right(10)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("black")
    
    petal = turtle.Turtle()
    petal.shape("turtle")
    petal.color("silver")
    petal.speed(10)
    
    draw_petal(petal)
    petal.right(90)
    petal.forward(300)
       
    window.exitonclick()
    

draw_flower()
