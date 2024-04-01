# HW3

[HW3pdf](../HWpdf/Homework4-Optimization-2024.pdf)


## 1. Exercise 4.24 of [Convex Optimization][textbook]

Complex  \(l_1\)-, \(l_2\)- and \(l_\infty\)-norm approximation.

Consider the problem

$$ \text{minimize} \|Ax - b\|_p $$

where \(A \in C^{m\times n}, b \in C^m\), and \(x \in C^n\).    
For \(p\le 1\), the complex \(l_p\)-norm is defined by

$$ \|y\|_p = \left(\sum_{j=1}^m |y_j|^p\right)^{1/p} $$

For \(p=1,2, \text{and} \infty\), express the complex \(l_p\)-norm approximation problem as a QCQP or SOCP with real variables and date.


!!! solution

    Let 

    $$ \begin{align}
    A = X + iY,     \qquad  & X, Y \in R^{m\times n}, \\
    x = u + iv,     \qquad  & u,v \in R^n, \\
    b = c + id,     \qquad  & c,d \in R^m.
    \end{align} $$

    a. For \(p=1\), it is equivalent to minimize

    $$ \begin{align}
        \sum_{j=0}^m |X[j, :]u - c_j + i(Y[j, :]v - d_j)|
    \end{align} $$

    Take each item as \(t_j\), then we get

    $$ \begin{align}
        \text{minimize} \qquad & \sum_{j=0}^m t_j   \\
        \text{subject to} \qquad & |X[j, :]u - c_j + i(Y[j, :]v - d_j)| \le t_j, \\
        & \quad j=1,\dots,m
    \end{align} $$

    So finally, the problem is in the SOCP form as

    $$ \begin{align}
        \text{minimize} \qquad & \sum_{j=0}^m t_j   \\
        \text{subject to} \qquad & 
        \left\| \begin{bmatrix}
        X[j, :] & -Y[j, :] \\ Y[j, :] & X[j, :]
        \end{bmatrix}
        \begin{bmatrix}
            u \\ v
        \end{bmatrix}
        - \begin{bmatrix}
            c_j \\ d_j
        \end{bmatrix}
        \right\|_2^2 \le t, \\
        & \quad j=1,\dots,m
    \end{align} $$

    ---

    b. For \(p=2\), minimize \( \|\cdot\|_2 \) is equivalent to minimize \( \| \cdot \|_2^2 \). Then

    $$\begin{align}    
    \|Ax - b\|_2^2 &= \| (X+iY)(u+iv)-(c+id) \|_2^2  \\
    &= \| Xu-Yv-c \|_2^2 + \| Xv+Yu-d \|_2^2 \\
    &= \left\| \begin{bmatrix}
        X & -Y \\ Y & X
    \end{bmatrix}
    \begin{bmatrix}
        u \\ v
    \end{bmatrix}
    - \begin{bmatrix}
        c \\ d
    \end{bmatrix}
    \right\|_2^2
    \end{align}$$

    That is in the QCQP form.

    ---

    c. For \(p=\infty\), the problem is equivalent to

    $$ \begin{align}
        \text{minimize} \qquad & t   \\
        \text{subject to} \qquad & |X[j, :]u - c_j + i(Y[j, :]v - d_j)| \le t, \\
        & \quad j=1,\dots,m
    \end{align}
    $$



    So, the problem is in the SOCP form as

    $$ \begin{align}
        \text{minimize} \qquad & t   \\
        \text{subject to} \qquad & 
        \left\| \begin{bmatrix}
        X[j, :] & -Y[j, :] \\ Y[j, :] & X[j, :]
        \end{bmatrix}
        \begin{bmatrix}
            u \\ v
        \end{bmatrix}
        - \begin{bmatrix}
            c_j \\ d_j
        \end{bmatrix}
        \right\|_2 \le t, \\
        & \quad j=1,\dots,m
    \end{align} $$



## 2. Exercise 5.30 of [Convex Optimization][textbook]

Derive the KKT conditions for the problem

$$ \begin{align}
    \text{minimize} \qquad & tr(X) - \log \det X \\
    \text{subject to} \qquad & Xs = y
\end{align} $$

with \(X \in S^n\) and domain \(S^n_{++}\). \(y, s\in R^n\) are given, with \(s^T y=1\).
Verify that the optimal solution is given by

$$ X^* = I + yy^T - \dfrac{1}{s^Ts}ss^T $$


!!! solution

The Lagrange dual function is

$$ tr(X)-\log \det X + \nu^T(Xs-y) $$

And we have 

$$ tr(X + tV) - tr(X) = t Tr(V) = t \langle I, V \rangle \Rightarrow \nabla tr(X) = I$$

from [HW2.3.b](HW2.md#3-exercise-26-of-最优化建模算法与理论)

$$ \nabla \log \det X = X^{-T} = X^{-1} $$

and

$$ \nu^TVs = tr(\nu V^T s) = tr(s\nu^TV) = \langle \nu s^T, V \rangle = \langle s \nu^T, V \rangle \Rightarrow \nabla \nu^T(Xs-y) = s \nu^T = \nu^T s $$

KKT conditions:

$$ Xs=y $$

$$ I - X^{-1} + s\nu^T = 0 $$



[textbook]: ../index.md#ee364a-convex-optimization-i-professor-stephen-boyd-stanford-university
[ref2]: ../index.md#最优化建模算法与理论