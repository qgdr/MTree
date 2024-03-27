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
        self.add(axes)

        def func(x):
            return 1/2 * x**2

        curve = axes.plot(func, x_range=[-3, 3], color=RED)
        self.add(curve)

        x1 = -1
        x2 = 1.2
        self.add(
            Dot(axes.c2p(x1, func(x1)), color=YELLOW),
            Dot(axes.c2p(x2, func(x2)), color=YELLOW)
        )
        line = Line(axes.c2p(x1, func(x1)), axes.c2p(x2, func(x2)), color=YELLOW)
        self.add( line )

        
        

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


class lsc(Scene):
    """
    下半连续函数
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

        x1 = -1
        x2 = 1.2
        def funcbase(x):
            return 1/2 * x**2
        
        def func(x):
            if x >= x1 and x <= x2:
                return funcbase(x) - 1
            else:
                return funcbase(x)
            
        axes.plot(func, x_range=[-3, 3], color=RED)
        b_curve = axes.plot(lambda x: 5, x_range=[-3, 3], color=RED)
        curve = axes.plot(func, x_range=[-3, 3], color=RED, discontinuities=[x1, x2])
        fill_region = axes.get_area(curve, x_range=[-3, 3], color=BLUE_E, opacity=0.5, bounded_graph=b_curve)
        self.add(fill_region)
        self.add(curve)

        d1 = Circle(radius=.1, color=RED).shift(axes.c2p(x1, func(x1))).set_fill(color=RED, opacity=1)
        d2 = Circle(radius=.1, color=RED).shift(axes.c2p(x2, func(x2))).set_fill(color=RED, opacity=1)

        d3 = Circle(radius=.1, color=RED).set_fill(opacity=0).shift(axes.c2p(x1, funcbase(x1)))
        d4 = Circle(radius=.1, color=RED).set_fill(opacity=0).shift(axes.c2p(x2, funcbase(x2)))

        self.add(d1, d2, d3, d4)
        