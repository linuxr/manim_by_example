from manim import *


class CreateUncreateExample(Scene):
    def construct(self):
        # 创建图形对象
        square = Square(color=BLUE, fill_opacity=0.3)
        circle = Circle(color=GREEN, fill_opacity=0.3)

        # 第一步：Create 逐笔绘制正方形
        self.play(Create(square), run_time=2)
        self.wait(0.5)

        # 第二步：Uncreate 逐笔擦除正方形
        self.play(Uncreate(square), run_time=2)
        self.wait(0.5)

        # 第三步：Create 逐笔绘制圆形
        self.play(Create(circle), run_time=2)
        self.wait(0.5)

        # 第四步：Uncreate 逐笔擦除圆形
        self.play(Uncreate(circle), run_time=2)
        self.wait(1)
