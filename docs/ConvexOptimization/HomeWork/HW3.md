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

    For \(V \in S^n\) 

    $$ tr(X + tV) - tr(X) = t Tr(V) = t \langle I, V \rangle \Rightarrow \nabla tr(X) = I$$

    from [HW2.3.b](HW2.md#3-exercise-26-of-最优化建模算法与理论)

    $$ \nabla \log \det X = X^{-T} = X^{-1} $$

    and

    $$ \nu^TVs = tr(\nu^T V s) = tr(s\nu^TV) = \langle \nu s^T, V \rangle \Rightarrow \nabla \nu^TXs = s\nu^T $$

    For \(X \in S^n_{++}\), we have
        
    $$\nabla \nu^TXs = \nabla s^TX\nu = \nu s^T$$

    So, \(\nabla \nu^TXs\) can be combination of \(\nu^T s\) and \(s\nu^T\). 
    But if we restrict it to \(S^n\), then there must be

    $$ \nabla \nu^TXs = \dfrac{\nu s^T + s\nu^T}{2} $$

    KKT conditions needs

    $$ I - X^{-1} + \nabla \nu^TXs = 0 $$

    but \(I-X^{-1}\) is in \(S^n\),
    so we get 

    KKT conditions are

    $$ I - X^{-1} + \dfrac{\nu s^T + s\nu^T}{2} = 0 $$

    $$ Xs=y $$

    ---

    the optimal solution satisfy the KKT conditions.

    Since \(s=X^{-1}y\) and \(s^Ty=y^Ts=1\), multiple \(y\) on the right, we have

    $$ y-s+\frac{\nu}{2} + \frac{(\nu^Ty) s}{2} = 0 $$

    Then multiply \(y^T\) on the left, we have

    $$ 1 - y^Ty =  \frac{y^T\nu}{2} + \frac{(\nu^Ty) y^Ts}{2} = \nu^Ty $$

    Substitute it to the upper equation, we get

    $$ \nu = -2y + (1+y^Ty)s $$

    Multiply \(X\) to the KKT condition on the left and subsitite \(\nu\) to it, we have

    $$ \begin{align}
        X^{-1} &= I + \frac{1}{2}( -2ys^T +(1+y^y)s s^T -2sy^T+ (1+y^y)ss^T ) \\
            &= I + (1+y^Ty)s s^T - ys^T - sy^T \\
            &= (I-sy^T)(I-ys^T) + ss^T
    \end{align} $$

    So, \(X^{-1}\) is semi-positive definite. 
    But if there is some \(u\) s.t. \(u^TX^{-1}u = 0\), there mus be
    \(s^u = 0\) and \(u-sy^Tu = 0\), that is \(u=0\).
    So, \(X^{-1}\) is **positive definite**, then \(X\) is positive definite.

    Verify the inverse

    $$ \begin{align}
        X^{-1}X^* =& ( I + (1+y^Ty)s s^T - ys^T - sy^T )( I + yy^T - \dfrac{1}{s^Ts}ss^T ) \\
        =& I + yy^T - \dfrac{1}{s^Ts}ss^T + (1+y^Ty)ss^T + (1+y^Ty)sy^T - (1+y^Ty)ss^T      \\
        & - ys^T - sy^T - yy^T - (y^Ty) sy^T + ys^T + \frac{ss^T}{s^Ts}   \\
        &= I
    \end{align} $$


## 3. Dual problems of the following convex optimizations

Given \(A ∈ R^{m×n}\) with \(m < n\) and \(b ∈ R^m\). Please give the dual problems of the following convex optimizations.      

(i) \(\min_{x ∈ R^n} \|x\|_1, \; \text{s.t.} \; \|A^T(Ax − b)||_\infty ≤ ε\)    

(ii) \(\min_{x ∈ R^n} λ‖x‖_1 + ‖A^T(Ax − b)‖_∞\)    

(iii) \(\min_{x ∈ R^n} λ‖x‖_1 + \frac{1}{2} ‖A^T(Ax − b)‖_∞^2\)    
 

!!! solution

    (i). 

    $$ L(x, \lambda) = \|x\|_1 + \lambda (\|A^T(Ax-b)\|_∞ - \epsilon) $$

    where \(\lambda \ge 0\). And then

    $$ g(\lambda) = \min_{x \in R^n} L(x, \lambda) = \min_{x \in R^n} \|x\|_1 + \lambda \|A^T(Ax-b)\|_∞ - \lambda \epsilon $$

    the dual problem is

    $$ \max_{λ \ge 0} g(\lambda) = \max_{λ \ge 0} \min_{x \in R^n} \{ \|x\|_1 + \lambda \|A^T(Ax-b)\|_∞ - \lambda \epsilon \} $$

    ---

    (ii). 
    Let \(y = -A^T(Ax-b)\), then the problem is equivalent to

    $$ \min_{x \in R^n} \{ \lambda ‖x‖_1 + ‖y‖_∞ \}, \; \text{s.t.} \; y=-A^T(Ax-b) $$

    The Lagrange dual function is

    $$ L(x, y, \nu) = \lambda ‖x‖_1 + ‖y‖_∞ + \langle \nu, -A^T(Ax-b) - y \rangle $$

    Then,

    $$ \begin{align}
        g(\nu) &= \min_{x,y \in R^n} L(x, \nu) = \min_{x,y \in R^n} \lambda ‖x‖_1 + ‖y‖_∞ + \langle \nu, -A^T(Ax-b) - y \rangle \\
        &= \min_{x \in R^n} \{ \lambda ‖x‖_1 - \nu^TA^TAx \} + \min_{y \in R^n} \{ ‖y‖_∞ - \nu^Ty \} + \nu^TA^Tb \\
        &= -\max_{x \in R^n} \{ \langle A^TA\nu, x \rangle - \lambda ‖x‖_1 \} - \max_{y \in R^n} \{ \langle \nu, y \rangle  - ‖y‖_∞\} + \nu^TA^Tb \\
        &= - \mathbb{I}_{\|A^TA\nu\|_\infty \le \lambda} - \mathbb{I}_{\|\nu\|_1 \le 1} + \nu^TA^Tb
    \end{align} $$

    The last equation is the conjugate of the norm function, see [Conjugate of Norm](../ConvexFunction/ConjugateFunction.md#范数的共轭函数-conjugate-of-norm).        
    So the dual problem is

    $$ \begin{align}
        \text{maximum} &\qquad b^TA\nu \\
        \text{subject to} &\qquad \|A^TA\nu\|_\infty \le \lambda, \| \nu \|_1 \le 1
    \end{align} $$

    ---

    (iii). 
    Let \(y = -A^T(Ax-b)\), similarly, the problem is equivalent to

    $$ \min_{x \in R^n} \{ \lambda ‖x‖_1 + \frac{1}{2} ‖y‖_∞^2 \}, \; \text{s.t.} \; y=-A^T(Ax-b) $$

    The Lagrange dual function is

    $$ L(x, y, \nu) = \lambda ‖x‖_1 + \frac{1}{2} ‖y‖_∞^2 + \langle \nu, -A^T(Ax-b) - y \rangle $$

    Then,

    $$ \begin{align}
        g(\nu) &= \min_{x,y \in R^n} L(x, \nu) = \min_{x,y \in R^n} \lambda ‖x‖_1 + \frac{1}{2} ‖y‖_∞^2 + \langle \nu, -A^T(Ax-b) - y \rangle \\
        &= \min_{x \in R^n} \{ \lambda ‖x‖_1 - \nu^TA^TAx \} + \min_{y \in R^n} \{ \frac{1}{2} ‖y‖_∞^2 - \langle \nu, y \rangle \} + \nu^TA^Tb \\
        &= -\max_{x \in R^n} \{ \langle A^TA\nu, x \rangle - \lambda ‖x‖_1 \} - \max_{y \in R^n} \{ \langle \nu, y \rangle - \frac{1}{2} ‖y‖_∞^2 \} + \nu^TA^Tb \\
        &= - \mathbb{I}_{\|A^TA\nu\|_\infty \le \lambda} - \frac{1}{2}\|\nu\|_1^2 + \langle A^Tb, \nu \rangle
    \end{align} $$

    The last equation is the conjugate of the norm-square function, see [Conjugate of Norm Squared](../ConvexFunction/ConjugateFunction.md#范数平方的共轭函数-conjugate-of-norm-squared).       
    So the dual problem is

    $$ \begin{align}
        \text{maximum} &\qquad \langle A^Tb, \nu \rangle - \frac{1}{2}\|\nu\|_1^2 \\
        \text{subject to} &\qquad \|A^TA\nu\|_\infty \le \lambda
    \end{align} $$









[textbook]: ../index.md#ee364a-convex-optimization-i-professor-stephen-boyd-stanford-university
[ref2]: ../index.md#最优化建模算法与理论