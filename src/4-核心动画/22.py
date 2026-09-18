from manim import *
import numpy as np


class ThinningStrokeWidthDemo(Scene):
    def construct(self):
        # 1. 一条水平线，作为扫过的路径
        line = Line(LEFT * 4, RIGHT * 4).set_color(BLUE)

        # 2. 一段正弦曲线，作为第二条路径
        curve = FunctionGraph(lambda x: np.sin(x), x_range=[-3, 3], color=GREY)

        self.add(line, curve)
        self.wait(0.5)

        # 3. 默认参数：光带从左向右扫过直线
        self.play(ShowPassingFlashWithThinningStrokeWidth(line))

        # 4. 更宽的光带，尾部更细，青色，扫过直线
        self.play(
            ShowPassingFlashWithThinningStrokeWidth(
                line.copy().set_color(TEAL),
                time_width=0.5,
            )
        )

        # 5. 光带沿正弦曲线扫过
        self.play(
            ShowPassingFlashWithThinningStrokeWidth(
                curve.copy().set_color(YELLOW),
                time_width=0.3,
            )
        )

        self.wait(0.5)
