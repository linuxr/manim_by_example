# 1. 🔲 基础对象：几何图形: 11-角度标记
from manim import (
    DOWN,
    GREEN,
    LEFT,
    ORIGIN,
    PI,
    RED,
    RIGHT,
    TEAL,
    UP,
    WHITE,
    YELLOW,
    Angle,
    Create,
    Elbow,
    Line,
    RightAngle,
    Scene,
    VGroup,
)


class AngleMarkersExample(Scene):
    def construct(self):
        # 第1组：锐角标记
        line1_a = Line(LEFT, RIGHT, color=WHITE)
        line2_a = Line(DOWN, UP, color=WHITE)
        acute_angle = Angle(line1_a, line2_a, radius=0.5, color=YELLOW)

        acute_group = VGroup(line1_a, line2_a, acute_angle)
        acute_group.shift(LEFT * 3)

        # 第2组：钝角标记
        line1_b = Line(LEFT + DOWN / 3, RIGHT + UP / 3, color=WHITE)
        line2_b = Line(DOWN + LEFT / 3, UP + RIGHT / 3, color=WHITE)
        obtuse_angle = Angle(
            line1_b,
            line2_b,
            quadrant=(1, -1),
            radius=0.5,
            color=RED,
            dot=True,
            dot_color=RED,
        )

        obtuse_group = VGroup(line1_b, line2_b, obtuse_angle)

        # 第3组：直角标记
        h_line = Line(LEFT * 1.2, RIGHT * 1.2, color=WHITE)
        v_line = Line(DOWN * 1.2, UP * 1.2, color=WHITE)
        right_angle = RightAngle(
            h_line, v_line, length=0.3, quadrant=(1, 1), color=GREEN
        )
        elbow = Elbow(width=0.3, color=TEAL)
        elbow.rotate(-PI, about_point=ORIGIN)
        elbow.next_to(ORIGIN, DOWN + LEFT, buff=0)

        right_group = VGroup(h_line, v_line, right_angle, elbow)
        right_group.shift(RIGHT * 3)

        # 动画展示
        self.play(
            Create(acute_group),
            Create(obtuse_group),
            Create(right_group),
        )
        self.wait(2)
