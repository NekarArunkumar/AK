from turtle import *
setup(800, 500)
speed(0)

#Set up the start coordinates for the red stripes
stripe_x = -400
stripe_y = 250

#Draw one red stripe
def stripe():
    color("firebrick")
    begin_fill()
    for i in range(2):
        forward(800)
        right(90)
        forward(38)
        right(90)
    end_fill()
    
#Draw the 7 red stripes
for i in range(7):
    penup()
    goto(stripe_x, stripe_y)
    pendown()
    stripe()
    stripe_y = stripe_y - 76
    
#Draw the blue rectangle
penup()
goto(-400, 250)
pendown()
color("navy")
begin_fill()
for i in range(2):
    forward(350)
    right(90)
    forward(266)
    right(90)
end_fill()

#Draw one star
def star():
    color("white")
    begin_fill()
    for i in range(5):
        forward(20)
        right(144)
    end_fill()

#Set up star coordinates
x1 = -380
y1 = 230

x2 = -350 
y2 = 205

#Code for one even row of stars
def even_row():
    global x1
    global y1
    for i in range(6):
        penup()
        goto(x1, y1)
        pendown()
        star()
        x1 = x1 + 57

#Draw the 5 even rows of stars
for i in range(5):
    even_row()
    x1 = -380
    y1 = y1 - 52
    
#Code for one odd row of stars
def odd_row():
    global x2
    global y2
    for i in range(5):
        penup()
        goto(x2, y2)
        pendown()
        star()
        x2 = x2 + 57
        
#Draw the 4 odd rows of stars
for i in range(4):
    odd_row()
    x2 = -350
    y2 = y2 - 51
    
hideturtle()