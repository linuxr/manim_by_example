from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    YELLOW,
    Create,
    CurvedArrow,
    CurvedDoubleArrow,
    Dot,
    Scene,
    Text,
    Write,
)


class CurvedArrowsExample(Scene):
    def construct(self):
        # 创建一组点标签
        start_point = LEFT * 3 + UP * 2
        end_point = RIGHT * 3 + UP * 2

        start_dot = Dot(start_point, color=BLUE)
        end_dot = Dot(end_point, color=RED)
        start_label = Text("起点", font_size=24, color=BLUE).next_to(start_point, UP)
        end_label = Text("终点", font_size=24, color=RED).next_to(end_point, UP)

        # 单箭头曲线
        curved_arrow = CurvedArrow(
            start_point,
            end_point,
            color=YELLOW,
            stroke_width=4,
        )

        # 双向箭头曲线（放在下方）
        curved_double_arrow = CurvedDoubleArrow(
            LEFT * 3 + DOWN,
            RIGHT * 3 + DOWN,
            color=GREEN,
            stroke_width=4,
        )

        # 动画展示
        self.play(Create(start_dot), Create(end_dot))
        self.play(Write(start_label), Write(end_label))

        self.play(Create(curved_arrow))

        self.play(Create(curved_double_arrow))
        self.wait()
