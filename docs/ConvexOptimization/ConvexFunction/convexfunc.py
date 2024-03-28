from manim import * 
from scipy.optimize import fsolve, minimize

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


class ConjugateFunc(Scene):
    """
    画一个视频，沿曲线上的点，一条固定斜率为 y 的直线移动，直线与 y 轴的交点记成 (0, -f^*(y))
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
        self.add(axes)
        def func(x):
            return 1/4 * x**4 -1/4*x**2 + 1/4*x + 1
        
        curve = axes.plot(func, x_range=[-3, 3], color=RED)
        self.add(curve)

        y = 1
        alpha = ValueTracker(0.45)
        point = always_redraw(
            lambda: Dot(
                curve.point_from_proportion(alpha.get_value()),
                color=BLUE
            )
        )

        def fx(x):
            pos = curve.point_from_proportion(alpha.get_value())
            pos = axes.p2c(pos)
            return y*x - y*pos[0] + pos[1]
            
        line = always_redraw(
            lambda: axes.plot(
                fx,
                x_range=[-3, 3],
                color=YELLOW
            )
        )

        nf0 = always_redraw(
            lambda: Dot(axes.c2p(0, fx(0)), color=GREEN)
        )
        nf0tail = TracedPath(nf0.get_center, dissipating_time=1, stroke_color=LIGHT_BROWN, stroke_width=15, stroke_opacity=[1, 0.3])

        texnf0 = always_redraw(
            lambda: Tex(r"$f(x)-y^T x$", color=WHITE, font_size=20).shift(UP*fx(0)+LEFT*.4)
        )
        self.add(axes, curve)
        self.add(nf0, nf0tail, texnf0, point, line)
        self.play(alpha.animate.set_value(0.55), rate_func=linear, run_time=3)

        x_m, = minimize(lambda x: -y*x + func(x), x0=0).x
        nfs = - y*x_m + func(x_m)
        self.play(
            FadeOut(point, line, nf0, texnf0),
            Create(axes.plot(lambda x: y*x + nfs, color=ORANGE)),
            Create(Dot(axes.c2p(x_m, func(x_m)), color=BLUE)),
            Create(Dot(axes.c2p(0, nfs), color=GREEN)),
            Create(Tex(r"$-f^*(y)$", color=WHITE, font_size=20).shift(UP*nfs+LEFT*.4)),
        )
        self.wait()



class ConjugateConvex(Scene):
    """
    画一个非凸曲线，和两条切线
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
        # axes.add_coordinates()
        self.add(axes)
        def func(x):
            return 1/4 * x**4 -1/4*x**2 + 1/4*x + 1
        def tangent(x):
            return 1 * x**3 - 1/2*x + 1/4
        
        curve = axes.plot(func, x_range=[-3, 3], color=RED)
        self.add(curve)

        
        x1 = -1.2
        x2 = 1.5
        self.add(
            Dot(axes.c2p(x1, func(x1)), color=YELLOW),
            Dot(axes.c2p(x2, func(x2)), color=YELLOW)
        )
        def fs1(x):
            return tangent(x1) * (x - x1) + func(x1)
        def fs2(x):
            return tangent(x2) * (x - x2) + func(x2)
        line1 = axes.plot(fs1, x_range=[-3, 3], color=YELLOW)
        line2 = axes.plot(fs2, x_range=[-3, 3], color=YELLOW)

        self.add( line1 ,line2 )

        self.add(
            Dot(axes.c2p(0, fs1(0)), color=GREEN),
            Dot(axes.c2p(0, fs2(0)), color=GREEN)
        )

        self.add(
            Tex(r"$-f^*(y_1)$", color=WHITE, font_size=20).shift(axes.c2p(0, fs1(0))).shift(LEFT*.8),
            Tex(r"$-f^*(y_2)$", color=WHITE, font_size=20).shift(axes.c2p(0, fs2(0))).shift(RIGHT*.8)
        )
        
        x_c, = fsolve(lambda x: fs1(x) - fs2(x), x0=0)
        x_m, = minimize(lambda x: -(tangent(x1) + tangent(x2)) / 2 * x + func(x), x0=0).x
        def fs_c(x):
            return (tangent(x1) + tangent(x2)) / 2 * (x - x_c) + fs1(x_c)
        def fs_m(x):
            return (tangent(x1) + tangent(x2)) / 2 * (x - x_m) + func(x_m)
        
        line_c = DashedLine( axes.c2p(-3, fs_c(-3)), axes.c2p(3, fs_c(3)) )
        line_m = DashedLine( axes.c2p(-3, fs_m(-3)), axes.c2p(3, fs_m(3)) )
        self.add(line_c, line_m)

        self.add(
            Dot(axes.c2p(0, fs_c(0)), color=ORANGE), 
            Tex(r"$-\dfrac{f^*(y_1) + f^*(y_2)}{2})$", color=WHITE, font_size=20).shift(axes.c2p(0, fs_c(0))).shift(LEFT*.8),
            Dot(axes.c2p(0, fs_m(0)), color=RED),
            Tex(r"$-f^*(\dfrac{y_1 + y_2}{2})$", color=WHITE, font_size=20).shift(axes.c2p(0, fs_m(0))).shift(UP*.5),
        )
