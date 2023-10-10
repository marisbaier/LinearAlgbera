from manim import *
from manim_editor import PresentationSectionType
from manim.opengl import *
config.background_color = DARKER_GRAY
config["background_color"] = DARKER_GRAY
Tex.set_default(color=WHITE)

class CoordinatesAsScalars(VectorScene):
    def construct(self):
        numberplane = NumberPlane(faded_line_ratio=2, background_line_style={'stroke_color': config.background_color}, faded_line_style={'stroke_color': config.background_color})
        self.add(numberplane)

        self.next_section()  

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
        self.next_section()
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
        self.next_section()
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
        
        self.next_section()
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
        self.next_section()

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
        self.next_section()

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

        self.next_section()

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

        equa.move_to(label)

        equa.shift_onto_screen()
        #i_hat, plus, j_hat = new_mob.split()
        self.x.set_color(GREEN)
        self.v.set_color(RED)

        print(self.mobjects)
        self.play(Transform(label, equa))
        self.next_section()

class WhatIfWeChoseADifferentBasis(Scene):
    def construct(self):
        self.play(Write(
            Tex("What ist, wenn wir andere Basisvektoren wählen?"),
            run_time = 2
        ))
        self.wait(2)

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
        self.next_section()
        v1 = self.add_vector(self.vector1, color = self.vector1_color)
        self.next_section()
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
        self.next_section()


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
        self.wait()
        
        label_anims = [
            MaintainPositionRelativeTo(label, v)
            for v, label in [(v1, v1_label), (v2, v2_label)]
        ]
        #scalar_anims = self.get_scalar_anims(v1, v2, v1_label, v2_label)
        self.last_scalar_pair = (1, 1)

        """ if self.start_with_non_sum_scaling:
            self.initial_scaling(v1, v2, label_anims, scalar_anims)
        self.show_sum(v1, v2, label_anims, scalar_anims)
        self.scale_with_sum(v1, v2, label_anims, scalar_anims)
        if self.finish_with_standard_basis_comparison:
            self.standard_basis_comparison(label_anims, scalar_anims)
        if self.finish_by_drawing_lines:
            self.draw_lines(v1, v2, label_anims, scalar_anims) """

    def get_scalar_anims(self, v1, v2, v1_label, v2_label):
        def get_val_func(vect):
            original_vect = np.array(vect.get_end()-vect.get_start())
            square_norm = np.linalg.norm(original_vect)**2
            return lambda a : np.dot(
                original_vect, vect.get_end()-vect.get_start()
            )/square_norm
        return [
            RangingValues(
                tracked_mobject = label,
                tracked_mobject_next_to_kwargs = {
                    "direction" : LEFT,
                    "buff" : 0.1
                },
                scale_factor = 0.75,
                value_function = get_val_func(v)
            )   
            for v, label in [(v1, v1_label), (v2, v2_label)]
        ]

    def get_rate_func_pair(self):
        return [
            squish_rate_func(smooth, a, b) 
            for a, b in [(0, 0.7), (0.3, 1)]
        ] 

    def initial_scaling(self, v1, v2, label_anims, scalar_anims):
        scalar_pair = self.scalar_pairs.pop(0)
        anims = [
            ApplyMethod(v.scale, s, rate_func = rf)
            for v, s, rf in zip(
                [v1, v2],
                scalar_pair,
                self.get_rate_func_pair()
            )
        ]
        anims += [
            ApplyMethod(v.copy().fade, 0.7)
            for v in (v1, v2)
        ]
        anims += label_anims + scalar_anims
        self.play(*anims, **{"run_time" : 2})
        self.wait()
        self.last_scalar_pair = scalar_pair

    def show_sum(self, v1, v2, label_anims, scalar_anims):
        self.play(
            ApplyMethod(v2.shift, v1.get_end()),
            *label_anims + scalar_anims
        )
        self.sum_vector = self.add_vector(
            v2.get_end(), color = self.sum_color
        )
        self.wait()

    def scale_with_sum(self, v1, v2, label_anims, scalar_anims):
        v2_anim, sum_anim = self.get_sum_animations(v1, v2)
        while self.scalar_pairs:
            scalar_pair = self.scalar_pairs.pop(0)
            anims = [
                ApplyMethod(v.scale, s/s_old, rate_func = rf)
                for v, s, s_old, rf in zip(
                    [v1, v2], 
                    scalar_pair, 
                    self.last_scalar_pair,
                    self.get_rate_func_pair()
                )
            ]
            anims += [v2_anim, sum_anim] + label_anims + scalar_anims
            self.play(*anims, **{"run_time" : 2})
            if self.leave_sum_vector_copies:
                self.add(self.sum_vector.copy())
            self.wait()
            self.last_scalar_pair = scalar_pair

    def get_sum_animations(self, v1, v2):
        v2_anim = UpdateFromFunc(
            v2, lambda m : m.shift(v1.get_end()-m.get_start())
        )
        sum_anim = UpdateFromFunc(
            self.sum_vector, 
            lambda v : v.put_start_and_end_on(v1.get_start(), v2.get_end())
        )
        return v2_anim, sum_anim

    def standard_basis_comparison(self, label_anims, scalar_anims):
        everything = self.get_mobjects()
        everything.remove(self.sum_vector)
        everything = VMobject(*everything)
        alt_coords = [a.mobject for a in scalar_anims]
        array = Matrix([
            mob.copy().set_color(color)
            for mob, color in zip(
                alt_coords, 
                [self.vector1_color, self.vector2_color]
            )
        ])
        array.scale(0.8)
        array.to_edge(UP)
        array.shift(RIGHT)
        brackets = array.get_brackets()

        anims = [
            Transform(*pair)
            for pair in zip(alt_coords, array.get_mob_matrix().flatten())
        ]
        # anims += [
        #     FadeOut(a.mobject)
        #     for a in label_anims
        # ]
        self.play(*anims + [Write(brackets)])
        self.wait()
        self.remove(brackets, *alt_coords)
        self.add(array)
        self.play(
            FadeOut(everything), 
            Animation(array),
        )

        self.add_axes(animate = True)
        ij_array, x_line, y_line = self.vector_to_coords(
            self.sum_vector, integer_labels = False
        )
        self.add(ij_array, x_line, y_line)
        x, y = ij_array.get_mob_matrix().flatten()
        self.play(
            ApplyMethod(x.set_color, GREEN),
            ApplyMethod(y.set_color, RED),
        )
        neq = OldTex("\\neq")
        neq.next_to(array)
        self.play(
            ApplyMethod(ij_array.next_to, neq),
            Write(neq)
        )
        self.wait()

    def draw_lines(self, v1, v2, label_anims, scalar_anims):
        sum_anims = self.get_sum_animations(v1, v2)
        aux_anims = list(sum_anims) + label_anims + scalar_anims

        scale_factor = 2
        for w1, w2 in (v2, v1), (v1, v2):
            w1_vect = w1.get_end()-w1.get_start()
            w2_vect = w2.get_end()-w2.get_start()
            for num in scale_factor, -1, -1./scale_factor:
                curr_tip = self.sum_vector.get_end()
                line = Line(ORIGIN, curr_tip)
                self.play(
                    ApplyMethod(w2.scale, num), 
                    UpdateFromFunc(
                        line, lambda l : l.put_start_and_end_on(curr_tip, self.sum_vector.get_end())
                    ),
                    *aux_anims
                )
                self.add(line, v2)
            self.wait()
