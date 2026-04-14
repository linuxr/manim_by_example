# 1. 🔲 基础对象：几何图形: 01-点
from manim import *


class DotExample(Scene):
    def construct(self):
        # 基本点：不同大小
        dot1 = Dot(radius=0.1, color=RED).shift(LEFT * 3 + UP * 2)
        dot2 = Dot(radius=0.2, color=GREEN).shift(UP * 2)
        dot3 = Dot(radius=0.3, color=BLUE).shift(RIGHT * 3 + UP * 2)
        self.play(Create(dot1), Create(dot2), Create(dot3))

        # 带标签的点
        labeled1 = LabeledDot(MathTex("a^2", font_size=36, color=RED)).shift(LEFT * 2)
        labeled2 = LabeledDot(Text("中文", font_size=24, color=GREEN)).shift(RIGHT * 2)
        self.play(Create(labeled1), Create(labeled2))

        # 注释点
        anno1 = AnnotationDot(
            stroke_width=5,
            stroke_color=YELLOW,
            fill_color=RED,
            radius=0.2,
        ).shift(LEFT + DOWN)
        anno2 = AnnotationDot(
            stroke_width=15,
            stroke_color=GREEN,
            fill_color=PURPLE,
            radius=0.15,
        ).shift(RIGHT + DOWN)
        self.play(Create(anno1), Create(anno2))

        self.wait()
