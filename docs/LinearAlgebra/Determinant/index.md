# 行列式 Determinant

## 消元法解方程

我们从解方程组开始

$$
a_{1} x + b_{1} y = c_1 \\
a_{2} x + b_{2} y = c_2
$$

使用消元法，在非退化的情况下，我们可以得到

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

这就是 **克莱姆法则** (Grammer's Rule).

## 向量的角度

现在我们把他们看作向量，$\vec{OA},\vec{OB},\vec{OC}$.
我们要找到 $\vec{OC}$ 怎么用 $\vec{OA},\vec{OB}$ 表示。

我们考虑 A 和 B 的仿射组合。
t 越大越靠近 A 这边
三角形面积的比例恰好是线段之间的比例
<!-- 插入视频 -->
<video controls width="100%">
  <source src="./media/videos/vectorscombine2d/1080p60/VectorsCombine2D.mp4" type="video/mp4">
</video>



## 变换的角度

我们现在从线性变换的角度看问题
x 是绿色三角形与直角等腰三角形面积的比值，y 是红色的

$$ 
\begin{bmatrix}
x \\ y
\end{bmatrix}
\mapsto 
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
y $$

在非退化的情况下，线性变换不改变线段之间的比例。
也不改变不同区域对应面积的比例。
事实上，一个区域变换后的面积是变换前乘以一个固定的倍数，
恰是两个基向量构成平行四边形的有向面积。
而变换后三角形面积的比例正是变换前三角形面积的比例。

<video controls width="100%">
  <source src="./media/videos/vectorscombine2d/1080p60/TransformAB.mp4" type="video/mp4">
</video>
  


## 行列式的计算


现在我们从两个角度观察了方程解和面积的关系。
我们很明确的意识到到，$a_1 b_{2} - a_2 b_{1}$ 是 $\triangle OAB$ 的 **有向面积** 的两倍。

我们 *创造* 一个符号来表示这个平行四边形的有向面积，叫做 **行列式** ，或更一般的 **外微分** 。
并且得到计算它的公式 

$$
\mathbf{a} \wedge \mathbf{b} =  
\begin{vmatrix}
a_1 & b_1 \\
a_2 & b_2
\end{vmatrix}
= a_1 b_2 - a_2 b_1
$$

事实上你遇见过多种证明他的方式，比如

![???](...)

或者根据定义

$$ 2S_{\triangle OAC} = OA \cdot OB \sin\angle AOB = OA\cdot OB \cos (\angle AOB-\frac{\pi}{2}) = \langle \vec{OA}, \vec{OB'} \rangle $$

你也许已经知道他是对的，
但是一般的 $n$ 维空间中 $n$ 个向量组成的平行立方体的体积又该怎么计算呢？

根据体积的性质，我们能得到行列式必须具备的一些性质

1. 我们规定 $|\mathbf{e}_1, \mathbf{e}_2, \cdots, \mathbf{e}_n| = 1$ 
2. 行列式关于任何一列的向量都是线性的， 
$$ |\mathbf{a}_1, \cdots, \lambda\mathbf{a}_i+\mu\mathbf{b}_i, \cdots, \mathbf{a}_n| = \lambda|\mathbf{a}_1 ,\cdots, \mathbf{a}_i, \cdots, \mathbf{a}_n| + \mu|\mathbf{a}_1, \cdots, \mathbf{b}_i, \cdots ,\mathbf{a}_n|$$
3. 由祖暅原理，
$$ |\mathbf{a}_1, \cdots, \mathbf{a}_i+\mathbf{a}_j, \cdots, \mathbf{a}_n| = |\mathbf{a}_1 ,\cdots, \mathbf{a}_i, \cdots, \mathbf{a}_n|, \quad j\ne i$$

从这三条可以推出计算公式。

由2,3，按线性规则将分量展开，消去为零的项。

$$ 
|\mathbf{a}_1, \mathbf{a}_2, \cdots, \mathbf{a}_n| =  \sum_{\sigma} a_{1\sigma(1)} a_{2\sigma(2)} \cdots a_{n\sigma(n)} |\mathbf{e}_{\sigma(1)}, \mathbf{e}_{\sigma(2)}, \cdots, \mathbf{e}_{\sigma(n)}| $$

$\sigma$ 表示从 $\{1, 2, \cdots, n\}$ 到自身的任何置换。

我们显然还能得到 $|\mathbf{a}_1, \cdots, \mathbf{0}, \cdots, \mathbf{a}_n|=0$
以及最重要的

$$
|\cdots, \mathbf{a}_i, \cdots, \mathbf{a}_j, \cdots| \\
= |\cdots, \mathbf{a}_i+\mathbf{a}_j, \cdots, \mathbf{a}_j, \cdots| \\
= |\cdots, \mathbf{a}_i+\mathbf{a}_j, \cdots, \mathbf{a}_j-(\mathbf{a}_i+\mathbf{a}_j), \cdots|  \\
= - |\cdots, \mathbf{a}_i+\mathbf{a}_j, \cdots, \mathbf{a}_i, \cdots| \\
= - |\cdots, \mathbf{a}_j, \cdots, \mathbf{a}_i, \cdots|
$$

即交换两个向量的顺序则得到的有向体积符号正好相反，这样我们就获得了
那么，求和式中每一项只差一个符号，
$|\mathbf{e}_{\sigma(1)}, \mathbf{e}_{\sigma(2)}, \cdots, \mathbf{e}_{\sigma(n)}| = (-1)^{\tau(\sigma)}$，$\tau(\sigma)$ 是 从顺序排序到 $\sigma$ 所需的对换次数。这也是自洽的。

因此有些教材会直接通过顺序对数来定义行列式。

回到最开始的方程
3 维自行推导

## 非奇异矩阵的逆




