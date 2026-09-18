from manim import *


class CircumscribeDemo(Scene):
    def construct(self):
        # 1. 展示一个数学公式作为被环绕的目标
        formula = MathTex(r"e^{i\pi} + 1 = 0")
        self.play(Write(formula))

        # 2. 默认矩形轮廓，黄色，标准间距
        self.play(Circumscribe(formula, color=YELLOW))

        # 3. 圆形轮廓，间距更大，颜色为青色
        self.play(Circumscribe(formula, shape=Circle, color=TEAL, buff=0.4))

        # 4. 矩形轮廓，更紧凑的间距，更连贯的绘制效果
        self.play(Circumscribe(formula, buff=0.05, time_width=0.5))

        self.wait(0.5)
