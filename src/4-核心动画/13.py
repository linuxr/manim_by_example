from manim import *


class GrowFromPointDemo(Scene):
    def construct(self):
        # 创建三个图形，分散在屏幕不同位置
        circle = Circle(radius=0.8, color=RED, fill_opacity=0.8).shift(
            LEFT * 3 + UP * 1.5
        )
        square = Square(side_length=1.5, color=BLUE, fill_opacity=0.8).shift(
            RIGHT * 3 + UP * 1.5
        )
        triangle = Triangle(color=GREEN, fill_opacity=0.8).shift(DOWN * 1.5)

        # 让三个图形都从原点方向生长出来
        origin = ORIGIN
        self.play(
            GrowFromPoint(circle, origin),
            GrowFromPoint(square, origin),
            run_time=2,
        )
        self.play(
            GrowFromPoint(triangle, origin, point_color=YELLOW),
            run_time=2,
        )
        self.wait(1)
