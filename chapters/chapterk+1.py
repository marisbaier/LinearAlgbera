from manim import *
from manim_slides import Slide
import itertools as it


class Linearitaet(Slide):
    def construct(self):
        title = Tex("Aus der Vorlesung zur Integration:")
        title.set_color(YELLOW).to_corner(UP+LEFT)
        self.play(Write(title))
        self.next_section()
        Homogenitaet = Tex(r'$\int\lambda\cdot F(x)\, dx\quad \,\,\,\,\,=\lambda\cdot \int F(x) \, dx$')
        Homogenitaet.shift(title.get_bottom()+1.3*DOWN).to_edge(LEFT)
        Additivitaet = Tex(r'$\int F(x)+g(x)\, dx=\int F(x)\, dx+\int g(x)\, dx$')
        Additivitaet.shift(Homogenitaet.get_bottom()+DOWN).to_edge(LEFT)
        Klammer = Tex(r'$\}$').scale(3.7).shift(Additivitaet.get_right()+0.7*UP+0.8*RIGHT)
        self.play(Write(Homogenitaet), Write(Additivitaet))
        self.next_section()
        Linearitaet = Tex(r'\glqq Linearität\grqq{}')
        Linearitaet.shift(Klammer.get_right()+1.7*RIGHT)
        self.play(Write(Klammer), Write(Linearitaet))
        Aussage = Tex(r'$\Rightarrow$'+" linear = homogen + additiv")
        Aussage.shift(1.6*DOWN)
        Aussage.set_color(RED)
        self.next_section()
        self.play(Write(Aussage))
        self.wait()

        self.next_section()
        self.remove(Aussage, Linearitaet, Klammer, Homogenitaet, Additivitaet)

        title = Tex("Das Integral erfüllt also:").to_edge(LEFT).shift(2*UP)
        Homogenitaet = Tex(r'$F(\lambda x)=\lambda F(x)$').shift(0.7*UP)
        Additivitaet = Tex(r'$F(a+b)=F(a)+F(b)$').shift(0.7*DOWN)

        self.play(Write(title), Write(Homogenitaet), Write(Additivitaet))
        
        subtitle = Tex(r'Ist das dieselbe Linearität, die wir schon kennen?')
        subtitle.shift(2*DOWN).to_edge(LEFT)
        subtitle.set_color(RED)

        self.play(Write(subtitle))
        self.next_section()

        Aussage2 = Tex(r'(Linien bleiben Linien, der Ursprung bleibt...)').scale(0.75)
        Aussage2.shift(2.65*DOWN+1.6*RIGHT)
        self.play(Write(Aussage2))
        self.wait()

class BeweisHinrichtung(Slide):
    def construct(self):
        title = Tex("Zu zeigen:")
        title.to_corner(UP+LEFT)
        self.play(Write(title))

        Homogenitaet = Tex(r'$F(\lambda x)=\lambda F(x)$').shift(0.45*UP+3.7*RIGHT)
        Additivitaet = Tex(r'$F(a+b)=F(a)+F(b)$').shift(0.45*DOWN+3.7*RIGHT)
        self.next_section()

        self.play(Write(Homogenitaet), Write(Additivitaet))

        equiv = Tex(r'$\Leftrightarrow$')
        text1 = Tex(r'Linien bleiben Linien,').shift(0.45*UP+3.7*LEFT)
        text2 = Tex(r'Ursprung bleibt fixed.').shift(0.45*DOWN+3.7*LEFT)

        self.play(Write(equiv), Write(text1), Write(text2))

        text2strich = Tex(r'$F(0)=0$').shift(0.45*DOWN+3.7*LEFT)
        text1strich = Tex(r'$F(a+t b)=c+t d$').shift(0.45*UP+3.7*LEFT)
        self.next_section()

        self.play(Transform(text2,text2strich))
        self.next_section()
        self.play(Transform(text1,text1strich))

        Quantoren = Tex(r'$\forall a,b\in \mathbb{R}^n\, \exists c,d\in\mathbb{R}^n:')
        Quantoren.next_to(text2strich,UP)
        self.next_section()
        self.play(Write(Quantoren))
        self.next_section()
        self.remove(Quantoren)

        self.next_section()
        Hinrichtung = Tex("Wir zeigen zuerst die eine Richtung:")
        Hinrichtung.to_corner(UP+LEFT)
        newFolgepfeil = Tex(r'$\Rightarrow$').shift(0.45*UP+1.5*LEFT)
        t0 = Tex(r'$t=0$').scale(0.6)
        t0.move_to(newFolgepfeil.get_top()+0.3*UP)
        self.remove(text1strich,text2strich,Homogenitaet, Additivitaet)
        self.play(Transform(title,Hinrichtung), Transform(equiv,newFolgepfeil), text1.animate.shift(0.5*LEFT), text2.animate.shift(0.5*LEFT))
        
        self.next_section()
        self.play(Write(t0))

        Zwischenschritt = Tex(r'$F(a)=c$').next_to(newFolgepfeil,RIGHT,0.5)
        self.next_section()
        self.play(Write(Zwischenschritt))

        Folgepfeil = newFolgepfeil.copy().shift(1.2*DOWN).rotate(-0.4)
        self.next_section()
        a0 = Tex(r'$a=0$').scale(0.6)
        a0.move_to(Folgepfeil.get_top()+0.4*UP)
        self.play(Write(Folgepfeil), Write(a0))

        Homogenitaet = Tex(r'$F(tb)=c+td$')
        Homogenitaet.next_to(Folgepfeil,RIGHT,0.5).shift(0.35*DOWN)
        self.next_section()
        self.play(Write(Homogenitaet))

        Pfeil = Arrow(start=Homogenitaet.get_top(), end=Zwischenschritt.get_bottom())
        Pfeil.shift([0.6,0,0]).set_color(YELLOW).rotate(-0.4)
        self.next_section()
        self.play(Create(Pfeil))

        Homogenitaet2 = Tex(r'$=F(0)+td$').next_to(Homogenitaet)
        self.next_section()
        self.play(Write(Homogenitaet2))

        Homogenitaet3 = Tex(r'$=td$').next_to(Homogenitaet2).shift(0.1*UP)
        self.next_section()
        self.play(Write(Homogenitaet3))

        Folgepfeil3 = Tex(r'$\Rightarrow$').next_to(Homogenitaet,DOWN).shift(0.5*LEFT+0.5*DOWN)
        t1 = Tex(r'$t=1$').scale(0.6)
        t1.next_to(Folgepfeil3,UP)
        Homogenitaet4 = Tex(r'$F(tb)=tF(b)$')
        Homogenitaet4.next_to(Folgepfeil3, buff=0.45)
        self.next_section()
        self.play(Write(Folgepfeil3), Write(t1), Write(Homogenitaet4))

        rect = Rectangle(height=0.8, width=3.35).shift([2.4,-2.225,0])
        rect.set_color(YELLOW)
        self.next_section()
        self.play(Create(rect))

        textAdditivitaet = Tex("Homogenität!").scale(0.8)
        textAdditivitaet.set_color(YELLOW)
        textAdditivitaet.next_to(rect, DOWN)
        self.next_section()
        self.play(Write(textAdditivitaet))

        self.next_section()
        self.remove(Homogenitaet, Homogenitaet2, Homogenitaet3, a0, Folgepfeil, t1, Folgepfeil3, Pfeil)
        self.play(rect.animate.shift([1,5.1,0]), Homogenitaet4.animate.shift([1,5.1,0]), textAdditivitaet.animate.shift([1,5.1,0]))

        Folgepfeil = newFolgepfeil.copy().shift(1.2*DOWN).rotate(-0.4)
        self.next_section()
        a0 = Tex(r'$t=1$').scale(0.6)
        a0.move_to(Folgepfeil.get_top()+0.4*UP)
        self.play(Write(Folgepfeil), Write(a0))

        eq = Tex(r'$F(a+b)=c+d$').next_to(Folgepfeil,RIGHT,0.5).shift(0.35*DOWN)
        self.next_section()
        self.play(Write(eq))
        
        eq2 = Tex(r'$=F(a)+d$').next_to(eq)
        self.next_section()
        self.play(Write(eq2))

        Folgepfeil4 = Tex(r'$\Rightarrow$').next_to(eq,DOWN).shift(0.45*LEFT+0.5*DOWN)
        a0 = Tex(r'symm.').scale(0.6)
        a0.next_to(Folgepfeil4,0.75*UP)
        eq3 = Tex(r'$F(a+b)=F(a)+F(b)$')
        eq3.next_to(Folgepfeil4, buff=0.5)
        self.next_section()
        self.play(Write(Folgepfeil4), Write(a0), Write(eq3))

        rect = Rectangle(height=0.8, width=5.5).shift([3.75,-2.225,0])
        rect.set_color(YELLOW)
        self.next_section()
        self.play(Create(rect))

        textAdditivitaet = Tex("Additivität!").scale(0.8)
        textAdditivitaet.set_color(YELLOW)
        textAdditivitaet.next_to(rect, DOWN)
        self.next_section()
        self.play(Write(textAdditivitaet))

        self.wait()

class BeweisRueckrichtung(Slide):
    def construct(self):
        title = Tex("Nun die Rückrichtung:").to_edge(LEFT+UP)
        self.play(Write(title))

        Homogenitaet = Tex(r'$F(\lambda x)=\lambda F(x)$').shift(0.45*UP+3.7*RIGHT)
        Additivitaet = Tex(r'$F(a+b)=F(a)+F(b)$').shift(0.45*DOWN+3.7*RIGHT)
        text1 = Tex(r'$F(a+t b)=c+t d$').shift(0.45*UP+3.7*LEFT)
        text2 = Tex(r'$F(0)=0$').shift(0.45*DOWN+3.7*LEFT)
        arrow = Tex(r'$\Leftarrow$')

        self.play(Write(Homogenitaet), Write(Additivitaet), Write(text1), Write(text2))
        self.play(Write(arrow))

        self.next_section()

        implication = Tex(r'$\Leftarrow$').next_to(Additivitaet,LEFT)
        self.remove(text1,text2)
        self.play(Transform(arrow, implication))
        
        LBL1 = Tex(r'$=F(a+\lambda b)$').next_to(implication,LEFT)
        LBL2 = Tex(r'$F(\lambda b)$').next_to(LBL1,LEFT)
        LBL3 = Tex(r'$F(a)+$').next_to(LBL2,LEFT)
        self.next_section()
        self.play(Write(LBL1), Write(LBL2), Write(LBL3))

        line = Line(start=Homogenitaet.get_left()+[-0.5,0,0], end=Homogenitaet.get_left()+[-5,0,0])
        line2 = Arrow(start=line.get_left()+[0,0.25,0], end=line.get_end()+[0,-0.7,0])
        line.set_color(YELLOW)
        line2.set_color(YELLOW)
        self.next_section()
        self.play(Create(line), Create(line2))

        newLBL2 = Tex(r'$\lambda F(b)$').next_to(LBL1,LEFT)
        self.next_section()
        self.play(Transform(LBL2, newLBL2))

        Definiere = Tex(r'mit $c:=F(a),\, d:=F(b)$').next_to(LBL3,DOWN,0.7).to_edge(LEFT).scale(0.7)
        self.next_section()
        self.play(Write(Definiere))
        result = Tex(r'$\Rightarrow \quad F(a+\lambda b)=c+\lambda d$').next_to(Definiere,DOWN,0.45)
        self.next_section()
        rect = Rectangle(height=0.8, width=4.6).shift([-3.4,-2.5,0])
        rect.set_color(YELLOW)
        self.play(Write(result), Create(rect))

        self.wait()

class NewDefinition(Slide):
    def construct(self):
        # Draw a box for the definition
        rect = Rectangle(height=2.8, width=9).shift(0.3*UP)
        rect.set_color(YELLOW)
        title = Tex("Neue Definition:").to_edge(LEFT+UP)
        self.play(Write(title), Create(rect))

        text = (r"Wir nennen $F: \mathbb{R}^n \to \mathbb{R}^m$ linear,\\"
                r"wenn $F$ homogen und additiv ist. Das bedeutet:")
        definition = Tex(text, tex_environment="flushleft").shift(UP+0.2*LEFT).scale(0.7)
        homogenundadditiv = (r"F(\lambda x)=\lambda F(x) \qquad \quad &\forall x \in \mathbb{R}^n, \lambda \in \mathbb{R} \\"
                             r"F(x+y)=F(x)+F(y) \qquad &\forall a,b \in \mathbb{R}^n")
        homogenundadditiv = Tex(homogenundadditiv, tex_environment="align*").scale(0.7).shift(0.2*DOWN)

        self.next_section()
        self.play(Write(definition))
        self.next_section()
        self.play(Write(homogenundadditiv))

        definition = VGroup(rect, definition, homogenundadditiv)
        self.next_section()
        self.play(definition.animate.scale(0.7))
        self.play(definition.animate.shift(2*UP+3*RIGHT))

        Frage = Tex(r"Ist $T: x\mapsto (x+y, y)$ linear?")
        Frage.scale(0.7).to_edge(LEFT)
        self.next_section()
        self.play(Write(Frage))

        homogen = Tex("Homogenität:").scale(0.7).next_to(Frage,DOWN,0.5).to_edge(LEFT)
        homogen2 = Tex(r"$T(\lambda (x,y))=(\lambda x+\lambda y, \lambda y)=\lambda (x+y,y)=\lambda T(x,y)$").scale(0.7).next_to(homogen,RIGHT,0.5)
        self.next_section()
        self.play(Write(homogen), Write(homogen2))

        additiv = Tex("Additivität:").scale(0.7).next_to(homogen2,DOWN,0.5).to_edge(LEFT)
        additiv2 = Tex(r"$T((x_1,y_1)+(x_2,y_2))=(x_1+x_2+y_1+y_2,y_1+y_2)$").scale(0.7).next_to(additiv,RIGHT, 0.5)
        additiv3 = Tex(r"$=(x_1+y_1,y_1)+(x_2+y_2,y_2)=T(x_1,y_1)+T(x_2,y_2)$").scale(0.7).next_to(additiv2,DOWN,0.3).shift(3*RIGHT)
        self.next_section()
        self.play(Write(additiv), Write(additiv2))
        self.next_section()
        self.play(Write(additiv3))

        JA = ImageMobject("src/images/yippie.png").scale(0.7).to_edge(DOWN).shift(0.8*DOWN+LEFT)
        self.add(JA)
        self.wait()

        self.next_section()
        self.remove(homogen, homogen2, additiv, additiv2, additiv3, JA)
        Frage2 = Tex(r"Ist $T: x\mapsto (x, x\cdot y)$ linear?")
        Frage2.scale(0.7).to_edge(LEFT).shift(UP)
        self.play(Transform(Frage,Frage2))

        homogen = Tex("Homogenität:").scale(0.7).next_to(Frage,DOWN,0.5).to_edge(LEFT)
        homogen2 = Tex(r"$T(\lambda (x,y))=(\lambda x, \lambda x \cdot\lambda y)\neq\lambda T(x,y)$").scale(0.7).next_to(homogen,RIGHT,0.5)
        self.next_section()
        self.play(Write(homogen), Write(homogen2))

        NEIN = ImageMobject("src/images/sad.png").scale(0.5).to_edge(DOWN)
        self.add(NEIN)
        self.wait()

        self.next_section()
        self.remove(homogen,homogen2,NEIN)
        nicethings = Tex(r"Ist $T(x)=F(x)+G(x)$ linear, wenn $F,G$ linear?")
        nicethings.scale(0.7).to_edge(LEFT).shift(UP)
        self.play(Transform(Frage, nicethings))

        homogen = Tex("Homogenität:").scale(0.7).next_to(Frage,DOWN,0.5).to_edge(LEFT)
        homogen2 = Tex(r"$T(\lambda x)=F(\lambda x)+G(\lambda x)$").scale(0.7).next_to(homogen,RIGHT,0.5)
        homogen3 = Tex(r"$=\lambda F(x)+\lambda G(x)=\lambda T(x)$").scale(0.7).next_to(homogen2,RIGHT)
        self.next_section()
        self.play(Write(homogen), Write(homogen2))
        self.next_section()
        self.play(Write(homogen3))

        additiv = Tex("Additivität:").scale(0.7).next_to(homogen2,DOWN,0.5).to_edge(LEFT)
        additiv2 = Tex(r"$T(x+y)=F(x+y)+G(x+y)$").scale(0.7).next_to(additiv,RIGHT, 0.5)
        additiv3 = Tex(r"$=F(x)+F(y)+G(x)+G(y)$").scale(0.7).next_to(additiv2,RIGHT)
        additiv4 = Tex(r'$=F(x)+G(x)+F(y)+G(y)=T(x)+T(y)$').scale(0.7).next_to(additiv3,DOWN)
        self.next_section()
        self.play(Write(additiv), Write(additiv2))
        self.next_section()
        self.play(Write(additiv3))
        self.next_section()
        self.play(Write(additiv4))

        self.next_section()
        JA = ImageMobject("src/images/yippie.png").scale(0.7).to_edge(DOWN).shift(0.8*DOWN+LEFT)
        self.add(JA)

        self.wait()
