import turtle

# Set up the game window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)

# left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("green")
left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-350, 0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("yellow")
right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Ball movement speed in the x-direction
ball.dy = 2  # Ball movement speed in the y-direction

# Function to move the left paddle up
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

# Function to move the left paddle down
def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Function to move the right paddle up
def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

# Function to move the right paddle down
def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Initialize scores
left_score = 0
right_score = 0

# Create the score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left: {}  Right: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary checking for ball
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Collision with paddles
    if (350 > ball.xcor() > 340) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.color("blue")  # Change ball color when it hits the right paddle
        ball.setx(340)
        ball.dx *= -1

    elif (-350 < ball.xcor() < -340) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.color("red")  # Change ball color when it hits the left paddle
        ball.setx(-340)
        ball.dx *= -1

    # Scoring
    if ball.xcor() > 390:
        left_score += 1
        score_display.clear()  # Clear previous score display
        score_display.write("Left: {}  Right: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)  # Reset ball position
        ball.dx *= -1  # Reverse ball direction

    elif ball.xcor() < -390:
        right_score += 1
        score_display.clear()  # Clear previous score display
        score_display.write("Left: {}  Right: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)  # Reset ball position
        ball.dx *= -1  # Reverse ball direction
