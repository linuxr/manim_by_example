from manim import *


class FadeInOutDemo(Scene):
    def construct(self):
        # 创建一个文本对象
        text = Text("Hello, Manim!", font_size=72, color=BLUE)

        # 带位移的淡入
        self.play(
            FadeIn(text, shift=UP * 0.5),
            run_time=1.5,
        )
        self.wait(0.5)

        # 带缩放和位移的淡出
        self.play(
            FadeOut(text, shift=DOWN * 0.5, scale=0.5),
            run_time=1.5,
        )
        self.wait(0.5)
