from manim import *


class SwapDemo(Scene):
    def construct(self):
        # 1. 两个不同颜色的圆，左右对称放置
        circle_a = Circle(color=RED, fill_opacity=0.8).shift(LEFT * 2.5)
        circle_b = Circle(color=BLUE, fill_opacity=0.8).shift(RIGHT * 2.5)

        # 2. 标签，帮助观众辨认谁和谁交换了位置
        label_a = Text("A", font_size=32, color=RED).next_to(circle_a, DOWN)
        label_b = Text("B", font_size=32, color=BLUE).next_to(circle_b, DOWN)

        self.add(circle_a, circle_b, label_a, label_b)
        self.wait(0.5)

        # 3. 默认参数：path_arc = 90°，弧线向上
        self.play(Swap(circle_a, circle_b))

        # 4. 自定义参数：更大的弧度，弧线更明显
        self.play(Swap(label_a, label_b, path_arc=180 * DEGREES))

        self.wait(0.5)
