from manim import *


class ShowPassingFlashDemo(Scene):
    def construct(self):
        # 1. 一条下划线，作为扫过的路径
        line = Underline(Text("Path", font_size=48)).set_color(BLUE)

        # 2. 一组路径，用于同时扫过
        paths = VGroup(
            Line(LEFT * 3 + UP * 1.5, RIGHT * 3 + UP * 1.5),
            Line(LEFT * 3 + DOWN * 1.5, RIGHT * 3 + DOWN * 1.5),
        ).set_color(GREY)

        self.add(line, paths)
        self.wait(0.5)

        # 3. 光带扫过下划线，默认参数
        self.play(ShowPassingFlash(line))

        # 4. 更宽的光带，青色，更粗，扫过下划线
        self.play(
            ShowPassingFlash(
                line.copy().set_color(TEAL).set_stroke(width=6),
                time_width=0.5,
            )
        )

        # 5. 光带同时扫过两条路径
        self.play(ShowPassingFlash(paths.copy().set_color(YELLOW)))

        self.wait(0.5)
