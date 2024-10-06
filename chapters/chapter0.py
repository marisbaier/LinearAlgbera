from manim import *
from manim_slides import Slide

from config import VectorSlide


class Intro(Slide):
    def construct(self):

        Title = Text("Lineare Algebra", font_size=60)
        subtitle = Text("Eine Einführung", font_size=30, color=GREY).shift(DOWN)
        self.add(Title, subtitle)
        self.wait()

        Info = [
            "Maris, irgendwas mit Physik",
            "Schlagzeug, Klettern, leider nur Rathaus 10 in Clash of Clans",
            r"kommt zum Peer-Mentoring-Programm, es ist \textit{sehr gut}",
        ]

        texts = VGroup()
        for text in Info:
            texts.add(Tex(text, font_size=30))

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
            "Gesamte Präsentation verfügbar unter:",
            "https://people.physik.hu-berlin.der/~baierluc/LinearAlgebra"
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

        Subtitle = Tex("...und wozu braucht man Vektorraeume?", font_size=25, color=GREY).shift(0.7*DOWN)
        self.play(Write(Subtitle, run_time=1.5))

        self.wait()
        self.next_slide()

        self.remove(Title,Subtitle)

        title = Text("Lineare Algebra").to_edge(UP)
        self.play(Write(title))

        Info = [
            "Fundamentaler Baustein für fast alle Bereiche der Mathematik",
            "Geometrie: Rotationen, Spiegelungen, Schnittpunkte",
            "Themenzweig Funktionalanalysis: ∞-dimensionale Vektorraeume",
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

        Today = Text("In diesem Vortrag", font_size=30).to_corner(UP+LEFT)
        self.play(Write(Today))
        self.next_section()

        LineareAbbildungen = Text("- Lineare Abbildungen", font_size=24)
        linAbSpannDim = Text("Lineare Abhängigkeit, Spann, Dimension", font_size=18)
        VisuelleVorstellung = Text("Visuelle Intuition", font_size=18)
        LineareGleichungssysteme = Text("- Lineare Gleichungssysteme", font_size=24)
        VisuelleVorstellung2 = Text("Visuelle Intuition", font_size=18)
        Gauß = Text("Gauß-Algorithmus", font_size=18)
        texts = VGroup(LineareAbbildungen, linAbSpannDim, VisuelleVorstellung, LineareGleichungssysteme, VisuelleVorstellung2, Gauß)
        texts.arrange(DOWN, buff=0.35).shift(0.5*UP)

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

        ImModul = Text("Im Modul LinA:", font_size=30).to_corner(UP+RIGHT).shift([-2.5,0,0])
        V1 = ImageMobject("src/images/LinA_Inhaltsverzeichnis.png")
        V1.scale(.8).to_edge(RIGHT).shift(0.2*DOWN+1.15*LEFT)
        self.next_section()
        self.play(Write(ImModul))
        self.add(V1)
        self.wait()

        self.next_section()
        self.remove(ImModul, V1, Today)
        for text in texts:
            self.remove(text)

        text = Text("Was wir nicht behandeln werden").to_edge(UP)

        Mengenlehre = Text("Mengenlehre", font_size=24).shift(3.5*LEFT+1.3*UP)
        RingeUndKoerper = Text("Ringe und Körper", font_size=24).shift(3.5*RIGHT+1.3*UP)
        Vektorraeume = Text("Vektorraeume (formal):", font_size=24).shift(0.55*UP)
        FormaleDefinitionen = ImageMobject("src/images/VektorraumDefinition.png").scale(0.85).shift(1.2*DOWN)

        self.play(Write(text))
        self.play(Write(Mengenlehre), Write(RingeUndKoerper))
        self.next_section()
        self.play(Write(Vektorraeume))
        self.add(FormaleDefinitionen)
        self.wait()

        sehrvielmehr = Text("...und sehr, sehr (!) viel mehr", font_size=24).to_edge(DOWN+RIGHT)
        self.next_section()
        self.play(Write(sehrvielmehr))

        self.next_section()
        self.remove(text,Mengenlehre,RingeUndKoerper,Vektorraeume,FormaleDefinitionen,sehrvielmehr,Today)

        linear = Text("linear?")
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

        self.next_section()
        self.wait()

        self.play(FadeOut(axis), FadeOut(linear_func))

class ImportantDefinitions(Slide):
    def construct(self):
        bulletpoints = VGroup(*[Text(a) for a in [
            "Funktionsgleichung:",
            "Zuordnung:",
            "Noch präziser:"
        ]])
        bulletpoints.arrange(DOWN, buff=2).shift(UP*0.5).scale(0.8)

        for (point, formula) in zip(bulletpoints, [
            Tex(r'$f(x)=x^2$'),
            Tex(r'$x \mapsto x^2$'),
            Tex(r'$f: A\to B \quad x \mapsto x^2$')
        ]):
            formula.next_to(point, DOWN)
            self.play(Write(point), Write(formula))
            self.next_section()
        twovectors = VGroup(*[
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([-1.7,-3.1,0],[-1.35,-2.7,0]).set_color(YELLOW),
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([0.3,-3.1,0],[-0.05,-2.7,0]).set_color(BLUE),
            ])
        """ self.play(Create(e1)) """
        Definitionsbereich = Text("Definitionsbereich", font_size=14, color=YELLOW).move_to(twovectors[0].get_start()+[0,-0.2,0])
        Zielmenge = Text("Zielmenge", font_size=14, color=BLUE).move_to(twovectors[1].get_start()+[0,-0.2,0])
        self.play(Create(twovectors[0]), Create(Definitionsbereich))
        self.next_section()
        self.play(Create(twovectors[1]), Create(Zielmenge))
        self.wait()

class ImportantConcepts(Slide):
    def construct(self):
        definition = Tex(r'Wenn z.B.: $f:x\mapsto x^2$, dann:').shift(UP)
        math = Tex(r'$f(\mathbb{R})=\mathbb{R}_+$')
        explain = Tex(r'$:=\{x\in \mathbb{R} \mid x\geq 0\}$')
        group = VGroup(math,explain).arrange()
        group.shift(0.6*DOWN)

        self.play(Write(definition))
        self.next_section()
        self.play(Write(group[0]))
        self.wait()
        self.next_section()
        self.play(Write(group[1]))

        text = Tex(r'Das \glqq Bild\grqq{} der Menge $\mathbb{R}$ unter \\ der Abbildung $f:x\mapsto x^2$ sind \\ die positiven reellen Zahlen!')
        text.shift(2.2*DOWN).scale(0.7)
        self.next_section()
        self.play(Write(text))

        self.next_section()
        self.remove(group[0], group[1], text)
        Frage = Tex(r'Was ist das \textit{Bild} von $5$ unter $f$?').scale(0.8).shift(DOWN*0.8)
        Antwort = Tex(r'$\Rightarrow$ 25')
        Antwort.next_to(Frage,DOWN)
        self.play(Write(Frage))
        self.next_section()
        self.play(Write(Antwort))

        self.wait()

class VectorAddition(VectorSlide):
    def construct(self):
        numberplane = NumberPlane(faded_line_ratio=2)
        self.add(numberplane)
        self.vector1_color = MAROON_C
        self.vector2_color = BLUE
        self.vector1_label = "v"
        self.vector2_label = "w"

        self.next_slide()

        v = Vector([1,2], color=self.vector1_color)
        self.play(Create(v))

        Physikmensch = ImageMobject("src/images/Physikmensch.png").scale(0.85).shift(5*LEFT+2*DOWN)
        self.add(Physikmensch)

        w = Vector([2,-1], color=MAROON_C).shift([-4,2,0])
        label = Tex(r'$\vec{v}$').next_to(w,(UP+RIGHT)/4).shift(LEFT+DOWN*0.3)
        label.set_color(MAROON_C).scale(1.2).add_background_rectangle()
        self.play(Transform(v,w))
        self.play(Write(label))
        group = VGroup(w,label)

        self.next_section()
        Wasserhahn = ImageMobject("src/images/WasserHahnMitZweiGriffen.jpg").scale(0.6)
        self.add(Wasserhahn)
        self.wait()

        self.next_section()
        Informatikmensch = ImageMobject("src/images/Informatiker.png").scale(0.85).shift(2*DOWN)
        Vektor = Matrix([[3],[1]]).set_color(MAROON_C).shift(1*UP).set_z_index(30).add_background_rectangle()
        Vektor.next_to(Informatikmensch,UP,0.5)
        self.add(Informatikmensch)
        self.remove(Wasserhahn, v)
        self.play(group.animate.shift(DOWN+2*LEFT))
        self.wait(0.3)
        self.play(Create(Vektor))
        self.wait()

        Mathemensch = ImageMobject("src/images/Bibbrainmath.jpg").scale(0.35).shift(2*DOWN+5*RIGHT)
        VektorraumDef = ImageMobject("src/images/VektorraumDefinition.png").scale(0.6).to_edge(RIGHT).shift(0.5*UP)
        self.add(Mathemensch, VektorraumDef)
        self.wait()


        """ v1_label = self.label_vector(
            v, self.vector1_label, color = self.vector1_color,
        )

        w = Vector([2,2], color=self.vector1_color, stroke_width=2)
        self.play(Create(v))

        v1_label = self.label_vector(
            v, self.vector1_label, color = self.vector1_color,
        ) """
