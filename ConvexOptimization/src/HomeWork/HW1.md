# HW1

[HW1](../../HWpdf/Homework1-2024.pdf)

## [1. Exercise 2.10 of Convex Optimization](../Introduction.md#参考资料)

$$ C=\\{ x\in R^n | x^T A x + b^T x + c \le 0\\} $$
with \\( A\in S^n, \quad b\in R^n, \quad c\in R \\).

(a) Show that \\( C\\) is \\( A\succeq  0\\) (which means \\( A\\) is positive semidefinite).    
> 
>   It is sufficient to show that \\( f(x) = x^T A x + b^T x + c \\) is a convex function (for the **epi** of a convex function is convex.)
>   i.e. $$ \frac{f(x_1) + f(x_2)}{2} \ge f(\frac{x_1+x_2}{2}) $$
>   that is 
>   $$ x_1^TAx_1 + x_2^TAx_2 \ge \frac{1}{2}(x_1^T+x_2^T)A(x_1 + x_2) $$
>   $$ \Leftrightarrow x_1^TAx_1 + x_2^TAx_2 \ge x_1^TAx_2 + x_2^TAx_1 $$
>   $$ \Leftrightarrow (x_1-x_2)^TA(x_1 - x_2) \ge 0 $$
>   it is true since \\( A\\) is positive semidefinite. \\(\blacksquare\\)  

(b) Show that intersection of \\(C\\) and the hyperplane defined by \\(g^T x + h = 0 \\) ( where \\(g \ne 0\\) ) is convex if \\(A + λgg^T \succeq 0 \\) for some \\(λ ∈ R \\). Are the converses of these statements true?
>
> Let $$ H = \\{x | g^T x + h = 0\\} $$
> for \\(x\in H\\), \\(x\in C\\) equavalent to
> $$ x^T (A+ λgg^T) x + b^T x + c + λh^2 \le 0 $$
> whose solution set defined \\(\tilde{C}\\),   
> if \\( A + λgg^T \succeq 0 \\) for some \\(λ ∈ R \\), then
> \\(\tilde{C}\\) is convex.
> $$ x \in H \cap C = H \cap \tilde{C} $$
> is intersection of two convex sets, so it is convex.  \\(\blacksquare\\)  
>
> the converses is **false**.
> let's consider the case
> $$ A = \begin{bmatrix} -1 & 0 \\\\ 0 & -1 \end{bmatrix}, g = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}, b=0, h = 0, c = 0 $$
> where \\( C=R^2\\), \\( H = \\{ (x_1, x_2) | x_2 = 0\\} \\),
> \\( C \cap H \\) is obvious convex,
> but \\( A + λgg^T = \begin{bmatrix} -1 & 0 \\\\ 0 & -1 + λ \end{bmatrix}\\) can never be positive semidefinite.


## [2. Exercise 2.18 of Convex Optimization](../Introduction.md#参考资料)

Invertible linear-fractional functions.     
$$ f(x) = \frac{Ax+b}{c^Tx+d}, \qquad dom f = \\{x | c^Tx+d > 0\\} $$
Suppose the matrix
$$ Q=\\begin{bmatrix} A & b \\\\ c^T & d \end{bmatrix} $$
is nonsingular. Show that \\(f\\) is an invertible linear fractional function.

> let \\( y = \(Ax+b)/(c^Tx+d) \\), then
> $$ Q\begin{bmatrix} x \\\\ 1 \end{bmatrix} = (c^Tx+d)\begin{bmatrix} y \\\\ 1 \end{bmatrix} $$
> since \\(Q\\) is inversible, and \\(\\{x | c^Tx+d > 0\\}\\) we get 
> $$ x = P(\begin{bmatrix} x \\\\ 1 \end{bmatrix}) 
> = P(Q^{-1}\begin{bmatrix} y \\\\ 1 \end{bmatrix}) $$
> so \\(f\\) is bijective.  
> For 
> $$ Q = \begin{bmatrix} A & b \\\\ c^T & d \end{bmatrix}
> = \begin{bmatrix} I &  \\\\ c^TA^{-1} & 1 \end{bmatrix}
> \begin{bmatrix} A &  \\\\  & d-c^TA^{-1}b \end{bmatrix}
> \begin{bmatrix} I & A^{-1}b \\\\  & 1 \end{bmatrix}
> $$ 
> $$ Q^{-1}
> = \begin{bmatrix} I & -A^{-1}b \\\\  & 1 \end{bmatrix}
> \begin{bmatrix} A^{-1} &  \\\\  & (d-c^TA^{-1}b)^{-1} \end{bmatrix}
> \begin{bmatrix} I &  \\\\ -c^TA^{-1} & 1 \end{bmatrix} \\\\
> \begin{bmatrix} 
> A^{-1} + A^{-1}b (d-c^TA^{-1}b)^{-1} c^TA^{-1} & -A^{-1}b (d-c^TA^{-1}b)^{-1} \\\\
> -(d-c^TA^{-1}b)^{-1} c^TA^{-1} & (d-c^TA^{-1}b)^{-1}
> \end{bmatrix}
> $$ 
> so,
> $$ x = \frac{(A^{-1} (d-c^TA^{-1}b) + A^{-1}b c^TA^{-1})y - A^{-1}b }{-c^TA^{-1}y + 1} $$
> $$ dom f^{-1} = \\{ y | (d-c^TA^{-1}b)(-c^TA^{-1}y + 1) > 0 \\} $$


## convex hull/Sparse Representation of a Polytope

reference:
[Sparse representation of a polytope and recovery of sparse signals and low-rank matrices](./Cai%20and%20Zhang%20-%202014%20-%20Sparse%20Representation%20of%20a%20Polytope%20and%20Recovery%20o.pdf)

Please give the Sparse Representation of a Polytope \\(A = \\{x ∈ R^n : ‖x‖_∞ ≤ θ, ‖x‖_1 ≤ sθ\\} \\).

