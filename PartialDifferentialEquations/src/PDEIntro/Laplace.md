# Laplace方程

[PDE 2.2](../Introduction.md#教材)

1. Laplace's equation  $$ \Delta u = 0 $$  
2. Poisson's equation  $$ -\Delta u = f $$  

满足 Laplace 方程的函数称为 **调和函数**(harmonic function)

## 调和函数

调和函数是函数本身的几何性质，所以坐标轴平移、旋转都不影响函数的调和性质。

### 调和函数基本解

$$
\Phi(x) :=
\begin{cases}
    -\frac{1}{2\pi}\log|x|  & (n=2) \\\\
    \frac{1}{n(n-2)\alpha(n)}\frac{1}{|x|^{n-2}}    & (n \ge 3)
\end{cases}
$$