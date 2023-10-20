from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",  font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",  font=("Courier", 80, "normal"))
    # def score_calculator(self, ball, Turtle1, Turtle2):
    #     if ball.distance(Turtle1) > 50 and ball.xcor() > 320:
    #         self.goto(-40, 230)
    #         self.r_score += 1
    #         self.write(f"{self.r_score}", move=False, font=("Courier", 20, "normal"))
    #         self.write(f"{self.r_score}", move=False, font=("Courier", 20, "normal"))
    #
    #         print(f"Score of left Paddle : {self.r_score}")

        #
        # elif ball.distance(Turtle2) > 50 and ball.xcor() < -320:
        #     self.goto(40, 230)
        #     self.l_score += 1
        #     self.write(f"{self.l_score}", move=False, font=("Courier", 20, "normal"))
        #     print(f"x_score {self.l_score}")
    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()

