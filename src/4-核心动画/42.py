from manim import *


class LaggedStartExample(Scene):
    def construct(self):
        dots = VGroup(*[Dot(radius=0.15) for _ in range(8)]).arrange(RIGHT, buff=0.5)
        dots.set_color_by_gradient(BLUE, RED)
        self.add(dots)

        self.play(
            LaggedStartMap(
                FadeOut,
                dots,
                lag_ratio=0.2,
            ),
            run_time=3,
        )
        self.wait(0.5)
