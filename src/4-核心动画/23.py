from manim import *


class WiggleDemo(Scene):
    def construct(self):
        # 1. 一个公式，作为被抖动的目标
        formula = MathTex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1")

        # 2. 一个图形，作为第二个被抖动的目标
        star = Star(color=YELLOW, fill_opacity=0.8).shift(RIGHT * 3.5)

        self.add(formula, star)
        self.wait(0.5)

        # 3. 默认参数：轻微晃动
        self.play(Wiggle(formula))

        # 4. 自定义参数：更大幅度的缩放和旋转，抖动次数更多
        self.play(
            Wiggle(
                star,
                scale_value=1.4,
                rotation_angle=15 * DEGREES,
                n_wiggles=10,
            )
        )

        self.wait(0.5)
