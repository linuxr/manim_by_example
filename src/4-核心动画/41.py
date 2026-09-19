from manim import *


class ChangeSpeedExample(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(LEFT * 4)
        self.add(dot)

        self.play(
            ChangeSpeed(
                dot.animate.shift(RIGHT * 8),
                speedinfo={0: 0.5, 0.5: 2, 1: 0.5},
                rate_func=linear,
            ),
            run_time=4,
        )
        self.wait(0.5)
