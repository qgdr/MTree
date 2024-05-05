from manim import *

class Subgrad(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 3, 1],
            y_range=[-3, 6, 3],
            x_length=12,
            y_length=9,
            x_axis_config={"include_tip": False},
            y_axis_config={"include_tip": False},
            axis_config={"color": BLUE},
            tips=False,
        )

        def f(x):
            if x < 1:
                return 1 - x
            elif x < 2:
                return x-1
            else:
                return 2*x-3
            
        f_graph = axes.plot(f, color=RED, use_smoothing=False)
        f_label = axes.get_graph_label(f_graph, "f(x)")
        f_label.set_color(RED)
        f_label.shift(0.3*UP)
        self.add(axes, f_graph, f_label)

        def make_subgrad(x, g):
            return lambda y : g*(y-x) + f(x)
        
        l1 = make_subgrad(1, 1)
        subg_1 = axes.plot(l1, color=YELLOW, use_smoothing=False)
        l2 = make_subgrad(1, 0.5)
        subg_2 = axes.plot(l2, color=YELLOW, use_smoothing=False)
        l3 = make_subgrad(2, 1)
        subg_3 = axes.plot(make_subgrad(2, 1), color=YELLOW, use_smoothing=False)
        l4 = make_subgrad(2, 1.5)
        subg_4 = axes.plot(l4, color=YELLOW, use_smoothing=False)
        co1, co2, co3, co4 = l1(0), l2(0), l3(0), l4(0)

        cross_dot = Dot(axes.c2p(0, co1), color=GREEN)

        self.play(Create(subg_1), Create(cross_dot))
        self.add(DashedLine(axes.c2p(0, co1), axes.c2p(1, f(1)), color=WHITE, dash_length=0.05))
        self.play(Transform(subg_1, subg_2), cross_dot.animate.move_to(axes.c2p(0, co2)))
        self.play(Transform(subg_1, subg_3), cross_dot.animate.move_to(axes.c2p(0, co3)))
        self.play(Transform(subg_1, subg_4), cross_dot.animate.move_to(axes.c2p(0, co4)))
        self.wait()


