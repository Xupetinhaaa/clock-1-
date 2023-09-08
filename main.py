import time
import turtle
from datetime import date

    

while True:

    # calculated dates

    today = date.today()
    
    
    #calculate times
    total_seconds = round(time.time())
    c_sec = round(total_seconds%60)
    c_minute = round(total_seconds//60)% 60
    c_hour = round(total_seconds//3600)%12
    east_hour = (c_hour - 5)%12
    military_time = round(east_hour+12)%12
    
    #Draw clock circle and format turtle
    t = turtle
    circle_1 = 60
    t.hideturtle()
    t.pensize(1)
    t.speed(100)
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    t.circle(circle_1)
    t.left(90)
    t.penup()
    t.forward(circle_1)
    t.pendown()
    #Draw hour hand
    t.right(30*east_hour)
    t.pensize(5)
    t.forward(30)
    t.back(30)
    t.left(30*east_hour)
  
    #Draw minute hand
  
    t.right(6*c_minute)
    t.pensize(3)
    t.forward(40)
    t.back(40)
    t.left(6*c_minute)
    #Draw second hand
    t.right(6*c_sec)
    t.pensize(2)
    t.pencolor('red')
    t.forward(40)
    t.back(40)
    t.left(6*c_sec)
    #Print time
    t.penup()
    t.goto(-40, -20)
    t.pencolor("black")

  
    if(c_minute < 12):
      zero = "0"
    else:
      zero = " "

    if(c_sec < 10):
      zero = "0"
    else:
      zero = " "

    

    if military_time > 12:
     period = "A.M"
    else:
      period = "P.M"
    
    #Uncomment the lines below once you define the time variables.
    turtle.write(zero + str(military_time) + ":"+ zero
                 + str(c_minute)+
                 ":"+ zero + str(c_sec)+":"+str(period))
    time.sleep(0.7)
    turtle.clear()
    

