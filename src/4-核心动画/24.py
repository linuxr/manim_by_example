from manim import *


class DirectionTransformDemo(Scene):
    def construct(self):
        # 1. 左侧：顺时针变换，右侧：逆时针变换
        dot_left = Dot(color=YELLOW).shift(LEFT * 2.5 + DOWN * 1.5)
        square_left = Square(side_length=1.2, color=YELLOW).shift(LEFT * 2.5 + UP * 1.5)

        dot_right = Dot(color=TEAL).shift(RIGHT * 2.5 + DOWN * 1.5)
        square_right = Square(side_length=1.2, color=TEAL).shift(RIGHT * 2.5 + UP * 1.5)

        # 2. 标签
        label_left = Text("Clockwise", font_size=28, color=YELLOW).shift(
            LEFT * 2.5 + UP * 3
        )
        label_right = Text("Counterclockwise", font_size=28, color=TEAL).shift(
            RIGHT * 2.5 + UP * 3
        )

        self.add(
            dot_left, dot_right, square_left, square_right, label_left, label_right
        )
        self.wait(0.5)

        # 3. 同时播放：左侧顺时针，右侧逆时针
        self.play(
            ClockwiseTransform(dot_left, square_left),
            CounterclockwiseTransform(dot_right, square_right),
        )

        self.wait(0.5)
