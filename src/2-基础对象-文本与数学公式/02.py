from manim import *


class ParagraphDemo(Scene):
    def construct(self):
        # ── 1. 基础多行文本 ──
        p1 = Paragraph(
            "Manim 是一个动画引擎",
            "用于制作解释性数学视频。",
            "它使用 Python 来创建动画。",
            font_size=32,
        )
        self.play(Write(p1), run_time=1)
        self.play(p1.animate.to_edge(UP, buff=0.5), run_time=1)

        # ── 2. 调整行间距 ──
        tight = Paragraph(
            "行间距：0.5",
            "这很紧凑。",
            "非常紧密。",
            font_size=24,
            line_spacing=0.5,
            color=BLUE,
        )
        loose = Paragraph(
            "行间距：1.5",
            "这很宽松。",
            "有更多呼吸空间。",
            font_size=24,
            line_spacing=1.5,
            color=GREEN,
        )

        spacing_group = VGroup(tight, loose).arrange(RIGHT, buff=1.5)
        self.play(FadeIn(spacing_group, shift=UP * 0.2), run_time=1)
        self.play(FadeOut(spacing_group), run_time=1)

        # ── 3. 调整对齐方式 ──
        left_align = Paragraph(
            "左对齐文本。",
            "短行。",
            "一条更长的线来展示对齐效果。",
            font_size=24,
            alignment="left",
        )
        center_align = Paragraph(
            "居中对齐文本。",
            "短行。",
            "一条更长的线来展示对齐效果。",
            font_size=24,
            alignment="center",
        )
        right_align = Paragraph(
            "右对齐文本。",
            "短行。",
            "一条更长的线来展示对齐效果。",
            font_size=24,
            alignment="right",
        )

        align_group = VGroup(left_align, center_align, right_align).arrange(
            DOWN, buff=0.5
        )
        self.play(FadeIn(align_group), run_time=1)
        self.play(FadeOut(align_group), run_time=1)

        # ── 4. 结合局部样式 (t2c, t2g) ──
        fancy_p = Paragraph(
            "第一行：内容中等内容中等",
            "第二行：内容短",
            "第三行：内容较长内容较长内容较长",
            font_size=32,
            t2c={
                "第一行": RED,
                "第二行": BLUE,
                "第三行": GREEN,
            },
            t2g={
                "内容中等": (BLUE, GREEN),
                "内容短": (GREEN, RED),
                "内容较长": (RED, BLUE),
            },
        )
        self.play(Write(fancy_p), run_time=1)

        # ── 5. 退场 ──
        self.play(
            FadeOut(p1),
            FadeOut(fancy_p, shift=DOWN),
            run_time=1,
        )
