from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.score = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.color("white")
        self.pu()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=("Courier", 20, "normal"))

    def score_up(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER", False, align="center", font=("Courier", 20, "normal"))