from manim import *
# from manim_editor import PresentationSectionType
from manim_slides import *
from manim.opengl import *
config.background_color = DARKER_GRAY
config["background_color"] = DARKER_GRAY
Tex.set_default(color=WHITE)

class VectorSlide(Slide, VectorScene):
    pass

class CoordinatesAsScalars(VectorSlide):
    def construct(self):
        numberplane = NumberPlane(faded_line_ratio=2, background_line_style={'stroke_color': config.background_color}, faded_line_style={'stroke_color': config.background_color})
        self.add(numberplane)

        # self.next_section()  

        v = Vector([1,2], color=YELLOW, stroke_width=2)
        self.play(Create(v))
        array, x_line, y_line = self.vector_to_coords(v)

        self.add(array)

        self.play(array.animate.shift([-0.75,1,0]))

        v2 = Vector([3,-2], color=PINK, stroke_width=2)
        self.play(Create(v2))

        array2, x_line2, y_line2 = self.vector_to_coords(v2)

        self.add(array2)

        starting_mobjects = [v,v2]
        starting_mobjects = self.mobjects
        starting_mobjects.remove(numberplane)

        title = Tex("Skalierungsfaktoren")
        title.to_edge(UP)
        title.add_background_rectangle()
        x, y = np.array(array2.get_mob_matrix(), dtype=object).flatten()
        new_x = x.copy().scale(2).set_color(GREEN)
        new_x.move_to(3*LEFT+2*UP)
        new_y = y.copy().scale(2).set_color(RED)
        new_y.move_to(3*RIGHT+2*UP)

        #self.remove(v,array,x_line,y_line,x_line2,y_line2)
        #self.remove(v2, array2)

        i_hat, j_hat = self.get_basis_vectors()
        new_i_hat = Vector(
            3*i_hat.get_end(), 
            color = GREEN
        )
        new_j_hat = Vector(
            -2*j_hat.get_end(), 
            color = RED
        )
        VGroup(i_hat, new_i_hat).shift(3*LEFT)
        VGroup(j_hat, new_j_hat).shift(3*RIGHT)

        #new_array = Matrix([new_x.copy(), new_y.copy()])
        new_array = Matrix([[3], [-2]]).set_row_colors(GREEN, RED)
        new_array.scale(0.7)
        new_array.shift(
            -new_array.get_boundary_point(-v2.get_end()) + \
            1.1*v2.get_end()
        )

        self.remove(*starting_mobjects)
        self.add(numberplane)
        #self.remove(v,v2, array,array2)
        # self.next_section()
        self.play(
            Transform(x, new_x),
            Transform(y, new_y),
            Write(title),
        )
        self.play(FadeIn(i_hat), FadeIn(j_hat))
        self.wait()
        self.play(
            Transform(i_hat, new_i_hat),
            Transform(j_hat, new_j_hat),
            run_time = 3
        )
        # self.next_section()
        starting_mobjects.remove(array)
        new_x, new_y = np.array(new_array.get_mob_matrix(), dtype=object).flatten()
        v2.set_color(YELLOW)
        self.play(
            FadeOut(i_hat),
            FadeOut(j_hat),
            FadeOut(title),
            #Transform(VGroup(*[new_x,new_y]), array2.get_mob_matrix),
            Transform(x, new_x),
            Transform(y, new_y),
            FadeIn(v2),
            Write(new_array.get_brackets()),
            #FadeIn(VGroup(*starting_mobjects)),
        )
        self.remove(x, y)
        self.add(new_array)

        self.wait()

        #numberplane = NumberPlane(faded_line_ratio=2)
        #self.play(Create(numberplane))

        i_hat, j_hat = self.get_basis_vectors()
        self.add_vector(i_hat)
        i_hat_label = self.label_vector(
            i_hat, "\\vec{e}_x", 
            color = GREEN, 
            label_scale_factor = 1,
            animate = False
        ).scale(0.8)
        self.add_vector(j_hat)
        j_hat_label = self.label_vector(
            j_hat, "\\vec{e}_y", 
            color = RED, 
            label_scale_factor = 1,
            animate = False
        ).scale(0.8)
        
        # self.next_section()
        x, y = np.array(new_array.get_mob_matrix(), dtype=object).flatten()
        for coord, v, label, factor, shift_right in [
            (x, i_hat, i_hat_label, 3, False), 
            (y, j_hat, j_hat_label, -2, True)
            ]:
            faded_v = v.copy().fade(0.7)
            scaled_v = Vector(factor*v.get_end(), color = v.get_color())

            scaled_label = VGroup(coord.copy(), label.copy())
            scaled_label.arrange(RIGHT, buff = 0.1)
            scaled_label.move_to(label, DOWN+RIGHT)
            scaled_label.shift((scaled_v.get_end()-v.get_end())/2).shift([0,0.07,0])
            coord_copy = coord.copy()
            self.play(
                Transform(v.copy(), faded_v),
                Transform(v, scaled_v),
                Transform(VGroup(coord_copy, label), scaled_label),
            )
            self.wait()
            if shift_right:
                group = VGroup(v, coord_copy, label)
                self.play(ApplyMethod(
                    group.shift, 3*RIGHT
                ))
        # self.next_section()

        equation = VGroup(*[
            Tex("3"),
            Tex(r"$\vec{e}_x$"),
            Tex("-2"),
            Tex(r"$\vec{e}_y$"),
        ])
        self.A, self.x, eq, self.v = equation.split()
        equa = VGroup(*[self.A,self.x,eq,self.v])
        equa.arrange(buff=0.2)

        equa.move_to(new_array)

        equa.shift_onto_screen()
        #i_hat, plus, j_hat = new_mob.split()
        self.x.set_color(GREEN)
        self.v.set_color(RED)

        self.play(Transform(new_array, equa))
        # self.next_section()
1
class CoordinatesAsScalarsExample(VectorScene):
    def construct(self):
        numberplane = NumberPlane(faded_line_ratio=2, background_line_style={'stroke_color': config.background_color}, faded_line_style={'stroke_color': config.background_color})
        self.add(numberplane)
        i_hat, j_hat = self.get_basis_vectors()
        self.add_vector(i_hat)
        i_hat_label = self.label_vector(
            i_hat, "\\vec{e}_x", 
            color = GREEN, 
            label_scale_factor = 1
        ).scale(0.8)
        self.add_vector(j_hat)
        j_hat_label = self.label_vector(
            j_hat, "\\vec{e}_y", 
            color = RED, 
            label_scale_factor = 1
        ).scale(0.8)
        self.play(Create(i_hat_label), Create(j_hat_label), run_time=0.01)

        text = Tex(r'''$\vec{e}_x$ und $\vec{e}_y$ sind\\\ die ``Basisvektoren'' \\\ des Koordinatensystems''')
        text[0][0:3].set_color(GREEN)
        text[0][6:9].set_color(RED)
        text.to_corner(UP+RIGHT)
        self.play(Write(text))

        # self.next_section()

        vector = Vector([-5,2], color=YELLOW)
        label = Matrix([[-5], [2]]).set_row_colors(GREEN, RED)
        label.scale(0.7)
        label.shift(
            -label.get_boundary_point(-vector.get_end()) + \
            1.1*vector.get_end()
        ).shift([0.1,-0.5,0])

        self.play(FadeIn(vector), FadeIn(label))

        x, y = np.array(label.get_mob_matrix(), dtype=object).flatten()
        for coord, v, label, factor, shift_right in [
            (x, i_hat, i_hat_label, -5, False), 
            (y, j_hat, j_hat_label, 2, True)
            ]:
            faded_v = v.copy().fade(0.7)
            scaled_v = Vector(factor*v.get_end(), color = v.get_color())

            scaled_label = VGroup(coord.copy(), label.copy())
            scaled_label.arrange(RIGHT, buff = 0.1)
            scaled_label.move_to(label, DOWN+RIGHT)
            scaled_label.shift((scaled_v.get_end()-v.get_end())/2).shift([0,0.07,0])
            coord_copy = coord.copy()
            self.play(
                Transform(v.copy(), faded_v),
                Transform(v, scaled_v),
                Transform(VGroup(coord_copy, label), scaled_label),
            )
            self.wait()
            if shift_right:
                group = VGroup(v, coord_copy, label)
                self.play(ApplyMethod(
                    group.shift, -5*RIGHT
                ))
        self.wait()

        equation = VGroup(*[
            Tex("-5"),
            Tex(r"$\vec{e}_x$"),
            Tex("+2"),
            Tex(r"$\vec{e}_y$"),
        ])
        self.A, self.x, eq, self.v = equation.split()
        equa = VGroup(*[self.A,self.x,eq,self.v])
        equa.arrange(buff=0.2)

        equa.move_to(label).shift(UP+2.3*RIGHT)

        equa.shift_onto_screen()
        #i_hat, plus, j_hat = new_mob.split()
        self.x.set_color(GREEN)
        self.v.set_color(RED)

        print(self.mobjects)
        self.play(Create(equa))
# TODO: Transform(label, equa) is not working as it should
2
class WhatIfWeChoseADifferentBasis(Scene):
    def construct(self):
        self.play(Write(
            Tex("Was ist, wenn wir andere Basisvektoren wählen?"),
            run_time = 2
        ))
        self.wait(2)
3
class ShowVaryingLinearCombinations(VectorScene):

    def construct(self):
        self.vector1 = [1, 2]
        self.vector2 = [3, -1]
        self.vector1_color = MAROON_C
        self.vector2_color = BLUE
        self.vector1_label = "v"
        self.vector2_label = "w"
        self.sum_color = PINK
        self.scalar_pairs = [
                (1.5, 0.6),
                (0.7, 1.3),
                (-1, -1.5),
                (1, -1.13),
                (1.25, 0.5),
                (-0.8, 1.3),
            ]
        self.leave_sum_vector_copies = False
        self.start_with_non_sum_scaling = True
        self.finish_with_standard_basis_comparison = True
        self.finish_by_drawing_lines = False

        numberplane = NumberPlane(faded_line_ratio=2) #background_line_style={'stroke_color': config.background_color}, faded_line_style={'stroke_color': config.background_color})
        self.add(numberplane)
        #self.lock_in_faded_grid()
        # self.next_section()
        v1 = self.add_vector(self.vector1, color = self.vector1_color)
        # self.next_section()
        v2 = self.add_vector(self.vector2, color = self.vector2_color)
        v1_label = self.label_vector(
            v1, self.vector1_label, color = self.vector1_color, 
            #buff_factor = 3
        )
        v2_label = self.label_vector(
            v2, self.vector2_label, color = self.vector2_color, 
            #buff_factor = 3
        )
        

        def get_len_txt(vector, factor):
            return str(vector.get_length()*factor)[0:4]

        v1scaled = v1.copy()
        textv1 = Tex(get_len_txt(v1scaled,0.4477)).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v1scaled,0.4477))).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle())
        
        v2scaled = v2.copy()
        textv2 = Tex(get_len_txt(v2scaled, 0.3157)).next_to(v2_label).shift([-1.4,-0.3,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v2scaled, 0.3157))).next_to(v2_label).shift([-1.4,0,0]).scale(0.7).add_background_rectangle())
        #print(np.linalg.norm(np.array((v1scaled.get_end()-v1scaled.get_start())/2)))
        
    
        v1_label.add_updater(lambda object: object.move_to(
            np.array((v1scaled.get_end()-v1scaled.get_start())/2+v1scaled.get_start()) + 
            np.array([-0.25,0.1,0])))
        v2_label.add_updater(lambda object: object.move_to(
            np.array((v2scaled.get_end()-v2scaled.get_start())/2+v2scaled.get_start()) + 
            np.array([0.2,0.5,0])))
        self.add(textv1, textv2)
        self.play(
            v1scaled.animate.scale(1.5).shift([0.25,0.5,0]), 
            ApplyMethod(v1.fade, 0.7),
            v2scaled.animate.scale(0.609).shift([-0.6,0.2,0]), 
            ApplyMethod(v2.fade, 0.7),
            )
        self.wait()
        # self.next_section()


        self.play(v2scaled.animate.shift([1.5,3,0]))


        v3 = self.add_vector(v2scaled.get_end(), color = self.sum_color)


        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+np.array([0.6*3,-0.6,0])))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN,v2scaled.get_end()))
        
        self.play(v1scaled.animate.scale(0.468).shift([-0.37,-0.75,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(2.166).shift([1.05,-0.35,0]))
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        #v2scaled.resume_updating()
        self.play(v1scaled.animate.scale(-1.429).shift([-0.86,-1.75,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(-1.05).shift([-4,1.37,0]))
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1,2,0]))
        #self.wait()
        v2scaled.clear_updaters()
        v3.clear_updaters()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v3.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.25,2.5,0]),
                  v3.animate.put_start_and_end_on(ORIGIN, [2.75,2,0]),)
        #self.wait()
        v2scaled.clear_updaters()
        v2now = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2now))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN, v2scaled.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [-0.8,-1.65,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), [3,-2.9,0]))
4
class NameLinearCombinations(VectorScene):
    def construct(self):
        self.vector1 = [1, 2]
        self.vector2 = [3, -1]
        self.vector1_color = MAROON_C
        self.vector2_color = BLUE
        self.vector1_label = "v"
        self.vector2_label = "w"
        self.sum_color = PINK

        numberplane = NumberPlane()
        self.add(numberplane)

        # self.next_section()
        v1 = self.add_vector(self.vector1, color = self.vector1_color)
        # self.next_section()
        v2 = self.add_vector(self.vector2, color = self.vector2_color)
        v1_label = self.label_vector(
            v1, self.vector1_label, color = self.vector1_color, 
            #buff_factor = 3
        )
        v2_label = self.label_vector(
            v2, self.vector2_label, color = self.vector2_color, 
            #buff_factor = 3
        )
        # self.next_section()

        rectangle = Rectangle(color=config.background_color, width=5.5, height=2.4, 
                              stroke_width=250).to_edge(UP+LEFT, buff=0)
        self.add(rectangle)
        text = Tex(r'''"Linearkombinationen" von $\vec{v}$ und $\vec{w}$''', font_size=35)
        text[0][24:26].set_color(self.vector1_color)
        text[0][29:33].set_color(self.vector2_color)
        text.to_edge(UP+LEFT, buff=0.35)

        formula = Tex(r'''$\lambda_1\vec{v}+\lambda_2\vec{w}$''')
        formula.next_to(text, DOWN, buff=0.7)
        formula[0][2:4].set_color(self.vector1_color)
        formula[0][7:9].set_color(self.vector2_color)

        Skalare = Tex("Skalare", font_size=35)
        Skalare.next_to(formula, DOWN, buff=1)

        twovectors = VGroup(*[
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([-4.1,1.5,0],[-4.55,2.05,0]),
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([-3.7,1.5,0],[-3.45,2.05,0]),
            ])
        twovectors.set_color(YELLOW)

        #Terminologie = VGroup(*[rectangle,text,formula,Skalare,twovectors]).z_index(50)

        self.play(Write(text), Write(formula), Write(Skalare), Create(twovectors))

        def get_len_txt(vector, factor):
            return str(vector.get_length()*factor)[0:4]

        v1scaled = v1.copy()
        textv1 = Tex(get_len_txt(v1scaled,0.4477)).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v1scaled,0.4477))).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle())
        
        v2scaled = v2.copy()
        textv2 = Tex(get_len_txt(v2scaled, 0.3157)).next_to(v2_label).shift([-1.4,-0.3,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v2scaled, 0.3157))).next_to(v2_label).shift([-1.4,0,0]).scale(0.7).add_background_rectangle())
        #print(np.linalg.norm(np.array((v1scaled.get_end()-v1scaled.get_start())/2)))
        
    
        v1_label.add_updater(lambda object: object.move_to(
            np.array((v1scaled.get_end()-v1scaled.get_start())/2+v1scaled.get_start()) + 
            np.array([-0.25,0.1,0])))
        v2_label.add_updater(lambda object: object.move_to(
            np.array((v2scaled.get_end()-v2scaled.get_start())/2+v2scaled.get_start()) + 
            np.array([0.2,0.5,0])))
        self.add(textv1, textv2)
        self.play(
            v1scaled.animate.scale(1.5).shift([0.25,0.5,0]), 
            ApplyMethod(v1.fade, 0.7),
            v2scaled.animate.scale(0.609).shift([-0.6,0.2,0]), 
            ApplyMethod(v2.fade, 0.7),
            )
        self.wait()
        # self.next_section()


        self.play(v2scaled.animate.shift([1.5,3,0]))


        v3 = self.add_vector(v2scaled.get_end(), color = self.sum_color)


        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+np.array([0.6*3,-0.6,0])))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN,v2scaled.get_end()))
        
        self.play(v1scaled.animate.scale(0.468).shift([-0.37,-0.75,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(2.166).shift([1.05,-0.35,0]))
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        #v2scaled.resume_updating()
        self.play(v1scaled.animate.scale(-1.429).shift([-0.86,-1.75,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(-1.05).shift([-4,1.37,0]))
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1,2,0]))
        #self.wait()
        v2scaled.clear_updaters()
        v3.clear_updaters()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v3.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.25,2.5,0]),
                  v3.animate.put_start_and_end_on(ORIGIN, [2.75,2,0]),)
        #self.wait()
        v2scaled.clear_updaters()
        v2now = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2now))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN, v2scaled.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [-0.8,-1.65,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), [3,-2.9,0]))
5
class LinearCombinationsWithSumCopies(VectorScene):

    def construct(self):
        self.vector1 = [1, 2]
        self.vector2 = [3, -1]
        self.vector1_color = MAROON_C
        self.vector2_color = BLUE
        self.vector1_label = "v"
        self.vector2_label = "w"
        self.sum_color = PINK
        self.scalar_pairs = [
                (1.5, 0.6),
                (0.7, 1.3),
                (-1, -1.5),
                (1, -1.13),
                (1.25, 0.5),
                (-0.8, 1.3),
            ]
        self.leave_sum_vector_copies = False
        self.start_with_non_sum_scaling = True
        self.finish_with_standard_basis_comparison = True
        self.finish_by_drawing_lines = False

        numberplane = NumberPlane(faded_line_ratio=2) #background_line_style={'stroke_color': config.background_color}, faded_line_style={'stroke_color': config.background_color})
        self.add(numberplane)
        #self.lock_in_faded_grid()
        # self.next_section()
        v1 = self.add_vector(self.vector1, color = self.vector1_color, animate=False)
        # self.next_section()
        v2 = self.add_vector(self.vector2, color = self.vector2_color, animate=False)
        v1_label = self.label_vector(
            v1, self.vector1_label, color = self.vector1_color, animate=False
            #buff_factor = 3
        )
        v2_label = self.label_vector(
            v2, self.vector2_label, color = self.vector2_color, animate=False
            #buff_factor = 3
        )
        

        def get_len_txt(vector, factor):
            return str(vector.get_length()*factor)[0:4]

        v1scaled = v1.copy()
        textv1 = Tex(get_len_txt(v1scaled,0.4477)).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v1scaled,0.4477))).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle())
        
        v2scaled = v2.copy()
        textv2 = Tex(get_len_txt(v2scaled, 0.3157)).next_to(v2_label).shift([-1.4,-0.3,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v2scaled, 0.3157))).next_to(v2_label).shift([-1.4,0,0]).scale(0.7).add_background_rectangle())
        #print(np.linalg.norm(np.array((v1scaled.get_end()-v1scaled.get_start())/2)))
        
        self.remove(v1,v2)
    
        v1_label.add_updater(lambda object: object.move_to(
            np.array((v1scaled.get_end()-v1scaled.get_start())/2+v1scaled.get_start()) + 
            np.array([-0.25,0.1,0])))
        v2_label.add_updater(lambda object: object.move_to(
            np.array((v2scaled.get_end()-v2scaled.get_start())/2+v2scaled.get_start()) + 
            np.array([0.2,0.5,0])))
        self.add(textv1, textv2)
        v1scaled.scale(1.5).shift([0.25,0.5,0])
        v2scaled.scale(0.609).shift([-0.6,0.2,0])
        """ self.play(
            v1scaled.animate.scale(1.5).shift([0.25,0.5,0]), 
            #ApplyMethod(v1.fade, 0.7),
            v2scaled.animate.scale(0.609).shift([-0.6,0.2,0]), 
            #ApplyMethod(v2.fade, 0.7),
            ) """

        v2scaled.shift([1.5,3,0])


        v3 = self.add_vector(v2scaled.get_end(), color = self.sum_color, animate=False)
        self.add(v3)
        self.add(v3.copy().clear_updaters())

        
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+np.array([0.6*3,-0.6,0])))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN,v2scaled.get_end()))
        
        self.add(v2scaled)  #####   remove if still a problem
        self.play(v1scaled.animate.scale(0.468).shift([-0.37,-0.75,0]))
        self.add(v3.copy().clear_updaters())
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(2.166).shift([1.05,-0.35,0]))
        self.add(v3.copy().clear_updaters())
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        #v2scaled.resume_updating()
        self.play(v1scaled.animate.scale(-1.429).shift([-0.86,-1.75,0]))
        self.add(v3.copy().clear_updaters())
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(-1.05).shift([-4,1.37,0]))
        self.add(v3.copy().clear_updaters())
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1,2,0]))
        self.add(v3.copy().clear_updaters())
        #self.wait()
        v2scaled.clear_updaters()
        v3.clear_updaters()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v3.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.25,2.5,0]),
                  v3.animate.put_start_and_end_on(ORIGIN, [2.75,2,0]),)
        self.add(v3.copy().clear_updaters())
        #self.wait()
        v2scaled.clear_updaters()
        v2now = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2now))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN, v2scaled.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [-0.8,-1.65,0]))
        self.add(v3.copy().clear_updaters())
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), [3,-2.9,0]))
        self.add(v3.copy().clear_updaters())
6
class UnluckyCase(VectorScene):
    def construct(self):
        self.vector1 = [1, 2]
        self.vector2 = [3, -1]
        self.vector1_color = MAROON_C
        self.vector2_color = BLUE
        self.vector1_label = "v"
        self.vector2_label = "w"
        self.sum_color = PINK
        self.scalar_pairs = [
                (1.5, 0.6),
                (0.7, 1.3),
                (-1, -1.5),
                (1, -1.13),
                (1.25, 0.5),
                (-0.8, 1.3),
            ]
        numberplane = NumberPlane(faded_line_ratio=2)
        self.add(numberplane)
        v1=self.add_vector([1,2], color=MAROON_C)
        v2=self.add_vector([0.5,1], color=BLUE)
        v1_label = self.label_vector(
            v1, self.vector1_label, color = self.vector1_color,
        )
        v2_label = self.label_vector(
            v2, self.vector2_label, color = self.vector2_color,
        )
        def get_len_txt(vector, factor):
            return str(vector.get_length()*factor)[0:4]

        v1scaled = v1.copy()
        textv1 = Tex(get_len_txt(v1scaled,0.4477)).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v1scaled,0.4477))).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle())
        
        v2scaled = v2.copy()
        textv2 = Tex(get_len_txt(v2scaled, 0.3157)).next_to(v2_label).shift([-1.4,-0.3,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v2scaled, 0.9))).next_to(v2_label).shift([-1.35,0,0]).scale(0.7).add_background_rectangle())
        #print(np.linalg.norm(np.array((v1scaled.get_end()-v1scaled.get_start())/2)))
        
        self.remove(v2)
        v1_label.add_updater(lambda object: object.move_to(
            np.array((v1scaled.get_end()-v1scaled.get_start())/2+v1scaled.get_start()) + 
            np.array([-0.05,0.5,0])))
        v2_label.add_updater(lambda object: object.move_to(
            np.array((v2scaled.get_end()-v2scaled.get_start())/2+v2scaled.get_start()) + 
            np.array([-0.3,0.2,0])))
        self.add(textv1, textv2)

        self.play(v2scaled.animate.shift(v1scaled.get_end()))
        v2rightnow = v2.get_end()-v2.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2rightnow))
        self.remove(v1)
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.5,3,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+0.6*v2rightnow))
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+0.6*v2rightnow))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [0.7,2*0.7,0]))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [-1,-2,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+[-0.75,-1.5,0]))
        v2rightnow = v2.get_end()-v2.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2rightnow))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.25,2*1.25,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+[0.25,0.5,0]))
        self.wait()
7
class EvenMoreUnluckyCase(VectorScene):
    def construct(self):
        self.vector1 = [1, 2]
        self.vector2 = [3, -1]
        self.vector1_color = MAROON_C
        self.vector2_color = BLUE
        self.vector1_label = "v"
        self.vector2_label = "w"
        self.sum_color = PINK
        self.scalar_pairs = [
                (1.5, 0.6),
                (0.7, 1.3),
                (-1, -1.5),
                (1, -1.13),
                (1.25, 0.5),
                (-0.8, 1.3),
            ]
        numberplane = NumberPlane(faded_line_ratio=2)
        self.add(numberplane)
        v1=self.add_vector([1,2], color=MAROON_C, animate=False)
        v2=self.add_vector([3,-1], color=BLUE, animate=False)
        self.add(v1,v2)
        dot = Dot()
        self.play(Transform(v1,dot), Transform(v2, dot))
        self.wait()
8
class NameLinearCombinations2(VectorScene):
    def construct(self):
        self.vector1 = [1, 2]
        self.vector2 = [3, -1]
        self.vector1_color = MAROON_C
        self.vector2_color = BLUE
        self.vector1_label = "v"
        self.vector2_label = "w"
        self.sum_color = PINK

        numberplane = NumberPlane()
        self.add(numberplane)

        # self.next_section()
        v1 = self.add_vector(self.vector1, color = self.vector1_color)
        # self.next_section()
        v2 = self.add_vector(self.vector2, color = self.vector2_color)
        v1_label = self.label_vector(
            v1, self.vector1_label, color = self.vector1_color, 
            #buff_factor = 3
        )
        v2_label = self.label_vector(
            v2, self.vector2_label, color = self.vector2_color, 
            #buff_factor = 3
        )

        rectangle = Rectangle(color=config.background_color, width=5.7, height=2.5, 
                              stroke_width=250).to_edge(UP+LEFT, buff=0)
        self.add(rectangle)
        text = Tex(r'''Der "Spann" von $\vec{v}$ und $\vec{w}$\\ist die Menge aller Linearkombinationen''', font_size=35)
        text[0][13:15].set_color(self.vector1_color)
        text[0][18:20].set_color(self.vector2_color)
        text.to_edge(UP+LEFT, buff=0.35)

        formula = Tex(r'''$\lambda_1\vec{v}+\lambda_2\vec{w}$''')
        formula.next_to(text, DOWN, buff=0.7)
        formula[0][2:4].set_color(self.vector1_color)
        formula[0][7:9].set_color(self.vector2_color)

        Skalare = Tex("Alle möglichen Faktoren", font_size=35)
        Skalare.next_to(formula, DOWN, buff=1)

        twovectors = VGroup(*[
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([-4.1,1.5,0],[-4.55,2.05,0]),
            Vector(max_tip_length_to_length_ratio=0.15).put_start_and_end_on([-3.7,1.5,0],[-3.45,2.05,0]),
            ])
        twovectors.set_color(YELLOW).shift([0.3,-0.5,0])

        #Terminologie = VGroup(*[rectangle,text,formula,Skalare,twovectors]).z_index(50)

        self.play(Write(text), Write(formula), Write(Skalare), Create(twovectors))

        
        def get_len_txt(vector, factor):
            return str(vector.get_length()*factor)[0:4]

        v1scaled = v1.copy()
        textv1 = Tex(get_len_txt(v1scaled,0.4477)).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v1scaled,0.4477))).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle())
        
        v2scaled = v2.copy()
        textv2 = Tex(get_len_txt(v2scaled, 0.3157)).next_to(v2_label).shift([-1.4,-0.3,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v2scaled, 0.3157))).next_to(v2_label).shift([-1.4,0,0]).scale(0.7).add_background_rectangle())
        #print(np.linalg.norm(np.array((v1scaled.get_end()-v1scaled.get_start())/2)))
        
    
        v1_label.add_updater(lambda object: object.move_to(
            np.array((v1scaled.get_end()-v1scaled.get_start())/2+v1scaled.get_start()) + 
            np.array([-0.25,0.1,0])))
        v2_label.add_updater(lambda object: object.move_to(
            np.array((v2scaled.get_end()-v2scaled.get_start())/2+v2scaled.get_start()) + 
            np.array([0.2,0.5,0])))
        self.add(textv1, textv2)
        self.play(
            v1scaled.animate.scale(1.5).shift([0.25,0.5,0]), 
            ApplyMethod(v1.fade, 0.7),
            v2scaled.animate.scale(0.609).shift([-0.6,0.2,0]), 
            ApplyMethod(v2.fade, 0.7),
            )
        self.wait()
        # self.next_section()


        self.play(v2scaled.animate.shift([1.5,3,0]))


        v3 = self.add_vector(v2scaled.get_end(), color = self.sum_color)


        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+np.array([0.6*3,-0.6,0])))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN,v2scaled.get_end()))
        
        self.play(v1scaled.animate.scale(0.468).shift([-0.37,-0.75,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(2.166).shift([1.05,-0.35,0]))
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        #v2scaled.resume_updating()
        self.play(v1scaled.animate.scale(-1.429).shift([-0.86,-1.75,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(-1.05).shift([-4,1.37,0]))
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1,2,0]))
        #self.wait()
        v2scaled.clear_updaters()
        v3.clear_updaters()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v3.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.25,2.5,0]),
                  v3.animate.put_start_and_end_on(ORIGIN, [2.75,2,0]),)
        #self.wait()
        v2scaled.clear_updaters()
        v2now = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2now))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN, v2scaled.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [-0.8,-1.65,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), [3,-2.9,0]))

        # self.next_section()

        self.remove(v2scaled,v1scaled,v3,textv1,textv2,v1_label,v2_label,v1,v2)
        v1=self.add_vector([1,2], color=MAROON_C)
        v2=self.add_vector([0.5,1], color=BLUE)
        v1_label = self.label_vector(
            v1, self.vector1_label, color = self.vector1_color,
        )
        v2_label = self.label_vector(
            v2, self.vector2_label, color = self.vector2_color,
        )
        def get_len_txt(vector, factor):
            return str(vector.get_length()*factor)[0:4]

        v1scaled = v1.copy()
        textv1 = Tex(get_len_txt(v1scaled,0.4477)).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v1scaled,0.4477))).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle())
        
        v2scaled = v2.copy()
        textv2 = Tex(get_len_txt(v2scaled, 0.3157)).next_to(v2_label).shift([-1.4,-0.3,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v2scaled, 0.9))).next_to(v2_label).shift([-1.35,0,0]).scale(0.7).add_background_rectangle())
        #print(np.linalg.norm(np.array((v1scaled.get_end()-v1scaled.get_start())/2)))
        
        self.remove(v2)
        v1_label.add_updater(lambda object: object.move_to(
            np.array((v1scaled.get_end()-v1scaled.get_start())/2+v1scaled.get_start()) + 
            np.array([-0.05,0.5,0])))
        v2_label.add_updater(lambda object: object.move_to(
            np.array((v2scaled.get_end()-v2scaled.get_start())/2+v2scaled.get_start()) + 
            np.array([-0.3,0.2,0])))
        self.add(textv1, textv2)

        self.play(v2scaled.animate.shift(v1scaled.get_end()))
        v2rightnow = v2.get_end()-v2.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2rightnow))
        self.remove(v1)
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.5,3,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+0.6*v2rightnow))
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+0.6*v2rightnow))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [0.7,2*0.7,0]))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [-1,-2,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+[-0.75,-1.5,0]))
        v2rightnow = v2.get_end()-v2.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2rightnow))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.25,2*1.25,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+[0.25,0.5,0]))
        self.wait()

        # self.next_section()
        self.remove(v2scaled,v1scaled,textv1,textv2,v1_label,v2_label)
        v1=self.add_vector([1,2], color=MAROON_C, animate=False)
        v2=self.add_vector([3,-1], color=BLUE, animate=False)
        self.add(v1,v2)
        dot = Dot()
        self.play(Transform(v1,dot), Transform(v2, dot))
        self.wait()


        

        # self.next_section()
        self.remove(v2scaled,v1scaled,v3,textv1,textv2,v1_label,v2_label)

        v1 = self.add_vector(self.vector1, color = self.vector1_color, animate=False)
        # self.next_section()
        v2 = self.add_vector(self.vector2, color = self.vector2_color, animate=False)
        v1_label = self.label_vector(
            v1, self.vector1_label, color = self.vector1_color, animate=False
            #buff_factor = 3
        )
        v2_label = self.label_vector(
            v2, self.vector2_label, color = self.vector2_color, animate=False
            #buff_factor = 3
        )
        

        def get_len_txt(vector, factor):
            return str(vector.get_length()*factor)[0:4]

        v1scaled = v1.copy()
        textv1 = Tex(get_len_txt(v1scaled,0.4477)).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v1scaled,0.4477))).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle())
        
        v2scaled = v2.copy()
        textv2 = Tex(get_len_txt(v2scaled, 0.3157)).next_to(v2_label).shift([-1.4,-0.3,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v2scaled, 0.3157))).next_to(v2_label).shift([-1.4,0,0]).scale(0.7).add_background_rectangle())
        #print(np.linalg.norm(np.array((v1scaled.get_end()-v1scaled.get_start())/2)))
        
        self.remove(v1,v2)
    
        v1_label.add_updater(lambda object: object.move_to(
            np.array((v1scaled.get_end()-v1scaled.get_start())/2+v1scaled.get_start()) + 
            np.array([-0.25,0.1,0])))
        v2_label.add_updater(lambda object: object.move_to(
            np.array((v2scaled.get_end()-v2scaled.get_start())/2+v2scaled.get_start()) + 
            np.array([0.2,0.5,0])))
        self.add(textv1, textv2)
        v1scaled.scale(1.5).shift([0.25,0.5,0])
        v2scaled.scale(0.609).shift([-0.6,0.2,0])
        """ self.play(
            v1scaled.animate.scale(1.5).shift([0.25,0.5,0]), 
            #ApplyMethod(v1.fade, 0.7),
            v2scaled.animate.scale(0.609).shift([-0.6,0.2,0]), 
            #ApplyMethod(v2.fade, 0.7),
            ) """

        v2scaled.shift([1.5,3,0])


        v3 = self.add_vector(v2scaled.get_end(), color = self.sum_color, animate=False)
        self.add(v3)
        self.add(v3.copy().clear_updaters())

        
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+np.array([0.6*3,-0.6,0])))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN,v2scaled.get_end()))
        
        self.add(v2scaled)  #####   remove if still a problem
        self.play(v1scaled.animate.scale(0.468).shift([-0.37,-0.75,0]))
        self.add(v3.copy().clear_updaters())
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(2.166).shift([1.05,-0.35,0]))
        self.add(v3.copy().clear_updaters())
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        #v2scaled.resume_updating()
        self.play(v1scaled.animate.scale(-1.429).shift([-0.86,-1.75,0]))
        self.add(v3.copy().clear_updaters())
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.scale(-1.05).shift([-4,1.37,0]))
        self.add(v3.copy().clear_updaters())
        v2vec = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2vec))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1,2,0]))
        self.add(v3.copy().clear_updaters())
        #self.wait()
        v2scaled.clear_updaters()
        v3.clear_updaters()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v3.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.25,2.5,0]),
                  v3.animate.put_start_and_end_on(ORIGIN, [2.75,2,0]),)
        self.add(v3.copy().clear_updaters())
        #self.wait()
        v2scaled.clear_updaters()
        v2now = v2scaled.get_end()-v2scaled.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2now))
        v3.add_updater(lambda me: me.put_start_and_end_on(ORIGIN, v2scaled.get_end()))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [-0.8,-1.65,0]))
        self.add(v3.copy().clear_updaters())
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), [3,-2.9,0]))
        self.add(v3.copy().clear_updaters())
#9
class JustSome3DVectors(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        a = np.array([1.5,-1.5,1.5])
        b = np.array([0,1,-1])
        v1 = Vector(a, color=MAROON_C)
        v2 = Vector(b, color=BLUE)
        self.add(axes,v1,v2)
        text = Tex(r'''Spann($\vec{v},\vec{w}$)?''')
        text[0][6:8].set_color(MAROON_C)
        text[0][9:11].set_color(BLUE)
        text.to_corner(UP+RIGHT)

        self.add(axes,v1,v2)
        self.add_fixed_in_frame_mobjects(text)

        self.set_camera_orientation(phi=80*DEGREES,theta=-45*DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI/7, about="theta",
        )
        #self.wait(8)
        self.play(Write(Tex(r"")))
        self.wait(8)
10
class WasIstDerSpann(Scene):
    def construct(self):
        self.play(Write(Tex(r"Was ist der Spann im $\mathbb{R}^3$?")))
#11
class ThreeDSpan(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        a = np.array([1.5,-1.5,1.5])
        b = np.array([0,1,1])
        v1 = Vector(a, color=MAROON_C)
        v2 = Vector(b, color=BLUE)

        text = Tex(r'''Spann($\vec{v},\vec{w}$)?''')
        text[0][6:8].set_color(MAROON_C)
        text[0][9:11].set_color(BLUE)
        text.to_corner(UP+RIGHT)

        self.add(axes,v1,v2)
        self.add_fixed_in_frame_mobjects(text)

        self.set_camera_orientation(phi=80*DEGREES,theta=-45*DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI/10, about="theta",
        )
        self.wait(2)
        shift = -(a+b)
        #poly = Polygon(np.array([2*a,ORIGIN,2*b,2*(a+b)])*2-(a+b), fill_color=GREY)
        poly = Polygon(2.5*a+shift,ORIGIN+shift, 2*b+shift,2.5*(a+b)+shift, fill_color=GREY)

        self.play(Create(poly))
        self.wait(2)
        startingv2 = v2.get_end()-v2.get_start()
        self.play(v2.animate.put_start_and_end_on(v1.get_end(),v1.get_end()+startingv2))
        self.wait(6)
        self.play(v2.animate.put_start_and_end_on(v1.get_end(),a-startingv2-np.array([0,0.05,0])))
        self.wait(1)
        v2.add_updater(lambda me: me.put_start_and_end_on(v1.get_end(),v1.get_end()-startingv2-np.array([0,0.05,0])))
        self.play(v1.animate.put_start_and_end_on(ORIGIN,-b*0.5))
        self.wait(8)
12
class WhatAboutThreeVectors(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        a = np.array([1.5,-1.5,1.5])
        b = np.array([0,1,1])
        v1 = Vector(a, color=MAROON_C)
        v2 = Vector(b, color=BLUE)
        self.add(axes,v1,v2)
        text = Tex(r'''Spann($\vec{v},\vec{w}, \vec{u}$)?''')
        text[0][6:8].set_color(MAROON_C)
        text[0][9:11].set_color(BLUE)
        text[0][12:14].set_color(RED)
        text.to_corner(UP+RIGHT)

        self.add(axes,v1,v2)
        self.add_fixed_in_frame_mobjects(text)

        self.set_camera_orientation(phi=80*DEGREES,theta=-45*DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI/7, about="theta",
        )
        #self.wait(8)
        shift = -(a+b)
        #poly = Polygon(np.array([2*a,ORIGIN,2*b,2*(a+b)])*2-(a+b), fill_color=GREY)
        poly = Polygon(2.5*a+shift,ORIGIN+shift, 2*b+shift,2.5*(a+b)+shift, fill_color=GREY)
        self.wait(1)
        self.play(Create(poly))
        c = np.array([-3,-1.5,1.5])
        self.wait(3.5)
        v3 = Vector(c, color=RED)
        self.play(Create(v3))
        self.wait(4)

        group = VGroup(*[v1,v2,poly])

        self.play(group.animate.shift(c))
        self.wait(1)
        self.play(group.animate.shift(-0.5*c))
        self.wait(1)
        self.play(group.animate.shift(-0.1*c))
        self.play(group.animate.shift(0.2*c))
        self.play(group.animate.shift(-1.2*c))
        self.play(group.animate.shift(2*c))
        self.play(group.animate.shift(-0.4*c))
        self.wait(8)
#13
class LinearDependence(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        a = np.array([1.5,-1.5,1.5])
        b = np.array([0,1,1])
        v1 = Vector(a, color=MAROON_C)
        v2 = Vector(b, color=BLUE)
        self.add(axes,v1,v2)
        text = Tex(r'''"Lineare Abhängigkeit""''').add_background_rectangle()
        text.to_corner(UP+RIGHT)

        self.add(axes,v1,v2)

        self.set_camera_orientation(phi=80*DEGREES,theta=-45*DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI/7, about="theta",
        )
        #self.wait(8)
        shift = -(a+b)
        #poly = Polygon(np.array([2*a,ORIGIN,2*b,2*(a+b)])*2-(a+b), fill_color=GREY)
        poly = Polygon(2.5*a+shift,ORIGIN+shift, 2*b+shift,2.5*(a+b)+shift, fill_color=GREY)
        self.wait(1)
        self.play(Create(poly))
        c = (a+b)/2
        self.wait(3.5)
        v3 = Vector(c, color=RED)
        self.play(Create(v3))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text)
        self.wait(8)
14
class LinearDependence2(VectorScene):
    def construct(self):
        self.vector1 = [1, 2]
        self.vector2 = [3, -1]
        self.vector1_color = MAROON_C
        self.vector2_color = BLUE
        self.vector1_label = "v"
        self.vector2_label = "w"
        self.sum_color = PINK
        self.scalar_pairs = [
                (1.5, 0.6),
                (0.7, 1.3),
                (-1, -1.5),
                (1, -1.13),
                (1.25, 0.5),
                (-0.8, 1.3),
            ]
        numberplane = NumberPlane(faded_line_ratio=2)
        self.add(numberplane)
        text = Tex(r'''"Lineare Abhängigkeit""''').add_background_rectangle()
        text.to_corner(UP+RIGHT)
        self.add(text)
        v1=self.add_vector([1,2], color=MAROON_C)
        v2=self.add_vector([0.5,1], color=BLUE)
        v1_label = self.label_vector(
            v1, self.vector1_label, color = self.vector1_color,
        )
        v2_label = self.label_vector(
            v2, self.vector2_label, color = self.vector2_color,
        )
        def get_len_txt(vector, factor):
            return str(vector.get_length()*factor)[0:4]

        v1scaled = v1.copy()
        textv1 = Tex(get_len_txt(v1scaled,0.4477)).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v1scaled,0.4477))).next_to(v1_label).shift([-1.3,0,0]).scale(0.7).add_background_rectangle())
        
        v2scaled = v2.copy()
        textv2 = Tex(get_len_txt(v2scaled, 0.3157)).next_to(v2_label).shift([-1.4,-0.3,0]).scale(0.7).add_background_rectangle().add_updater(lambda text: text.become(Tex(get_len_txt(v2scaled, 0.9))).next_to(v2_label).shift([-1.35,0,0]).scale(0.7).add_background_rectangle())
        #print(np.linalg.norm(np.array((v1scaled.get_end()-v1scaled.get_start())/2)))
        
        self.remove(v2)
        v1_label.add_updater(lambda object: object.move_to(
            np.array((v1scaled.get_end()-v1scaled.get_start())/2+v1scaled.get_start()) + 
            np.array([-0.05,0.5,0])))
        v2_label.add_updater(lambda object: object.move_to(
            np.array((v2scaled.get_end()-v2scaled.get_start())/2+v2scaled.get_start()) + 
            np.array([-0.3,0.2,0])))
        self.add(textv1, textv2)

        self.play(v2scaled.animate.shift(v1scaled.get_end()))
        v2rightnow = v2.get_end()-v2.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2rightnow))
        self.remove(v1)
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.5,3,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+0.6*v2rightnow))
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+0.6*v2rightnow))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [0.7,2*0.7,0]))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [-1,-2,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+[-0.75,-1.5,0]))
        v2rightnow = v2.get_end()-v2.get_start()
        v2scaled.add_updater(lambda me: me.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+v2rightnow))
        self.play(v1scaled.animate.put_start_and_end_on(ORIGIN, [1.25,2*1.25,0]))
        v2scaled.clear_updaters()
        self.play(v2scaled.animate.put_start_and_end_on(v1scaled.get_end(), v1scaled.get_end()+[0.25,0.5,0]))
        self.wait()
15