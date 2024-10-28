
from manim import *

class TestScene(Scene):
    def construct(self):
        text = Text("Texto animado con manim!")
        self.play(Write(text))
        self.wait(2)
        