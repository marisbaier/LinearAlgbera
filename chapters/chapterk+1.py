from manim import *
from manim_slides import Slide
import itertools as it


class Linearität(Slide):
    def construct(self):
        title = Tex("Aus der Vorlesung zur Integration:")
        title.set_color(YELLOW).to_corner(UP+LEFT)
        self.play(Write(title))
        self.next_section()
        Homogenität = Tex(r'$\int\lambda\cdot F(x)\, dx\quad \,\,\,\,\,=\lambda\cdot \int F(x) \, dx$')
        Homogenität.shift(title.get_bottom()+1.3*DOWN).to_edge(LEFT)
        Additivität = Tex(r'$\int F(x)+g(x)\, dx=\int F(x)\, dx+\int g(x)\, dx$')
        Additivität.shift(Homogenität.get_bottom()+DOWN).to_edge(LEFT)
        Klammer = Tex(r'$\}$').scale(3.7).shift(Additivität.get_right()+0.7*UP+0.8*RIGHT)
        self.play(Write(Homogenität), Write(Additivität))
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
        self.remove(Aussage, Linearitaet, Klammer, Homogenität, Additivität)

        title = Tex("Das Integral erfüllt also:").to_edge(LEFT).shift(2*UP)
        Homogenität = Tex(r'$F(\lambda\cdot x)=\lambda\cdot F(x)$').shift(0.7*UP)
        Additivität = Tex(r'$F(a+b)=F(a)+F(b)$').shift(0.7*DOWN)

        self.play(Write(title), Write(Homogenität), Write(Additivität))
        
        subtitle = Tex(r'Ist das dieselbe Linearität, die wir schon kennen?')
        subtitle.shift(2*DOWN).to_edge(LEFT)
        subtitle.set_color(RED)

        self.play(Write(subtitle))
        self.next_section()

        Aussage2 = Tex(r'(Linien bleiben Linien, der Ursprung bleibt...)').scale(0.75)
        Aussage2.shift(2.65*DOWN+1.6*RIGHT)
        self.play(Write(Aussage2))
        self.wait()

class Beweis(Slide):
    def construct(self):
        title = Tex("Zu zeigen:")
        title.to_corner(UP+LEFT)
        self.play(Write(title))

        Homogenität = Tex(r'$F(\lambda\cdot x)=\lambda\cdot F(x)$').shift(0.45*UP+3.7*RIGHT)
        Additivität = Tex(r'$F(a+b)=F(a)+F(b)$').shift(0.45*DOWN+3.7*RIGHT)
        self.next_section()

        self.play(Write(Homogenität), Write(Additivität))

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

        self.next_section()
        Hinrichtung = Tex("Wir zeigen die Hinrichtung:")
        Hinrichtung.to_corner(UP+LEFT)
        newFolgepfeil = Tex(r'$\Rightarrow$').shift(0.45*UP+1.5*LEFT)
        t0 = Tex(r'$t=0$').scale(0.5)
        t0.move_to(newFolgepfeil.get_top()+0.4*UP)
        self.remove(text1strich,text2strich,Homogenität, Additivität)
        self.play(Transform(title,Hinrichtung), Transform(equiv,newFolgepfeil), text1.animate.shift(0.5*LEFT), text2.animate.shift(0.5*LEFT))
        
        self.next_section()
        self.play(Write(t0))

        Zwischenschritt = Tex(r'$F(a)=c$').next_to(newFolgepfeil,RIGHT,0.5)
        self.next_section()
        self.play(Write(Zwischenschritt))

        Folgepfeil = newFolgepfeil.copy().shift(1.2*DOWN).rotate(-0.4)
        self.next_section()
        a0 = Tex(r'$a=0$').scale(0.5)
        a0.move_to(Folgepfeil.get_top()+0.4*UP)
        self.play(Write(Folgepfeil), Write(a0))

        Homogenität = Tex(r'$F(tb)=c+td$')
        Homogenität.next_to(Folgepfeil,RIGHT,0.5).shift(0.35*DOWN)
        self.next_section()
        self.play(Write(Homogenität))

        Homogenität2 = Tex(r'$=F(0)+td$').next_to(Homogenität)
        self.next_section()
        self.play(Write(Homogenität2))

        Homogenität3 = Tex(r'$=td$').next_to(Homogenität2)
        self.next_section()
        self.play(Write(Homogenität3))

        Folgepfeil3 = Tex(r'$\Rightarrow$').next_to(Homogenität,DOWN).shift(0.5*LEFT+0.5*DOWN)
        t1 = Tex(r't=1').scale(0.5)
        t1.next_to(Folgepfeil3,UP)
        Homogenität4 = Tex(r'$F(tb)=tF(b)$')
        Homogenität4.next_to(Folgepfeil3, buff=0.45)
        self.next_section()
        self.play(Write(Folgepfeil3), Write(t1), Write(Homogenität4))

        rect = Rectangle(height=0.8, width=3.2).shift([2.3,-2.225,0])
        rect.set_color(YELLOW)
        self.next_section()
        self.play(Create(rect))

        textAdditivität = Tex("Homogenität!").scale(0.8)
        textAdditivität.set_color(YELLOW)
        textAdditivität.next_to(rect, DOWN)
        self.next_section()
        self.play(Write(textAdditivität))

        self.next_section()
        self.remove(Homogenität, Homogenität2, Homogenität3, a0, Folgepfeil, t1, Folgepfeil3)
        self.play(rect.animate.shift([1,5.1,0]), Homogenität4.animate.shift([1,5.1,0]), textAdditivität.animate.shift([1,5.1,0]))

        Folgepfeil = newFolgepfeil.copy().shift(1.2*DOWN).rotate(-0.4)
        self.next_section()
        a0 = Tex(r'$r=1$').scale(0.5)
        a0.move_to(Folgepfeil.get_top()+0.4*UP)
        self.play(Write(Folgepfeil), Write(a0))

        eq = Tex(r'$F(a+b)=c+d$').next_to(Folgepfeil,RIGHT,0.5).shift(0.35*DOWN)
        self.next_section()
        self.play(Write(eq))
        
        eq2 = Tex(r'$=F(a)+d$').next_to(eq)
        self.next_section()
        self.play(Write(eq2))

        Folgepfeil4 = Tex(r'$\Rightarrow$').next_to(eq,DOWN).shift(0.5*LEFT+0.5*DOWN)
        a0 = Tex(r'a=0').scale(0.5)
        a0.next_to(Folgepfeil4,UP)
        eq3 = Tex(r'$F(a+b)=F(a)+F(b)$')
        eq3.next_to(Folgepfeil4, buff=0.45)
        self.next_section()
        self.play(Write(Folgepfeil4), Write(a0), Write(eq3))

        rect = Rectangle(height=0.8, width=5.5).shift([3.75,-2.225,0])
        rect.set_color(YELLOW)
        self.next_section()
        self.play(Create(rect))

        textAdditivität = Tex("Additivität!").scale(0.8)
        textAdditivität.set_color(YELLOW)
        textAdditivität.next_to(rect, DOWN)
        self.next_section()
        self.play(Write(textAdditivität))

        self.wait()

class BeweisRueckwaerts(Slide):
    def construct(self):
        title = Tex("Nun die Rückrichtung:").to_edge(LEFT+UP)
        self.play(Write(title))

        Homogenität = Tex(r'$F(\lambda\cdot x)=\lambda\cdot F(x)$').shift(0.45*UP+3.7*RIGHT)
        Additivität = Tex(r'$F(a+b)=F(a)+F(b)$').shift(0.45*DOWN+3.7*RIGHT)
        text1 = Tex(r'$F(a+t b)=c+t d$').shift(0.45*UP+3.7*LEFT)
        text2 = Tex(r'$F(0)=0$').shift(0.45*DOWN+3.7*LEFT)
        arrow = Tex(r'$\Leftarrow$')

        self.play(Write(Homogenität), Write(Additivität), Write(text1), Write(text2))
        self.play(Write(arrow))

        self.next_section()

        implication = Tex(r'$\Leftarrow$').next_to(Additivität,LEFT)
        self.remove(text1,text2)
        self.play(Transform(arrow, implication))
        
        linear = Tex(r'$F(a)+F(\lambda b)=F(a+\lambda b)$')
        linear.next_to(implication, LEFT)
        self.next_section()
        self.play(Write(linear, reverse=True))

        linear2 = Tex(r'$F(a)+\lambda F(b)=$')
        linear2.next_to(linear,LEFT)
        self.next_section()
        self.play(Write(linear2,reverse=True))

        self.wait()
