from manim import *

class TestVMobject(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE},
            x_axis_config={"color": GREEN},
            y_axis_config={"color": GREEN},
            tips=True,
        )
        x = np.arange(-3, 3, 1)
        y = np.arange(-3, 3, 1)-2
        curve = VMobject().set_points_as_corners([axes.c2p(x, y) for x, y in zip(x, y)])
        self.add(axes, curve)

