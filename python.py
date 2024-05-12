# import turtle
# pluma = turtle.Turtle()

# pluma.speed(2)

# for i in range(0,4):
#     pluma.forward(100)
#     pluma.left(90)

# windonw configure
import turtle
import time
import random

delay = 0.1

# marker
score = 0
high_score = 0

# Windonws
wn = turtle.Screen()
wn.title("game snake")
wn.bgcolor("#724911")
wn.setup(width =  600, height = 600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#218704")
head.penup()
head.goto(0,0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#d3036b")
food.penup()
food.goto(0,100)
food.direction = "stop"

# snake body
body = []

# text
text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0,260)
text.write('Score: 0    High Score: 0', align="center", font=("Courier", 24, "normal"))

# funtions
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"
    
def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
        
# keyboard
wn.listen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")

while True:
    wn.update()
    
    # border collision
    if (head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280):
        time.sleep(1)
        head.goto(0,0)
        head.direction = " stop"
        
        # hide the segment
        for segment in body:
            segment.goto(1000,1000)
            
        # delete segment
        body.clear()
        
        # marker reset
        score = 0
        text.clear()
        text.write('Score: {}    High Score: {}'.format(score,high_score), align="center", font=("Courier", 24, "normal"))
        
    # food collision
    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#29b300")
        new_segment.penup()
        body.append(new_segment)
            
        # increase marker
        score += 10
        if score > high_score:
            high_score = score

        # text marker
        text.clear()
        text.write('Score: {}    High Score: {}'.format(score,high_score), align="center", font=("Courier", 24, "normal"))
        
    # snake body movement
    totalseg = len(body)
    for index in range(totalseg -1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x,y)
        
    if totalseg > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)
    
    mov()
    
    # body collision
    for segment in body:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # hide the segment
            for segment in body:
                segment.goto(1000,1000)
                
            # delete segment
            body.clear()
            
            # marker reset
            score = 0
            text.clear()
            text.write('Score: {}    High Score: {}'.format(score,high_score), align="center", font=        ("Courier", 24, "normal"))
            
    time.sleep(delay)