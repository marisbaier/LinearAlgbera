from manim import *
from manim_editor import PresentationSectionType
from manim.opengl import *
config.background_color = DARKER_GRAY
config["background_color"] = DARKER_GRAY
Tex.set_default(color=WHITE)

class Intro(Scene):
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
        self.next_section()

        e1 = Ellipse(2,2.2, stroke_width=20).shift([0.5,-0.2,0])
        e2 = Ellipse(1.5,0.5, stroke_width=20).move_to([-5.5,1.15,0])
        e3 = Ellipse(1,0.7, stroke_width=20).move_to([4.55,2.5,0])
        e4 = Ellipse(1.4,0.7, stroke_width=20).move_to([-4.9,-2.1,0])

        ellipses = VGroup()
        ellipses.add(e1,e2,e3,e4)
        self.add(ellipses)

        self.wait()
        self.next_section()

        self.play(FadeOut(V1,V2,V3,zoom,ellipses))
        self.wait(0.2)

        Title = Tex("Was ist Lineare Algebra?")
        self.play(Write(Title))

        self.wait()
        self.next_section()

        Subtitle = Tex("...und wozu braucht man Vektorräume?", font_size=25, color=GREY, opacity=0.7).shift(0.7*DOWN)
        self.play(Write(Subtitle, run_time=1.5))

        self.wait()
        self.next_section()

        linear = Text("linear?")
        self.remove(Title,Subtitle)
        self.wait(0.2)
        self.play(Write(linear))

        self.wait()
        self.next_section()

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
        self.next_section()

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
        self.next_section()

        affine_func = axis.plot(
            lambda t: 0.7*t+1,
            color=RED,
        )
        self.play(ReplacementTransform(linear_func,affine_func))

        self.wait()
        self.next_section()

        linear_func = axis.plot(
            lambda t: 0.7*t,
            color=RED,
        )
        self.play(ReplacementTransform(affine_func,linear_func))

        self.wait()

        self.play(FadeOut(axis), FadeOut(linear_func))
0