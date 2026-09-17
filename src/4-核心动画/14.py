from manim import *


class SpinInFromNothingDemo(Scene):
    def construct(self):
        # 创建两个图形并排排列
        square = Square(side_length=2, color=BLUE, fill_opacity=0.8).shift(LEFT * 2.5)
        triangle = Triangle(color=GREEN, fill_opacity=0.8).shift(RIGHT * 2.5)

        # 默认旋转角度为 PI/2，从无到有旋转生长
        self.play(
            SpinInFromNothing(square),
            run_time=2,
        )
        self.wait(0.5)

        # 指定旋转角度为 270 度，并设置生长过程中的初始颜色为黄色
        self.play(
            SpinInFromNothing(triangle, angle=-270 * DEGREES, point_color=YELLOW),
            run_time=2,
        )
        self.wait(1)
