from manim import *


class AnimatedBoundaryDemo(Scene):
    def construct(self):
        # 1. 一个文本对象，作为被添加动态边界的对象
        text = Text("So shiny!", font_size=72)

        # 2. 创建动态边界：红绿蓝三色循环，循环速率为 3
        boundary = AnimatedBoundary(
            text,
            colors=[RED, GREEN, BLUE],
            cycle_rate=3,
            max_stroke_width=5,
        )

        # 3. 将文本和边界一起添加到场景
        self.add(text, boundary)

        # 4. 等待动画运行，让边界颜色持续循环
        self.wait(3)
