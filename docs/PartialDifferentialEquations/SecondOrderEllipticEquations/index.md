# Second-order Elliptic Equations 二阶椭圆方程


本章研究了在给定边界条件下，一致椭圆型二阶偏微分方程的可解性。
我们将使用两种本质上不同的技术，Sobolev空间内的能量方法和最大值原理方法。



## definition 定义

设 \(U\) 是 \(\mathbb{R}^n\) 中的 **有界开集** ，\(u: \bar{U} \to \mathbb{R}\) 是未知函数。
这里 \(f:U \to \mathbb{R}\) 是给定函数。
我们研究边值问题。

$$ \begin{cases}
    Lu=f & \text{in } U \\
    u=0 & \text{on } \partial U
\end{cases} $$

其中 \(L\) 代表偏微分算子，具有下面的某一种形式。

**散度形式 divergence form**

$$ Lu = -\sum_{i,j=1}^n \partial_j(a^{ij}(x)\partial_i u) + \sum_{i=1}^n b^i(x) \partial_i u + c(x) u $$

或者 **非散度形式 non-divergence form**

$$ Lu = -\sum_{i,j=1}^n a^{ij}(x)\partial^2_{ij} u + \sum_{i=1}^n b^i(x) \partial_i u + c(x) u $$

\(a^{ij}, b^i, c \;(i,j=1,2,...,n)\) 是给定的系数函数。

\(u=0 \text{  on } \partial U\) 又是称为 Dirichlet 边界条件。

此后，我们同样假设对称条件

$$ a^{ij}(x) = a^{ji}(x) \quad (i,j=1,2,...,n) $$

## (Uniformly) Elliptic （一致）椭圆算子

如果偏微分算子满足下面条件，则称该算子是 **一致椭圆算子** 。

$$ \sum_{i,j=1}^n a^{ij}(x) \xi_i\xi_j \ge \theta |\xi|^2 \quad \text{for a.e.} x \in U, \forall \xi \in \mathbb{R}^n $$

因此，椭圆性意味着对于每一点 \(x \in U\)，对称的\(n \times n\) 矩阵 \(A (x) = ((a^{ij}(x)))\) 是正定的，其最小特征值大于等于\(\theta\)。

