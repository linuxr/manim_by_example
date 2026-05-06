# 1. 🔲 基础对象：几何图形: 06-圆形
import numpy as np
from manim import (
    BLUE,
    GREEN,
    ORANGE,
    PI,
    PINK,
    PURPLE,
    RED,
    RIGHT,
    TEAL,
    YELLOW,
    Circle,
    Create,
    Dot,
    FadeOut,
    LaggedStart,
    Scene,
    Star,
    Triangle,
    VGroup,
)


class CircleByExample(Scene):
    def construct(self):
        # 1. 基础圆形
        circle1 = Circle(radius=0.5, color=BLUE, stroke_width=4)
        circle2 = Circle(radius=0.8, color=YELLOW, stroke_width=2)
        circle3 = Circle(radius=1.0, color=RED, fill_opacity=0.3)

        circles = VGroup(circle1, circle2, circle3).arrange(RIGHT, buff=0.8)
        self.play(Create(circles))
        self.play(FadeOut(circles))

        # 2. 三点确定一个圆
        d1 = Dot(np.array([2, 1, 0]), color=RED)
        d2 = Dot(np.array([-1, -1, 0]), color=BLUE)
        d3 = Dot(np.array([1, -1.5, 0]), color=GREEN)
        dots = VGroup(d1, d2, d3)

        circle_from_points = Circle.from_three_points(
            d1.get_center(),
            d2.get_center(),
            d3.get_center(),
            color=PURPLE,
            stroke_width=3,
        )

        self.play(Create(dots))
        self.play(Create(circle_from_points))
        self.wait(0.5)
        self.play(FadeOut(dots), FadeOut(circle_from_points))

        # 3. 获取圆周上的点
        c = Circle(radius=1.5, color=YELLOW)
        self.play(Create(c))

        angles = [PI / 6, PI / 4, PI / 3, PI / 2, PI, 3 * PI / 2]
        dots_on_circle = VGroup()

        for angle in angles:
            point = c.point_at_angle(angle)
            dot = Dot(point, color=RED, radius=0.05)
            dots_on_circle.add(dot)

        self.play(LaggedStart(*[Create(dot) for dot in dots_on_circle], lag_ratio=0.2))
        self.wait(0.5)
        self.play(FadeOut(c), FadeOut(dots_on_circle))

        # 4. 圆形环绕图形
        star = Star().scale(0.6)
        star.set_color(ORANGE)

        circle_around_star = Circle().surround(star, buffer_factor=1.2)
        circle_around_star.set_color(GREEN)

        self.play(Create(star))
        self.wait(0.3)
        self.play(Create(circle_around_star))
        self.wait(0.5)

        # 内部圆环绕三角形
        triangle = Triangle().scale(0.8)
        triangle.set_color(TEAL)
        triangle.next_to(star, RIGHT, buff=1.5)

        circle_inside = Circle().surround(triangle, buffer_factor=0.4)
        circle_inside.set_color(PINK)

        self.play(Create(triangle))
        self.play(Create(circle_inside))
        self.wait(1)
