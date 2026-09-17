from manim import *


class CursorTypingDemo(Scene):
    def construct(self):
        # 创建文本对象
        text = Text("Hello, Manim!", font_size=72, color=BLUE)

        # 创建光标（白色矩形块）
        cursor = Rectangle(
            color=GREY_A,
            fill_color=GREY_A,
            fill_opacity=1.0,
            height=1.0,
            width=0.08,
        )

        # 带光标的逐字输入
        self.play(
            TypeWithCursor(text, cursor, time_per_char=0.1),
            run_time=2,
        )
        self.wait(0.5)

        # 带光标的逐字删除
        self.play(
            UntypeWithCursor(text, cursor, time_per_char=0.06),
            run_time=1.5,
        )
        self.wait(0.5)
