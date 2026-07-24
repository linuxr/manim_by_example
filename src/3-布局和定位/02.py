from manim import *


class RelativePositioningExample(Scene):
    def construct(self):
        # 创建一个参照物——正方形
        square = Square(color=BLUE)
        square_label = Text("参照物", font_size=24, color=BLUE).move_to(square)
        self.play(Create(square), Write(square_label))
        self.wait(0.5)

        # 1. shift - 相对偏移
        circle = Circle(color=RED).shift(RIGHT * 3 + UP * 1.5)
        circle_label = Text("shift", font_size=20, color=RED).move_to(circle)
        self.play(Create(circle), Write(circle_label))
        self.wait(0.5)

        # 2. next_to - 放在另一个元素的旁边
        triangle = Triangle(color=GREEN).next_to(square, RIGHT, buff=0.8)
        triangle_label = Text("next_to", font_size=20, color=GREEN).move_to(triangle)
        self.play(Create(triangle), Write(triangle_label))
        self.wait(0.5)

        # 3. next_to 带对齐边缘
        diamond = (
            Square(color=YELLOW, side_length=1.5)
            .rotate(PI / 4)
            .next_to(square, UP, buff=0.2, aligned_edge=LEFT)
        )
        diamond_label = Text("next_to+对齐", font_size=20, color=YELLOW).move_to(
            diamond
        )
        self.play(Create(diamond), Write(diamond_label))
        self.wait(0.5)

        # 4. align_to - 对齐边缘
        rect = Rectangle(color=PURPLE).shift(RIGHT * 3 + DOWN * 1.5)
        rect.align_to(square, LEFT)
        rect_label = Text("align_to", font_size=20, color=PURPLE).move_to(rect)
        self.play(Create(rect), Write(rect_label))

        self.wait(1)
