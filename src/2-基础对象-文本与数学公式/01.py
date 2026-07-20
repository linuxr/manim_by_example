from manim import *


class TextDemo(Scene):
    def construct(self):
        # ── 1. 基础文本 ──
        title = Text("Manim Text", font="Arial", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP, buff=0.5))

        # ── 2. 字体与样式 ──
        plain = Text("Hello World", font_size=36)
        bold = Text("Bold Text", font_size=36, weight=BOLD)
        italic = Text("Italic Text", font_size=36, slant=ITALIC)

        styles = VGroup(plain, bold, italic).arrange(DOWN, buff=0.3)
        self.play(FadeIn(styles, shift=RIGHT * 0.3))
        self.wait()
        self.play(FadeOut(styles))

        # ── 3. 渐变色 ──
        gradient_text = Text(
            "Gradient Colors",
            font_size=42,
            gradient=(RED, YELLOW, GREEN, BLUE),
        )
        self.play(Write(gradient_text))
        self.wait()
        self.play(FadeOut(gradient_text))

        # ── 4. t2* 局部样式 ──
        # t2c: 局部颜色
        t2c_text = Text(
            "Hello Manim World",
            font_size=36,
            t2c={"Hello": RED, "Manim": GREEN, "World": BLUE},
        )
        # t2w: 局部粗体
        t2w_text = Text(
            "Hello Manim World",
            font_size=36,
            t2w={"Manim": BOLD},
        )
        # t2s: 局部斜体
        t2s_text = Text(
            "Hello Manim World",
            font_size=36,
            t2s={"Hello": ITALIC, "World": ITALIC},
        )

        t2_group = VGroup(t2c_text, t2w_text, t2s_text).arrange(DOWN, buff=0.3)
        self.play(FadeIn(t2_group, shift=UP * 0.2))
        self.wait(2)
        self.play(FadeOut(t2_group))

        # ── 5. 组合局部样式 + 渐变 ──
        fancy = Text(
            "Style is Limitless",
            font_size=42,
            t2c={"Style": PINK, "Limitless": GOLD},
            t2w={"Limitless": BOLD},
            t2s={"Style": ITALIC},
        )
        self.play(Write(fancy))
        self.wait()

        # ── 6. Transform 动画 ──
        target = Text(
            "Create Something Amazing",
            font_size=42,
            gradient=(PURPLE, TEAL),
        )
        self.play(Transform(fancy, target))
        self.wait()

        # ── 7. 退场 ──
        self.play(
            FadeOut(title),
            FadeOut(fancy, shift=DOWN),
        )
