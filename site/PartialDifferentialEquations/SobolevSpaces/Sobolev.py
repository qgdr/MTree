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


def chi(Internal):
            return lambda x : (x >= Internal[0]) * (x <= Internal[1])


def mollifier_epsilon(epsilon, n):
            if epsilon <= 0:
                raise "epsilon must be greater than 0"
            return lambda x: mollifier(x/epsilon, n)/epsilon**n


class Urysohn(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
            tips=False,
        )
        # axes.add_coordinates()
        self.add(axes)
        V = [-1, 1]
        U = [-2, 2]
        eps = min(abs(V[0]-U[0]), abs(V[1]-U[1]))
        W = [V[0]-eps/2, V[1]+eps/2]

        # def chi(Internal):
        #     return lambda x : (x >= Internal[0]) * (x <= Internal[1])
            

        
        dx = 0.01
        x_samples = np.arange(-2.5, 2.5, dx, dtype=np.float64)
        chiW = chi(W)(x_samples)
        convker = list(map(mollifier_epsilon(eps/2, 1), x_samples))

        conv_samples = np.convolve(chiW, convker, mode='same')*dx

        conv_points = [axes.c2p(x, y) for x, y in zip(x_samples, conv_samples)]
        conv_graph = VMobject(color=ORANGE).set_points_smoothly(conv_points)
        # conv_graph.set_stroke(TEAL, 2)

        chiW_graph = axes.plot(chi(W), x_range=[-2.5, 2.5], color=RED, use_smoothing=False, discontinuities=W)

        ## 区间表示

        vline = Line(axes.c2p(V[0], 0), axes.c2p(V[1], 0), color=GREEN_A).shift(DOWN*0.2)
        uline = Line(axes.c2p(U[0], 0), axes.c2p(U[1], 0), color=GREEN_B).shift(DOWN*0.4)
        self.add(vline, Tex("V", color=GREEN_A).next_to(vline, RIGHT, buff=0.1), 
                 uline, Tex("U", color=GREEN_B).next_to(uline, RIGHT, buff=0.1))


        texchiW = Tex(r"$\chi_W$", color=RED).shift(2*UP+RIGHT)
        textconv = Tex(r"$f(x) = \chi_W * \eta_\epsilon(x)$", color=ORANGE).shift(2*UP+RIGHT)
        self.play(Create(chiW_graph), Create(texchiW))
        self.wait()
        molli = axes.plot(lambda x : mollifier_epsilon(eps/2, 1)(x - W[0]), color=GRAY, x_range=[U[0], V[0]])
        self.play(FadeIn(molli))
        self.wait()
        self.play(FadeOut(molli), FadeTransform(chiW_graph, conv_graph), Transform(texchiW, textconv), run_time=2)
        self.wait()





class POU(Scene):
    """
    Partition of unity
    """
    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
            tips=False,

        )
        axes.add_coordinates()
        self.add(axes)


        U = [-2, 2]
        V_1 = [-3 ,1]
        V_2 = [-1, 3]
        W_1 = [-2.5, 0.5]
        W_2 = [-0.5, 2.5]

        uline = Line(axes.c2p(U[0], 0), axes.c2p(U[1], 0), color=GREEN_A).shift(DOWN*0.6)
        v1line = Line(axes.c2p(V_1[0], 0), axes.c2p(V_1[1], 0), color=GREEN_B).shift(DOWN*1)
        v2line = Line(axes.c2p(V_2[0], 0), axes.c2p(V_2[1], 0), color=GREEN_C).shift(DOWN*1.4)


        self.add(uline, Tex(r"$U$", color=GREEN_A).next_to(uline, RIGHT, buff=0.1), 
                 v1line, Tex(r"$V_1$", color=GREEN_B).next_to(v1line, LEFT, buff=0.1),
                 v2line, Tex(r"$V_2$", color=GREEN_C).next_to(v2line, RIGHT, buff=0.1)
                )
        
        w1line = Line(axes.c2p(W_1[0], 0), axes.c2p(W_1[1], 0), color=GREEN_D, stroke_width=15).shift(DOWN*1)
        w2line = Line(axes.c2p(W_2[0], 0), axes.c2p(W_2[1], 0), color=GREEN_E, stroke_width=15).shift(DOWN*1.4)
        self.add(w1line, Tex(r"$W_1$", color=GREEN_D).next_to(w1line, RIGHT, buff=0.1), 
                 w2line, Tex(r"$W_2$", color=GREEN_E).next_to(w2line, LEFT, buff=0.1)
                )

        dx = 0.01
        x_samples = np.arange(-4, 4, dx, dtype=np.float64)
        eps = 0.5/2
        chiW = chi([W_1[0]-eps, W_1[1]+eps])(x_samples)
        convker = list(map(mollifier_epsilon(eps, 1), x_samples))
        phi1 = np.convolve(chiW, convker, mode='same')*dx
        phi1_p = [axes.c2p(x, y) for x, y in zip(x_samples, phi1)]
        phi1_graph = VMobject(color=RED_A).set_points_smoothly(phi1_p)

        chiW = chi([W_2[0]-eps, W_2[1]+eps])(x_samples)
        convker = list(map(mollifier_epsilon(0.5/2, 1), x_samples))
        phi2 = np.convolve(chiW, convker, mode='same')*dx
        phi2_p = [axes.c2p(x, y) for x, y in zip(x_samples, phi2)]
        phi2_graph = VMobject(color=RED_B).set_points_smoothly(phi2_p)

        eps = 0.5/2
        chiW = chi([U[0]-eps, U[1]+eps])(x_samples)
        convker = list(map(mollifier_epsilon(eps, 1), x_samples))
        omphi0 = 1- np.convolve(chiW, convker, mode='same')*dx
        omphi0_p = [axes.c2p(x, y) for x, y in zip(x_samples, omphi0)]
        omphi0_graph = VMobject(color=RED_C).set_points_smoothly(omphi0_p)

        tex1, tex2, texu = Tex(r"$\phi_1$", color=RED).shift(2*UP+LEFT), Tex(r"$\phi_2$", color=RED).shift(2*UP+RIGHT), Tex(r"$1-\phi_0$", color=RED).shift(2*UP)

        self.play(
            FadeIn(phi1_graph),
            Create(tex1), 
        )
        self.wait()
        
        self.play(
            FadeOut(phi1_graph),
            FadeOut(tex1),
            FadeIn(phi2_graph),
            Create(tex2), 
        )
        self.wait()

        self.play(
            FadeOut(phi2_graph),
            FadeOut(tex2),
            FadeIn(omphi0_graph),
            Create(texu), 
        )
        self.wait()
        self.play(
            FadeOut(omphi0_graph),
            FadeOut(texu),
        )


        zeta1 = phi1/(phi1 + phi2 + omphi0)
        zeta2 = phi2/(phi1 + phi2 + omphi0)
        zeta1_p = [axes.c2p(x, y) for x, y in zip(x_samples, zeta1)]
        zeta2_p = [axes.c2p(x, y) for x, y in zip(x_samples, zeta2)]
        zeta1_graph = VMobject(color=GREEN_A).set_points_smoothly(zeta1_p)
        zeta2_graph = VMobject(color=GREEN_B).set_points_smoothly(zeta2_p)


        self.play(
            FadeIn(zeta1_graph),
            FadeIn(Tex(r"$\zeta_1 = \frac{\phi_1}{\phi_1 + \phi_2 + 1-\phi_0}$", color=RED).shift(2*UP+3*LEFT)),
        )
        self.wait()
        self.play(
            FadeIn(zeta2_graph),
            FadeIn(Tex(r"$\zeta_2 = \frac{\phi_2}{\phi_1 + \phi_2 + 1-\phi_0}$", color=RED).shift(2*UP+3*RIGHT)),
        )
        self.wait()
        self.play(Create(Tex(r"$\zeta_1 + \zeta_2 = 1$ on $U$").shift(DOWN*3)))
        self.wait()



        
