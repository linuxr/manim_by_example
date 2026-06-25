from manim import BLUE, LEFT, RED, RIGHT, YELLOW, Create, Ellipse, Scene


class EllipseDemo(Scene):
    def construct(self):
        # 创建三个不同尺寸和颜色的椭圆
        ellipse_small = Ellipse(width=2, height=1, color=RED, fill_opacity=0.5).shift(
            RIGHT * 0.5
        )

        ellipse_medium = Ellipse(width=4, height=2, color=BLUE, stroke_width=8).shift(
            LEFT * 3
        )

        # 当 width == height 时，即为圆形
        ellipse_circle = Ellipse(width=2, height=2, color=YELLOW).shift(RIGHT * 3)

        # 动画展示
        self.play(Create(ellipse_medium))
        self.play(Create(ellipse_small))
        self.play(Create(ellipse_circle))
        self.wait()

        # 演示变换：将椭圆拉伸为圆
        self.play(ellipse_small.animate.stretch_to_fit_height(2), run_time=1.5)
        self.wait()
