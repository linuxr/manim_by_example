# 1. 🔲 基础对象：几何图形: 07-圆环形
from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    PI,
    PURPLE,
    RED,
    RIGHT,
    TEAL,
    UP,
    YELLOW,
    AnnularSector,
    Annulus,
    Create,
    FadeOut,
    Scene,
    Text,
    VGroup,
    Write,
)


class AnnulusAndSectorByExample(Scene):
    def construct(self):
        # ========== 第一部分：Annulus 基础圆环 ==========
        # 1. 三个不同粗细的圆环
        annulus_thin = Annulus(
            inner_radius=0.9,
            outer_radius=1.0,
            color=RED,
        )

        annulus_medium = Annulus(
            inner_radius=0.6,
            outer_radius=1.0,
            color=BLUE,
        )

        annulus_thick = Annulus(
            inner_radius=0.2,
            outer_radius=1.0,
            color=YELLOW,
        )

        annuli = VGroup(annulus_thin, annulus_medium, annulus_thick)
        annuli.arrange(RIGHT, buff=0.8)

        labels = VGroup(
            Text("细环", font_size=24),
            Text("中环", font_size=24),
            Text("粗环", font_size=24),
        )
        labels.arrange(RIGHT, buff=0.8)
        labels.next_to(annuli, DOWN, buff=0.3)

        self.play(Write(annuli), Write(labels))
        self.wait(0.5)
        self.play(FadeOut(annuli), FadeOut(labels))

        # ========== 第二部分：AnnularSector 基础环形圆弧 ==========
        # 2. 不同厚度的半圆弧
        sector_thick = AnnularSector(
            inner_radius=0.5,
            outer_radius=1.5,
            angle=PI,  # 180度
            color=GREEN,
        )

        sector_thin = AnnularSector(
            inner_radius=0.5,
            outer_radius=0.8,
            angle=PI,
            color=ORANGE,
        )

        sectors = VGroup(sector_thick, sector_thin)
        sectors.arrange(RIGHT, buff=1.0)

        sector_labels = VGroup(
            Text("厚环形弧", font_size=24),
            Text("薄环形弧", font_size=24),
        )
        sector_labels.arrange(RIGHT, buff=1.0)
        sector_labels.next_to(sectors, DOWN, buff=0.3)

        self.play(Create(sectors), Write(sector_labels))
        self.wait(0.5)
        self.play(FadeOut(sectors), FadeOut(sector_labels))

        # ========== 第三部分：不同起始角度 ==========
        # 3. 四个环形圆弧组成一个完整圆环
        inner_r, outer_r = 0.6, 1.2
        colors_list = [RED, YELLOW, GREEN, BLUE]
        start_angles = [0, PI / 2, PI, 3 * PI / 2]

        pie_chart = VGroup()
        for start, color in zip(start_angles, colors_list):
            sector = AnnularSector(
                inner_radius=inner_r,
                outer_radius=outer_r,
                start_angle=start,
                angle=PI / 2,
                color=color,
                fill_opacity=0.8,
            )
            pie_chart.add(sector)

        pie_chart.move_to(LEFT * 2)

        self.play(Create(pie_chart))
        self.wait(0.5)

        # 添加文字说明每个扇形
        labels_pie = VGroup(
            Text("0°", font_size=20, color=RED).next_to(pie_chart, RIGHT, buff=0.1),
            Text("90°", font_size=20, color=YELLOW).next_to(pie_chart, UP, buff=0.1),
            Text("180°", font_size=20, color=GREEN).next_to(pie_chart, LEFT, buff=0.1),
            Text("270°", font_size=20, color=BLUE).next_to(pie_chart, DOWN, buff=0.1),
        )
        self.play(Write(labels_pie))
        self.wait(0.5)

        # ========== 第四部分：环形进度条效果 ==========
        # 4. 一个增量动画的环形扇形
        progress = AnnularSector(
            inner_radius=0.8,
            outer_radius=1.3,
            start_angle=-PI / 2,  # 从顶部开始（-90°）
            angle=0,  # 初始为0
            color=PURPLE,
            fill_opacity=0.9,
        )
        progress.move_to(RIGHT * 3)

        self.play(Create(progress))

        # 动态增加角度，模拟进度条
        for angle in [
            PI / 6,
            PI / 4,
            PI / 3,
            PI / 2,
            2 * PI / 3,
            3 * PI / 4,
            5 * PI / 6,
            PI,
        ]:
            self.play(
                progress.animate.become(
                    AnnularSector(
                        inner_radius=0.8,
                        outer_radius=1.3,
                        start_angle=-PI / 2,
                        angle=angle,
                        color=PURPLE,
                        fill_opacity=0.9,
                    )
                ),
                run_time=0.3,
            )

        self.wait(0.5)

        # 重置并淡出
        self.play(FadeOut(progress), FadeOut(pie_chart), FadeOut(labels_pie))

        # ========== 第五部分：对比 Annulus 和 AnnularSector ==========
        full_ring = Annulus(
            inner_radius=0.6,
            outer_radius=1.2,
            color=TEAL,
            fill_opacity=0.5,
        )

        partial_ring = AnnularSector(
            inner_radius=0.6,
            outer_radius=1.2,
            start_angle=0,
            angle=PI * 1.5,  # 270度
            color=TEAL,
            fill_opacity=0.5,
        )

        comparison = VGroup(full_ring, partial_ring)
        comparison.arrange(RIGHT, buff=1.0)

        comp_labels = VGroup(
            Text("Annulus\n完整圆环", font_size=20, line_spacing=0.5),
            Text("AnnularSector\n270° 环形弧", font_size=20, line_spacing=0.5),
        )
        comp_labels.arrange(RIGHT, buff=1.0)
        comp_labels.next_to(comparison, DOWN, buff=0.3)

        self.play(Create(comparison), Write(comp_labels))
        self.wait(1)
