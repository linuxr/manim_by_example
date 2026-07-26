from manim import *


class WriteUnwriteExample(Scene):
    def construct(self):
        # 创建文字对象
        text = Text("Hello, Manim!", color=BLUE, font_size=72)

        # 第一步：模拟手写效果，让文字逐笔出现
        self.play(Write(text), run_time=2)
        self.wait(1)

        # 第二步：模拟擦除效果，让文字逐笔消失
        self.play(Unwrite(text), run_time=2)
        self.wait(1)

        # 第三步：再次书写，展示重复使用
        text2 = Text("Write & Unwrite", color=GREEN, font_size=72)
        self.play(Write(text2), run_time=2)
        self.wait(1)
        self.play(Unwrite(text2), run_time=2)
        self.wait(1)
