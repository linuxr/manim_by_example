from manim import *


class ReplacementTransformDemo(Scene):
    def construct(self):
        # 1. 起始对象：圆形
        circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(Create(circle), run_time=1)

        # 2. 第一次替换：圆 -> 方
        square = Square(color=GREEN, fill_opacity=0.5)
        self.play(ReplacementTransform(circle, square), run_time=1.5)

        # 3. 第二次替换：方 -> 三角
        triangle = Triangle(color=YELLOW, fill_opacity=0.5)
        self.play(ReplacementTransform(square, triangle), run_time=1.5)

        # 4. 对最终对象做强调，证明 triangle 是场景中的活动对象
        self.play(Indicate(triangle), run_time=1)
        self.wait(0.3)
