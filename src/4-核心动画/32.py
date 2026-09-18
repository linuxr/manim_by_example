from manim import *


class TransformMatchingTexDemo(Scene):
    def construct(self):
        # 1. 源公式：勾股定理
        eq1 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")

        # 2. 目标公式：移项后的形式
        eq2 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.play(Write(eq1), run_time=1.5)
        self.wait(0.5)

        # 3. 字符串匹配变换：相同 TeX 片段平滑过渡
        self.play(
            TransformMatchingTex(eq1, eq2),
            run_time=2,
        )

        self.wait(0.5)
