from manim import *

class VectorsCombine2D(Scene):
    def construct(self):
        # 坐标轴
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-1, 5],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
        ).scale(0.7).shift(DOWN+3*LEFT)
        # 创建两个向量
        v1 = np.array([4, 2])
        v2 = np.array([1, 3])
        vector1 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*v1), color=RED, buff=0.02)
        vector2 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*v2), color=GREEN, buff=0.02) 

        # 标签， 向量1
        label_O = MathTex(r"O", color=WHITE).next_to(axes.c2p(0, 0), UL)

        label1 = MathTex(r"A", color=RED)
        label1.next_to(vector1.get_end(), RIGHT)
        # 标签， 向量2
        label2 = MathTex(r"B", color=GREEN)
        label2.next_to(vector2.get_end(), LEFT)

        # 再创建一个向量是前两各向量的线性组合
        vector3 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*(1/2 * v1 + 1 * v2)), color=BLUE, buff=0.02)
        # 标签， 向量3
        label3 = MathTex(r"C", color=BLUE)
        label3.next_to(vector3.get_end(), RIGHT)

        # 将向量和标签添加到坐标轴上
        self.play(Create(axes), Create(label_O), Create(vector1), Create(vector2), Create(label1), Create(label2))
        self.play( Create(vector3),Create(label3))
        self.wait(1)

        equation = MathTex(r"\vec{OC} = x\vec{OA} + y\vec{OB}, x,y=?", color=WHITE)
        equation.next_to(axes.c2p(4, 4.5), RIGHT)
        self.play(Write(equation))
        self.wait(1)

        self.play(FadeOut(equation), FadeOut(vector3), FadeOut(label3))

        # 动画，向量 t a + (1-t)b, t 从 0 到 1，再回到1/3
        label_tab = MathTex(r"t \vec{OA} + (1-t) \vec{OB}", color=WHITE).next_to(axes.c2p(5, 4.5), RIGHT)
        t = ValueTracker(0)
        genvec = always_redraw(
            lambda: Arrow(start=axes.c2p(0, 0), end=axes.c2p(*(t.get_value() * v1 + (1-t.get_value()) * v2)), color=BLUE, buff=0.02)
        )
        text_t = always_redraw(
            lambda: MathTex(r"t", color=WHITE).move_to(t.get_value()/2*vector1.get_end() + (1-t.get_value()/2)*vector2.get_end(), UP)
        )
        text_1_t = always_redraw(
            lambda: MathTex(r"1-t", color=WHITE).move_to((1/2+t.get_value()/2)*vector1.get_end() + (1/2-t.get_value()/2)*vector2.get_end(), UR)
        )

        self.play(
            Create(genvec), Create(label_tab), 
            FadeIn(DashedLine(start=axes.c2p(*v1), end=axes.c2p(*v2), color=PINK)),
            FadeIn(text_t), FadeIn(text_1_t)
        )

        self.play(t.animate.set_value(1), run_time=3)
        self.play(t.animate.set_value(1/3))
        textD = MathTex(r"D", color=BLUE_C).next_to(genvec.get_end(), RIGHT)
        self.play(FadeIn(textD), run_time=0.3)
        self.wait(1)

        # 两个三角形填充颜色， OAD 和 OBD
        triangle_OAD = Polygon(axes.c2p(0, 0), axes.c2p(*v1), genvec.get_end(), color=RED_B, fill_opacity=0.2, stroke_width=0.05)
        triangle_OBD = Polygon(axes.c2p(0, 0), axes.c2p(*v2), genvec.get_end(), color=GREEN_B, fill_opacity=0.2, stroke_width=0.05)
        self.play(Create(triangle_OAD), Create(triangle_OBD) )

        label_D = MathTex(
            r"\vec{OD} = \frac{  \vec{DB}  }{  \vec{AB}  }  {\vec{OA}} + \frac{ \vec{AD} }{ \vec{AB} } {\vec{OB}}", 
            color=BLUE_C).shift(label_tab.get_center())
        label_D[0][11:14].set_color(RED)
        label_D[0][-3:].set_color(GREEN)
        label_D[0][4:7].set_color(GREEN_B)
        label_D[0][15:18].set_color(RED_B)

        label_OD = MathTex(
            r"\vec{OD} = \frac{  { S_{\triangle ODB} }  }{  S_{\triangle OAB}  }  {\vec{OA}} + \frac{ {S_{\triangle OAD}} }{ S_{\triangle OAB} } {\vec{OB}}", 
            color=BLUE_C).shift(label_tab.get_center())
        label_OD[0][15:18].set_color(RED)
        label_OD[0][30:].set_color(GREEN)

        label_OD[0][4:9].set_color(GREEN_B)
        label_OD[0][19:24].set_color(RED_B)
        
        self.play(
            ReplacementTransform( label_tab, label_D )
        )
        self.wait(1)
        self.play(
            ReplacementTransform( label_D, label_OD )
        )
        self.wait(1)

        triangle_OAC = Polygon(axes.c2p(0, 0), axes.c2p(*v1), vector3.get_end(), color=RED_B, fill_opacity=0.2, stroke_width=0.05)
        triangle_OCB = Polygon(axes.c2p(0, 0), axes.c2p(*v2), vector3.get_end(), color=GREEN_B, fill_opacity=0.2, stroke_width=0.05)
        self.play(
            FadeOut(textD),FadeIn(label3),
            ReplacementTransform(genvec, vector3),
            Transform(triangle_OAD, triangle_OAC),
            Transform(triangle_OBD, triangle_OCB)
        )

        label_OC = MathTex(
            r"\vec{OC} = \frac{  { S_{\triangle OCB} }  }{  S_{\triangle OAB}  }  {\vec{OA}} + \frac{ {S_{\triangle OAC}} }{ S_{\triangle OAB} } {\vec{OB}}", 
            color=BLUE_C).shift(label_tab.get_center())
        label_OC[0][15:18].set_color(RED)
        label_OC[0][30:].set_color(GREEN)

        label_OC[0][4:9].set_color(GREEN_B)
        label_OC[0][19:24].set_color(RED_B)
        self.play(Transform(label_OD, label_OC))
            
        self.wait(1)

        solve_equation = MathTex(
            r"\begin{bmatrix} c_1 \\ c_2 \end{bmatrix} =\frac{c_1 b_{2} - c_2 b_{1}}{a_{1} b_{2} - a_{2} b_{1}} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} + \frac{a_1 c_{2} - a_2 c_{1}}{a_{1} b_{2} - a_{2} b_{1}} \begin{bmatrix} b_1 \\ b_2\end{bmatrix}",color=BLUE_C).next_to(label_OC, 2*DOWN).scale(0.8)
        solve_equation[0][26:32].set_color(RED)
        solve_equation[0][52:].set_color(GREEN)
        solve_equation[0][7:16].set_color(GREEN_B)
        solve_equation[0][33:42].set_color(RED_B)
        self.play(Write(solve_equation))
        self.wait(1)

        determinant = MathTex(
            r"2S_{\triangle OAB} = a_{1} b_{2} - a_{2} b_{1} ?", 
            color=BLUE_C).next_to(solve_equation, 2*DOWN)
        self.play(Write(determinant))
        self.wait(1)


class TransformAB(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-1, 5],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
        ).scale(0.7).shift(DOWN+3*LEFT)
        # 创建两个向量
        v1 = np.array([4, 2])
        v2 = np.array([1, 3])
        vector1 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*v1), color=RED, buff=0.02)
        vector2 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*v2), color=GREEN, buff=0.02) 

        # 标签， 向量1
        label_O = MathTex(r"O", color=WHITE).next_to(axes.c2p(0, 0), UL)

        label1 = MathTex(r"A", color=RED)
        label1.next_to(vector1.get_end(), RIGHT)
        # 标签， 向量2
        label2 = MathTex(r"B", color=GREEN)
        label2.next_to(vector2.get_end(), LEFT)

        # 再创建一个向量是前两各向量的线性组合
        x,y = 1/2, 1
        vector3 = Arrow(start=axes.c2p(0, 0), end=axes.c2p(*(x * v1 + y * v2)), color=BLUE, buff=0.02)
        # 标签， 向量3
        label3 = MathTex(r"\vec{OC}=x\vec{OA}+y\vec{OB}", color=BLUE)
        label3.next_to(vector3.get_end(), RIGHT)

        vec_x = Arrow(start=axes.c2p(0, 0), end=axes.c2p(1, 0), color=RED, buff=0.02)
        label_x = MathTex(r"\mathbf{e}_1", color=RED).next_to(vec_x.get_end(), RIGHT)
        vec_y = Arrow(start=axes.c2p(0, 0), end=axes.c2p(0, 1), color=GREEN, buff=0.02)
        label_y = MathTex(r"\mathbf{e}_2", color=GREEN).next_to(vec_y.get_end(), UP)
        vec_xy = Arrow(start=axes.c2p(0, 0), end=axes.c2p(x, y), color=BLUE, buff=0.02)
        label_xy = MathTex(r"x\mathbf{e}_1 + y\mathbf{e}_2", color=BLUE).next_to(vec_xy.get_end(), RIGHT)

        dle12 = DashedLine(axes.c2p(1,0), axes.c2p(0, 1), dash_length=0.05)
        
        self.add(axes)
        self.play(
            FadeIn(vec_x), Create(label_x),
            FadeIn(vec_y), Create(label_y),
            FadeIn(vec_xy), Create(label_xy),
            FadeIn(dle12), Create(label_O))
        self.wait()
        
        triangle_12 = Polygon(axes.c2p(0, 0), axes.c2p(1, 0), axes.c2p(0,1), color=BLUE, fill_opacity=0.2, stroke_width=0.05)
        triangle_x = Polygon(axes.c2p(0, 0), axes.c2p(1,0), axes.c2p(x,y), color=RED_B, fill_opacity=0.2, stroke_width=0.05)
        triangle_y = Polygon(axes.c2p(0, 0), axes.c2p(x,y), axes.c2p(0,1), color=GREEN_B, fill_opacity=0.2, stroke_width=0.05)
        self.play(FadeIn(triangle_12), FadeIn(triangle_x), FadeIn(triangle_y))
        self.wait()
        
        triangle_OAB = Polygon(axes.c2p(0, 0), axes.c2p(*v1), axes.c2p(*v2), color=BLUE_B, fill_opacity=0.2, stroke_width=0.05)
        triangle_OAC = Polygon(axes.c2p(0, 0), axes.c2p(*v1), vector3.get_end(), color=RED_B, fill_opacity=0.2, stroke_width=0.05)
        triangle_OCB = Polygon(axes.c2p(0, 0), vector3.get_end(), axes.c2p(*v2), color=GREEN_B, fill_opacity=0.2, stroke_width=0.05)
        ratio = np.linalg.norm(v1-v2)/np.sqrt(2)
        dlab = DashedLine(axes.c2p(*v1), axes.c2p(*v2), dash_length=0.05*ratio)

        #
        self.play(
            ReplacementTransform(vec_x, vector1),
            ReplacementTransform(vec_y, vector2),
            ReplacementTransform(vec_xy, vector3),
            ReplacementTransform(label_x, label1),
            ReplacementTransform(label_y, label2),
            ReplacementTransform(label_xy, label3),
            ReplacementTransform(triangle_12, triangle_OAB),
            ReplacementTransform(triangle_x, triangle_OAC),
            ReplacementTransform(triangle_y, triangle_OCB),
            ReplacementTransform(dle12, dlab),
            run_time = 3
        )
        self.wait()
        
        ratio_eq = MathTex(
            r"\frac{  S_{\triangle OCB}  }{ S_{\triangle OAB}  }  = x \quad \frac{  S_{\triangle OAC}  }{ S_{\triangle OAB}  }  = y ", 
            color=BLUE_C).shift(RIGHT*3)
        ratio_eq[0][13:18].set_color(RED_B)
        ratio_eq[0][24:].set_color(RED)
        ratio_eq[0][0:5].set_color(GREEN_B)
        ratio_eq[0][12:13].set_color(GREEN)
        self.play(Write(ratio_eq))
        self.wait()

class RatioEq(Scene):
    def construct(self):
        ratio_eq = MathTex(
            r"\frac{  S_{\triangle OCB}  }{ S_{\triangle OAB}  }  = x \quad \frac{  S_{\triangle OAC}  }{ S_{\triangle OAB}  }  = y ", 
            color=BLUE_C)
        self.add(index_labels(ratio_eq[0]))
        ratio_eq[0][13:18].set_color(RED_B)
        ratio_eq[0][24:].set_color(RED)
        ratio_eq[0][0:5].set_color(GREEN_B)
        ratio_eq[0][12:13].set_color(GREEN)
        self.add(ratio_eq)
        







class LabelOD(Scene):
    def construct(self):
        label_OD = MathTex(
            r"\vec{OD} = \frac{  { S_{\triangle ODB} }  }{  S_{\triangle OAB}  }  {\vec{OA}} + \frac{ {S_{\triangle OAD}} }{ S_{\triangle OAB} } {\vec{OB}}", 
            color=BLUE_C)
        self.add(index_labels(label_OD[0]))
        label_OD[0][15:18].set_color(RED)
        label_OD[0][30:].set_color(GREEN)

        label_OD[0][4:9].set_color(GREEN_B)
        label_OD[0][19:24].set_color(RED_B)
        self.add(label_OD)

class LabelD(Scene):
    def construct(self):
        label_D = MathTex(
            r"\vec{OD} = \frac{  \vec{DB}  }{  \vec{AB}  }  {\vec{OA}} + \frac{ \vec{AD} }{ \vec{AB} } {\vec{OB}}", 
            color=BLUE_C)
        self.add(index_labels(label_D[0]))
        label_D[0][11:14].set_color(RED)
        label_D[0][-3:].set_color(GREEN)
        label_D[0][4:7].set_color(GREEN_B)
        label_D[0][15:18].set_color(RED_B)
        self.add(label_D)


class SolveEquation(Scene):
    def construct(self):
        solve_equation = MathTex(
            r"\begin{bmatrix} c_1 \\ c_2 \end{bmatrix} =\frac{b_1 c_{2} - b_2 c_{1}}{a_{1} b_{2} - a_{2} b_{1}} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} + \frac{b_2 c_{1} - b_1 c_{2}}{a_{1} b_{2} - a_{2} b_{1}} \begin{bmatrix} b_1 \\ b_2\end{bmatrix}", color=BLUE_C)
        self.add(index_labels(solve_equation[0]))
        solve_equation[0][26:32].set_color(RED)
        solve_equation[0][52:].set_color(GREEN)
        solve_equation[0][7:16].set_color(GREEN_B)
        solve_equation[0][33:42].set_color(RED_B)
        self.add(solve_equation)
        