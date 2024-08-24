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
