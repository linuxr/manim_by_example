from manim import *


class FlashDemo(Scene):
    def construct(self):
        # 1. 创建一个点作为闪烁目标
        dot = Dot(color=YELLOW).shift(LEFT * 2)

        # 2. 创建一个公式作为另一个闪烁目标
        formula = MathTex(r"E = mc^2").shift(RIGHT * 2)

        self.add(dot, formula)
        self.wait(0.5)

        # 3. 默认参数闪烁：12 条短线，黄色
        self.play(Flash(dot))

        # 4. 更多线条，更长，更粗
        self.play(
            Flash(
                formula,
                color=TEAL,
                num_lines=24,
                line_length=0.5,
                line_stroke_width=6,
            )
        )

        self.wait(0.5)
