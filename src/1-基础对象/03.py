import numpy as np
from manim import (
    BLUE,
    DOWN,
    GREEN,
    GREEN_A,
    LEFT,
    ORIGIN,
    PURPLE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    LabeledArrow,
    Scene,
    StealthTip,
    Text,
    Vector,
    VGroup,
    Write,
)


class ArrowByExample(Scene):
    def construct(self):
        # 1. 基础 Arrow：从起点到终点
        arrow1 = Arrow(
            start=LEFT * 3,
            end=RIGHT * 3,
            color=BLUE,
            buff=0,
        )
        label1 = Text("Arrow", font_size=24).next_to(arrow1, UP)

        # 2. Vector：从原点指向指定坐标
        vector = Vector(
            direction=np.array([2, 1.5, 0]),
            color=YELLOW,
        )
        vec_label = vector.coordinate_label(color=YELLOW)

        # 3. LabeledArrow：带标签的箭头
        labeled = LabeledArrow(
            label=r"\vec{v} = (x, y)",
            start=RIGHT * 2,
            end=LEFT * 2 + UP,
            label_config={
                "font_size": 28,
                "color": WHITE,
            },
            frame_config={
                "fill_color": GREEN,
                "fill_opacity": 0.8,
            },
            color=GREEN_A,
        )

        # 4. 调整箭头与线的比例
        thin_arrow = Arrow(
            start=LEFT * 2,
            end=RIGHT * 2,
            color=RED,
            max_tip_length_to_length_ratio=0.05,  # 小箭头
            buff=0,
        )
        thin_label = Text("小箭头", font_size=20).next_to(thin_arrow, DOWN)
        thin_group = VGroup(thin_arrow, thin_label)

        fat_arrow = Arrow(
            start=LEFT * 2,
            end=RIGHT * 2,
            color=RED,
            max_tip_length_to_length_ratio=0.25,  # 大箭头
            buff=0,
        )
        fat_label = Text("大箭头", font_size=20).next_to(fat_arrow, DOWN)
        fat_group = VGroup(fat_arrow, fat_label)

        # 5. 不同的箭头样式
        custom_tip = Arrow(
            start=LEFT * 2,
            end=RIGHT * 2,
            color=PURPLE,
            tip_shape=StealthTip,  # 隐形战机风格
            buff=0,
        )
        tip_label = Text("StealthTip 箭头", font_size=20).next_to(custom_tip, DOWN)

        # 布局：将所有对象分组并排列
        group1 = VGroup(arrow1, label1)
        group2 = VGroup(vector, vec_label)
        group3 = VGroup(labeled)
        group4 = VGroup(thin_group, fat_group).arrange(RIGHT, buff=0.5)
        group5 = VGroup(custom_tip, tip_label)

        all_groups = VGroup(group1, group2, group3, group4, group5).arrange(
            DOWN, buff=0.5
        )
        all_groups.move_to(ORIGIN)

        # 动画演示
        self.play(Write(group1))
        self.play(Write(group2))
        self.play(Write(group3))
        self.play(Write(group4))
        self.play(Write(group5))
        self.wait()
