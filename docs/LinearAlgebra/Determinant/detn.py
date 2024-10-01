from manim import *

class Detn(Scene):
    def construct(self):
        textdef = MathTex(
            r" \mathbf{a} \wedge \mathbf{b} = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1"
        )
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-1, 5],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
        )
        
        self.add(textdef)
        self.wait(1)
        self.play(FadeOut(textdef))

        vec_x = Arrow(start=axes.c2p(0, 0), end=axes.c2p(1, 0), color=RED, buff=0.02)
        label_x = MathTex(r"\mathbf{e}_1", color=RED).next_to(vec_x.get_end(), RIGHT)
        vec_y = Arrow(start=axes.c2p(0, 0), end=axes.c2p(0, 1), color=GREEN, buff=0.02)
        label_y = MathTex(r"\mathbf{e}_2", color=GREEN).next_to(vec_y.get_end(), UP)
        sqr1 = Polygon(axes.c2p(0, 0), axes.c2p(1, 0), axes.c2p(1,1), axes.c2p(0,1), color=BLUE, fill_opacity=0.5, stroke_width=0.05)
        
        self.play(
            Create(axes),
            FadeIn(vec_x), FadeIn(label_x),
            FadeIn(vec_y), FadeIn(label_y),
            FadeIn(sqr1)
        )
        self.wait()

        prop1 = VGroup(axes, vec_x, label_x, vec_y, label_y, sqr1)
        self.play(
            prop1.animate.scale(0.6).shift(DOWN+3.5*LEFT)
        )
        ptext1 = MathTex(r"1: \quad \mathbf{e}_1 \wedge \mathbf{e}_2 \wedge \cdots \wedge  \mathbf{e}_n = 1").shift(RIGHT*3+UP*2.5).scale(0.6)
        self.play(Write(ptext1))
        self.wait()
        
        self.play(FadeOut(VGroup(vec_x, label_x, vec_y, label_y, sqr1)))


        v1 = np.array([4, 2])
        v2 = np.array([1, 3])
        vector1 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*v1), color=RED, buff=0.02)
        
        t = ValueTracker(0)
        vector2 = always_redraw(
            lambda: Arrow(start=axes.c2p(0, 0), end=axes.c2p(*(v2+t.get_value()*v1)), color=GREEN, buff=0.02) 
        )
        v3 = np.array([-1, 1])
        vector3 = Arrow(start=axes.c2p(*v2), end=axes.c2p(*(v2+v3)), color=BLUE, buff=0.02)

        # label1 = MathTex(r"\vec{a}", color=RED)
        # label1.next_to(vector1.get_end(), RIGHT)
        # # 标签， 向量2
        # label2 = MathTex(r"\vec{b}", color=GREEN)
        # label2.next_to(vector2.get_end(), LEFT)
        sqr2 = always_redraw(
            lambda: Polygon(axes.c2p(0, 0), axes.c2p(*v1), axes.c2p(*(v2+ (1+t.get_value())*v1)), axes.c2p(*(v2+t.get_value()*v1)), color=BLUE, fill_opacity=0.5, stroke_width=0.05)
        )
        sqr3 = Polygon(
            axes.c2p(*v2), axes.c2p(*(v2+v1)), axes.c2p(*(v2+v3+v1)), axes.c2p(*(v2+v3)), color=GREEN, fill_opacity=0.5, stroke_width=0.05
        )
        sqrp = Polygon(
            axes.c2p(0, 0), axes.c2p(*v1), axes.c2p(*(v1+v2+v3)), axes.c2p(*(v2+v3)), color=GREEN_C, fill_opacity=0.5, stroke_width=0.05
        )
        self.play(FadeIn(VGroup(vector1, vector2, vector3, sqr2, sqr3)))
        self.play(FadeOut(VGroup(sqr2, sqr3)), FadeIn(sqrp))
        self.wait()
        
        ptext2 = MathTex(r"2: \quad \begin{aligned}&\mathbf{a}_1 \wedge \cdots \wedge (\lambda\mathbf{a}_i+\mu\mathbf{b}_i)\wedge \cdots \wedge \mathbf{a}_n \\&= \lambda \mathbf{a}_1 \wedge \cdots\wedge \mathbf{a}_i\wedge \cdots \wedge \mathbf{a}_n + \mu \mathbf{a}_1\wedge  \cdots\wedge  \mathbf{b}_i\wedge \cdots \wedge \mathbf{a}_n\end{aligned}").next_to(ptext1, DOWN).scale(0.6)
        self.play(Write(ptext2))
        self.wait()
        self.play(FadeOut(VGroup(vector3, sqrp)), FadeIn(sqr2))
        self.play(t.animate.set_value(-1/3))
        self.play(t.animate.set_value(0))
        self.wait()
        
        ptext3 = MathTex(r"3: \quad \mathbf{a}_1 \wedge \cdots \wedge (\mathbf{a}_i+\mathbf{a}_j) \wedge \cdots \wedge \mathbf{a}_n = \mathbf{a}_1 \wedge \cdots \wedge \mathbf{a}_i \wedge \cdots \wedge \mathbf{a}_n").next_to(ptext2, DOWN).scale(0.6)
        self.play(Write(ptext3))
        self.wait()

        cor1 = MathTex(
            r"2+3\Rightarrow \begin{aligned} &\mathbf{a}_1\wedge \mathbf{a}_2\wedge \cdots\wedge \mathbf{a}_n \\ &=  \sum_{\sigma} a_{1\sigma(1)} a_{2\sigma(2)} \cdots a_{n\sigma(n)} \; \mathbf{e}_{\sigma(1)}\wedge \mathbf{e}_{\sigma(2)}\wedge \cdots \wedge \mathbf{e}_{\sigma(n)}\end{aligned}"
        ).next_to(ptext3, DOWN).scale(0.6)
        self.play(Write(cor1))
        self.wait()

        cor2 = MathTex(
            r"3\Rightarrow \begin{aligned} &\cdots \wedge \mathbf{a}_i \wedge \cdots \wedge \mathbf{a}_j \wedge \cdots \\ &= \cdots \wedge (\mathbf{a}_i+\mathbf{a}_j)\wedge \cdots \wedge \mathbf{a}_j\wedge \cdots \\ &= \cdots \wedge (\mathbf{a}_i+\mathbf{a}_j)\wedge \cdots \wedge (\mathbf{a}_j-(\mathbf{a}_i+\mathbf{a}_j))\wedge \cdots  \\ &= - \cdots\wedge (\mathbf{a}_i+\mathbf{a}_j)\wedge \cdots\wedge \mathbf{a}_i\wedge \cdots \\&= - \cdots\wedge \mathbf{a}_j\wedge \cdots\wedge \mathbf{a}_i\wedge \cdots \end{aligned}"
        ).scale(0.6).next_to(cor1, DOWN)
        
        cor2new = MathTex(
            r"4: \quad \begin{aligned}\cdots \wedge \mathbf{a}_i \wedge \cdots \wedge \mathbf{a}_j \wedge \cdots \\ = - \cdots \wedge \mathbf{a}_j \wedge \cdots \wedge \mathbf{a}_i \wedge \cdots \end{aligned}"
        ).scale(0.6).next_to(cor1, DOWN)
        self.play(Write(cor2))
        self.wait()
        self.play(ReplacementTransform(cor2, cor2new))
        self.wait()

        cor3 = MathTex(
            r"4\Rightarrow \mathbf{e}_{\sigma(1)}\wedge \mathbf{e}_{\sigma(2)}\wedge \cdots \wedge \mathbf{e}_{\sigma(n)} = (-1)^{\tau(\sigma)}"
        ).scale(0.6).next_to(cor2new, DOWN)
        self.play(Write(cor3))
        self.wait()
        finaltext = MathTex(
            r"\mathbf{a}_1\wedge \mathbf{a}_2\wedge \cdots\wedge \mathbf{a}_n = \sum_{\sigma} (-1)^{\tau(\sigma)} a_{1\sigma(1)} a_{2\sigma(2)} \cdots a_{n\sigma(n)} "
        ).next_to(cor3, DOWN).scale(0.6)
        self.play(Write(finaltext))
        self.wait()
        # self.play(FadeOut(VGroup(axes, vector1, vector2, sqr2)))
        self.play(
            FadeOut(VGroup(axes, vector1, vector2, sqr2)),
            FadeOut(ptext1), FadeOut(ptext2), FadeOut(ptext3), FadeOut(cor1) ,FadeOut(cor2new), FadeOut(cor3),
            finaltext.animate.scale(2).move_to(ORIGIN)
        )


        

