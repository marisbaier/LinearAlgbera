from manim import *
from manim_slides import Slide
from manim.opengl import * # TODO: Check if this is necessary

from config import VectorSlide


class Intro(Slide):
    def construct(self):

        V1 = ImageMobject("src/images/BSc_2022_Studienplan.jpg")
        V2 = ImageMobject("src/images/Studienverlaufsplan.png")
        V3 = ImageMobject("src/images/StudienverlaufsplanLMU.png")
        zoom = ImageMobject("src/images/zoom.png")

        V1.scale(0.18)
        V2.scale(0.45)
        V3.scale(0.5)
        zoom.scale(1)

        V1.to_corner(LEFT + UP, buff=1)
        V2.to_corner(RIGHT + UP, buff=1)
        V3.to_corner(LEFT + DOWN, buff=1)

        self.add(V1, V2, V3, zoom)

        self.wait()
        self.next_slide()

        e1 = Ellipse(2,2.2, stroke_width=20).shift([0.5,-0.2,0])
        e2 = Ellipse(1.5,0.5, stroke_width=20).move_to([-5.5,1.15,0])
        e3 = Ellipse(1,0.7, stroke_width=20).move_to([4.55,2.5,0])
        e4 = Ellipse(1.4,0.7, stroke_width=20).move_to([-4.9,-2.1,0])

        ellipses = VGroup()
        ellipses.add(e1,e2,e3,e4)
        self.add(ellipses)

        self.wait()
        self.next_slide()

        self.play(FadeOut(V1,V2,V3,zoom,ellipses))
        self.wait(0.2)

        Title = Tex("Was ist Lineare Algebra?")
        self.play(Write(Title))

        self.wait()
        self.next_slide()

        Subtitle = Tex("...und wozu braucht man Vektorräume?", font_size=25, color=GREY).shift(0.7*DOWN) # , opacity=0.7
        self.play(Write(Subtitle, run_time=1.5))

        self.wait()
        self.next_slide()

        linear = Text("linear?")
        self.remove(Title,Subtitle)
        self.wait(0.2)
        self.play(Write(linear))

        self.wait()
        self.next_slide()

        text = VGroup()
        text.add(
            Text("linearer Operator", color=BLUE, font_size=30).move_to([3.5,1,0]),
            Text("lineare Gleichungen", color=BLUE, font_size=30).move_to([-3.7,2,0]),
            Text("linearer Faltungsfilter", color=BLUE, font_size=30).move_to([3,-1,0]),
            Text("linearer Verband", color=BLUE, font_size=30).move_to([-3,-1,0]),
            Text("lineare Abbildung", color=BLUE, font_size=30).move_to([1,2,0]),
            Text("lineare Ordnung", color=BLUE, font_size=30).move_to([1,-2,0]),
            Text("lineares Funktional", color=BLUE, font_size=30).move_to([4,3,0]),
            Text("linearer Raum", color=BLUE, font_size=30).move_to([-2,1,0]),
            Text("linearer Code", color=BLUE, font_size=30).move_to([-0.5,3,0]),
            Text("lineare Regression", color=BLUE, font_size=30).move_to([-3.5,-2.5,0]),
            Text("lineare Separierbarkeit", color=BLUE, font_size=30).move_to([-4.5,3.3,0]),
            Text("lineare Relation", color=BLUE, font_size=30).move_to([4,-3,0]),
            Text("lineare Optimierung", color=BLUE, font_size=30).to_edge()
            )
        self.play(FadeIn(text))

        self.wait()
        self.next_slide()

        self.play(FadeOut(text), linear.animate.move_to([0,3,0]))

        axis = Axes(x_range=[-2,6], y_range=[-1,4])
        #axes1 = Axes(x_range=[-.5,3], y_range=[-.5,3], x_length=3, y_length=3).shift([-4,0,0])
        #axes2 = Axes(x_range=[-.5,3], y_range=[-.5,3], x_length=3, y_length=3).shift([4,0,0])

        #self.play(Create(axes1), Create(axes2))
        self.play(Create(axis))
        self.wait()

        linear_func = axis.plot(
            lambda t: 0.7*t,
            color=RED,
        )

        self.play(Write(linear_func))

        self.wait()
        self.next_slide()

        affine_func = axis.plot(
            lambda t: 0.7*t+1,
            color=RED,
        )
        self.play(ReplacementTransform(linear_func,affine_func))

        self.wait()
        self.next_slide()

        linear_func = axis.plot(
            lambda t: 0.7*t,
            color=RED,
        )
        self.play(ReplacementTransform(affine_func,linear_func))

        self.wait()

        self.play(FadeOut(axis), FadeOut(linear_func))

class VectorAddition(VectorSlide):
    def construct(self):
        numberplane = NumberPlane(faded_line_ratio=2)
        self.add(numberplane)
        self.vector1_color = MAROON_C
        self.vector2_color = BLUE
        self.vector1_label = "v"
        self.vector2_label = "w"

        self.next_slide()

        v = Vector([1,2], color=self.vector1_color, stroke_width=2)
        self.play(Create(v))

        v1_label = self.label_vector(
            v, self.vector1_label, color = self.vector1_color,
        )

        w = Vector([2,2], color=self.vector1_color, stroke_width=2)
        self.play(Create(v))

        v1_label = self.label_vector(
            v, self.vector1_label, color = self.vector1_color,
        )
