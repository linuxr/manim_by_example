from manim import *


class ScaleInPlaceDemo(Scene):
    def construct(self):
        # 1. 一个公式，作为原地放大的目标
        formula = MathTex(r"e^{i\pi} + 1 = 0").shift(LEFT * 3)

        # 2. 一个正方形，作为原地缩小的目标
        square = Square(side_length=2, color=TEAL, fill_opacity=0.6).shift(RIGHT * 3)

        self.add(formula, square)
        self.wait(0.5)

        # 3. 公式原地放大 1.5 倍
        self.play(ScaleInPlace(formula, 1.5), run_time=1.5)

        # 4. 正方形原地缩小到 0.5 倍
        self.play(ScaleInPlace(square, 0.5), run_time=1.5)

        self.wait(0.5)
