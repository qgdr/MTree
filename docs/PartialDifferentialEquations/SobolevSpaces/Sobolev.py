from manim import *

class Func1(Scene):
    """
    y = |x|
    """
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
            tips=False,
        )
        curve = axes.plot(lambda x: 3-abs(x), color=YELLOW, x_range=[-3, 3], use_smoothing=False)
        self.add(axes, curve, Tex(r"$y = |x|$", color=WHITE).shift(3.5 * UP))

        diff = axes.plot(lambda x: -np.sign(x), color=RED, use_smoothing=False, x_range=[-3, 3], discontinuities=[0])
        self.add(diff, Tex(r"$f'(x)$").shift(LEFT))


class Func2(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
            tips=False,
        )
        def func(x):
            if x < -2:
                return 0
            elif x < 0:
                return x+2
            elif x < 3:
                return 3-x
            else:
                return 0
        
        curve = axes.plot(func, color=YELLOW, use_smoothing=False, x_range=[-3, 3], discontinuities=[0])
        self.add(axes, curve, Tex(r"$f(x)$", color=WHITE).shift(2.5 * UP-0.6*RIGHT))

        def difffunc(x):
            if x < -2:
                return 0
            elif x < 0:
                return 1
            elif x < 3:
                return -1
            else:
                return 0
            
        diff = axes.plot(difffunc, color=RED, x_range=[-3, 3], use_smoothing=False, discontinuities=[-2, 0, 1, 3])
        self.add(diff, Tex(r"$f'(x) ?$").shift(RIGHT+0.8*DOWN))


class log1dr(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-0.2, 1.2, 1],
            y_range=[-0.5, 1.2, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
            tips=False,
        )
        def func(r, n):
            return np.abs(np.log(r))**n * r**(n-1)
        
        func2 = axes.plot(lambda r: func(r, 2), color=YELLOW, x_range=[1e-6, 1], discontinuities=[0])
        func3 = axes.plot(lambda r: func(r, 3), color=RED, x_range=[1e-6, 1], discontinuities=[0])

        self.add(axes, func2, func3)
        self.add(
            Tex(r"$f(r) = |\log \frac{1}{r}|^n r^{n-1}$", color=WHITE), 
            Tex(r"$n=2$", color=YELLOW).shift(3.5 * UP),
            Tex(r"$n=3$", color=RED).shift(3.5 * UP+2*RIGHT)
        )


