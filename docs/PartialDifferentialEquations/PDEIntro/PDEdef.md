# PDE 定义

[Lawrence C.Evans Partial differential equations 1.1](../index.md#教材)

令 \( k\ge 1 \)，\( U \) 是一个 \( R^n \) 中的 **开集**。 
给定函数

$$
\begin{equation}
    F: R^{n^k} \times R^{n^{k-1}} \times \cdots \times R^n \times R \times U \to R
\end{equation}
$$

与未知函数

$$
u: U \to R
$$

等式

$$
\begin{equation}
F(D^ku(x), D^{k-1}u(x), ... , Du(x), u(x), x)=0 \quad (x\in U)
\end{equation}
$$

称为 \( k \) 阶偏微分方程。

## 按线性性分类

1 . 线性 linear： 

$$ \sum_{|\alpha|\le k}a_\alpha(x) D^\alpha u = f(x) $$

2 . 半线性 semilinear：

$$ \sum_{ |\alpha|=k} a_\alpha(x) D^\alpha u + a_0(D^{k-1}u, ... , Du, u, x) = 0 $$

3 . 次线性 quasilinear:

$$ \sum_{ |\alpha|=k}a_\alpha(D^{k-1}u, ... , Du, u, x) D^\alpha u + a_0(D^{k-1}u, ... , Du, u, x) = 0 $$  

4 . 非线性 nonlinear：非线性的依赖最高阶导。
