from manim import *


class TracedPathBasic(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(LEFT * 2)
        path = TracedPath(
            dot.get_center,
            stroke_color=YELLOW,
            stroke_width=3,
        )

        self.add(dot, path)

        self.play(dot.animate.shift(RIGHT * 4), run_time=1.5)
        self.play(dot.animate.shift(UP * 2 + LEFT * 2), run_time=1.5)
        self.play(dot.animate.shift(DOWN * 2 + LEFT * 2), run_time=1.5)
        self.wait(0.5)
