import turtle
import random
import time

# creating vars
playerScore = 0
highestScore = 0
delayTime = 0.1

# create window screen
window = turtle.Screen()
window.title("First game: Snake by Sergei Chernyahovsky")
window.bgcolor("orange")
window.bgpic("backgroundlogo.png")
window.setup(width=800, height=600)
window.tracer(0)

# creating the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("red")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# creating the food for the snake
snakeFood = turtle.Turtle()
snakeFood.shape("square")
snakeFood.color("green")
snakeFood.speed(0)
snakeFood.penup()
snakeFood.goto(0, 100)
# scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 250)
sc.write("Your score: 0 Highest Score : 0", align="center", font=("Arial", 24, "normal"))


# Assigning directions

def moveLeft():
    if snake.direction != "right":
        snake.direction = "left"


def moveRight():
    if snake.direction != "left":
        snake.direction = "right"


def moveUp():
    if snake.direction != "down":
        snake.direction = "up"


def moveDown():
    if snake.direction != "up":
        snake.direction = "down"


def move():
    if snake.direction == "up":
        coord_y = snake.ycor()
        snake.sety(coord_y + 20)
    if snake.direction == "down":
        coord_y = snake.ycor()
        snake.sety(coord_y - 20)
    if snake.direction == "right":
        coord_x = snake.xcor()
        snake.setx(coord_x + 20)
    if snake.direction == "left":
        coord_x = snake.xcor()
        snake.setx(coord_x - 20)


# keyboard bindings
window.listen()

window.onkeypress(moveLeft, "a")
window.onkeypress(moveRight, "d")
window.onkeypress(moveUp, "w")
window.onkeypress(moveDown, "s")

segments = []
# Implementing the gameplay


while True:
    window.update()

    if snake.xcor() > 390 or snake.xcor() < -390 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        playerScore = 0
        delayTime = 0.1
        sc.clear()
        sc.write(f"Player's score: {playerScore} Highest score: {highestScore}", align="center",
                 font=("Arial", 24, "normal"))

    if snake.distance(snakeFood) < 20:
        coordX = random.randint(-290, 290)
        coordY = random.randint(-290, 290)
        snakeFood.goto(coordX, coordY)

        # Adding segment
        addedSegment = turtle.Turtle()
        addedSegment.speed(0)
        addedSegment.shape("square")
        addedSegment.color("black")
        addedSegment.penup()
        segments.append(addedSegment)
        delayTime -= 0.001
        playerScore += 100

        if playerScore > highestScore:
            highestScore = playerScore
        sc.clear()
        sc.write(f"Player's score : {playerScore} Highest score: {highestScore}", align="center",
                 font=("Arial", 24, "normal"))

    # checking for collisions
    for i in range(len(segments) - 1, 0, -1):
        coordX = segments[i - 1].xcor()
        coordY = segments[i - 1].ycor()
        segments[i].goto(coordX, coordY)

    if len(segments) > 0:
        coordX = snake.xcor()
        coordY = snake.ycor()
        segments[0].goto(coordX, coordY)

    move()

    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"

            for t in segments:
                t.goto(1000, 1000)
            t.clear()
            playerScore = 0
            delayTime = 0.1
            c.clear()
            sc.write(f"Player's score: {playerScore} Highest score: {highestScore}", align="center",
                     font=("Arial", 24, "normal"))
    time.sleep(delayTime)

window.mainloop()
