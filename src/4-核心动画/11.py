from manim import *


class GrowFromCenterDemo(Scene):
    def construct(self):
        # 创建一个带填充色的星形
        star = Star(
            n=5,
            outer_radius=1.5,
            color=GOLD,
            fill_opacity=0.9,
        )

        # 从中心向外生长
        self.play(
            GrowFromCenter(star),
            run_time=2,
        )
        self.wait(0.5)

        # 一组圆点依次从中心冒出
        dots = VGroup(
            *[Dot(radius=0.2, color=BLUE).shift(RIGHT * i) for i in range(-2, 3)]
        )
        self.play(
            LaggedStart(
                *[GrowFromCenter(d) for d in dots],
                lag_ratio=0.3,
            ),
            run_time=2.5,
        )
        self.wait(1)
