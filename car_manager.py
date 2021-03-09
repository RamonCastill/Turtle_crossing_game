from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 240]
X_POSITIONS = [300, 320, 340, 360, 380, 420, 460, 480, 500, 540, 560, 580, 600, 640, 680, 690, 700, 720, 740, 780, 800]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.x_move = 5
        self.color(random.choice(COLORS))
        self.goto(random.choice(X_POSITIONS), random.choice(Y_POSITIONS))

    def move(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(random.choice(X_POSITIONS), random.choice(Y_POSITIONS))
        self.x_move += MOVE_INCREMENT

    def refresh(self):
        random_y = random.choice(Y_POSITIONS)
        self.goto(self.xcor(), random_y)

    def go_back(self):
        self.goto(random.choice(X_POSITIONS), random.choice(Y_POSITIONS))

