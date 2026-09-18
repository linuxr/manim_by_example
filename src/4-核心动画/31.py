from manim import *


class TransformMatchingShapesDemo(Scene):
    def construct(self):
        # 1. 源公式：勾股定理
        source = MathTex(r"a^2 + b^2 = c^2")

        # 2. 目标公式：将 c^2 移到左侧
        target = MathTex(r"a^2 + b^2 - c^2 = 0")

        self.play(Write(source), run_time=1.5)
        self.wait(0.5)

        # 3. 形状匹配变换：相同的子部分平滑过渡，不同的部分淡入淡出
        self.play(
            TransformMatchingShapes(source, target),
            run_time=2,
        )

        self.wait(0.5)
