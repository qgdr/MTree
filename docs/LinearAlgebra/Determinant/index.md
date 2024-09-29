# 行列式 Determinant

我们从解方程组开始

$$
a_{1} x + b_{1} y = c_1 \\
a_{2} x + b_{2} y = c_2
$$

使用消元法，在足够好的情况下，我们可以得到

$$
x = \frac{c_1 b_{2} - c_2 b_{1}}{a_{1} b_{2} - a_{2} b_{1}}
$$

$$
y = \frac{a_1 c_{2} - a_2 c_{1}}{a_{1} b_{2} - a_{2} b_{1}}
$$

但是，我们从另一个角度来理解，并找到方程组的解。
我们知道，方程组可以理解为向量组的线性组合。

$$
\begin{bmatrix}
a_{1}  \\
a_{2}
\end{bmatrix}
x
+
\begin{bmatrix}
b_{1} \\
b_{2}
\end{bmatrix}
y
=
\begin{bmatrix}
c_1 \\
c_2
\end{bmatrix}
$$

即

$$
\begin{bmatrix}
c_1 \\ c_2
\end{bmatrix}
=
\frac{c_1 b_{2} - c_2 b_{1}}{a_{1} b_{2} - a_{2} b_{1}}
\begin{bmatrix}
a_1 \\ a_2
\end{bmatrix}
+
\frac{a_1 c_{2} - a_2 c_{1}}{a_{1} b_{2} - a_{2} b_{1}}
\begin{bmatrix}
b_1 \\ b_2
\end{bmatrix}
$$

现在我们把他们看作向量，$\vec{OA},\vec{OB},\vec{OC}$.
我们要找到 $\vec{OC}$ 怎么用 $\vec{OA},\vec{OB}$ 表示。

<!-- 插入视频 -->
<video controls width="100%">
  <source src="./media/videos/vectorscombine2d/1080p60/VectorsCombine2D.mp4" type="video/mp4">
  您的浏览器不支持 video 标签。
</video>

我们很明确的意识到到，$a_1 c_{2} - a_2 c_{1}$ 是 $\triangle OAC$ 的 **有向面积** 的两倍。
并且经过验证确实是这样的。

我们 *创造* 一个符号来表示这个平行四边形的有向面积，叫做 **行列式** 。
并且得到计算它的公式

$$
\begin{vmatrix}
a_1 & b_1 \\
a_2 & b_2
\end{vmatrix}
= a_1 b_2 - a_2 b_1
$$


