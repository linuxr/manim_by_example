from manim import *


class LetterByLetterDemo(Scene):
    def construct(self):
        # 创建文本对象
        text = Text("Hello, Manim!", font_size=72, color=BLUE)

        # 逐字添加（打字机效果）
        self.play(
            AddTextLetterByLetter(text, time_per_char=0.1),
            run_time=2,
        )
        self.wait(1)

        # 逐字删除（反向打字机效果）
        self.play(
            RemoveTextLetterByLetter(text, time_per_char=0.08),
            run_time=2,
        )
        self.wait(0.5)
