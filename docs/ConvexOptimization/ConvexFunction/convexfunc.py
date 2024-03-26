from manim import * 

class ConvexFunc(Scene):
    """
    画一个二次函数的图像，和一条割线，表示凸函数
    """
    def construct(self):
        x_range = [-3, 3, 1]
        y_range = [-3, 3, 1]
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=8,
            y_length=8,
            axis_config={"stroke_color": BLUE},
            tips=False,
        )
        axes.add_coordinates()
        self.play(Create(axes))

        def func(x):
            return 1/2 * x**2

        curve = axes.plot(func, x_range=[-3, 3], color=RED)
        self.play(Create(curve))

        x1 = -1
        x2 = 1.2
        self.play(
            Create(Dot(axes.c2p(x1, func(x1)), color=YELLOW)),
            Create(Dot(axes.c2p(x2, func(x2)), color=YELLOW))
        )
        line = Line(axes.c2p(x1, func(x1)), axes.c2p(x2, func(x2)), color=YELLOW)
        self.play( Create(line) )

        self.wait()
        

class Epi(Scene):
    """
    上方图
    """
    def construct(self):
        x_range = [-3, 3, 1]
        y_range = [-3, 3, 1]
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=8,
            y_length=8,
            axis_config={"stroke_color": BLUE},
            tips=False,
        )
        axes.add_coordinates()
        self.add(axes)

        def func(x):
            return 1/2 * x**2 - 1
        
        curve = axes.plot(func, x_range=[-3, 3], color=RED)
        self.add(curve)
        b_curve = axes.plot(lambda x: 5, x_range=[-3, 3], color=RED)

        # 函数 上方！ 填充颜色
        fill_color = BLUE_E
        fill_region = axes.get_area(curve, x_range=[-3, 3], color=fill_color, opacity=0.5, bounded_graph=b_curve)
        self.add(fill_region)

        self.add(Tex(r"$f(x)$", color=WHITE).shift(RIGHT*2+UP*-1))
        self.add(Tex("$epi(f)$").shift(UP*1))
