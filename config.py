from manim import *
from manim_slides import Slide


config.background_color = BLACK
config["background_color"] = BLACK
Tex.set_default(color=WHITE)

class VectorSlide(Slide, VectorScene):
    pass

class LinearTransformationSlide(Slide, LinearTransformationScene):
    pass

class ThreeDSlide(Slide, ThreeDScene):
    pass

class LinearSystemTransformationSlide(LinearTransformationSlide):
    def setup(self):
        LinearTransformationSlide.setup(self)
        equation = VGroup(*[
            Tex("A"),
            Tex(r"$\vec{\textbf{x}}$"),
            Tex("="),
            Tex(r"$\vec{\textbf{b}}$"),
        ])
        equation.scale(1.5)
        self.equation = equation
        self.A, self.x, eq, self.v = equation.split()
        self.x.set_color(PINK)
        self.v.set_color(YELLOW)
        equa = VGroup(*[self.A,self.x,eq,self.v])
        equa.arrange(buff=0.1)
        equa.next_to(ORIGIN, LEFT).to_edge(UP)
        equa.add_background_rectangle()
        self.add_foreground_mobject(equa)
