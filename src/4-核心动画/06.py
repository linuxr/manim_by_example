from manim import *


class ShowSubmobjectsOneByOneDemo(Scene):
    def construct(self):
        # 创建一排依次排列的圆点
        dots = VGroup(
            *[Dot(radius=0.25, color=BLUE).shift(RIGHT * i) for i in range(-3, 4)]
        )

        # 逐个替换显示：屏幕上始终只有一个圆点
        self.play(
            ShowSubmobjectsOneByOne(dots),
            run_time=3,
        )
        self.wait(1)
