import turtle
import time
import random

#delay
delay=0.1

#Scores
score=0
high_score=0

#Screen Settings
wn = turtle.Screen()
wn.title("Sandy's Snake Game")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#Snake Settings
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "right"

#Snake Segments
segments = []

#Snake Food Settings
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(10,20)

#Score Card
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 HighScore: 0",align="Center",font=("Courier", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Key Bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#Main Loop for the game
while(1):
    wn.update()

    #Check for collision
    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()

        #Reset Score for every collision
        score=0

        pen.clear()
        pen.write("Score: {} HighScore: {}".format(score, high_score), align="Center", font=("Courier", 24, "normal"))

    #Eating Food
    if(head.distance(food) < 20):
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #Add segment to Snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.001

        #Increase by 10 for each food
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} HighScore: {}".format(score, high_score), align="Center", font=("Courier", 24, "normal"))

    #Move the segments in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if(len(segments) > 0):
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide Segments
            for seg in segments:
                seg.goto(1000, 1000)

            segments.clear()

            score=0

            delay=0.1

            pen.clear()
            pen.write("Score: {} HighScore: {}".format(score, high_score), align="Center",font=("Courier", 24, "normal"))

    time.sleep(delay)   #Speed of the Snake
