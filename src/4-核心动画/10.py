from manim import *


class GrowArrowDemo(Scene):
    def construct(self):
        # 创建一条从左侧指向右侧的箭头
        arrow = Arrow(
            start=LEFT * 4,
            end=RIGHT * 4,
            color=BLUE,
            stroke_width=6,
            tip_length=0.3,
        )

        # 箭头从起点向尖端生长
        self.play(
            GrowArrow(arrow),
            run_time=2,
        )
        self.wait(0.5)

        # 再创建一个箭头，用 point_color 控制初始颜色
        arrow2 = Arrow(
            start=DOWN * 2 + LEFT * 2,
            end=UP * 1 + RIGHT * 2,
            color=GREEN,
            stroke_width=6,
        )
        self.play(
            GrowArrow(arrow2, point_color=YELLOW),
            run_time=2,
        )
        self.wait(1)
