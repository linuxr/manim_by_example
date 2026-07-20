from manim import *


class BulletedListDemo(Scene):
    def construct(self):
        # ── 1. 基础列表 ──
        bl = BulletedList(
            "Python",
            "JavaScript",
            "Rust",
            "Go",
            font_size=36,
        )

        self.play(Write(bl))
        self.wait(1)

        # ── 2. 高亮特定项（通过索引）──
        # 高亮第 2 项（索引 1：JavaScript），其他项变淡
        self.play(bl.animate.fade_all_but(1, opacity=0.2))
        self.wait(1)

        # ── 3. 高亮特定项（通过索引）──
        # 高亮第 3 项（索引 2：Rust）
        self.play(bl.animate.fade_all_but(2, opacity=0.2))
        self.wait(1)

        # ── 4. 恢复所有项 ──
        self.play(bl.animate.set_opacity(1))
        self.wait(0.5)

        # ── 5. 退场 ──
        self.play(FadeOut(bl))
