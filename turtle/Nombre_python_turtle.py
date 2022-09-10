import turtle 
t = turtle.Turtle()  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.speed(0)
X=1
for i in range(250):  
    for colors in ["blue", "yellow", "white"]:  
        turtle.color(colors)  
        turtle.forward(5+X)  
        turtle.right(200) 
        X+=1
t=turtle.Turtle()

#L
t.shape("circle")
t.color("purple")
t.penup()
t.goto(-500,180)
t.pendown()
t.pensize(10)
t.forward(75)
t.back(75)
t.left(90)
t.forward(100)

#A
t.shape("circle")
t.color("yellow")
t.penup()
t.goto(-500,70)
t.pendown()
t.pensize(10)
t.left(-20)
t.forward(100)
t.right(130)
t.forward(100)
t.back(50)
t.right(115)
t.forward(42)

#U
t.shape("circle")
t.color("pink")
t.penup()
t.goto(-500,-40)
t.pendown()
t.pensize(10)
t.left(-96)
t.forward(85)
t.back(90)
t.right(89)
t.forward(68)
t.left(90)
t.forward(100)

#R
t.shape("circle")
t.color("white")
t.penup()
t.goto(-500,-159)
t.pendown()
t.pensize(10)
t.left(-6)
t.forward(100)
t.right(-90)
t.circle(29, extent=-181)
t.right(60)
t.forward(60)

#A
t.shape("circle")
t.color("green")
t.penup()
t.goto(-500,-271)
t.pendown()
t.pensize(10)
t.left(-938)
t.forward(100)
t.right(130)
t.forward(100)
t.back(50)
t.right(115)
t.forward(42)
turtle.done()



