from manim import *


class DrawBorderThenFillDemo(Scene):
    def construct(self):
        # 创建一个带填充色的五边形
        pentagon = RegularPolygon(
            n=5,
            radius=1.5,
            color=BLUE,
            fill_opacity=0.8,
        )

        # 先描边、后填充
        self.play(
            DrawBorderThenFill(pentagon),
            run_time=2.5,
        )
        self.wait(1)
