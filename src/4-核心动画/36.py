from manim import *


class MoveAlongPathDemo(Scene):
    def construct(self):
        # 1. 创建坐标轴和一条正弦曲线作为路径
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=6,
            y_length=3,
            axis_config={"include_tip": False},
        )
        graph = axes.plot(lambda x: np.sin(x), x_range=[-3, 3], color=BLUE)

        # 2. 创建一个黄色圆点，放在曲线的起点
        dot = Dot(color=YELLOW).move_to(axes.c2p(-3, np.sin(-3)))

        # 3. 创建轨迹追踪器，记录圆点走过的路径
        trace = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=3)

        self.add(axes, graph, dot, trace)
        self.wait(0.5)

        # 4. 圆点沿曲线匀速移动
        self.play(
            MoveAlongPath(dot, graph, rate_func=linear),
            run_time=3,
        )

        # 5. 圆点沿同一条曲线反向移动回去（使用反向的 rate_func）
        self.play(
            MoveAlongPath(dot, graph, rate_func=lambda t: 1 - t),
            run_time=2,
        )

        self.wait(0.5)
