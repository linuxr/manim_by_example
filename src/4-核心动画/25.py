from manim import *


class CyclicReplaceDemo(Scene):
    def construct(self):
        # 1. 三个不同颜色的圆，排成一行
        circles = VGroup(
            Circle(color=RED, fill_opacity=0.8).shift(LEFT * 3),
            Circle(color=GREEN, fill_opacity=0.8),
            Circle(color=BLUE, fill_opacity=0.8).shift(RIGHT * 3),
        )

        self.add(circles)
        self.wait(0.5)

        # 2. 默认参数：path_arc = 90°
        self.play(CyclicReplace(*circles))

        # 3. 自定义参数：更大的弧线，更慢的速度
        self.play(CyclicReplace(*circles, path_arc=180 * DEGREES, run_time=2))

        self.wait(0.5)
