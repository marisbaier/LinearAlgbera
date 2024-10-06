from manim import *
from manim_slides import Slide
import itertools as it

from config import LinearSystemTransformationSlide


class LinearTransformationSlide(Slide, LinearTransformationScene):
    pass


class UsefulnessOfMatrices(Slide):
    def construct(self):
        title1 = Tex("Visuelle Interpretation")
        title1.set_color(YELLOW)
        title1.to_edge(UP)
        FachiniAdler = ImageMobject("src/images/logo_flipped.png")
        FachiniAdler.scale(0.6)
        FachiniAdler.to_corner(DOWN+RIGHT).shift(DOWN*2.5)
        self.add(FachiniAdler)
        e0 = Ellipse(width=1.35, height=0.7, color=WHITE)
        e1 = Ellipse(width=0.8, height=0.45, color=WHITE)
        e2 = Ellipse(width=0.45, height=0.2, color=WHITE)
        e0.shift(RIGHT*2.2+UP*0.15)
        e1.shift(RIGHT*3.2+DOWN*0.55)
        e2.shift(RIGHT*4+DOWN*0.9)
        self.next_section()
        self.play(Write(title1))
        cube = Cube().rotate(PI/8, axis=UP+LEFT)
        cube.set_color(GREEN)
        self.next_section()
        axes = ThreeDAxes()
        self.play(Create(e1), Create(e2))
        self.play(cube.animate.rotate(PI/3, axis=RIGHT))
        self.play(cube.animate.rotate(PI/3, axis=UP))
        self.next_section()
        self.remove(cube, e1, e2)

        title = Tex("Nützlichkeit von Matrizen")
        title.set_color(YELLOW)
        title.to_edge(UP)
        # TODO: Add content
        self.next_slide()
        self.play(Transform(title1, title))

        V1 = ImageMobject("src/images/ENIAC-changing_a_tube.jpg")
        V1.scale(0.7)
        self.add(V1)
        self.wait()

        self.next_slide()
        self.remove(V1)

        equations = MathTex(r"""
            6x - 3y + 2z &= 7 \\
            x + 2y + 5z &= 0 \\
            2x - 8y - z &= -2 \\
        """)
        equations.to_edge(RIGHT, buff = 2)
        self.next_slide()
        self.play(FachiniAdler.animate.shift(DOWN+RIGHT), Write(equations))
        #self.play(Create(equations[0][1].copy().shift([-2,0,0])))
        syms = VGroup(*[equations[0][i] for i in [1, 4, 7]])
        new_syms = VGroup(*[
            equations[0][i].copy().set_color(c) 
            for i, c in zip([1,4,7], [GREEN, RED, BLUE])
        ])
        new_syms.arrange(RIGHT, buff = 0.5)
        new_syms.next_to(equations, LEFT, buff = 3)
        sym_brace = Brace(new_syms, DOWN)
        unknowns = sym_brace.get_text("Unbekannte Variablen")
        eq_brace = Brace(equations, DOWN)
        eq_words = eq_brace.get_text("Gleichungen")

        self.next_slide()
        self.play(Transform(syms.copy(), new_syms, path_arc = np.pi/2))
        for brace, words in (sym_brace, unknowns), (eq_brace, eq_words):
            self.play(
                GrowFromCenter(brace),
                Write(words)
            )
            self.wait()
        self.remove()
        self.next_slide()
59
class ComplicatedSystem(Slide):
    def construct(self):
        system = MathTex(r"""
            \frac{1}{1-e^{2x-3y+4z}} &= 1 \\
            \sin(xy) + z^2 &= \sqrt{y} \\
            x^2 + y^2 &= e^{-z}
        """)
        system.to_edge(UP)
        #randy = Randolph().to_corner(DOWN+LEFT)

        #self.add(randy)
        self.play(Write(system, run_time = 1))
        #self.play(randy.change_mode, "sassy")
        #self.play(Blink(randy))
        self.wait()
60
class SystemOfEquations(Slide):
    def construct(self):
        equations = self.get_equations()
        self.play(Write(equations))
        self.add(equations)
        self.next_slide()
        self.show_linearity_rules(equations)
        self.next_slide()
        self.describe_organization(equations)
        self.factor_into_matrix(equations)

    def get_equations(self):
        matrix = Matrix([
            [2, 5, 3],
            [4, 0, 8],
            [1, 3, 0]
        ])
        mob_matrix = matrix.get_mob_matrix()
        rhs = list(map(Tex, list(map(str, [-3, 0, 2]))))
        variables = list(map(Tex, list("xyz")))
        for v, color in zip(variables, [RED, GREEN, BLUE]):
            v.set_color(color)
        equations = VGroup()
        for row in mob_matrix:
            equation = VGroup(*it.chain(*list(zip(
                row, 
                [v.copy() for v in variables],
                list(map(Tex, list("++=")))
            ))))
            equation.arrange(
                RIGHT, buff = 0.1, 
                aligned_edge = DOWN
            )
            equation.split()[4].shift(0.1*DOWN)
            equation.split()[-1].next_to(equation.split()[-2], RIGHT)
            equations.add(equation)
        equations.arrange(DOWN, aligned_edge = RIGHT)
        for eq, rhs_elem in zip(equations.split(), rhs):
            rhs_elem.next_to(eq, RIGHT)
            eq.add(rhs_elem)
        equations.center()
        return equations

    def show_linearity_rules(self, equations):
        top_equation = equations.split()[0]
        other_equations = VGroup(*equations.split()[1:])
        other_equations.save_state()
        scaled_vars = VGroup(*[
            VGroup(*top_equation.split()[3*i:3*i+2])
            for i in range(3)
        ])
        scaled_vars.save_state()
        isolated_scaled_vars = scaled_vars.copy()
        isolated_scaled_vars.scale(1.5)
        isolated_scaled_vars.next_to(top_equation, UP)
        scalars = VGroup(*[m.split()[0] for m in scaled_vars.split()])
        plusses = VGroup(*[top_equation.split()[2],top_equation.split()[5]])

        self.next_slide()

        self.play(other_equations.animate.fade())
        self.play(Transform(scaled_vars, isolated_scaled_vars))
        self.play(scalars.animate.set_color(YELLOW), lag_ratio = 0.5)
        self.play(*[
            ApplyMethod(m.scale, 1.2, rate_func = there_and_back)
            for m in scalars.split()
        ])

        self.next_slide()
        
        self.remove(scalars)
        self.play(scaled_vars.animate.restore())
        self.play(*[
            ApplyMethod(p.scale, 1.5, rate_func = there_and_back)
            for p in plusses
        ])
        self.wait()
        self.show_nonlinearity_examples()
        self.play(other_equations.animate.restore())

    def show_nonlinearity_examples(self):
        squared = Tex(r"$x^2$")
        squared[0][0].set_color(RED)
        sine = Tex(r"$\sin(x)$")
        sine[0][-2].set_color(RED)
        product = Tex(r"$xy$")
        product[0][0].set_color(RED)
        product[0][1].set_color(GREEN)


        words = Tex("Nicht erlaubt!")
        words.set_color(RED)
        words.to_corner(UP+LEFT, buff = 1)
        arrow = Vector(RIGHT, color = RED)
        arrow.next_to(words, RIGHT)
        for mob in squared, sine, product:
            mob.scale(1.7)
            mob.next_to(arrow.get_end(), RIGHT, buff = 0.5)
        circle_slash = Circle(color = RED)
        line = Line(LEFT, RIGHT, color = RED)
        line.rotate(np.pi/4)
        circle_slash.add(line)
        circle_slash.next_to(arrow, RIGHT)
        def draw_circle_slash(mob):
            circle_slash.replace(mob)
            circle_slash.scale(1.4)
            self.play(Create(circle_slash), run_time = 0.5)
            self.wait(0.5)
            self.play(FadeOut(circle_slash), run_time = 0.5)

        self.play(
            Write(squared),
            Write(words, run_time = 1),
            Create(arrow),
        )
        draw_circle_slash(squared)
        for mob in sine, product:
            self.play(Transform(squared, mob))
            draw_circle_slash(mob)
            self.next_slide()
        self.play(*list(map(FadeOut, [words, arrow, squared])))
        self.wait()

    def describe_organization(self, equations):
        variables = VGroup(*it.chain(*[
            eq.split()[:-2]
            for eq in equations.split()
        ]))
        variables.words = "Alle Variablen nach links"
        constants = VGroup(*[
            eq.split()[-1]
            for eq in equations.split()
        ])
        constants.words = "Konstanten nach rechts"
        xs, ys, zs = [
            VGroup(*[
                eq.split()[i]
                for eq in equations.split()
            ])
            for i in (1, 4, 7)
        ]
        ys.words = "Variablen vertikal untereinander"
        colors = [PINK, YELLOW, BLUE_B, BLUE_C, BLUE_D]
        for mob, color in zip([variables, constants, xs, ys, zs], colors):
            mob.square = Square(color = color)
            mob.square.replace(mob, stretch = True)
            mob.square.scale(1.1)
            if hasattr(mob, "words"):
                mob.words = Tex(mob.words)
                mob.words.set_color(color)
                mob.words.next_to(mob.square, UP)
        ys.square.add(xs.square, zs.square)
        zero_circles = VGroup(*[
            Circle().replace(mob).scale(1.3)
            for mob in [
                VGroup(*equations.split()[i].split()[j:j+2])
                for i, j in [(1, 3), (2, 6)]
            ]
        ])
        zero_circles.set_color(PINK)
        zero_circles.words = Tex("Nullen hinzufügen, wenn nötig")
        zero_circles.words.set_color(zero_circles.get_color())
        zero_circles.words.next_to(equations, UP)

        for mob in variables, constants, ys:
            self.play(
                FadeIn(mob.square),
                FadeIn(mob.words)
            )
            self.next_slide()
            self.play(*list(map(FadeOut, [mob.square, mob.words])))
        self.next_slide()
        self.play(
            Create(zero_circles),
            Write(zero_circles.words, run_time = 1)
        )
        self.wait()
        self.play(*list(map(FadeOut, [zero_circles, zero_circles.words])))
        self.wait()
        title = Tex("``Lineares Gleichungssystem''")
        title.scale(1.5)
        title.to_edge(UP)

        self.next_slide()
 
        self.play(Write(title))
        self.next_slide()
        self.play(FadeOut(title))
    
    def factor_into_matrix(self, equations):
        coefficients = VGroup()
        for eq in VGroup(*equations.split()):
            coefficients.add(VGroup(*[eq.split()[0],eq.split()[3],eq.split()[6]]))
        variable_arrays = VGroup()
        for eq in VGroup(*equations.split()):
            variable_arrays.add(VGroup(*[eq[1],eq[4],eq[7]]))
        rhs_entries = VGroup()
        for eq in VGroup(*equations.split()):
            rhs_entries.add(VGroup(*[eq[-1]]))
        """ matrix = Matrix(coefficients.copy())
        x_array = Matrix(variable_arrays[0].copy())
        v_array = Matrix(rhs_entries.copy()) """
        matrix = Matrix([[2,5,3],[4,0,8],[1,3,0]],
            left_bracket="(",
            right_bracket=")")
        x_array = Matrix([["x"],["y"],["z"]],
            left_bracket="(",
            right_bracket=")").set_row_colors(RED, GREEN, BLUE)
        v_array = Matrix([[-3],[0],[2]],
            left_bracket="(",
            right_bracket=")")
        equals = Tex("=")
        ax_equals_v = VGroup(matrix, x_array, equals, v_array)
        ax_equals_v.arrange(RIGHT)
        ax_equals_v.to_edge(RIGHT)
        all_brackets = [
            mob.get_brackets()
            for mob in (matrix, x_array, v_array)
        ]

        self.play(equations.animate.to_edge(LEFT))
        arrow = Vector(RIGHT, color = YELLOW)
        arrow.next_to(ax_equals_v, LEFT)
        self.play(Create(arrow))
        self.play(*it.chain(*[
            [
                Transform(
                    m1.copy(), m2, 
                    run_time = 2,
                    path_arc = -np.pi/2
                )
                for m1, m2 in zip(
                    np.array(start_array, dtype=object).flatten(),
                    matrix_mobject.get_entries().split()
                )
            ]
            for start_array, matrix_mobject in [
                (coefficients, matrix),
                (variable_arrays[0], x_array),
                (variable_arrays[1], x_array),
                (variable_arrays[2], x_array),
                (rhs_entries, v_array)
            ]
        ]))
        self.play(*[
            Write(mob)
            for mob in all_brackets + [equals]
        ])
        self.wait()
        self.label_matrix_product(matrix, x_array, v_array)

    def label_matrix_product(self, matrix, x_array, v_array):
        matrix.words = "Koeffizienten"
        matrix.symbol = "A"
        x_array.words = "Variablen"
        x_array.symbol = r"$\vec{\textbf{x}}$"
        v_array.words = "Konstanten"
        v_array.symbol = r"$\vec{\textbf{b}}$"
        parts = matrix, x_array, v_array
        for mob in parts:
            mob.brace = Brace(mob, UP)
            mob.words = mob.brace.get_text(mob.words)
            mob.words.shift_onto_screen()
            mob.symbol = Tex(mob.symbol)
            mob.brace.put_at_tip(mob.symbol)
        x_array.words.set_submobject_colors_by_gradient(
            RED, GREEN, BLUE
        )
        x_array.symbol.set_color(PINK)
        v_array.symbol.set_color(YELLOW)
        for mob in parts:
            self.play(
                GrowFromCenter(mob.brace),
                FadeIn(mob.words)
            )
            self.next_slide()
            self.play(*list(map(FadeOut, [mob.brace, mob.words])))
        self.next_slide()
        for mob in parts:
            self.play(
                FadeIn(mob.brace),
                Write(mob.symbol)
            )
            self.next_slide()
        compact_equation = VGroup(*[
            mob.symbol for mob in parts
        ])
        compact_equation.submobjects.insert(
            2, Tex("=").next_to(x_array, RIGHT)
        )
        compact_equation.target = compact_equation.copy()
        compact_equation.target.arrange(buff = 0.1)
        compact_equation.target.to_edge(UP)

        self.play(Transform(
            compact_equation.copy(), 
            compact_equation.target
        ))
        self.next_slide()
61

class LinearSystemTransformationSceneOne(LinearTransformationSlide):
    def __init__(self):
        LinearTransformationSlide.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=True
        )

    def construct(self):
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
        brace = Brace(self.A)
        words = brace.get_text("Transformation")
        words.add_background_rectangle()
        #self.add_foreground_mobject(words, brace)
        self.add_foreground_mobject(equa)
        self.play(GrowFromCenter(brace), Write(words, run_time = 1))
        matrix = np.array([[2, 1], [2, 3]])
        self.next_slide()
        self.moving_mobjects = []
        self.apply_matrix(matrix.T)
        self.wait()
        v = [-4, -1]
        x = np.linalg.solve(matrix.T, v)
        v = Vector(v, color = YELLOW)
        x = Vector(x, color = PINK)
        v_label = self.get_vector_label(v, "b", color = YELLOW)
        x_label = self.get_vector_label(x, "x", color = PINK)
        for label in x_label, v_label:
            label.add_background_rectangle()
        self.moving_mobjects = []
        self.apply_inverse(matrix.T, run_time=0.01)
        self.remove(self.i_hat,self.j_hat)
        self.next_slide()
        self.play(
            Create(v),
            Write(v_label)
        )
        self.add_foreground_mobject(v_label)
        x = self.add_vector(x, animate = False)
        self.play(
            Create(x),
            Write(x_label)
        )
        self.next_slide()
        """ self.wait()
        self.add(VGroup(x, x_label).copy().fade())
        self.moving_mobjects = []
        self.show_basis_vectors = False
        self.apply_transposed_matrix(matrix, show_basis_vectors=False)
        self.wait() """
62
class LinearSystemTransformationSceneTwo(LinearTransformationSlide):
    def __init__(self):
        LinearTransformationSlide.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=False
        )

    def construct(self):
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
        brace = Brace(self.A)
        words = brace.get_text("Transformation")
        words.add_background_rectangle()
        #self.add_foreground_mobject(words, brace)
        self.add_foreground_mobject(equa)
        self.add(brace)
        self.add(words)
        matrix = np.array([[2, 1], [2, 3]])
        self.moving_mobjects = []
        #self.apply_matrix(matrix,run_time=0.001)
        v = [-4, -1]
        x = np.linalg.solve(matrix.T, v)
        v = Vector(v, color = YELLOW)
        x = Vector(x, color = PINK)
        self.add(v)
        v_label = self.get_vector_label(v, "b", color = YELLOW)
        x_label = self.get_vector_label(x, "x", color = PINK)
        for label in x_label, v_label:
            label.add_background_rectangle()
        """ self.apply_inverse(matrix, run_time=0.01)
        self.remove(self.basis_vectors)
        self.play(
            Create(v),
            Write(v_label)
        ) """
        self.add_foreground_mobject(v_label)
        x = self.add_vector(x, animate = False)
        self.add(x)
        self.add(x_label)
        self.add(VGroup(x, x_label).copy().fade())
        self.moving_mobjects = []
        self.apply_transposed_matrix(matrix)
        self.next_slide()

class ThinkAboutWhatsHappening(Slide):
    def construct(self):
        V1 = ImageMobject("src/images/logo.png")
        V1.scale(0.6)
        V1.to_corner(DOWN+LEFT).shift(DOWN*2.5)
        self.add(V1)
        self.wait(0.1)
        equations = SystemOfEquations.get_equations(self)
        equations.shift(RIGHT+UP*1.2).shift(LEFT*1.4+DOWN*0.6)
        e0 = Ellipse(width=1.35, height=0.7, color=WHITE)
        e1 = Ellipse(width=0.8, height=0.45, color=WHITE)
        e2 = Ellipse(width=0.45, height=0.2, color=WHITE)
        e0.shift(LEFT*2.2+UP*0.15)
        e1.shift(LEFT*3.2+DOWN*0.55)
        e2.shift(LEFT*4+DOWN*0.9)
        self.play(Write(equations), Create(e1), Create(e2)) #, Create(e0)
        self.add(equations)
        self.wait(1)

class LinearSystemTransformationSceneTwoButFaster(LinearTransformationSlide):
    def __init__(self):
        LinearTransformationSlide.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
            show_basis_vectors=False
        )

    def construct(self):
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
        brace = Brace(self.A)
        words = brace.get_text("Transformation")
        words.add_background_rectangle()
        #self.add_foreground_mobject(words, brace)
        self.add_foreground_mobject(equa)
        self.add(brace)
        self.add(words)
        matrix = np.array([[2, 1], [2, 3]])
        self.moving_mobjects = []
        #self.apply_matrix(matrix,run_time=0.001)
        v = [-4, -1]
        x = np.linalg.solve(matrix.T, v)
        v = Vector(v, color = YELLOW)
        x = Vector(x, color = PINK)
        self.add(v)
        v_label = self.get_vector_label(v, "b", color = YELLOW)
        x_label = self.get_vector_label(x, "x", color = PINK)
        for label in x_label, v_label:
            label.add_background_rectangle()
        """ self.apply_inverse(matrix, run_time=0.01)
        self.remove(self.basis_vectors)
        self.play(
            Create(v),
            Write(v_label)
        ) """
        self.add_foreground_mobject(v_label)
        x = self.add_vector(x, animate = False)
        self.add(x)
        self.add(x_label)
        self.add(VGroup(x, x_label).copy().fade())
        self.wait(1)
        self.moving_mobjects = []
        self.apply_transposed_matrix(matrix, run_time=1)
        self.next_slide()

class LabeledExample(LinearSystemTransformationSlide):
    CONFIG = {
        "title" : "",
        "t_matrix" : [[0, 0], [0, 0]],
        "show_square" : False,
    }
    def setup(self):
        LinearSystemTransformationSlide.setup(self)
        title = Tex(self.title)
        title.next_to(self.equation, DOWN, buff = 1)
        title.add_background_rectangle()
        title.shift_onto_screen()
        self.add_foreground_mobject(title)        
        self.title = title
        if self.show_square:
            self.add_unit_square()

    def construct(self):
        self.wait()
        self.apply_transposed_matrix(self.t_matrix)
        self.wait()

class SystemOfTwoEquationsTwoUnknowns(Slide):
    def construct(self):
        system = Tex(r"""\begin{align*}
            2x + 2y &= -4 \\
            1x + 3y &= -1\end{align*}
        """)
        system.to_edge(UP)
        #print(len(system))
        #system[0][3].set_color(RED)
        for indices, color in ((1, 9), GREEN), ((4, 12), RED):
            for i in indices:
                system[0][i].set_color(color)
        matrix = Matrix([[2, 2], [1, 3]],
                        left_bracket="(",
            right_bracket=")")
        v = Matrix([[-4], [-1]], left_bracket="(",
            right_bracket=")")
        x = Matrix([["x"], ["y"]], left_bracket="(",
            right_bracket=")")
        x.get_entries().set_submobject_colors_by_gradient(GREEN, RED)
        matrix_system = VGroup(
            matrix, x, Tex("="), v
        )
        matrix_system.arrange(RIGHT)
        matrix_system.next_to(system, DOWN, buff = 1)
        matrix.label = "A"
        matrix.label_color = WHITE
        x.label = r"$\vec{\textbf{x}}$"
        x.label_color = PINK
        v.label = r"$\vec{\textbf{b}}$"
        v.label_color = YELLOW
        for mob in matrix, x, v:
            brace = Brace(mob)
            label = brace.get_text("$%s$"%mob.label)
            label.set_color(mob.label_color)
            brace.add(label)
            mob.brace = brace

        self.add(system)
        self.play(Write(matrix_system))
        self.next_slide()
        for mob in matrix, v, x:
            self.play(Write(mob.brace))
            self.next_slide()
        self.next_slide()

class IntoLowerDimension(LinearSystemTransformationSlide):
    def play_animation(self):
        self.t_matrix = np.array([[1.2, 0.6], [-1, -0.5]])
        self.moving_mobjects = []
        self.apply_transposed_matrix(self.t_matrix)

    def construct(self):
        self.setup()
        self.play_animation()
        words = Tex("A bildet auf einen Unterraum ab:").shift(1.5*UP+2.5*LEFT)
        words.add_background_rectangle()
        self.play(Write(words, run_time = 1))
        self.add_foreground_mobject(words)
        self.wait()
        self.next_slide()

class Bijektiv(LinearSystemTransformationSlide):
    def construct(self):
        self.setup()
        self.t_matrix = np.array([[1, 0.2], [0.2, 1]])
        self.moving_mobjects = []
        self.apply_transposed_matrix(self.t_matrix)
        words = Tex("A bleibt in "+r'$\mathbb{R}^2$:').shift(1.5*UP+2.5*LEFT)
        words.add_background_rectangle()
        self.play(Write(words, run_time = 1))
        self.add_foreground_mobject(words)
        self.wait()
        self.next_slide()

class DeterminantZero(LinearSystemTransformationSlide):
    def construct(self):
        self.setup()
        poly = Polygon([0.2,0.2,0],[0.1,1,0],[0.3,1.1,0],[2,2,0],[2.5,1,0],[1.3,0.13,0], fill_color=BLUE, fill_opacity=1).shift([0.4,0.4,0])
        text2 = Tex("Fläche").add_updater(lambda me: me.move_to(poly.get_center()))
        self.add_transformable_mobject(poly, text2)
        words = Tex("det(A)=0").shift(1.5*UP+2*LEFT)
        words.add_background_rectangle()
        self.play(Write(words, run_time = 1))
        self.add_foreground_mobject(words)
        self.t_matrix = np.array([[1.2, 0.6], [-1, -0.5]])
        self.moving_mobjects = []
        self.next_section()
        self.apply_transposed_matrix(self.t_matrix)
        self.wait()

class Inverse1(LinearTransformationSlide):
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
            self.apply_transposed_matrix([[3,0],[1,2]])

            matrix1 = Matrix([[3,1],[0,2]]).set_color(MAROON_C).add_background_rectangle()
            matrix1.to_corner(UP+RIGHT)
            matrix1brace = Brace(matrix1, DOWN).set_color(MAROON_C)
            matrix1bracetext = matrix1brace.get_text("A").set_color(MAROON_C).add_background_rectangle()
            text1=Tex("Abbildung:").next_to(matrix1, LEFT).add_background_rectangle()
            first = VGroup(text1, matrix1, matrix1brace, matrix1bracetext)

            self.add_foreground_mobject(first)
            self.wait()
            self.next_slide()

            matrix2 = Matrix([["1/3","-1/6"],["0","1/2"]]).set_color(YELLOW).add_background_rectangle()
            matrix2.to_corner(UP+RIGHT)
            matrix2brace = Brace(matrix2, DOWN).set_color(YELLOW)
            matrix2bracetext = matrix2brace.get_text(r"$A^{-1}$").set_color(YELLOW).add_background_rectangle()
            text2 = Tex("Inverse Abbildung:").next_to(matrix2, LEFT).add_background_rectangle()
            second = VGroup(text2, matrix2,matrix2brace,matrix2bracetext)

            self.play(Transform(first, second), Transform(text1,text2))
            self.apply_inverse_transpose([[3,0],[1,2]])
65
class Inverse2(LinearTransformationSlide):
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

            matrix1 = Matrix([[0,-1],[1,0]]).set_color(MAROON_C).add_background_rectangle()
            matrix1.to_corner(UP+RIGHT)
            matrix1brace = Brace(matrix1, DOWN).set_color(MAROON_C)
            matrix1bracetext = matrix1brace.get_text("A").set_color(MAROON_C).add_background_rectangle()
            text1=Tex("Abbildung:").add_background_rectangle().next_to(matrix1, LEFT)
            first = VGroup(text1, matrix1, matrix1brace, matrix1bracetext)

            self.add_foreground_mobject(first)

            self.apply_transposed_matrix([[0,1],[-1,0]])
            self.next_slide()

            matrix2 = Matrix([[0,1],[-1,0]]).set_color(YELLOW).add_background_rectangle()
            matrix2.to_corner(UP+RIGHT).shift(LEFT*0.2)
            matrix2brace = Brace(matrix2, DOWN).set_color(YELLOW)
            matrix2bracetext = matrix2brace.get_text(r"$A^{-1}$").set_color(YELLOW).add_background_rectangle()
            text2 = Tex("Inverse Abbildung:").add_background_rectangle().next_to(matrix2, LEFT)
            second = VGroup(text2, matrix2,matrix2brace,matrix2bracetext)

            self.play(Transform(first, second), Transform(text1,text2))
            self.moving_mobjects = []
            self.apply_inverse_transpose([[0,1],[-1,0]])
66
