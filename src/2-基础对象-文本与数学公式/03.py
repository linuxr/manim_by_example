from manim import *


class MarkupTextDemo(Scene):
    def construct(self):
        # ── 1. 基础标记标签 ──
        basic = MarkupText(
            "<b>Bold</b> <i>Italic</i> <u>Under</u> <s>Strike</s>",
            font_size=36,
        )
        self.play(Write(basic))
        self.wait(0.5)
        self.play(basic.animate.to_edge(UP, buff=0.5).scale(0.7))

        # ── 2. span 标签：颜色与背景色 ──
        colors = MarkupText(
            '<span foreground="red">Red</span> text &amp; '
            '<span background="yellow" foreground="black">Highlight</span>',
            font_size=32,
        )
        self.play(FadeIn(colors, shift=UP * 0.2))
        self.wait(0.5)
        self.play(FadeOut(colors))

        # ── 3. 上下标与字号 ──
        sub_super = MarkupText(
            'H<sub>2</sub>O is <span size="x-large">Water</span>' ", E=mc<sup>2</sup>",
            font_size=32,
        )
        self.play(Write(sub_super))
        self.wait(0.5)
        self.play(FadeOut(sub_super))

        # ── 4. 综合应用：模拟代码高亮 ──
        code = MarkupText(
            '<span font="Monospace" foreground="gray">>>> </span>'
            '<b>print</b>(<span foreground="orange">"Manim"</span>)',
            font_size=34,
        )
        self.play(FadeIn(code, scale=0.8))
        self.wait(1)

        # ── 5. 退场 ──
        self.play(FadeOut(VGroup(basic, code)))
