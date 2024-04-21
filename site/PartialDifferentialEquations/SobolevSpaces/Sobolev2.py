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
                theta=-10*DEGREES,
                phi=50*DEGREES
            )

        self.add(surface, surface_mesh)
        self.wait(2)
        self.play(self.camera.animate.set_euler_angles(theta=60*DEGREES))
        self.wait(2)

    
    