import turtle

t = turtle.Turtle()

def drawStumpC():
    x, y = -70, 153
    t.goto(x, y)
    dx, dy = 8, 4
    t.write("C", font=("Arial Black", 20, "bold"))
    t.hideturtle()    

def angleForAnsi(): 
    turtle.color("red")
    turtle.penup()

    text = "ANSI"
    x, y = -90, 172
    dx, dy = 12, 4  

    for letter in text:
        turtle.goto(x, y)
        turtle.write(letter, font=("Arial black", 12, "bold"))
        x += dx  
        y += dy
    turtle.hideturtle()  

def drawAnsi():
    t.penup()
    t.goto(0, 0)
    t.setheading(30)  
    t.write("ANSI", font=("Arial black", 15, "bold"))

def drawStump():
    t.color("red") 
    for i in range(2):
        t.forward(60)
        t.right(90)
        t.forward(45)
        t.right(90)

def drawSoftwareSeries():
    turtle.color("black")
    turtle.penup()  
    turtle.goto(-100, 10)  
    turtle.pendown()
    turtle.write("SOFTWARE SERIES", align="center", font=("Times New Roman", 6, "italic"))
    turtle.hideturtle()   

def drawAutorDenis():
    turtle.color("steel blue")
    turtle.penup()  
    turtle.goto(-125, 35)  
    turtle.pendown()
    turtle.write("DENNIS M.RITCHIE", align="center", font=("Times New Roman", 12, "italic"))


def drawAuthorBrian():
    turtle.color("steel blue")
    turtle.penup()  
    turtle.goto(-125, 50)  
    turtle.pendown()
    turtle.write("BRIAN W.KERNIGHAN", align="center", font=("Times New Roman", 12, "italic"))



def drawProgrammingLanguage():
    turtle.penup()  
    turtle.goto(-225, 132)  
    turtle.pendown()
    turtle.color("black")
    turtle.forward(200)
    turtle.penup()  
    turtle.goto(-125, 104)  
    turtle.pendown() 
    turtle.write("PROGRAMMING", align="center", font=("Times New Roman", 20, "italic"))
    turtle.penup()
    turtle.penup()  
    turtle.goto(-125, 84)  
    turtle.pendown() 
    turtle.write("LANGUAGE", align="center", font=("Times New Roman", 20, "italic"))
    turtle.penup()
    # Синяя линия под программинг лаунгуаге
    turtle.penup()  
    turtle.goto(-225, 87)  
    turtle.pendown()
    turtle.color("steel blue")
    turtle.forward(200)
    # Линия под програминг лаунгуаге
    turtle.penup()  
    turtle.goto(-225, 85)  
    turtle.pendown()
    turtle.color("black")
    turtle.forward(200)


# Пишем С
def drawC():
    turtle.color("cornflower blue")
    turtle.penup()  
    turtle.goto(-125, 105)  
    turtle.pendown() 
    turtle.write("C", align="center", font=("Arial Black", 90, "bold"))

# Пишем The
def drawThe():
    turtle.penup()  
    turtle.goto(-125, 236)  
    turtle.pendown() 
    turtle.write("THE", align="center", font=("Times New Roman", 20, "italic"))
    turtle.penup()  
    turtle.goto(-225, 238)  
    turtle.pendown()
    turtle.color("black")
    turtle.forward(200)

# Длинна обложки
def lenghtBook():    
    turtle.left(90)
    turtle.forward(300)

# Ширина обложки
def widthBook():
    turtle.left(90)
    turtle.forward(250)

# Рисуем  макет обложки
def drawRectangle():
    for i in range(2): 
        lenghtBook()
        widthBook() 

# Пишем SECOND EDITION
def drawSecondEdition():
    turtle.color("dark red")  
    turtle.penup()  
    turtle.goto(-125, 268)  
    turtle.pendown()     
    turtle.write("SECOND EDITION", align="center", font=("Times New Roman", 10, "italic"))
    turtle.penup()
    turtle.goto(-225, 267)  
    turtle.pendown()
    turtle.color("black") 
    turtle.forward(200)
    turtle.penup()
    turtle.goto(-225, 265)     
    turtle.pendown()
    turtle.color("steel blue")
    turtle.forward(200)


turtle.speed(1)
#turtle.goto()
drawRectangle()
drawSecondEdition()
turtle.color("black") # синий цвет
drawThe()
drawC()
drawProgrammingLanguage()
drawAuthorBrian()
drawAutorDenis()
drawSoftwareSeries()
t.penup()  
t.goto(-104, 185)
t.setheading(25)
t.pendown()
drawStump()
t.penup()  # Чтобы не рисовал при перемещении
t.goto(200, 500)
stamp_id = t.stamp()  # Создаём штамп
t.hideturtle()
#drawAnsi()
angleForAnsi()
drawStumpC()

turtle.done()
