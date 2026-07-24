from manim import *


class VGroupArrangementDemo(Scene):
    def construct(self):
        # 创建一组形状（全部为 Manim 内置的标准图形）
        shapes = [
            Circle(color=BLUE).scale(0.6),
            Square(color=RED).scale(0.6),
            Triangle(color=GREEN).scale(0.6),
            Rectangle(color=YELLOW).scale(0.6),  # 替代 Diamond
            RegularPolygon(5, color=PURPLE).scale(0.6),  # 五角星
            RegularPolygon(6, color=ORANGE).scale(0.6),  # 六边形
        ]

        # 1. 水平排列（右）
        group_h = VGroup(*shapes[:4]).arrange(RIGHT, buff=0.3)
        label_h = Text("水平排列", font_size=24).next_to(group_h, UP, buff=0.2)
        self.play(Create(group_h), Write(label_h))
        self.play(FadeOut(label_h)), FadeOut(group_h)

        # 2. 垂直排列（下）
        group_v = VGroup(*shapes[:4]).arrange(DOWN, buff=0.5)
        label_v = Text("垂直排列", font_size=24).next_to(group_v, LEFT, buff=0.2)
        self.play(Create(group_v), Write(label_v))
        self.play(FadeOut(label_v)), FadeOut(group_v)

        # 3. 水平排列 + 底部对齐
        group_align = VGroup(*shapes[:4]).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
        label_align = Text("底部对齐", font_size=24).next_to(group_align, UP, buff=0.2)
        self.play(Create(group_align), Write(label_align))
        self.play(FadeOut(label_align)), FadeOut(group_align)

        # 4. 网格排列（2行3列）
        group_grid = VGroup(*shapes[:6]).arrange_in_grid(rows=2, cols=3, buff=0.4)
        label_grid = Text("网格排列", font_size=24).next_to(group_grid, DOWN, buff=0.2)
        self.play(Create(group_grid), Write(label_grid))

        # 对其中一个组整体做动画
        self.play(group_grid.animate.scale(1.2).set_color(YELLOW))
        self.play(group_grid.animate.shift(RIGHT * 1).rotate(PI / 6))

        self.wait(1)
