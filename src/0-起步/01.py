# 0. 🚀 起步: 01-Hello Manim
from manim import BLUE, Scene, Text


class HelloManim(Scene):
    def construct(self):
        hello = Text("Hello, Manim!", font_size=72, color=BLUE)
        self.add(hello)
        self.wait(2)
