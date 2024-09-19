from manim import *
from manim_slides import Slide

from config import VectorSlide # Why is this here?


class Intro(Slide):
    def construct(self):

        Title = Text("Lineare Algebra", font_size=60)
        subtitle = Text("Eine Einführung", font_size=30, color=GREY).shift(DOWN)
        self.add(Title, subtitle)
        self.wait()

        Info = [
            "Maris, 6tes Semester Physik",
            "Schlagzeug, Klettern, Rathaus 10 in Clash of Clans",
            "Koordinator des Peer-Mentoring-Programms",
        ]

        texts = VGroup()
        for text in Info:
            texts.add(Text(text, font_size=30))

        texts.arrange(DOWN, buff=0.5)

        self.next_section()
        self.remove(Title, subtitle)
        Title = Text("Hallo!").to_edge(UP)
        self.play(Write(Title))
        for text in texts:
            text.to_edge(LEFT).shift(0.8*UP)
            self.play(Write(text))
            self.next_section()
        
        me = ImageMobject("src/images/Me.jpg").shift(4*LEFT+2*DOWN)
        self.add(me)
        self.wait()
        V1 = ImageMobject("src/images/bikepacking1.jpg").scale(0.3).shift(3.5*RIGHT+2*DOWN)
        self.add(V1)
        self.wait()
        self.next_section()
        V2 = ImageMobject("src/images/bikepacking2.jpg").scale(0.1).shift(3.5*RIGHT+2*DOWN)
        self.remove(V1)
        self.add(V2)
        self.wait()
        self.next_section()

        Title2 = Text("Bezüglich dieser Vorlesung").to_edge(UP)
        self.remove(me, V2)
        for text in texts:
            self.remove(text)
        self.play(Transform(Title, Title2))

        Info = [
            "Vortrag von 3h, aufgeteilt in 2x 1.5h",
            "-> keine Angst, wir werden Pausen machen",
            "Live-Stream über Zoom, Upload auf Moodle",
            "Mentimeter für Fragen und Feedback",
            "Gesamte Präsentation verfügbar unter",
            "people.physik.hu-berlin.der/~baierluc/LinearAlgebra"
        ]

        texts = VGroup()
        for text in Info:
            texts.add(Text(text, font_size=30))

        texts.arrange(DOWN, buff=0.5)
        self.next_section()

        self.play(Write(texts[0].to_edge(LEFT)),Write(texts[1].to_edge(LEFT)))
        self.next_section()
        self.play(Write(texts[2].to_edge(LEFT)))
        self.next_section()
        self.play(Write(texts[3].to_edge(LEFT)))
        self.next_section()
        self.play(Write(texts[4].to_edge(LEFT)), Write(texts[5].to_edge(LEFT)))
        self.next_section()
        for text in texts:
            self.remove(text)
        self.remove(Title)

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

        self.remove(Title,Subtitle)

        title = Text("Lineare Algebra").to_edge(UP)
        self.play(Write(title))

        Info = [
            "Fundamentaler Baustein für fast alle Bereiche der Mathematik",
            "Geometrie: Vektorräume, Rotationen, Spiegelungen",
            "Funktionalanalysis: unendlichdimensionale Vektorräume",
            "In den Naturwissenschaften: Um Naturgesetze zu beschreiben",
            "-> Auch nichtlineare Phänomene lassen sich oft linear approximieren",
        ]

        texts = VGroup()
        for text in Info:
            texts.add(Text(text, font_size=30))

        texts.arrange(DOWN, buff=0.5)

        for text in texts:
            text.to_edge(LEFT)
            self.play(Write(text))
            self.next_section()

        for text in texts:
            self.remove(text)
        self.remove(title)

        Today = Text("In diesem Vortrag").to_corner(UP+LEFT)
        self.play(Write(Today))
        self.next_section()

        LineareAbbildungen = Text("- Lineare Abbildungen", font_size=30)
        linAbSpannDim = Text("Lineare Abhängigkeit, Spann, Dimension", font_size=25)
        VisuelleVorstellung = Text("Visuelle Intuition", font_size=25)
        LineareGleichungssysteme = Text("- Lineare Gleichungssysteme", font_size=30)
        VisuelleVorstellung2 = Text("Visuelle Intuition", font_size=25)
        Gauß = Text("Gauß-Algorithmus", font_size=25)
        texts = VGroup(LineareAbbildungen, linAbSpannDim, VisuelleVorstellung, LineareGleichungssysteme, VisuelleVorstellung2, Gauß)
        texts.arrange(DOWN, buff=0.5)

        self.play(Write(texts[0].to_edge(LEFT)))
        self.next_section()
        self.play(Write(texts[1].to_edge(LEFT, buff=1)))
        self.next_section()
        self.play(Write(texts[2].to_edge(LEFT, buff=1)))
        self.next_section()
        self.play(Write(texts[3].to_edge(LEFT)))
        self.next_section()
        self.play(Write(texts[4].to_edge(LEFT, buff=1)))
        self.next_section()
        self.play(Write(texts[5].to_edge(LEFT, buff=1)))

        for text in texts:
            self.remove(text)

        linear = Text("linear?")
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
