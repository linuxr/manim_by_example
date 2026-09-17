from manim import *


class GrowFromEdgeDemo(Scene):
    def construct(self):
        # 创建两个正方形，并排排列
        squares = [
            Square(side_length=2, color=BLUE, fill_opacity=0.8) for _ in range(2)
        ]
        VGroup(*squares).set_x(0).arrange(buff=2)

        # 从底边向上生长
        self.play(
            GrowFromEdge(squares[0], DOWN),
            run_time=2,
        )
        self.wait(0.5)

        # 从右上角方向生长，并设置初始颜色为红色
        self.play(
            GrowFromEdge(squares[1], UR, point_color=RED),
            run_time=2,
        )
        self.wait(1)
