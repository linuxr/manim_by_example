from manim import *


class BroadcastDemo(Scene):
    def construct(self):
        # 1. 一个圆环，作为被广播的对象
        circle = Circle(radius=1, color=TEAL, fill_opacity=0.4)

        self.add(circle)
        self.wait(0.5)

        # 2. 默认参数：5 个副本从中心扩散
        self.play(Broadcast(circle), run_time=2)

        # 3. 更多副本、更小的起始宽度、更紧凑的错位
        self.play(
            Broadcast(
                circle,
                n_mobs=8,
                initial_width=0.1,
                lag_ratio=0.1,
                run_time=2,
            )
        )

        self.wait(0.5)
