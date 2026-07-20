# 1. 🔲 基础对象：几何图形: 10-扇形
from manim import (
    BLUE,
    LEFT,
    PI,
    RED,
    RIGHT,
    UP,
    YELLOW,
    Create,
    FadeIn,
    GrowFromCenter,
    Scene,
    Sector,
    Transform,
)


class SectorDemo(Scene):
    def construct(self):
        # 基础扇形：90度蓝色扇形
        sector_basic = Sector(
            radius=2,
            angle=PI / 2,
            start_angle=0,
            fill_color=BLUE,
            fill_opacity=0.7,
            stroke_width=2,
        ).shift(UP + LEFT)

        # 环形扇区：用于饼图或进度环
        sector_ring = Sector(
            radius=2,
            angle=3 * PI / 4,
            start_angle=PI / 2,
            fill_color=YELLOW,
            fill_opacity=0.8,
        ).shift(RIGHT * 3)

        # 小扇形用于后续变换演示
        sector_small = Sector(
            radius=2,
            angle=PI / 6,
            start_angle=PI,
            fill_color=RED,
            fill_opacity=0.6,
        ).shift(LEFT * 2)

        # 动画展示
        self.play(GrowFromCenter(sector_basic))
        self.play(Create(sector_ring))
        self.play(FadeIn(sector_small))
        self.wait()

        # 动态扩展扇形角度（使用 Transform）
        sector_target = Sector(
            radius=1,
            angle=PI,  # 从30°扩展到180°
            start_angle=PI,
            fill_color=RED,
            fill_opacity=0.6,
        ).shift(LEFT * 2)
        self.play(Transform(sector_small, sector_target), run_time=1.5)
        self.wait()
