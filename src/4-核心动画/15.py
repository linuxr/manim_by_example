from manim import *


class ApplyWaveDemo(Scene):
    def construct(self):
        # 创建一个文本对象
        text = Text("Manim", font_size=96, color=BLUE)

        # 波浪从右向左传播
        self.play(
            ApplyWave(text, direction=LEFT),
            run_time=2,
        )
        self.wait(0.5)

        # 创建一行圆点，波浪从下向上传播，波纹更多
        dots = VGroup(
            *[Dot(radius=0.2, color=GOLD).shift(RIGHT * i) for i in range(-3, 4)]
        )
        self.play(
            ApplyWave(dots, direction=UP, amplitude=0.5, ripples=2),
            run_time=2,
        )
        self.wait(1)
