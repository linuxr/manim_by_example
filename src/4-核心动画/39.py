from manim import *


class AnimationGroupExample(Scene):
    def construct(self):
        circle = Circle(color=BLUE).shift(LEFT * 3)
        square = Square(color=GREEN)
        triangle = Triangle(color=RED).shift(RIGHT * 3)

        self.add(circle, square, triangle)

        self.play(
            AnimationGroup(
                circle.animate.shift(UP * 2),
                square.animate.rotate(PI),
                triangle.animate.scale(1.5),
                lag_ratio=0.3,
            ),
            run_time=2,
        )
        self.wait(0.5)
