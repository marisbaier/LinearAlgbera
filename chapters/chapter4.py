from manim import *
from manim_slides import Slide

from config import LinearTransformationSlide


class LinearTransformationSlide(Slide, LinearTransformationScene):
    pass

class TwoSuccessiveTransformations(LinearTransformationSlide):
    """ CONFIG = {
        "foreground_plane_kwargs" : {
            "x_radius" : FRAME_WIDTH,
            "y_radius" : FRAME_WIDTH,
            "secondary_line_ratio" : 0
        },
    } """
    def construct(self):
        self.setup()
        self.next_section()
        self.apply_transposed_matrix([[2, 1],[1, 2]], run_time=1.3)
        self.moving_mobjects = []
        self.apply_transposed_matrix([[-1, -0.5],[0, -0.5]], run_time=1.5)
        self.wait()
48
class RotationThenShear(LinearTransformationSlide):
    def construct(self):
        self.setup()
        text = Tex("Erst Rotation, dann Scheerung", font_size=60).to_edge(UP+LEFT).add_updater(lambda me: me.to_edge(UP+LEFT))
        text[0][4:12].set_color(YELLOW)
        text[0][17:26].set_color(MAROON_C)
        text.add_background_rectangle()

        self.play(Write(text, run_time = 1))    
        self.apply_transposed_matrix([[0, 1], [-1, 0]])

        self.moving_mobjects = []
        self.apply_transposed_matrix([[1, 0], [1, 1]])
        text.clear_updaters()
        self.wait()
49
class RotationThenShear2(LinearTransformationSlide):
    def construct(self):
        self.setup()    
        self.apply_transposed_matrix([[0, 1], [-1, 0]], run_time=1.5)

        self.moving_mobjects = []
        self.apply_transposed_matrix([[1, 0], [1, 1]], run_time=1.5)
        self.wait()
        self.next_slide()
        text = Tex("Verknüpfung zweier Matrizen")
        text[0][0:12].set_color_by_gradient(YELLOW, PINK)
        text.to_edge(UP).add_background_rectangle()
        self.play(Write(text))
        self.wait()
        self.next_slide()
        text2 = Tex(r'''Wo landen die Basisvektoren?''')
        text2.next_to(text, DOWN).add_background_rectangle()
        self.play(Write(text2))
        self.wait()
        self.next_slide()

        ex, ey = self.get_basis_vectors()

        VektorX = Matrix([[1],[1]], color=GREEN).set_color(GREEN).add_background_rectangle()
        VektorX.move_to(ex.get_end() + RIGHT + UP)

        VektorY = Matrix([[-1],[0]], color=RED).set_color(RED).add_background_rectangle()
        VektorY.move_to(ey.get_end() + 2*LEFT + DOWN)

        self.play(Write(VektorX), Write(VektorY))

        self.next_slide()

        matrix = Matrix([[1,-1],[1,0]])
        matrix.next_to(text2,RIGHT).add_background_rectangle()

        self.play(ReplacementTransform(VGroup(VektorX,VektorY), matrix))

        """ self.next_slide()
        self.remove(self.plane, text,text2,ex,ey)
        self.play(matrix.animate.move_to(UP)) """
50
class RotationThenShear3(LinearTransformationSlide):
    def construct(self):
        matrix = Matrix([[1,-1],[1,0]])
        matrix.to_edge(UP).add_background_rectangle()
        self.add(matrix)
        self.next_slide()
        self.setup()
        self.apply_transposed_matrix([[0, 1], [-1, 0]], run_time=1.5)

        self.moving_mobjects = []
        self.apply_transposed_matrix([[1, 0], [1, 1]], run_time=1.5)
        self.wait()
51
class OneWayToThinkAboutIt(LinearTransformationSlide):
    def construct(self):
        self.setup()
        v = self.add_vector([2,3,0], color=YELLOW)
        self.apply_transposed_matrix([[0, 1], [-1, 0]], run_time=1.5)

        self.moving_mobjects = []
        self.apply_transposed_matrix([[1, 0], [1, 1]], run_time=1.5)
        self.wait()
52
class OneWayToThinkAboutIt2(Slide):
    def construct(self):
        v = Matrix([["x"],["y"]])
        v.set_row_colors(YELLOW, YELLOW)
        self.add(v)
        matrix1 = Matrix([[0, -1], [1, 0]]).next_to(v,LEFT).set_color(BLUE_A)
        matrix1brace = Brace(matrix1, DOWN)
        matrix1bracetext = Tex("Rotation").next_to(matrix1brace, DOWN)
        self.next_slide()
        self.play(Write(matrix1), Write(matrix1brace),Write(matrix1bracetext),)

        Bigbrace1 = Tex("(", font_size=130).next_to(matrix1,LEFT)
        Bigbrace2 = Tex(")", font_size=130).next_to(v,RIGHT)
        self.play(Create(Bigbrace1),Create(Bigbrace2))

        matrix2 = Matrix([[1, 1], [0, 1]]).next_to(Bigbrace1,LEFT).set_color(BLUE_A)
        matrix2brace = Brace(matrix2, DOWN)
        matrix2bracetext = Tex("Scheerung").next_to(matrix2brace, DOWN)
        self.next_slide()
        self.play(Write(matrix2), Write(matrix2brace),Write(matrix2bracetext),)

        equals = Tex("=").next_to(Bigbrace2,RIGHT)

        composition = Matrix([[1, -1], [1, 0]]).next_to(equals,RIGHT).set_color(BLUE_A)
        compositionbrace = Brace(composition, DOWN)
        compositionbracetext = Tex("Verknüpfung").next_to(compositionbrace, DOWN)
        secondx = v.copy().next_to(composition,RIGHT)
        self.next_slide()
        self.play(Write(composition), Write(compositionbrace),Write(compositionbracetext),Write(equals),Write(secondx))

        matrix1 = VGroup(matrix1,matrix1brace,matrix1bracetext)
        matrix2 = VGroup(matrix2,matrix2brace,matrix2bracetext)
        composition = VGroup(composition,compositionbrace,compositionbracetext)
        group = VGroup(*[matrix2,matrix1,equals,composition])
        self.next_slide()
        self.play(FadeOut(Bigbrace1), FadeOut(Bigbrace2), FadeOut(v), FadeOut(secondx))
        self.play(group.animate.arrange(),equals.animate.shift([-0.3,0.5,0]))
        self.wait()
        self.next_slide()
        vector = Vector(4*LEFT, color=YELLOW, max_tip_length_to_length_ratio=0.15).next_to(group,UP).shift(2*LEFT)
        self.play(Create(vector))

        text = Tex("Von rechts nach links gelesen").next_to(vector,UP).scale(0.7).shift([0.1,-0.1,0])
        self.play(Write(text, reverse=True))
        self.add(text)
        self.next_slide()
        text2 = Tex("f(g(x))").scale(0.7).next_to(text,UP)
        self.play(Write(text2))
53
class Composition(LinearTransformationSlide):
    def __init__(self):
        LinearTransformationSlide.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_background_plane=True,
            show_basis_vectors=True,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        matrix = Matrix([[1,-2],[1,0]]).move_to([-2.5,1.8,0]).set_color(YELLOW).scale(1.1)
        matrix.add_background_rectangle()

        self.add_foreground_mobject(matrix)
        self.next_slide()
        self.apply_transposed_matrix([[1,1],[-2,0]])
        brace1 = Brace(matrix,UP)
        brace1text = brace1.get_text(r'$M_1$')
        self.next_slide()
        self.play(Write(brace1),)
        self.play(Write(brace1text))
        matrix2 = Matrix([[0,2],[1,0]]).scale(1.1).next_to(matrix,LEFT).set_color(MAROON_C)
        matrix2.add_background_rectangle()
        self.next_slide()
        self.play(Write(matrix2))
        self.next_slide()
        self.moving_mobjects = []
        self.apply_inverse_transpose([[1,1],[-2,0]], run_time=0.01)
        self.next_slide()
        self.moving_mobjects = []
        self.apply_matrix([[0,2],[1,0]])
        self.next_slide()
        self.moving_mobjects = []
        self.apply_inverse([[0,2],[1,0]], run_time=0.01)
        brace2 = Brace(matrix2,UP)
        brace2text = brace2.get_text(r'$M_2$')
        self.next_slide()
        self.play(Write(brace2),Write(brace2text))

        self.next_slide()

        self.moving_mobjects = []
        self.apply_transposed_matrix([[1,1],[-2,0]], run_time=1)
        self.moving_mobjects = []
        self.apply_matrix([[0,2],[1,0]], run_time=1)

        eq = Tex("=").next_to(matrix, RIGHT)
        matrix3 = Matrix([["?","?"],["?","?"]]).scale(1.1).next_to(eq,RIGHT).set_row_colors(YELLOW, MAROON_C)
        matrix3.add_background_rectangle()
        self.next_slide()
        self.play(Write(eq), Write(matrix3))

        VGroup(matrix,matrix2,matrix3,eq,brace1,brace2,brace1text,brace2text).set_z_index(30)
        Rec = Rectangle(color=config.background_color,stroke_width=1000)
        self.play(FadeIn(Rec))

        text = Tex(r'''Wo geht $\vec{e}_x$ hin?''', font_size=80).shift(1.5*DOWN)
        self.play(Write(text))

        self.next_slide()
        self.remove(text)
        ell = Ellipse(color=GREEN, height=1.5,width=0.8).move_to(matrix.get_center()).shift(0.75*LEFT).set_z_index(50)
        vec = Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([-1.4,-0.2,0],[-2.7,0.7,0]).set_color(YELLOW)
        text = Tex(r'''Erster Ort, wo $\vec{e}_x$ hingeht!''').move_to([1.75,-0.5,0])
        self.play(Create(ell), Create(vec), Write(text))

        self.next_slide()
        matrix2new = matrix2.copy()

        self.play(matrix2new.animate.shift(3*DOWN))
        exfirst = Matrix([[1],[1]]).set_color(GREEN).next_to(matrix2new)
        self.play(Write(exfirst))
        self.next_slide()
        brace = Brace(VGroup(matrix2new,exfirst,),DOWN)
        bracetext = brace.get_text("Finaler Ort nach zweiter Transformation :DDDD").shift(3.5*RIGHT)
        self.remove(vec)
        self.play(Create(brace), Transform(text,bracetext))
        self.next_slide()
        V1 = ImageMobject("src/images/stonks.webp")
        self.add(V1)
        self.play(Rotate(V1))
        self.remove(V1)
        self.next_slide()
        vec = Vector(1.3*UP).shift(0.05*RIGHT+0.5*DOWN).set_color(YELLOW).set_z_index(51)
        ell2 = Ellipse(color=GREEN, height=1.5,width=0.8).move_to(matrix3.get_center()).shift(0.7*LEFT).set_z_index(50)
        self.play(Create(vec), Create(ell2), FadeOut(ell))
54



