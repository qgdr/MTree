from manim import *
from manim.opengl import *

class Counterexample(Scene):
    """
    3D 极坐标函数
    z = rho**2(pi-theta)
    """
    def construct(self):
        surface = OpenGLSurface(
            lambda u, v: (u * np.cos(v),
                    u * np.sin(v),
                    -0.2*u**2 * (np.pi - v)),
            u_range=(0, 1),
            v_range=(0, 2*np.pi),
            color=BLUE,
            resolution=(20, 20)
        ).scale(3)
        surface_mesh = OpenGLSurfaceMesh(surface)

        self.camera.set_euler_angles(
                theta=0*DEGREES,
                phi=0*DEGREES
            )

        self.add(surface, surface_mesh)
        self.wait(2)
        self.play(self.camera.animate.set_euler_angles(theta=90*DEGREES, phi=90*DEGREES), run_time=2)
        self.wait(2)
        self.play(self.camera.animate.set_euler_angles(theta=0*DEGREES, phi=0*DEGREES), run_time=2)
        self.wait(2)

# manim -pqm Sobolev2.py --format=gif --renderer=opengl Counterexample
    
class GSI1(Scene):
    def construct(self):
        n = 6
        line = NumberLine(x_range=[0, n+2])

        p = 1.8
        ps = [n*p/(n-i*p) for i in range(3) ]

        pointers = [Vector(DOWN).next_to(line.number_to_point(pi), UP) for pi in ps]
        texs = [Tex(r"$p^{(" + str(i) + ")}$").next_to(pointers[i], UP) for i in range(1, 3)]
        texs = [Tex(r"$p$").next_to(pointers[0], UP)] + texs
        texk = [Tex(r"$" + str(3-i) + "$").next_to(pointers[i], UP).shift(1*UP) for i in range(3)]

        
        self.add(line, Tex(r"1").next_to(line.number_to_point(1), DOWN), Tex(r"n").next_to(line.number_to_point(n), DOWN), Tex(r"k=").shift(2.7*UP+4*LEFT))
        for i in range(3):
            self.play(Create(pointers[i]), Write(texs[i]), Write(texk[i]))

        self.wait(2)


class GSI2(Scene):
    def construct(self):
        n = 6
        line = NumberLine(x_range=[0, n+2])

        p = 2
        ps = [n*p/(n-i*p) for i in range(3) ]

        pointers = [Vector(DOWN).next_to(line.number_to_point(pi), UP) for pi in ps]
        texs = [Tex(r"$p^{(" + str(i) + ")}$").next_to(pointers[i], UP) for i in range(1, 3)]
        texs = [Tex(r"$p$").next_to(pointers[0], UP)] + texs
        texk = [Tex(r"$" + str(3-i) + "$").next_to(pointers[i], UP).shift(1*UP) for i in range(3)]

        
        self.add(line, Tex(r"1").next_to(line.number_to_point(1), DOWN), Tex(r"n").next_to(line.number_to_point(n), DOWN), Tex(r"k=").shift(2.7*UP+4*LEFT))
        for i in range(3):
            self.play(Create(pointers[i]), Write(texs[i]), Write(texk[i]))

        self.wait(2)


class GSI3(Scene):
    def construct(self):
        n = 6
        line = NumberLine(x_range=[0, n+2])

        p = 2.1
        ps = [n*p/(n-i*p) for i in range(3) ]

        pointers = [Vector(DOWN).next_to(line.number_to_point(pi), UP) for pi in ps]
        texs = [Tex(r"$p^{(" + str(i) + ")}$").next_to(pointers[i], UP) for i in range(1, 3)]
        texs = [Tex(r"$p$").next_to(pointers[0], UP)] + texs
        texk = [Tex(r"$" + str(3-i) + "$").next_to(pointers[i], UP).shift(1*UP) for i in range(3)]

        
        self.add(line, Tex(r"1").next_to(line.number_to_point(1), DOWN), Tex(r"n").next_to(line.number_to_point(n), DOWN), Tex(r"k=").shift(2.7*UP+4*LEFT))
        for i in range(3):
            self.play(Create(pointers[i]), Write(texs[i]), Write(texk[i]))

        self.wait(2)



class Fepsx(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 1],
            y_range=[-0.2, 1.2],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE},
            tips=False,
        )

        def F(eps):
            return lambda x : 0 if x < 0 else np.sqrt(x**2+eps**2) - eps
        
        def dF(eps):
            return lambda x : 0 if x < 0 else x/np.sqrt(x**2+eps**2)
        
        F1 = axes.plot(F(0.3), x_range=[-2, 2, 0.001], color=RED_A)
        F2 = axes.plot(F(0.2), x_range=[-2, 2, 0.001], color=GREEN_A)
        F3 = axes.plot(F(0.1), x_range=[-2, 2, 0.001], color=YELLOW_A)

        dF1 = axes.plot(dF(0.3), x_range=[-2, 2, 0.001], color=RED_B)
        dF2 = axes.plot(dF(0.2), x_range=[-2, 2, 0.001], color=GREEN_B)
        dF3 = axes.plot(dF(0.1), x_range=[-2, 2, 0.001], color=YELLOW_B)

        texF1 = Tex(r"$F_{0.3}(x)$", color=RED_A).shift(2.5*UP+3*LEFT)
        texF2 = Tex(r"$F_{0.2}(x)$", color=GREEN_A).next_to(texF1, DOWN)
        texF3 = Tex(r"$F_{0.1}(x)$", color=YELLOW_A).next_to(texF2, DOWN)
        texdF1 = Tex(r"$F'_{0.3}(x)$", color=RED_B).next_to(texF3, DOWN)
        texdF2 = Tex(r"$F'_{0.2}(x)$", color=GREEN_B).next_to(texdF1, DOWN)
        texdF3 = Tex(r"$F'_{0.1}(x)$", color=YELLOW_B).next_to(texdF2, DOWN)

        self.add(axes, F1, F2, F3, dF1, dF2, dF3)
        self.add(texF1, texF2, texF3, texdF1, texdF2, texdF3)

