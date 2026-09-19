from manim import *


class RotateAndRotating(Scene):
    def construct(self):
        title = Text("Rotate / Rotating", font_size=40).to_edge(UP)
        origin = Dot(ORIGIN, color=RED)
        arrow = Arrow(ORIGIN, RIGHT * 2, buff=0, color=YELLOW)
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5).move_to(RIGHT * 2)

        self.add(title, origin, arrow, square)

        self.play(Rotate(arrow, angle=PI / 2, about_point=ORIGIN), run_time=1.5)
        self.play(
            Rotating(
                square,
                angle=TAU,
                about_point=ORIGIN,
                run_time=3,
                rate_func=linear,
            )
        )
        self.wait(0.5)
