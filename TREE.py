import turtle, random
from random import randint
window = turtle.Screen()
turtle.screensize(1200, 1200)
window.bgcolor("MediumSeaGreen")

colors  = ["red","green","FireBrick","Crimson","MediumVioletRed", "blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from

t = turtle.Turtle(shape="arrow")

t.color(random.choice(colors))
t.lt(90)

lv = 10
l = 120
s = 26

t.width(lv)

t.penup()
t.bk(l)
t.pendown()
t.fd(l)


#Draw Tree
def draw_tree(l, level):
   
    width = t.width()  # save the current pen width

    t.width(width * 3.0 / 4.0)  # narrow the pen width

    l = 3.0 / 4.0 * l

    t.lt(s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.rt(2 * s)#change back to *
    t.fd(l)
    t.color(random.choice(colors))
    if level < lv:
        draw_tree(l, level + 1)#change back to 1
    t.bk(l)
    t.lt(s)#change back to s

    t.width(width)  # restore the previous pen width

t.speed("fastest")

draw_tree(l, 2)

#draw SUN
def draw_square(zach):
    for i in range(1,7):
        zach.forward(50)
        zach.right(90)
        zach.left(750)
        zach.forward(50) 
def draw_art(): 
    #Create the turtle zach - draws a square
    zach = turtle.Turtle()
    zach.hideturtle()
    zach.penup()
    zach.goto(450, 350)
    zach.showturtle()
    zach.pendown()
    zach.shape("arrow")
    zach.speed(12)
    for i in range (1,73):
        zach.color(random.choice(colors))
        draw_square(zach)
        zach.right(5)
    #Create the turtle angie - draws a circle
    angie = turtle.Turtle()
    angie.hideturtle()
    angie.penup()
    angie.goto(450, 350)
    angie.showturtle()
    angie.pendown()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(70)
    angie.speed(11)
    for i in range (1,73):
        angie.circle(70)
        angie.right(5)
    #Creat the turtle jane - draws a circle
    jane = turtle.Turtle()
    jane.hideturtle()
    jane.penup()
    jane.goto(450, 350)
    jane.showturtle()
    jane.pendown()
    jane.shape("arrow")
    jane.color("yellow")
    jane.circle(50)
    jane.speed(11)
    for i in range (1,73):
        jane.circle(50)
        jane.right(5)


draw_art()

#Draw Random Clouds
def draw_cloud() :
    for i in range(1, 20):
        tommy = turtle.Turtle()
        tommy.penup()
        tommy.goto(random.randint(-800, 400),randint(400, 600))
        tommy.pendown()
        tommy.color("white")
        tommy.begin_fill()
        tommy.circle(10)
        tommy.forward(15)
        tommy.circle(10)
        tommy.forward(15)
        tommy.circle(10)
        tommy.back(30)
        tommy.right(90)
        tommy.forward(5)
        tommy.left(90)
        tommy.back(10)
        tommy.circle(10)
        tommy.forward(15)
        tommy.circle(10)
        tommy.forward(15)
        tommy.circle(10)
        tommy.forward(15)
        tommy.circle(10)
        tommy.back(5)
        tommy.left(90)
        tommy.forward(10)
        tommy.left(90)
        tommy.circle(10)
        tommy.forward(15)
        tommy.circle(10)
        tommy.forward(15)
        tommy.circle(10)
        tommy.end_fill()
        tommy.left(180)
        tommy.speed("fastest")
draw_cloud()

#Draw Random Birds
def draw_bird() :
    for i in range(1, 10):
        tommy = turtle.Turtle()
        tommy.hideturtle()
        tommy.penup()
        tommy.goto(random.randint(-600,-400),random.randint(475,595))
        tommy.color("black")
        tommy.pendown()
        tommy.left(110)
        tommy.circle(10,100)
        tommy.penup()
        tommy.circle(10,260)
        tommy.right(210)
        tommy.circle(10,260)
        tommy.pendown()
        tommy.circle(10,100)
        tommy.left(100)
        tommy.speed("fastest")

draw_bird()







window.exitonclick()
