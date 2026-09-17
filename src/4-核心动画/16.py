from manim import *


class BlinkDemo(Scene):
    def construct(self):
        # 创建一个圆形
        circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.8)

        # 让圆形闪烁一下
        self.play(
            Blink(circle),
            run_time=0.5,
        )
        self.wait(0.5)

        # 创建一个文本，让它闪烁
        text = Text("Blink!", font_size=96, color=GOLD)
        self.play(
            Blink(text),
            run_time=0.5,
        )
        self.wait(1)
