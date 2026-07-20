from manim import *


class MathTexDemo(Scene):
    def construct(self):
        # ── 1. 基础公式渲染 ──
        eq1 = MathTex(r"E = mc^2")
        self.play(Write(eq1))
        self.wait(0.5)
        self.play(eq1.animate.to_edge(UP, buff=0.8))

        # ── 2. 多参数拆分与局部动画 ──
        # 每个参数是一个独立的子对象，可通过索引访问
        eq2 = MathTex(r"a^2", r"+", r"b^2", r"=", r"c^2")
        self.play(Write(eq2))
        self.wait(0.5)

        # 分别对 a^2, b^2, c^2 进行着色
        self.play(
            eq2[0].animate.set_color(RED),
            eq2[2].animate.set_color(BLUE),
            eq2[4].animate.set_color(GREEN),
        )
        self.wait(0.5)
        self.play(FadeOut(eq2))

        # ── 3. 子串隔离与颜色映射 ──
        eq3 = MathTex(
            r"\int_0^1 x^2 \, dx = \frac{1}{3}",
            substrings_to_isolate=[r"\int_0^1", r"x^2", r"\frac{1}{3}"],
            tex_to_color_map={
                r"\int_0^1": YELLOW,
                r"x^2": TEAL,
                r"\frac{1}{3}": ORANGE,
            },
        )
        self.play(Write(eq3))
        self.wait(1)

        # ── 4. 退场 ──
        self.play(FadeOut(VGroup(eq1, eq3)))
