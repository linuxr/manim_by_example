# 1. 🔲 基础对象：几何图形: 09-圆弧
from manim import (
    BLUE,
    DOWN,
    LEFT,
    PI,
    RED,
    RIGHT,
    UP,
    YELLOW,
    Arc,
    Create,
    DashedVMobject,
    GrowFromCenter,
    Scene,
    Transform,
)


class ArcDemo(Scene):
    def construct(self):
        # 创建基础圆弧：半径2，从0度开始，扫过90度（PI/2）
        arc_basic = Arc(
            radius=2, start_angle=0, angle=PI / 2, color=BLUE, stroke_width=6
        ).shift(UP)

        # 创建带箭头的圆弧（用于角度标注）
        arc_arrow = Arc(
            radius=1.2,
            start_angle=PI / 4,
            angle=3 * PI / 4,
            color=YELLOW,
            tip_length=0.2,
        ).add_tip()
        arc_arrow.shift(LEFT * 2 + DOWN)

        # 创建虚线圆弧
        arc_dashed = DashedVMobject(
            Arc(radius=2.5, start_angle=PI, angle=PI / 3, color=RED), num_dashes=20
        )
        arc_dashed.shift(RIGHT * 3)

        # 布局

        # 动画演示
        self.play(Create(arc_basic))
        self.play(GrowFromCenter(arc_arrow))
        self.play(Create(arc_dashed))
        self.wait()

        # 使用 Transform 实现圆弧角度从 90° → 180° 的动画
        arc_target = Arc(
            radius=2, start_angle=0, angle=PI, color=BLUE, stroke_width=6
        ).shift(UP)
        self.play(Transform(arc_basic, arc_target), run_time=1.5)
        self.wait()
