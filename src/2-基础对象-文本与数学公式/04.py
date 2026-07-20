from manim import *


class TitleDemo(Scene):
    def construct(self):
        # ── 1. 基础 Title（默认带全屏宽度下划线）──
        title1 = Title("Introduction to Manim")
        self.play(Write(title1))
        self.wait(1)
        self.play(FadeOut(title1))

        # ── 2. 自定义下划线样式 ──
        title2 = Title(
            "Customizing Titles",
            font_size=48,
            color=YELLOW,
            match_underline_width_to_text=True,  # 下划线宽度匹配文本
            underline_buff=MED_SMALL_BUFF,  # 调整下划线与文本的间距
        )
        # title2 是一个 VGroup: title2[0] 是 Text, title2[1] 是 Line
        title2[1].set_color(RED)  # 将下划线设置为红色

        self.play(Write(title2))
        self.wait(1)

        # ── 3. 配合正文内容排版 ──
        body = Text("This is the main content of the scene.", font_size=24, color=GRAY)
        body.next_to(title2, DOWN, buff=0.8)
        self.play(FadeIn(body, shift=UP * 0.2))
        self.wait(1)

        # ── 4. 无下划线的 Title ──
        self.play(FadeOut(VGroup(title2, body)))

        title3 = Title(
            "No Underline",
            include_underline=False,
            color=TEAL,
        )
        self.play(Write(title3))
        self.wait(1)

        # ── 5. 退场 ──
        self.play(FadeOut(title3))
