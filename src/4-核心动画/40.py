from manim import *


class SuccessionExample(Scene):
    def construct(self):
        # 在矩形四个顶点各放一个点
        corners = [LEFT * 3, ORIGIN, UP * 2, LEFT * 3 + UP * 2]
        colors = [YELLOW, BLUE, GREEN, RED]
        dots = VGroup(
            *(
                Dot(point=corner, radius=0.12, color=color)
                for corner, color in zip(corners, colors)
            )
        )
        self.add(dots)
        self.wait(0.5)

        # Succession 依次播放：每个点移动到下一个顶点，接力绕矩形一圈
        # 注意：每个 .animate 必须作用在不同对象上；若对同一对象多次
        # .animate，会因反复覆盖共享的 target 而只保留最后一步
        self.play(
            Succession(
                dots[0].animate.move_to(dots[1]),
                dots[1].animate.move_to(dots[2]),
                dots[2].animate.move_to(dots[3]),
                dots[3].animate.move_to(dots[0]),
            )
        )
        self.wait(0.5)
