from manim import *


class AbsolutePositioningExample(Scene):
    def construct(self):
        # 创建一个带网格的背景，帮助观察位置
        grid = NumberPlane()
        self.add(grid)

        # 1. move_to - 移动到绝对坐标
        circle = Circle(color=BLUE).move_to([-3, 2, 0])
        dot = Dot(color=RED).move_to([-3, 2, 0])

        # 2. to_edge - 移动到屏幕边缘
        top_text = Text("边缘", color=YELLOW).to_edge(UP)
        bottom_text = Text("边缘", color=YELLOW).to_edge(DOWN, buff=0.5)

        # 3. to_corner - 移动到屏幕角落
        corner_text = Text("角落", color=GREEN).to_corner(UR)

        # 4. move_to + aligned_edge - 用指定边缘对齐到目标点
        square = Square(color=PURPLE).move_to(ORIGIN, aligned_edge=LEFT)

        # 5. align_to - 对齐到另一个元素的边缘
        triangle = Triangle(color=ORANGE).shift(RIGHT * 3 + UP * 1)
        triangle.align_to(square, DOWN)

        # 添加到场景
        self.play(
            Create(circle),
            Create(dot),
            Create(top_text),
            Create(bottom_text),
            Create(corner_text),
            Create(square),
            Create(triangle),
        )
        self.wait(1)
