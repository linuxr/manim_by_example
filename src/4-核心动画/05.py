from manim import *


class ShowIncreasingSubsetsDemo(Scene):
    def construct(self):
        # 创建一排依次排列的圆点
        dots = VGroup(
            *[Dot(radius=0.15, color=BLUE).shift(RIGHT * i) for i in range(-3, 4)]
        )

        # 逐个累积显示
        self.play(
            ShowIncreasingSubsets(dots),
            run_time=3,
        )
        self.wait(1)
