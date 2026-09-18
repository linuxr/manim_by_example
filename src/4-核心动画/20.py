from manim import *


class IndicateDemo(Scene):
    def construct(self):
        # 1. 一个公式，作为被强调的目标
        formula = MathTex(r"a^2 + b^2 = c^2")

        # 2. 一个图形，作为第二个被强调的目标
        square = Square(side_length=1.5, color=BLUE).shift(RIGHT * 3.5)

        self.add(formula, square)
        self.wait(0.5)

        # 3. 默认参数：放大 1.2 倍，黄色
        self.play(Indicate(formula))

        # 4. 自定义参数：放大 1.5 倍，青色，更长的持续时间
        self.play(
            Indicate(
                square,
                scale_factor=1.5,
                color=TEAL,
                run_time=1.5,
            )
        )

        self.wait(0.5)
