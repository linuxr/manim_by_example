from manim import *


class SpiralInDemo(Scene):
    def construct(self):
        # 创建一组沿水平方向排列的几何图形
        shapes = VGroup(
            Triangle(color=RED, fill_opacity=0.8).shift(LEFT * 3),
            Square(color=BLUE, fill_opacity=0.8),
            Circle(color=GREEN, fill_opacity=0.8).shift(RIGHT * 3),
        )

        # 螺旋式入场
        self.play(
            SpiralIn(shapes, fade_in_fraction=0.6),
            run_time=3,
        )
        self.wait(1)
