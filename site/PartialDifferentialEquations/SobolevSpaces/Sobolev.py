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
        self.add(axes, curve, Tex(r"$u(x) = |x|$", color=WHITE).shift(3.5 * UP))

        diff = axes.plot(lambda x: -np.sign(x), color=RED, use_smoothing=False, x_range=[-3, 3], discontinuities=[0])
        self.add(diff, Tex(r"$u'(x)$").shift(LEFT))


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
            # if x < -2:
            #     return 0
            # elif x < 0:
            #     return x+2
            # elif x < 3:
            #     return 3-x
            # else:
            #     return 0
            if x < 0:
                return 0
            else:
                return 1
        
        curve = axes.plot(func, color=YELLOW, use_smoothing=False, x_range=[-3, 3], discontinuities=[0])
        self.add(axes, curve, Tex(r"$u(x)=\begin{cases} 0, & x < 0 \\ 1, & x \geq 0 \end{cases}$", color=WHITE).shift(2.5 * UP-0.6*RIGHT))

        # def difffunc(x):
            # if x < -2:
            #     return 0
            # elif x < 0:
            #     return 1
            # elif x < 3:
            #     return -1
            # else:
            #     return 0
            
        # diff = axes.plot(difffunc, color=RED, x_range=[-3, 3], use_smoothing=False, discontinuities=[-2, 0, 1, 3])
        # self.add(diff, Tex(r"$f'(x) ?$").shift(RIGHT+0.8*DOWN))
        self.add(Tex(r"$u'(x) = ?$").shift(RIGHT+0.8*DOWN))



def _mollifier(x, n):
    """
    x: np.1darray [x_1, x_2, ..., x_n]
    n: dimension
    """
    norm_squared = np.sum(x**2)
    if norm_squared >= 1:
        return 0
    else:
        return np.exp(1/(x**2-1))


def Alpha(n: int):
    from scipy.special import gamma
    return np.pi**(n/2)/gamma(n/2+1)

def omega(n: int):
    # if n == 1: 
    #     raise ValueError("n must be greater than 1")
    return n*Alpha(n)


def mollifier(x, n):
    from scipy import integrate

    C, err = integrate.quad(lambda r: _mollifier(r, n)*omega(n)*r**(n-1), 0, 1)
    return _mollifier(x, n)/C

def u(x):
    if x < 0:
        return 0
    else:
        return 1

class FmultU(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
            tips=False,
        )
        
        self.add(axes)

        fx = axes.plot(lambda x: mollifier(x, 1), color=GREEN_A, x_range=[-2, 2], discontinuities=[0])
        self.add(fx, Tex(r"$\phi(x)$", color=GREEN_A).shift(2.5 * UP + 2*LEFT))

        ux = axes.plot(u, color=RED_B, x_range=[-2, 2], use_smoothing=False, discontinuities=[0])
        self.add(ux, Tex(r"$u(x)$", color=RED_B).shift(3 * UP+2*RIGHT))
        
        fu = axes.plot(lambda x: u(x)*mollifier(x, 1), color=YELLOW, x_range=[-2, 2], discontinuities=[0])
        self.add(fu, Tex(r"$\phi(x)u(x)$", color=YELLOW).shift(0.5 * UP))




class LowerThanxinv(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 3, 1],
            y_range=[-1, 3, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
            tips=False,
        )
        axes.add_coordinates()
        self.add(axes)
        
        xinv = axes.plot(lambda r: 1/r, x_range=[0.1, 3], color=WHITE)
        self.add(
            xinv,
            Dot(axes.c2p(1, 1), color=YELLOW), 
            axes.get_vertical_line(axes.c2p(1, 1), color=YELLOW)
        )

        self.add(Tex(r"$f(x) = \dfrac{1}{|x|}$ is not integrable", color=WHITE, font_size=24).shift(np.array([3, 3, 0])))

        olt1, ogt1 = 0.6, 1.5
        xlt1 = axes.plot(lambda r: 1/r**(olt1), x_range=[0.1, 1], color=ORANGE)
        xgt1 = axes.plot(lambda r: 1/r**(ogt1), x_range=[1, 3], color=ORANGE)
        self.add( xlt1, xgt1 )

        self.add(
            Tex(r"but $g(x)=\begin{cases} \dfrac{1}{|x|^\alpha} , & 0< \alpha <1 \\  \dfrac{1}{|x|^\beta} , & \beta > 1 \end{cases}$ is integrable", color=ORANGE, font_size=24).shift(np.array([3, 2, 0])) 
        )



class Holder(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 3, 1],
            y_range=[-1, 5, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
            tips=False,
        )
        axes.add_coordinates()
        self.add(axes)

        alpha = 0.3
        def func(x):
            return x**(alpha)
        
        def fdiff(x):
            return x**(alpha-1)/alpha
        
        f = axes.plot(func, color=YELLOW, x_range=[0, 3, 0.001])
        fd = axes.plot(fdiff, color=RED, x_range=[0.1, 3])

        self.add(f, fd)
        self.add(Tex(r"$f(x) = x^\alpha$", color=YELLOW).shift(1*DOWN))
        self.add(Tex(r"$f'(x) = \alpha x^{\alpha-1}$", color=RED).shift(2 * UP))

