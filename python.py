from manim import *

class CreateCircle(Scene):
    def construct(self):
        circ = Circle()
        circ.set_fill(RED,opacity=0.5)
        self.play(Create(circ))