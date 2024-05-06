from manim import *

class Young(Scene):
    def construct(self):
        title = Tex("Young's inequality")
        self.add(title.shift(3*UP))
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[-1, 2, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
        )
        self.add(axes)
        ln = axes.plot(lambda x: np.log(x), x_range=[0.1, 3], color=RED)
        self.add(ln)

        a, b = 0.8, 2.4
        dota = Dot(axes.c2p(a, np.log(a)), color=GREEN)
        dotb = Dot(axes.c2p(b, np.log(b)), color=GREEN)
        self.add(dota, dotb)
        texa = Tex(r"$a$", color=GREEN).move_to(axes.c2p(a, 0)).shift(0.3*UP)
        texb = Tex(r"$b$", color=GREEN).move_to(axes.c2p(b, 0)).shift(0.3*DOWN)
        self.add(texa, texb)

        theta = 0.4
        line = Line(axes.c2p(a, np.log(a)), axes.c2p(b, np.log(b)), color=YELLOW)
        self.add(line)
        text = Tex(r"$\theta a + (1-\theta)b$", color=PURPLE).move_to(axes.c2p(a * theta + b * (1 - theta), 0)).shift(0.3*DOWN)
        self.add(text)

        dott = Dot(axes.c2p(a * theta + b * (1 - theta), np.log(a * theta + b * (1 - theta))), color=PINK)
        dotl = Dot(axes.c2p(a * theta + b * (1 - theta), theta * np.log(a) + (1 - theta)* np.log(b) ), color=PURPLE)
        self.add(dott, dotl)

        dasha = axes.get_line_from_axis_to_point(0, dota.get_center())
        dashb = axes.get_line_from_axis_to_point(0, dotb.get_center())
        dasht = axes.get_line_from_axis_to_point(0, dott.get_center())
        self.add(dasha, dashb, dasht)

        tex_ineq = Tex(r"$\theta \ln a + (1-\theta)\ln b \leq \ln(\theta a + (1-\theta) b)$", color=YELLOW)
        self.add(tex_ineq.shift(2*UP+2*LEFT))





