from manim import *

class Equation(Scene):
    def construct(self):
        eq = MathTex(
            r"a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2",
            substrings_to_isolate=["a_1", "a_2", "b_1", "b_2", "c_1", "c_2"]
        )
        eq.set_color_by_tex_to_color_map({
            "a_1": RED,
            "a_2": RED,
            "b_1": GREEN,
            "b_2": GREEN,
            "c_1": BLUE,
            "c_2": BLUE
        })
        self.play(Write(eq))
        self.wait()
        self.play(eq.animate.shift(UP*2))

        Elim_y = MathTex(
            r"a_1 b_2 x + b_1 b_2 y = c_1 b_2 \\ a_2 b_1 x + b_2 b_1 y = c_2 b_1",
            substrings_to_isolate=["a_1", "a_2", "b_1", "b_2", "c_1", "c_2"]
        ).shift(LEFT*2.5)
        Elim_y.set_color_by_tex_to_color_map({
            "a_1": RED,
            "a_2": RED,
            "b_1": GREEN,
            "b_2": GREEN,
            "c_1": BLUE,
            "c_2": BLUE
        })
        Elim_x = MathTex(
            r"a_2 a_1 x + a_2 b_1 y = a_2 c_1 \\ a_1 a_2 x + a_1 b_2 y = a_1 c_2",
            substrings_to_isolate=["a_1", "a_2", "b_1", "b_2", "c_1", "c_2"]
        ).shift(RIGHT*2.5)
        Elim_x.set_color_by_tex_to_color_map({
            "a_1": RED,
            "a_2": RED,
            "b_1": GREEN,
            "b_2": GREEN,
            "c_1": BLUE,
            "c_2": BLUE
        })
        self.play(FadeIn(Elim_y), FadeIn(Elim_x))
        self.wait()
        
        solve_x = MathTex( 
            r"x = \frac{c_1 b_2 - c_2 b_1}{a_1 b_2 - a_2 b_1}"
        ).next_to(Elim_y, 2*DOWN)
        solve_y = MathTex( 
            r"y = \frac{a_1 c_2 - a_2 c_1}{a_1 b_2 - a_2 b_1}"
        ).next_to(Elim_x, 2*DOWN)
        self.play(Write(solve_x), Write(solve_y))
        self.wait()


class VecEq(Scene):
    def construct(self):
        eq = MathTex(
            r"a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2",
            substrings_to_isolate=["a_1", "a_2", "b_1", "b_2", "c_1", "c_2"]
        ).shift(UP)
        eq.set_color_by_tex_to_color_map({
            "a_1": RED,
            "a_2": RED,
            "b_1": GREEN,
            "b_2": GREEN,
            "c_1": BLUE,
            "c_2": BLUE
        })
        self.play(Write(eq))
        self.wait()
        
        veceq = MathTex(
            r" \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} x + \begin{bmatrix} b_1 \\ b_2\end{bmatrix} y = \begin{bmatrix} c_1 \\ c_2 \end{bmatrix}",
            substrings_to_isolate=[r"\begin{bmatrix} a_1 \\ a_2 \end{bmatrix}", r"\begin{bmatrix} b_1 \\ b_2\end{bmatrix}", r"\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}"]
        ).next_to(eq, 2*DOWN)
        veceq.set_color_by_tex_to_color_map({
            "a_1": RED,
            "a_2": RED,
            "b_1": GREEN,
            "b_2": GREEN,
            "c": BLUE
        })
        self.play(
            FadeIn(veceq),
        )
        self.wait()


class ExcalEq(Scene):
    def construct(self):
        eq = MathTex(
            r"\mathbf{a} x + \mathbf{b} y = \mathbf{c}",
            
        ).shift(UP)
        eq.set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            "c": BLUE
        })
        ex_cal_b = MathTex(
            r"\mathbf{a}\wedge\mathbf{b}  x + \mathbf{b}\wedge\mathbf{b} y = \mathbf{c}\wedge\mathbf{b}",
            
        ).shift(LEFT*3)
        ex_cal_left_x = MathTex(
            r"\mathbf{a}\wedge\mathbf{b}  x  = \mathbf{c}\wedge\mathbf{b}",
            
        ).next_to(ex_cal_b, DOWN)
        ev_x = MathTex(
            r"x = \frac{\mathbf{c}\wedge\mathbf{b}}{\mathbf{a}\wedge\mathbf{b}}",
            
        ).next_to(ex_cal_left_x, DOWN)

        ex_cal_a = MathTex(
            r"\mathbf{a}\wedge\mathbf{a}  x + \mathbf{a}\wedge\mathbf{b} y = \mathbf{a}\wedge\mathbf{c}",
        ).shift(RIGHT*3)
        ex_cal_left_y = MathTex(
            r"\mathbf{a}\wedge\mathbf{b}  y  = \mathbf{a}\wedge\mathbf{c}",  
        ).next_to(ex_cal_a, DOWN)
        ev_y = MathTex(
            r"y = \frac{\mathbf{a}\wedge\mathbf{c}}{\mathbf{a}\wedge\mathbf{b}}"
        ).next_to(ex_cal_left_y, DOWN)

        self.play(Write(eq))
        self.wait()
        self.play(FadeIn(ex_cal_b), FadeIn(ex_cal_a))
        self.wait()
        self.play(
            FadeIn(ex_cal_left_x),
            FadeIn(ex_cal_left_y)
        )
        self.wait()
        self.play(
            FadeIn(ev_x),
            FadeIn( ev_y)
        )
        self.wait()
        







class Elimination(Scene):
    def construct(self):
        Elim_y = MathTex(
            r"a_1 b_2 x + b_1 b_2 y = c_1 b_2 \\ a_2 b_1 x + b_2 b_1 y = c_2 b_1",
            substrings_to_isolate=["a_1", "a_2", "b_1", "b_2", "c_1", "c_2"]
        )
        Elim_y.set_color_by_tex_to_color_map({
            "a_1": RED,
            "a_2": RED,
            "b_1": GREEN,
            "b_2": GREEN,
            "c_1": BLUE,
            "c_2": BLUE
        })
        self.add(Elim_y)