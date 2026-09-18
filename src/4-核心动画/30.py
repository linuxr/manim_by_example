from manim import *


class ShrinkToCenterDemo(Scene):
    def construct(self):
        # 1. 左侧：一个公式，作为收缩消失的目标
        formula = MathTex(r"\frac{d}{dx} e^x = e^x").shift(LEFT * 3)

        # 2. 右侧：一个正方形，作为第二个目标
        square = Square(side_length=2, color=TEAL, fill_opacity=0.6).shift(RIGHT * 3)

        self.add(formula, square)
        self.wait(0.5)

        # 3. 公式收缩到屏幕中心并消失
        self.play(ShrinkToCenter(formula), run_time=1.5)

        # 4. 正方形也收缩到屏幕中心并消失
        self.play(ShrinkToCenter(square), run_time=1.5)

        self.wait(0.5)
