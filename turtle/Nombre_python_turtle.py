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
turtle.penup()
turtle.goto(0,0)
turtle.pencolor("red")

turtle.write("LAURA",False,align="center",font=("Algerian",200,"normal"))
turtle.mainloop()
