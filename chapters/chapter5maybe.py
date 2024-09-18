from manim import *
from manim_slides import Slide

from config import LinearTransformationSlide


class stretchspace(LinearTransformationSlide):
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
            text=Tex("Dehnt den Raum aus").to_edge(UP).add_background_rectangle()
            self.add(text)
            self.next_section()
            self.apply_transposed_matrix([[3,1],[-1,2]])
55
class compressspace(LinearTransformationSlide):
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
            text=Tex("Komprimiert den Raum").to_edge(UP).add_background_rectangle()
            self.add(text)
            self.next_section()
            self.apply_transposed_matrix([[0.5,-0.5],[1,0.25]])
56
""" class Blob(Circle):
    CONFIG = {
        "stroke_color" : TEAL,
        "fill_color" : BLUE_E,
        "fill_opacity" : 1,
        "random_seed" : 1,
        "random_nudge_size" : 0.5,
        "height" : 2,
    }
    
    def __init__(self, **kwargs):
        self.random_seed = 1
        self.random_nudge_size = 0.5
        Circle.__init__(self, **kwargs)
        random.seed(self.random_seed)
        self.apply_complex_function(
            lambda z : z*(1+self.random_nudge_size*(random.random()-0.5))
        )
        self.set_height(self.height).center()

    def probably_contains(self, point):
        border_points = np.array(self.get_anchors_and_handles()[0])
        distances = [np.linalg.norm(p-point) for p in border_points]
        min3 = border_points[np.argsort(distances)[:3]]
        center_direction = self.get_center() - point
        in_center_direction = [np.dot(p-point, center_direction) > 0 for p in min3]
        return sum(in_center_direction) <= 2 """

class exactlyhowmuch(LinearTransformationSlide):
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
            text=Tex("Wie sehr wird gestreckt?", color=YELLOW).to_corner(UP+RIGHT).add_background_rectangle()
            self.add(text)
            self.next_section()
            self.apply_transposed_matrix([[2,1],[-1,3]])
57
class exactlyhowmuch2(LinearTransformationSlide):
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
            text=Tex("Wie sehr werden Flächen gestreckt?").scale(1.34).to_edge(UP).add_background_rectangle()
            text[0][13:20].set_color(YELLOW)
            self.add(text)
            poly = Polygon([0.2,0.2,0],[0.1,1,0],[0.3,1.1,0],[2,2,0],[2.5,1,0],[1.3,0.13,0], fill_color=BLUE, fill_opacity=1).shift([0.4,0.4,0])
            text2 = Tex("Fläche").add_updater(lambda me: me.move_to(poly.get_center()))
            self.add_transformable_mobject(poly, text2)
            self.next_section()
            #text3.set_color(WHITE)
            self.apply_transposed_matrix([[2,-1],[1,1]])
58