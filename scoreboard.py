from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()
        self.level = 1
        self.goto(-240, 250)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 15, "bold"))

    def level_upgrade(self):
        self.level += 1
        self.clear()
        self.goto(-240, 250)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "bold"))


