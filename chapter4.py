from manim import *
from manim_editor import PresentationSectionType
from manim.opengl import *
config.background_color = DARKER_GRAY
config["background_color"] = DARKER_GRAY
Tex.set_default(color=WHITE)

class TwoSuccessiveTransformations(LinearTransformationScene):
    """ CONFIG = {
        "foreground_plane_kwargs" : {
            "x_radius" : FRAME_WIDTH,
            "y_radius" : FRAME_WIDTH,
            "secondary_line_ratio" : 0
        },
    } """
    def construct(self):
        self.setup()
        self.apply_transposed_matrix([[2, 1],[1, 2]], run_time=1.3)
        self.moving_mobjects = []
        self.apply_transposed_matrix([[-1, -0.5],[0, -0.5]], run_time=1.5)
        self.wait()

class RotationThenShear(LinearTransformationScene):
    """ CONFIG = {
        "foreground_plane_kwargs" : {
            "x_radius" : FRAME_X_RADIUS,
            "y_radius" : FRAME_WIDTH,
            "secondary_line_ratio" : 0
        },
    } """
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

class RotationThenShear2(LinearTransformationScene):
    """ CONFIG = {
        "foreground_plane_kwargs" : {
            "x_radius" : FRAME_X_RADIUS,
            "y_radius" : FRAME_WIDTH,
            "secondary_line_ratio" : 0
        },
    } """
    def construct(self):
        self.setup()    
        self.apply_transposed_matrix([[0, 1], [-1, 0]], run_time=1.5)

        self.moving_mobjects = []
        self.apply_transposed_matrix([[1, 0], [1, 1]], run_time=1.5)
        self.wait()
        self.next_section()
        text = Tex("Verknüpfung zweier Matrizen")
        text[0][0:12].set_color_by_gradient(YELLOW, PINK)
        text.to_edge(UP).add_background_rectangle()
        self.play(Write(text))
        self.wait()
        self.next_section()
        text2 = Tex(r'''Wo landen die Basisvektoren?''')
        text2.next_to(text, DOWN).add_background_rectangle()
        self.play(Write(text2))
        self.wait()
        self.next_section()

        ex, ey = self.get_basis_vectors()

        VektorX = Matrix([[1],[1]], color=GREEN).set_color(GREEN).add_background_rectangle()
        VektorX.move_to(ex.get_end() + RIGHT + UP)

        VektorY = Matrix([[-1],[0]], color=RED).set_color(RED).add_background_rectangle()
        VektorY.move_to(ey.get_end() + 2*LEFT + DOWN)

        self.play(Write(VektorX), Write(VektorY))

        self.next_section()

        matrix = Matrix([[1,-1],[1,0]])
        matrix.next_to(text2,RIGHT).add_background_rectangle()

        self.play(ReplacementTransform(VGroup(VektorX,VektorY), matrix))

        """ self.next_section()
        self.remove(self.plane, text,text2,ex,ey)
        self.play(matrix.animate.move_to(UP)) """

class RotationThenShear3(LinearTransformationScene):
    def construct(self):
        matrix = Matrix([[1,-1],[1,0]])
        matrix.to_edge(UP).add_background_rectangle()
        self.add(matrix)
        self.next_section()
        self.setup()
        self.apply_transposed_matrix([[0, 1], [-1, 0]], run_time=1.5)

        self.moving_mobjects = []
        self.apply_transposed_matrix([[1, 0], [1, 1]], run_time=1.5)
        self.wait()

class OneWayToThinkAboutIt(LinearTransformationScene):
    def construct(self):
        self.setup()
        v = self.add_vector([2,3,0], color=YELLOW)
        self.apply_transposed_matrix([[0, 1], [-1, 0]], run_time=1.5)

        self.moving_mobjects = []
        self.apply_transposed_matrix([[1, 0], [1, 1]], run_time=1.5)
        self.wait()

class OneWayToThinkAboutIt2(Scene):
    def construct(self):
        v = Matrix([["x"],["y"]])
        v.set_row_colors(YELLOW, YELLOW)
        self.add(v)
        matrix1 = Matrix([[0, -1], [1, 0]]).next_to(v,LEFT).set_color(BLUE_A)
        matrix1brace = Brace(matrix1, DOWN)
        matrix1bracetext = Tex("Rotation").next_to(matrix1brace, DOWN)
        self.next_section()
        self.play(Write(matrix1), Write(matrix1brace),Write(matrix1bracetext),)

        Bigbrace1 = Tex("(", font_size=130).next_to(matrix1,LEFT)
        Bigbrace2 = Tex(")", font_size=130).next_to(v,RIGHT)
        self.play(Create(Bigbrace1),Create(Bigbrace2))

        matrix2 = Matrix([[1, 1], [0, 1]]).next_to(Bigbrace1,LEFT).set_color(BLUE_A)
        matrix2brace = Brace(matrix2, DOWN)
        matrix2bracetext = Tex("Scheerung").next_to(matrix2brace, DOWN)
        self.next_section()
        self.play(Write(matrix2), Write(matrix2brace),Write(matrix2bracetext),)

        equals = Tex("=").next_to(Bigbrace2,RIGHT)

        composition = Matrix([[1, -1], [1, 0]]).next_to(equals,RIGHT).set_color(BLUE_A)
        compositionbrace = Brace(composition, DOWN)
        compositionbracetext = Tex("Verknüpfung").next_to(compositionbrace, DOWN)
        secondx = v.copy().next_to(composition,RIGHT)
        self.next_section()
        self.play(Write(composition), Write(compositionbrace),Write(compositionbracetext),Write(equals),Write(secondx))

        matrix1 = VGroup(matrix1,matrix1brace,matrix1bracetext)
        matrix2 = VGroup(matrix2,matrix2brace,matrix2bracetext)
        composition = VGroup(composition,compositionbrace,compositionbracetext)
        group = VGroup(*[matrix2,matrix1,equals,composition])
        self.next_section()
        self.play(FadeOut(Bigbrace1), FadeOut(Bigbrace2), FadeOut(v), FadeOut(secondx))
        self.play(group.animate.arrange(),equals.animate.shift([-0.3,0.5,0]))
        self.wait()

