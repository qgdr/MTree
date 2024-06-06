from manim import *

class DirichletNeumann(Scene):
    def construct(self):
        c1, c2 = Circle(radius=1, color=RED), Circle(radius=2, color=BLUE)
        g1, g2 = Tex(r"$\Gamma_1$", color=RED).next_to(c1, RIGHT), Tex(r"$\Gamma_2$", color=BLUE).next_to(c2, RIGHT)
        self.add(c1, c2, g1, g2)
