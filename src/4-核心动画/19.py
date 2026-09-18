from manim import *


class FocusOnDemo(Scene):
    def construct(self):
        # 1. 创建一个点和一个公式，分别作为聚焦目标
        dot = Dot(color=YELLOW).shift(LEFT * 3)
        formula = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}").shift(
            RIGHT * 2
        )

        self.add(dot, formula)
        self.wait(0.5)

        # 2. 默认参数：灰色聚光灯收缩到圆点
        self.play(FocusOn(dot))

        # 3. 青色聚光灯，更高的不透明度，收缩到公式
        self.play(
            FocusOn(
                formula,
                color=TEAL,
                opacity=0.4,
                run_time=1.5,
            )
        )

        self.wait(0.5)
