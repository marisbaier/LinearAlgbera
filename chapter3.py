from manim import *
from manim_editor import PresentationSectionType
from manim.opengl import *
config.background_color = DARKER_GRAY
config["background_color"] = DARKER_GRAY
Tex.set_default(color=WHITE)

class Erweiterung(Scene):
    def construct(self):
        LineareAbbildung = Tex("Lineare Abbildung").move_to([0,3,0])
        self.play(Write(LineareAbbildung))

        self.wait()
        self.next_section()

        brace = Brace(mobject=LineareAbbildung[0][7:16], direction=DOWN, buff=0.2).shift([0,0.2,0])
        brace_text = brace.get_text("Funktion").scale(0.75).shift([0,0.2,0])
        brace_text.set_opacity(0.8)
        brace_text.set_color(YELLOW)
        self.play(LineareAbbildung[0][0:7].animate.set_color(GREY), GrowFromCenter(brace), FadeIn(brace_text))
        
        self.wait()
        self.next_section()

        zero = np.array([0,0,0])
        def polar(r, theta):
           return np.array([r*np.cos(theta/180*np.pi), r*np.sin(theta/180*np.pi), 0])
        a = np.array([-0.3,-1.3,0])
        b = a + polar(1.2,5)
        c = a + [0,1,0]
        d = c + polar(1.2,5)
        e = a + polar(0.5,90+40)
        f = c + polar(0.5,90+40)
        g = d + polar(0.5,90+40)
        line = Line(start=a, end=b)
        line2 = Line(start=c, end=d)
        line3 = Line(start=a, end=c)
        line4 = Line(start=b, end=d)
        line5 = Line(start=a, end=e)
        line6 = Line(start=c, end=f)
        line7 = Line(start=d, end=g)
        line8 = Line(start=e, end=f)
        line9 = Line(start=f, end=g)

        f = Text(text='f', font_size=25).move_to([0.3,-0.7,0])
        #ellipse = Ellipse(width=.5, height=.125, color=WHITE).move_to([-0.6,0.25,0])

        self.play(Write(line), Write(line2), Write(line3), Write(line4), Write(line5), Write(line6), Write(line7), Write(line8), Write(line9), Write(f), run_time=0.5)
        
        self.wait()
        self.next_section()

        curvedarrowin = CurvedArrow(start_point=[-1.2,1.2,0], end_point=[-0.1,0.5,0], angle=-0.6)
        x = Tex("x").move_to([-1.5,1.2,0])
        self.play(Create(curvedarrowin), Write(x))
        self.wait()
        y = Tex("y").move_to([1.9,-2.1,0])
        curvedarrowout = CurvedArrow(start_point=[0.4,-1.5,0], end_point=[1.5,-2,0], angle=0.5)
        self.play(Create(curvedarrowout), Write(y))

        self.wait()
        self.next_section()

        box = VGroup()
        box.add(line,line2,line3,line4,line5,line6,line7,line8,line9,f,x,y,curvedarrowin,curvedarrowout)
        axplusb = MathTex(r"x\mapsto ax+b").shift([3,-0.5,0])
        self.play(box.animate.shift([-2.2,0,0]), Write(axplusb))

        self.wait()
        self.next_section()

        morefunctions = MathTex(r"&x\mapsto x^2\\&x\mapsto \sqrt{x}\\&x\mapsto\sin(x)\\&x\mapsto e^x").shift([2.95,-1,0])
        self.play(axplusb.animate.shift([0,1.7,0]))
        self.play(Write(morefunctions), run_time=1.5)

        self.wait()
        self.next_section()

        self.remove(morefunctions)
        self.play(axplusb.animate.shift([0,-1.7,0]))

        self.wait()
        self.next_section()

        self.remove(axplusb)
        axis = Axes(x_range=[-.5,2.5], y_range=[-.5,3.5], x_length=3, y_length=3, tips=False).shift([3,-0.2,0])
        linear_func = axis.plot(
            lambda t: t,
            color=RED,
        )
        strecke = MathTex(r"s=v\cdot t").shift([3.3,1,0])
        self.play(Create(axis))
        self.play(Write(linear_func), FadeIn(strecke))

        self.wait()
        self.next_section()

        poly = axis.plot(
            lambda t: (4*t**3-9*t**2)/10+1.5,
            color=WHITE,
            x_range=[-.5,2.7,0.005]
        )
        deriv = axis.plot(
            lambda t: (4*1.45**3-9*1.45**2)/10+1.5-1.45*(1.5-1.45)*(t-1.45),
            color=RED,
        )
        point = Dot(color=RED).move_to(axis.coords_to_point(1.45,(4*1.45**3-9*1.45**2)/10+1.5))
        fofx = MathTex(r"").shift([3.2,1,0])

        self.play(ReplacementTransform(linear_func, poly), ReplacementTransform(strecke, fofx))
        self.play(Write(deriv), Write(point))

        self.wait()
        self.next_section()

        self.play(FadeOut(point), FadeOut(deriv), FadeOut(poly), FadeOut(axis))
        self.play(box.animate.shift([2.2,0,0]))

        self.wait()
        self.next_section()

        x1x2x3 = MathTex(r"x_1, x_2, ... , x_n", font_size=35).move_to([-2.35,1.2,0])
        y1y2y3 = MathTex(r"y_1, y_2, ... , y_m", font_size=35).move_to([2.7,-2,0])
        self.play(ReplacementTransform(x, x1x2x3))

        self.wait()
        self.next_section()

        x1x2vector = MathTex(r"(x_1, x_2, ... , x_n)", font_size=35).move_to([-2.4,1.2,0])
        self.play(ReplacementTransform(x1x2x3,x1x2vector))

        self.wait()
        self.next_section()

        self.play(ReplacementTransform(y, y1y2y3))
        y1y2vector = MathTex(r"(y_1, y_2, ... , y_m)", font_size=35).move_to([2.7,-2,0])
        self.play(ReplacementTransform(y1y2y3,y1y2vector))

        self.wait()
        self.next_section()
16
class TransformJustOneVector(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        #self.setup()

    def construct(self):
        numberplane = self.add_plane(animate=True).add_coordinates()
        v1_coords = [-3, 1]
        t_matrix = [[0, -1], [2, -1]]
        v1 = Vector(v1_coords, tip_length=0.2, color=YELLOW)
        self.add(numberplane, v1) 
        v2 = Vector(
            np.dot(np.array(t_matrix).transpose(), v1_coords),
            tip_length=0.2, color=PINK
        )
        for v, word in (v1, "Input"), (v2, "Output"):
            v.label = Tex("%s Vektor"%word)
            v.label.next_to(v.get_end(), UP)
            v.label.set_color(v.get_color())
            self.play(Create(v))
            self.next_section()
            self.play(Write(v.label))
            self.next_section()

        self.remove(v2)
        self.play(
            Transform(
                v1.copy(), v2, 
                path_arc = -np.pi/2, run_time = 3
            ),
            ApplyMethod(v1.fade),
            ApplyMethod(v1.label.fade)
        )
        self.next_section()
17
class MultipleVectors(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        vectors = VGroup(*[
            Vector([x, y], tip_length=0.2)
            for x in np.arange(-int(7)+0.5, int(7)+0.5)
            for y in np.arange(-int(4)+0.5, int(4)+0.5)
        ])
        vectors.set_submobject_colors_by_gradient(PINK, PURE_BLUE, BLUE, GREEN_E, YELLOW)
        self.play(Create(vectors, lag_ratio = 0.5))
        t_matrix = [[2, 1], [1, 2]]
        transformed_vectors = VGroup(*[
            Vector(
                np.dot(np.array(t_matrix).transpose(), v.get_end()[:2]),
                color = v.get_color()
            )
            for v in vectors.split()
        ])
        transformed_vectors.set_submobject_colors_by_gradient(PINK, PURE_BLUE, BLUE, GREEN_E, YELLOW)
        self.next_section()
        self.play(Transform(
                vectors, transformed_vectors,
                run_time = 3,
                path_arc = -np.pi/2
            ))
        self.next_section(type=PresentationSectionType.NORMAL)
        self.remove(vectors)
        vectors = VGroup(*[
            Vector([x, y], tip_length=0.2)
            for x in np.arange(-int(7)+0.5, int(7)+0.5)
            for y in np.arange(-int(4)+0.5, int(4)+0.5)
        ])
        vectors.set_submobject_colors_by_gradient(PINK, PURE_BLUE, BLUE, GREEN_E, YELLOW)
        self.add(vectors)
        #self.wait()
        dots = VGroup(*[
            Dot([x, y, 0])
            for x in np.arange(-int(7)+0.5, int(7)+0.5)
            for y in np.arange(-int(4)+0.5, int(4)+0.5)
        ])
        dots.set_submobject_colors_by_gradient(PINK, PURE_BLUE, BLUE, GREEN_E, YELLOW)
        self.next_section()
        self.play(Transform(vectors, dots, run_time=3))
        self.next_section()
        transformed_dots = VGroup(*[
            Dot([2*x+y, 2*y+x, 0])
            for x in np.arange(-int(7)+0.5, int(7)+0.5)
            for y in np.arange(-int(4)+0.5, int(4)+0.5)
        ])
        transformed_dots.set_submobject_colors_by_gradient(PINK, PURE_BLUE, BLUE, GREEN_E, YELLOW)
        self.remove(vectors)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Transform(
                dots, transformed_dots,
                run_time=3,
            ))
        self.next_section(type=PresentationSectionType.NORMAL)
18
class TransformInfiniteGrid(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            include_background_plane=False,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )

    def construct(self):
        self.next_section()
        self.wait()
        self.moving_mobjects = []
        self.next_section()
        matrix = [[2, 1], [1, 2]]
        self.apply_matrix(matrix)
        self.wait()
19
class TransformInfiniteGridWithBackground(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )

    def construct(self):
        self.next_section()
        self.wait()
        self.moving_mobjects = []
        self.next_section()
        matrix = [[2, 1], [1, 2]]
        self.apply_matrix(matrix)
        self.wait(2)
20
class ApplyComplexFunction(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )

    def construct(self):
        self.wait()
        self.moving_mobjects = []
        self.next_section()
        self.plane.prepare_for_nonlinear_transform(100)
        self.wait()
        self.play(ApplyMethod(
            self.plane.apply_complex_function, lambda z : 0.5*z**2,
            run_time = 5,
            path_arc = np.pi/2
        ))
        self.wait(2)
21
class ExponentialTransformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )

    def construct(self):
        self.wait()
        self.moving_mobjects = []
        self.next_section()
        self.plane.prepare_for_nonlinear_transform(100)
        self.wait()
        self.play(ApplyMethod(
            self.plane.apply_complex_function, np.exp,
            run_time = 5,
            path_arc = np.pi/2
        ))
        self.wait(2)
22
class CrazyTransformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )

    def construct(self):
        self.wait()
        self.moving_mobjects = []
        self.next_section()
        self.plane.prepare_for_nonlinear_transform(100)
        self.wait()
        self.play(ApplyMethod(
            self.plane.apply_complex_function, lambda z : np.sin(z)**2 + np.sinh(z),
            run_time = 5,
            path_arc = np.pi/2
        ))
23
class Back(Scene):
    def construct(self):
        LineareAbbildung = Tex("Lineare Abbildung").move_to([0,3,0])
        brace = Brace(mobject=LineareAbbildung[0][7:16], direction=DOWN, buff=0.2).shift([0,0.2,0])
        brace_text = brace.get_text("Funktion").scale(0.75).shift([0,0.2,0])
        brace_text.set_opacity(0.8)
        brace_text.set_color(YELLOW)
        LineareAbbildung[0][0:7].set_color(GREY)
        self.add(LineareAbbildung, brace, brace_text)

        self.wait()
        self.next_section()

        brace2 = Brace(mobject=LineareAbbildung[0][0:7], direction=DOWN, buff=0.2)
        brace2_text = brace2.get_text('''Was ist ``linear''?''').scale(0.75).shift([0,0.2,0])
        brace2_text.set_opacity(0.8)
        brace2_text.set_color(BLUE)
        self.play(ReplacementTransform(brace,brace2), 
                  ReplacementTransform(brace_text,brace2_text),
                  LineareAbbildung[0][0:7].animate.set_color(WHITE),
                  LineareAbbildung[0][7:16].animate.set_color(GREY),
                  )
        self.wait()
24
class TransformInfiniteGridWithBackground2(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        self.wait()
        self.moving_mobjects = []

        matrix = [[2, 1], [1, 2]]
        self.apply_matrix(matrix)
        
        self.wait()
        self.next_section()

        lines_rule = Tex("Linien bleiben Linien")
        lines_rule.shift(2*UP).to_edge(LEFT)
        origin_rule = Tex("Ursprung bleib im Ursprung")
        origin_rule.shift(2*UP).to_edge(RIGHT)
        arrow = Arrow(origin_rule, ORIGIN)
        dot = Dot(ORIGIN, radius = 0.1, color = RED)

        for rule in lines_rule, origin_rule:
            rule.add_background_rectangle()

        self.play(
            Write(lines_rule, run_time = 2),
        )

        self.wait()
        self.play(
            Write(origin_rule, run_time = 2),
            Create(arrow),
            GrowFromCenter(dot)
        )
        self.wait()
        self.next_section()
25
def curvy_squish(point):
    x, y, z = point
    return (x+np.cos(y))*RIGHT + (y+np.sin(x))*UP
26
class SimpleNonlinearTransformationScene(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
        )

    def construct(self):
        self.setup()
        self.apply_nonlinear_transformation(self.func)
        words = Tex("nichtlinear: manche Linien werden gekrümmt")
        words.to_corner(UP+RIGHT)
        words.set_color(RED)
        words.add_background_rectangle()
        self.play(Write(words))
        self.wait()

    def func(self, point):
        return curvy_squish(point)
27  
class MovingOrigin(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
        )

    def construct(self):
        self.setup()
        dot = Dot(ORIGIN, color = RED)
        self.add_transformable_mobject(dot)
        self.apply_nonlinear_transformation(self.func)
        words = Tex("nichtlinear: Ursprung bewegt sich")
        words.to_corner(UP+RIGHT)
        words.set_color(RED)
        words.add_background_rectangle()
        self.play(Write(words))
        self.wait()
    
    def func(self, point):
        matrix_transform = self.get_matrix_transformation([[2, 0], [1, 1]])
        return matrix_transform(point) + 2*UP+3*LEFT
28
class SneakyNonlinearTransformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
        )

    def construct(self):
        self.setup()
        self.apply_nonlinear_transformation(self.func)
        words = Tex("")
        words.to_corner(UP+RIGHT)
        words.set_color(RED)
        words.add_background_rectangle()    
        self.play(Write(words))
        self.wait()

    def func(self, point):
        x, y, z = point
        new_x = np.sign(x)*(int(7)+0.5)*smooth(abs(x) / (int(7)+0.5))
        new_y = np.sign(y)*(int(4)+0.5)*smooth(abs(y) / (int(4)+0.5))
        return [new_x, new_y, 0]
29    
class SneakyNonlinearTransformationExplained(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
        )

    def construct(self):
        self.setup()
        FRAME_Y_RADIUS = int(4)+0.5
        FRAME_X_RADIUS = int(7)+0.5
        diag = Line(
            FRAME_Y_RADIUS*LEFT+FRAME_Y_RADIUS*DOWN,
            FRAME_Y_RADIUS*RIGHT + FRAME_Y_RADIUS*UP
        )
        diag.insert_n_curves(20)
        diag.make_smooth()
        diag.set_color(YELLOW)
        self.add_transformable_mobject(diag)
        #self.play(Create(diag))
        self.apply_nonlinear_transformation(self.func)
        words = Tex("nichtlinear: Diagonelen werden gekrümmt")
        words.to_corner(UP+RIGHT)
        words.set_color(RED)
        words.add_background_rectangle()    
        self.play(Write(words))
        self.wait()

    def func(self, point):
        x, y, z = point
        new_x = np.sign(x)*(int(7)+0.5)*smooth(abs(x) / (int(7)+0.5))
        new_y = np.sign(y)*(int(4)+0.5)*smooth(abs(y) / (int(4)+0.5))
        return [new_x, new_y, 0]
30  
class GridlinesRemainParallel(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )

    def construct(self):
        self.next_section()
        self.wait()
        self.moving_mobjects = []
        self.next_section()
        matrix = [[3, 1], [0, 2]]
        self.apply_matrix(matrix)
        self.wait(2)
        text = Tex(r'''Gitterlinien bleiben parallel und gleich gespaced''')
        text[0][19:27].set_color(YELLOW)
        text[0][36:48].set_color(GREEN)
        text.add_background_rectangle()
        text.shift(-text.get_bottom())
        self.play(Write(text))
        self.wait()
31
class Rotation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        self.wait()
        self.moving_mobjects = []

        self.angle = -np.pi/3
        matrix = [
            [np.cos(self.angle), np.sin(self.angle)], 
            [-np.sin(self.angle), np.cos(self.angle)]
        ]
        self.apply_matrix(matrix)

        self.wait()
32
class YetAnotherLinearTransformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        self.wait()
        self.moving_mobjects = []

        matrix = np.array([
            [-1, 1],
            [3, 2],
        ])
        self.apply_matrix(matrix)

        self.wait()

        text = Tex(
            r'''Wie beschreiben wir das\\
            mit Zahlen?'''
        )
        text.to_edge(UP)
        text[0].set_color(GREEN)
        text.add_background_rectangle()

        self.next_section()
        self.play(Write(text))

        self.next_section()

        matrix_1 = Matrix([["x_\\text{in}"],["y_\\text{in}"]])
        rightarrow = Tex(r"$\quad\rightarrow \quad????\quad\rightarrow\quad$")
        matrix_2 = Matrix([["x_\\text{out}"],["y_\\text{out}"]])
        formula = VGroup(*[matrix_1,rightarrow,matrix_2])
        formula.arrange(buff=0.1)

        formula.add_background_rectangle()

        self.next_section()

        self.play(
            ApplyMethod(self.plane.fade, 0.7),
            ApplyMethod(self.background_plane.fade, 0.7),
            Write(formula, run_time = 2),
            Animation(text)
        )
        self.wait()
33
class Follow_ex_ey(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        #i_hat, j_hat = self.get_basis_vectors()
        i_hat = self.add_vector([1,0], color = GREEN, animate=False)
        i_hat_label = self.label_vector(
            i_hat, "\\vec{e}_x", 
            color = GREEN,
            label_scale_factor = 1,
            animate = False
        ).scale(0.8)
        self.play(Create(i_hat), Create(i_hat_label))

        j_hat = self.add_vector([0,1], color = RED, animate=False)
        j_hat_label = self.label_vector(
            j_hat, "\\vec{e}_y", 
            color = RED,
            label_scale_factor = 1,
            animate = False
        ).scale(0.8)
        self.play(Create(j_hat), Create(j_hat_label))

        self.next_section()
        self.play(*list(map(FadeOut, [i_hat_label, j_hat_label])))
        self.moving_mobjects = []
        self.apply_transposed_matrix([[-1, 1], [-2, -1]])
        self.wait()
34
class TrackBasisVectorsExample(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        self.i_hat = self.add_vector([1,0], color = GREEN, animate=False)
        self.j_hat = self.add_vector([0,1], color = RED, animate=False)
        self.v_coords = [-1,2]
        v = self.add_vector([-1,2], color=YELLOW)
        coords = Matrix([[self.v_coords[0]],[self.v_coords[1]]])
        coords.scale(1)
        coords.next_to(v.get_end(), np.sign(self.v_coords[0])*RIGHT)
        self.play(Write(coords), run_time=1)

        v_def = self.get_v_definition()
        pre_def = VGroup(
            VectorizedPoint(coords.get_center()),
            VGroup(*[
                mob.copy()
                for mob in np.array(coords.get_mob_matrix(), dtype=object).flatten()
            ])
        )
        self.play(Transform(
            pre_def, v_def, 
            run_time = 2, 
            lag_ratio = 0
        ))
        self.remove(pre_def)
        self.add_foreground_mobject(v_def)
        self.wait()
        self.show_linear_combination(clean_up = False)
        self.play(FadeOut(i_hat_copy), FadeOut(j_hat_copy), FadeOut(coords))
        self.moving_mobjects = []
        self.apply_transposed_matrix([[1,-2],[3,0]])

        triplets = [
            (self.i_hat, "\\text{Neuer }\\vec{e}_x", GREEN, [-0.1,-0.25,0]),
            (self.j_hat, "\\text{Neuer }\\vec{e}_y", RED, [0.25,-0.1,0]),
        ]
        label_mobs = []
        for vect, label, color, shift in triplets:
            label_mobs.append(self.add_transformable_label(
                vect, label, "\\text{Transformed } " + label,
                color = color,
                direction = "right",
                animate = False,
            ).shift(shift))
        self.play(Write(label_mobs[0]), Write(label_mobs[1]))
        self.i_label, self.j_label = label_mobs

        self.show_linear_combination(shift=[[-1,2,0],[1.5,0,0]])

        self.next_section()

        v_def = Tex(r'''Neuer $\vec{\textbf{v}}=-1 (neuer) \vec{\textbf{e}}_x+2 (neuer) \vec{\textbf{e}}_y$''')
        v_def[0][0:8].set_color(YELLOW)
        v_def[0][10:20].set_color(GREEN)
        v_def[0][22:34].set_color(RED)
        v_def.add_background_rectangle()
        v_def.to_corner(UP + LEFT).shift([0,-1,0])
        self.v_def = v_def

        self.play(Write(self.v_def))

        self.next_section()

        t1=Tex("=-1")
        m1 = Matrix([[1],[-2]]).set_row_colors(GREEN,GREEN)
        t2 = Tex("+2")
        m2 = Matrix([[3],[0]]).set_row_colors(RED,RED)
        group1 = VGroup(t1,m1,t2,m2).arrange().next_to(self.v_def,DOWN).to_edge(LEFT).add_background_rectangle()
        self.play(Write(group1))
        self.next_section()
        m3 = Matrix([["-1(1)+2(3)"],["-1(-2)+2(0)"]])
        t3 = Tex("=")
        m4 = Matrix([[5],[2]])
        t4 = Tex("=")
        group2 = VGroup(t3,m3,t4,m4).arrange().next_to(group1,DOWN).add_background_rectangle().scale(0.7).to_edge(LEFT)
        self.play(Write(group2))

        #self.write_linear_map_rule()
        #self.show_basis_vector_coords()
    
    def get_v_definition(self):
        v_def = Tex(r'''$\vec{\textbf{v}}=-1\vec{\textbf{e}}_x+2\vec{\textbf{e}}_y$''')
        v_def[0][0:2].set_color(YELLOW)
        v_def[0][5:8].set_color(GREEN)
        v_def[0][10:14].set_color(RED)
        v_def.add_background_rectangle()
        v_def.to_corner(UP + LEFT)
        self.v_def = v_def
        return v_def
    
    def show_linear_combination(self, shift=[[-1,0,0],[0,0.5,0]] ,clean_up = True):
        global i_hat_copy, j_hat_copy
        i_hat_copy, j_hat_copy = [m.copy() for m in (self.i_hat, self.j_hat)]
        self.play(ApplyFunction(
            lambda m : m.scale(self.v_coords[0]).shift(shift[0]).fade(0.3),
            i_hat_copy
        ))
        self.play(ApplyFunction(
            lambda m : m.scale(self.v_coords[1]).shift(shift[1]).fade(0.3),
            j_hat_copy
        ))
        self.play(ApplyMethod(j_hat_copy.shift, i_hat_copy.get_end()))
        self.wait(2)
        if clean_up:
            self.play(FadeOut(i_hat_copy), FadeOut(j_hat_copy))
35  
class YouGiveMeVector(Scene):
    def construct(self):
        exto = Tex(r'''$\vec{e}_x\to$''')
        eyto = Tex(r'''$\vec{e}_y\to$''')

        ex = Matrix([[1], [-2]])
        ey = Matrix([[3], [0]])

        exx = VGroup(exto,ex).arrange().set_color(GREEN)
        eyy = VGroup(eyto,ey).arrange().set_color(RED)

        exx.to_edge(UP).shift(2*LEFT)
        eyy.to_edge(UP).shift(2*RIGHT)

        self.add(exx, eyy)

        self.wait()
        self.next_section()

        x = Matrix([["x"],["y"]]).set_row_colors(YELLOW,YELLOW)
        m1 = ex.copy()
        m2 = ey.copy()
        to = Tex(r"$\to x$")
        plus = Tex(r"$+y$")
        equals = Tex("=")
        m3 = Matrix([["1x+3y"],["-2x+0y"]])
        group = VGroup(x,to,m1,plus,m2,equals,m3).arrange()

        self.play(FadeIn(x),FadeIn(to),FadeIn(plus),FadeIn(m1),FadeIn(m2))

        self.wait()
        self.next_section()
        
        self.play(FadeIn(equals), FadeIn(m3))
36
class CompletelyDescribed(LinearTransformationScene):
    def construct(self):
        self.setup()
        self.apply_transposed_matrix([[3,-2],[2,1]])

        ex, ey = self.get_basis_vectors()

        exvec = Matrix([[3],[-2]]).set_color(GREEN).next_to(ex.get_end(), RIGHT).shift(2.2*RIGHT+2.5*DOWN)
        eyvec = Matrix([[2],[1]]).set_color(RED).next_to(ey.get_end(), RIGHT).shift(2.2*RIGHT+0.3*UP)

        self.play(Write(exvec), Write(eyvec))
        
        self.wait()
        self.next_section()

        matrix = Matrix([[3,2], [-2,1]]).set_column_colors(GREEN,RED).to_edge(UP)
        print(self.mobjects)
        self.play(FadeOut(self.background_plane), FadeOut(self.plane), FadeOut(ex), FadeOut(ey),FadeOut(self.mobjects[2]))
        self.play(Transform(exvec, VGroup(matrix.submobjects[0][0],matrix.submobjects[0][2])),
                  Transform(eyvec, VGroup(matrix.submobjects[0][1],matrix.submobjects[0][3])),
                  Write(matrix),
                  
                  )
        
        text = Tex('''"2x2 Matrix"''').to_corner(LEFT+UP)

        self.next_section()
        self.play(Write(text))

        twovectors = VGroup(*[
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([-1.4,0,0],[-0.75,1.5,0]),
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([1.4,0,0],[0.85,1.5,0]),
            ]).set_color(YELLOW)
        
        rec1 = Ellipse(color=GREEN, height=1.5,width=0.8).move_to(matrix.get_center()).shift(0.5*LEFT)
        rec2 = Ellipse(color=RED, height=1.5,width=0.8).move_to(matrix.get_center()).shift(0.85*RIGHT)
        
        woex = Tex(r"Wo $\vec{e}_x$ landet").next_to(twovectors[0],DOWN).shift(LEFT).set_color(GREEN)
        woey = Tex(r"Wo $\vec{e}_y$ landet").next_to(twovectors[1],DOWN).shift(RIGHT).set_color(RED)

        self.play(Create(rec1))
        self.play(Create(twovectors[0]), Write(woex))

        self.next_section()
        self.play(Create(rec2))
        self.play(Create(twovectors[1]), Write(woey))

        input = Matrix([[5],[7]]).next_to(matrix).shift(1*RIGHT)
        brace = Brace(input)
        bracetext = Tex("Inputvektor").next_to(brace, DOWN)

        self.play(FadeOut(rec1), FadeOut(rec2), FadeOut(twovectors), FadeOut(woex), FadeOut(woey))
        self.play(Create(VGroup(input,brace)), Write(bracetext))

        group = VGroup(
            Tex("5"),
            Matrix([[3],[-2]]).set_column_colors(GREEN),
            Tex("+7"),
            Matrix([[2],[1]]).set_column_colors(RED),
        ).arrange()
        self.play(Transform(VGroup(matrix,input).copy(),group))

        self.wait()
        self.next_section()
        self.clear()
        self.add(text)
        self.wait()
        

        matrix2 = Matrix([["a","b"], ["c","d"]]).set_column_colors(GREEN,RED).to_edge(UP)
        self.play(
                  Write(matrix2),
                  )

        input = Matrix([["x"],["y"]]).next_to(matrix2).shift(1*RIGHT)
        brace = Brace(input)
        bracetext = Tex("Inputvektor").next_to(brace, DOWN)

        self.play(Create(VGroup(input,brace)), Write(bracetext))

        group = VGroup(
            Tex("x"),
            Matrix([["a"],["c"]]).set_column_colors(GREEN),
            Tex("+y"),
            Matrix([["b"],["d"]]).set_column_colors(RED),
            Tex("="),
            Matrix([["ax+by"],["cx+dy"]]),
        ).arrange().shift(DOWN).shift(2*RIGHT)
        self.play(Transform(VGroup(matrix2,input).copy(),group[0:4]))

        self.next_section()
        self.play(Write(group[-2]),Write(group[-1]))

        self.next_section()

        self.play(matrix2.animate.shift(4.9*LEFT+3.68*DOWN),FadeOut(brace),FadeOut(bracetext))
        self.play(input.animate.next_to(matrix2,RIGHT))
        self.play(Create(Tex(":=").next_to(input,RIGHT)))

        newbrace = Brace(group[0:4])
        btext = Tex("Intuition?!!!!11?!!!").next_to(newbrace, DOWN)

        self.next_section()

        self.play(Create(newbrace), Write(btext))
37
class isntitmorefun(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_background_plane=True,
            show_basis_vectors=True,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        matrixx = [[3,1],[1,2]]
        matrix = Matrix(matrixx).set_column_colors(GREEN,RED).to_corner(UP+LEFT).add_background_rectangle()
        v = Matrix([[-1],[2]]).set_column_colors(YELLOW).next_to(matrix,RIGHT).add_background_rectangle()

        self.add(matrix,v)
        self.wait(0.5)
        self.moving_mobjects = []
        self.apply_transposed_matrix(matrixx, run_time=1.5)
        
        ex, ey = self.get_basis_vectors()
        group = VGroup(
            Matrix([[3],[1]]).set_color(GREEN).next_to(ex).add_background_rectangle().shift(2*RIGHT+UP),
            Matrix([[1],[2]]).set_color(RED).next_to(ey).add_background_rectangle().shift(-1*LEFT+2*UP)
        )
        self.play(Transform(matrix.copy(),group))
        self.wait()

        new1 = Vector([-3,-1,0], color=GREEN)
        new2 = Vector([2,4,0], color=RED).shift(new1.get_end())

        self.play(Create(new1), Tex("-1", color=YELLOW).move_to(v.get_center()+0.5*UP).animate.next_to(new1,DOWN).shift(0.5*UP))
        self.play(Create(new2), Tex("2", color=YELLOW).move_to(v.get_center()+0.5*DOWN).animate.next_to(new2,LEFT).shift(0.75*RIGHT))

        self.play(Create(Vector([-1,3,0], color=YELLOW)))
38
class letspractise(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_background_plane=True,
            show_basis_vectors=True,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        emptymatrix = Matrix([["0","0"],["0","0"]]).to_corner(UP+LEFT).set_column_colors(GREEN,RED)
        emptymatrix.add_background_rectangle()
        emptymatrix[1][0] = Tex("")
        emptymatrix[1][1] = Tex("")
        emptymatrix[1][2] = Tex("")
        emptymatrix[1][3] = Tex("")

        self.add_foreground_mobject(emptymatrix)

        self.apply_transposed_matrix([[0,1],[-1,0]])

        text = Tex(r"90$\circ$ Drehung gegen den Uhrzeigersinn").shift(DOWN).add_background_rectangle()
        self.play(Write(text))

        ex, ey = self.get_basis_vectors()

        m1 = Matrix([[0],[1]]).set_color(GREEN).shift(UP+LEFT).set_z_index(30)
        m2 = Matrix([[-1],[0]]).set_color(RED).shift(2*LEFT+0.2*UP).set_z_index(31)

        self.next_section()
        self.play(Write(m1))
        self.next_section()
        self.play(m1[0][0].animate.shift([-5,1.8,0]), m1[0][1].animate.shift([-5,1.65,0]), FadeOut(m1[1]), FadeOut(m1[2]))
        self.next_section()
        self.play(Write(m2))
        self.next_section()
        self.play(m2[0][0].animate.shift([-5,1.8,0]).shift([1.9,0.8,0]), m2[0][1].animate.shift([-5,1.65,0]).shift([1.9,0.8,0]), FadeOut(m2[1]), FadeOut(m2[2]))

        self.next_section()
        self.moving_mobjects = []
        self.apply_inverse_transpose([[0,1],[-1,0]], run_time=1)
        vnew = self.add_vector([1,2,0], color=YELLOW, max_tip_length_to_length_ratio=0.15)
        self.moving_mobjects = []
        self.apply_transposed_matrix([[0,1],[-1,0]])

        xvector = Matrix([["x"],["y"]]).set_column_colors(YELLOW).next_to(emptymatrix,RIGHT)
        self.play(Write(xvector))
39
class funTrafo(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_background_plane=True,
            show_basis_vectors=True,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        emptymatrix = Matrix([["0","0"],["0","0"]]).to_corner(UP+LEFT).set_column_colors(GREEN,RED)
        emptymatrix.add_background_rectangle()
        emptymatrix[1][0] = Tex("")
        emptymatrix[1][1] = Tex("")
        emptymatrix[1][2] = Tex("")
        emptymatrix[1][3] = Tex("")

        self.add_foreground_mobject(emptymatrix)

        self.apply_transposed_matrix([[1,0],[1,1]])

        text = Tex(r'''"Scheerung"''').shift(DOWN).add_background_rectangle()
        self.play(Write(text))

        m1 = Matrix([[1],[0]]).set_color(GREEN).shift(2*RIGHT +0.2*UP).set_z_index(30)
        m2 = Matrix([[1],[1]]).set_color(RED).shift(RIGHT+UP).set_z_index(31)

        self.next_section()
        self.play(Write(m1))
        self.next_section()
        self.play(m1[0][0].animate.shift([-5,1.8,0]).shift([-3,0.75,0]), m1[0][1].animate.shift([-5,1.65,0]).shift([-3,0.75,0]), FadeOut(m1[1]), FadeOut(m1[2]))
        self.next_section()
        self.play(Write(m2))
        self.next_section()
        self.play(m2[0][0].animate.shift([-5,1.8,0]).shift([-1,-0.05,0]), m2[0][1].animate.shift([-5,1.65,0]).shift([-1,-0.05,0]), FadeOut(m2[1]), FadeOut(m2[2]))

        self.wait()

        self.next_section()
        self.moving_mobjects = []
        self.apply_inverse_transpose([[1,0],[1,1]], run_time=1)
        vnew = self.add_vector([1,2,0], color=YELLOW, max_tip_length_to_length_ratio=0.15)
        self.moving_mobjects = []
        self.apply_transposed_matrix([[1,0],[1,1]])

        xvector = Matrix([["x"],["y"]]).set_column_colors(YELLOW).next_to(emptymatrix,RIGHT)
        self.play(Write(xvector))
40
class UndAndersherum(Scene):
    def construct(self):
        text = Tex("Und andersherum?")
        self.play(Write(text))
41
class UndAndersherum2(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_background_plane=True,
            show_basis_vectors=True,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        matrix = Matrix([["1","3"],["2","1"]]).to_corner(UP+LEFT).set_column_colors(GREEN,RED)
        matrix.add_background_rectangle()
        self.add(matrix)

        self.wait()
        self.next_section()
        self.moving_mobjects = []
        m1 = Matrix([[1],[2]]).set_color(GREEN).shift(1.7*RIGHT +2.3*UP).set_z_index(30)
        self.apply_transposed_matrix([[1,2],[0,1]])
        self.play(Transform(matrix.copy(),m1))

        self.next_section()
        self.moving_mobjects = []
        m2 = Matrix([[3],[1]]).set_color(RED).shift(3.8*RIGHT +1*UP).set_z_index(30)
        self.apply_transposed_matrix([[-5,0],[3,1]])
        self.play(Transform(matrix.copy(),m2))
42
class Mitmachspiel(Scene):
    def construct(self):
        text = Tex("Mitmachspiel!!!!!!").set_color_by_gradient(RED,YELLOW,PINK)
        self.play(Write(text))
43
class Untervektorraum(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_background_plane=True,
            show_basis_vectors=True,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        matrix = Matrix([["2","-2"],["1","-1"]]).to_corner(UP+LEFT).set_column_colors(GREEN,RED)
        matrix.add_background_rectangle()
        text = Tex("Linear abhängige", color=YELLOW).next_to(matrix,DOWN).shift(0.7*RIGHT)
        text2 = Tex("Spaltenvektoren", color=YELLOW).next_to(text,DOWN).shift(0*RIGHT)
        self.add(matrix,text,text2)

        self.wait()
        self.next_section()
        self.moving_mobjects = []
        m1 = Matrix([[2],[1]]).set_color(GREEN).shift(1.7*RIGHT-0.6*UP).set_z_index(30)
        self.apply_transposed_matrix([[2,1],[0,1]])
        self.play(Transform(matrix.copy(),m1))

        self.next_section()
        self.moving_mobjects = []
        m2 = Matrix([[-2],[-1]]).set_color(RED).shift(-2.8*RIGHT).set_z_index(30)
        self.apply_transposed_matrix([[2,1],[-2,-1]])
        self.play(Transform(matrix.copy(),m2))
44
class sumUp(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=False,
            background_plane_kwargs={'faded_line_ratio':2}
        )

    def construct(self):
        self.next_section()
        self.wait()
        self.moving_mobjects = []
        self.next_section()
        matrix = [[3, 1], [0, 2]]
        self.apply_matrix(matrix)
        self.wait(2)
        text = Tex(r'''Gitterlinien bleiben parallel und gleich gespaced''')
        text[0][19:27].set_color(YELLOW)
        text[0][36:48].set_color(GREEN)
        text.add_background_rectangle()
        text.shift(-text.get_bottom())
        self.play(Write(text))
        self.wait()
45
class sumUp2(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=True,
            background_plane_kwargs={'faded_line_ratio':2}
        )

    def construct(self):
        self.apply_transposed_matrix([[3,-2],[2,1]])
        m1 = Matrix([[3],[-2]]).set_color(GREEN).shift(4*RIGHT-2*UP).set_z_index(30)
        m2 = Matrix([[2],[1]]).set_color(RED).shift(2.7*RIGHT+1*UP).set_z_index(31)
        self.play(Write(m1))
        self.play(Write(m2))

        matrix = Matrix([[3,2], [-2,1]]).set_column_colors(GREEN,RED).to_edge(UP)
        print(self.mobjects)
        self.play(FadeOut(self.background_plane), FadeOut(self.plane), FadeOut(self.i_hat), FadeOut(self.j_hat),FadeOut(self.mobjects[2]))
        self.play(Transform(m1, VGroup(matrix.submobjects[0][0],matrix.submobjects[0][2])),
                  Transform(m2, VGroup(matrix.submobjects[0][1],matrix.submobjects[0][3])),
                  Write(matrix),
                  
                  )
        
        text = Tex('''"2x2 Matrix"''').to_corner(LEFT+UP)

        self.next_section()
        self.play(Write(text))

        twovectors = VGroup(*[
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([-1.4,0,0],[-0.75,1.5,0]),
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([1.4,0,0],[0.85,1.5,0]),
            ]).set_color(YELLOW)
        
        rec1 = Ellipse(color=GREEN, height=1.5,width=0.8).move_to(matrix.get_center()).shift(0.5*LEFT)
        rec2 = Ellipse(color=RED, height=1.5,width=0.8).move_to(matrix.get_center()).shift(0.85*RIGHT)
        
        woex = Tex(r"Wo $\vec{e}_x$ landet").next_to(twovectors[0],DOWN).shift(LEFT).set_color(GREEN)
        woey = Tex(r"Wo $\vec{e}_y$ landet").next_to(twovectors[1],DOWN).shift(RIGHT).set_color(RED)

        self.play(Create(rec1))
        self.play(Create(twovectors[0]), Write(woex))

        self.next_section()
        self.play(Create(rec2))
        self.play(Create(twovectors[1]), Write(woey))

        self.next_section()

        self.play(FadeOut(rec1), FadeOut(rec2), FadeOut(twovectors), FadeOut(woex), FadeOut(woey))

        group = VGroup(
            Matrix([["a","b"], ["c","d"]]).set_column_colors(GREEN,RED),
            Tex(":="),
            Tex("x"),
            Matrix([["a"],["c"]]).set_column_colors(GREEN),
            Tex("+y"),
            Matrix([["b"],["d"]]).set_column_colors(RED),
            Tex("="),
            Matrix([["ax+by"],["cx+dy"]]),
        ).arrange().shift(DOWN)
    
        self.play(FadeIn(group))
46
class YouCanInterpretMatrices(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            include_background_plane=True,
            show_basis_vectors=True,
            background_plane_kwargs={'faded_line_ratio':2}
        )
        self.setup()

    def construct(self):
        matrix = Matrix([["1","3"],["2","1"]]).to_corner(UP+LEFT).set_column_colors(GREEN,RED)
        matrix.add_background_rectangle()
        self.add(matrix)

        self.wait()
        self.next_section()
        self.moving_mobjects = []
        m1 = Matrix([[1],[2]]).set_color(GREEN).shift(1.7*RIGHT +2.3*UP).set_z_index(30)
        self.apply_transposed_matrix([[1,2],[0,1]])
        self.play(Transform(matrix.copy(),m1))

        self.next_section()
        self.moving_mobjects = []
        m2 = Matrix([[3],[1]]).set_color(RED).shift(3.8*RIGHT +1*UP).set_z_index(30)
        self.apply_transposed_matrix([[-5,0],[3,1]])
        self.play(Transform(matrix.copy(),m2))
47