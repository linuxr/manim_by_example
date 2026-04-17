# 1. 🔲 基础对象：几何图形: 02-直线类
from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    PURPLE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Create,
    DashedLine,
    LabeledLine,
    Line,
    Scene,
    TangentLine,
)


class LineExample(Scene):
    def construct(self):
        # 基本直线
        line1 = Line(LEFT * 4, RIGHT * 4, color=BLUE)
        line1.to_edge(UP)
        self.play(Create(line1))

        # 带弯曲度的直线
        line2 = Line(LEFT * 3, RIGHT * 3, path_arc=1, color=GREEN)
        line2.next_to(line1, DOWN, buff=0.5)
        self.play(Create(line2))

        # 虚线
        dashed = DashedLine(
            LEFT * 3, RIGHT * 3, dash_length=0.3, dashed_ratio=0.6, color=YELLOW
        )
        dashed.next_to(line2, DOWN, buff=0.5)
        self.play(Create(dashed))

        # 圆的切线
        circle = Circle(radius=1, color=WHITE)
        circle.next_to(dashed, DOWN, buff=0.5)
        tangent = TangentLine(circle, alpha=0.25, length=3, color=RED)
        self.play(Create(circle), Create(tangent))

        # 带标签的直线
        labeled = LabeledLine(
            "y = kx + b",
            start=LEFT * 3,
            end=RIGHT * 3,
            label_config={
                "font_size": 24,
                "color": WHITE,
            },
            frame_config={
                "fill_color": PURPLE,
                "fill_opacity": 0.8,
            },
        )
        labeled.next_to(circle, DOWN, buff=0.5)
        self.play(Create(labeled))

        self.wait()
