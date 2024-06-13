# HW8

[HWpdf](../HWpdf/Homework9-2024.pdf)

## 1

Consider the **sparse phase retrieval** problem \(b = |Ax_0|^2 + e ∈ \mathbb{R}^m\). 
We can solve it via the following model 

$$ \min_{X\succeq O} \frac{‖\mathcal{A}(X) − b‖_2^2/2 + λ\text{Tr}(X) + μ‖X‖_1}{‖X ‖_F} ,$$

where \(\mathcal{A} : \mathbb{C}^{n×n} → \mathbb{R}^m, \mathcal{A}(X)_j = 〈a_j a_j^∗, X〉 =: 〈A_j, X〉\). 
Please design an solving algorithm and give the iterated scheme


**solution**

Let \(f(X)=\mu\|X\|_1, h(X)=‖\mathcal{A}(X) − b‖_2^2/2 + λ\text{Tr}(X), g(X)= \|X\|_F\)，


step 1: 

$$ Y^{k} = \partial g(X^k) = \begin{cases}
    \frac{X^k}{\|X^k\|_F} , & \text{ if } X^k \neq O \\
    O, & \text{ else }
\end{cases} $$

step 2:

<!-- $$ p^k = \frac{‖\mathcal{A}(X^k) − b‖_2^2/2 + λ\text{Tr}(X^k) + μ‖X^k‖_1}{‖X^k ‖_F} $$ -->
$$ p^k = \frac{f(X^k) + h(X^k)}{g(X^k)} $$


step 3:

$$ \begin{aligned}
    X^{k+1} &= \text{Prox}_{\alpha_k f}(X^k + \alpha_k (\partial h(X^k)-p^k(Y^k)))  \\
    &= \text{Prox}_{\alpha_k \mu \|\cdot\|_1}(X^k + \alpha_k (\lambda I + \mathcal{A}^*(\mathcal{A}(X^k)-b)-p^k Y^k))
\end{aligned} $$



## 2

Please give the projector operator, Tangent space, normal space, Riemannian gradient, Riemannian Hessian of the following Grassmann manifold 

$$ \text{Grass}(n, p) = \text{St}(n, p)/\mathcal{O}(p) $$

where \(\mathcal{O}(p) = \{X ∈ R^{p×p} : X^T X = I_p\}\) is the orthogonal group, and \(\text{St}(n, p) = \{X ∈ R^{n×p} : X^TX = I_p\}\) is the Stiefel orthogonal group. 
Please give the details rather than only the final results. 
Tips: You can refer to Section 9.16 of [Boumal N. An introduction to optimization on smooth manifolds[M]. Cambridge University Press, 2023.]


**solution**


$$ \pi: \text{St}(n, p) \rightarrow \text{Grass}(n, p): X \mapsto \pi(X) \triangleq [X]=\{XQ:Q\in \mathcal{O}(p)\} $$


