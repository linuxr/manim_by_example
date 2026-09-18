from manim import *


class ChangeDecimalToValueDemo(Scene):
    def construct(self):
        # 1. 创建一个 DecimalNumber，初始值为 0
        number = DecimalNumber(0, num_decimal_places=2)

        # 2. 一个公式，指数用 DecimalNumber 表示，可被动态改变
        formula = MathTex("E = m", "c")
        exponent = DecimalNumber(2, num_decimal_places=0, font_size=36)
        exponent.next_to(formula[1], UR, buff=0.05)
        formula.add(exponent)
        formula.shift(UP * 2)

        self.add(number, formula)
        self.wait(0.5)

        # 3. 数字从 0 变化到 10
        self.play(ChangeDecimalToValue(number, 10, run_time=2))

        # 4. 公式中的指数 2 变化到 4
        self.play(ChangeDecimalToValue(exponent, 4, run_time=1.5))

        self.wait(0.5)
