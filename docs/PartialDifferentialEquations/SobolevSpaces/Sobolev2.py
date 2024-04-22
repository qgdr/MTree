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