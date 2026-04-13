# 0. 🚀 起步: 02-常用命令行参数
from manim import (
    LEFT,
    RED,
    RIGHT,
    YELLOW,
    Circle,
    Create,
    Scene,
)


class FPSCircleMotion(Scene):
    def construct(self):
        # 创建一个高视觉对比度的圆形
        circle = Circle(color=YELLOW, fill_color=RED, fill_opacity=0.8, stroke_width=5)
        self.play(Create(circle))

        # 关键动画：让圆形在屏幕两端快速往复移动
        # 移动距离大、速度快，帧率差异会非常明显
        for _ in range(2):  # 来回2次
            self.play(circle.animate.move_to(RIGHT * 5), run_time=0.5)
            self.play(circle.animate.move_to(LEFT * 5), run_time=0.5)

        self.wait(0.5)
