import turtle
import random
import time

def window(width, height):
    screen = turtle.Screen()
    screen.title("SNAKE")
    screen.bgcolor("white")
    screen.setup(width, height)
    screen.tracer(0)
    return screen

def snakeHead():
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("red")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"
    return head

def snakeFood():
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("blue")
    food.penup()
    food.goto(0,150)
    return food

def scoreBoard(height):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, height)
    return pen

def movement(head,screen):

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

    screen.listen()
    screen.onkeypress(go_up, "Up")
    screen.onkeypress(go_down, "Down")
    screen.onkeypress(go_left, "Left")
    screen.onkeypress(go_right, "Right")

def move(head):
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

def main(width, height):

    screen = window(width, height)
    head = snakeHead()
    food = snakeFood()
    pen = scoreBoard(260)
    movement(head, screen)

    segments = []
    score = 0
    high_score = 0

    while True:
        screen.update()

        # Border collision
        yborder = (height // 2)
        xborder = (width // 2)
        if head.xcor() > xborder or head.xcor() < -xborder or head.ycor() > yborder or head.ycor() < -yborder:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            pen.clear()
            pen.write(f"Puntuación: {score}  Récord: {high_score}", align="center", font=("Arial", 22, "normal"))

        # Food collision
        if head.distance(food) < 20:
            x = random.randint(-xborder // 20, xborder // 20) * 20
            y = random.randint(-yborder // 20, yborder // 20) * 20

            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("pink")
            new_segment.penup()
            segments.append(new_segment)

            score += 1
            if score > high_score:
                high_score = score

            pen.clear()
            pen.write(f"Score: {score}  Best: {high_score}", align="center", font=("Arial", 22, "normal"))

        # Move body
        for i in range(len(segments)-1, 0, -1):
            segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())

        if segments:
            segments[0].goto(head.xcor(), head.ycor())

        move(head)

        # Body collision
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()

                score = 0
                pen.clear()
                pen.write(f"Score: {score}  Best: {high_score}", align="center", font=("Arial", 22, "normal"))

        time.sleep(0.1)

main(800,600)
