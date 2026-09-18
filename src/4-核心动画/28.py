from manim import *


class RestoreDemo(Scene):
    def construct(self):
        # 1. 创建一个正方形，并保存其初始状态
        square = Square(color=BLUE, fill_opacity=0.5)
        square.save_state()

        self.play(Create(square), run_time=1)
        self.wait(0.3)

        # 2. 对正方形做一系列变换：变色、移位、缩放、旋转
        self.play(
            square.animate.set_color(PURPLE)
            .set_opacity(0.3)
            .scale(1.8)
            .shift(RIGHT * 2 + UP * 1),
            run_time=1.5,
        )
        self.play(
            square.animate.rotate(PI / 4).shift(DOWN * 1.5),
            run_time=1.5,
        )

        # 3. 一键恢复：回到最初保存的蓝色、原始大小和位置
        self.play(Restore(square), run_time=2)

        self.wait(0.5)
