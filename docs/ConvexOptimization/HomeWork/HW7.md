# HW7

[HWpdf](../HWpdf/Homework8-2024.pdf)

# 1

Consider the **low-rank matrix recovery** problem \(b = \mathcal{A}(X_0)+e ∈ \mathbb{R}^m\). 
We can solve it via the following matrix decomposition model 

$$ \min_{U∈\mathbb{R}^{n_1×r} ,V∈\mathbb{R}^{n_2×r}} \frac{1}{2} ‖\mathcal{A}(UV^∗) − b‖_2^2 + λ‖U^∗U − V^∗V‖_F^2 $$

where \(\mathcal{A} : \mathbb{C}^{n_1×n_2} → \mathbb{R}^m, \mathcal{A}(X)_j = 〈A_j, X〉\) with \(A_j ∈ \mathbb{R}^{n_1×n_2}\).         
Please design an solving algorithm via BCD and give the iterated scheme. Tips: You can solve each subproblems via Gradient Descent.

**solution**

Let

$$ f(U,V) = \frac{1}{2} ‖\mathcal{A}(UV^∗) − b‖_2^2 + λ‖U^∗U − V^∗V‖_F^2 $$

1 . We first calculate the gradient of different part in the objective function.

$$ \begin{aligned}
    \frac{1}{2} ‖\mathcal{A}((U+tD)V^∗) − b‖_2^2 &- \frac{1}{2} ‖\mathcal{A}(UV^∗) − b‖_2^2  \\
    &= \frac{1}{2} \sum_{j=1}^m \left(〈A_j, UV^*+tDV^∗〉- b_j\right)^2 - \left(〈A_j, UV^∗〉-b_j\right)^2 \\
    &= \sum_{j=1}^m t \left(〈A_j, UV^∗〉-b_j\right)〈A_j, DV^∗〉 + O(t^2)     \\
    &= \sum_{j=1}^m t \left(〈A_j, UV^∗〉-b_j\right)〈A_j V, D〉 + O(t^2)     \\
    &= t〈\sum_{j=1}^m \left(〈A_j, UV^∗〉 -b_j\right)A_j V, D〉 + O(t^2)     \\
    &= t〈\mathcal{A}^* (\mathcal{A}(UV^*)-b)V, D〉 + O(t^2)     \\
\end{aligned} $$

So, we can get 

$$ \frac{\partial}{\partial U} \frac{1}{2} ‖\mathcal{A}(UV^∗) − b‖_2^2 = \mathcal{A}^* (\mathcal{A}(UV^*)-b)V $$

Similarly, we can get 

$$ \begin{aligned}
    \frac{1}{2} ‖\mathcal{A}(U(V+tD)^∗) − b‖_2^2 &- \frac{1}{2} ‖\mathcal{A}(UV^∗) − b‖_2^2 \\
    &= \sum_{j=1}^m t \left(〈A_j, UV^∗〉-b_j\right)〈A_j, UD^∗〉 + O(t^2)     \\
    &= \sum_{j=1}^m t \left(〈A_j, UV^∗〉-b_j\right)〈A_j^* U , D〉 + O(t^2)     \\
    &= t〈\mathcal{A}^* (\mathcal{A}(UV^*)-b)^* U, D〉 + O(t^2)     \\
\end{aligned} $$

So we can get 

$$ \frac{\partial}{\partial V} \frac{1}{2} ‖\mathcal{A}(UV^∗) − b‖_2^2 = \mathcal{A}^* (\mathcal{A}(UV^*)-b)^*U $$


For the latter part, we have

$$ \begin{aligned}
    ‖(U+tD)^∗(U+tD) − V^∗V‖_F^2 &- ‖U^∗U − V^∗V‖_F^2    \\
    &= 2 t \; \langle U^∗U − V^∗V, U^*D+D^*U \rangle + O(t^2)    \\
    &= 4 t \; \langle U(U^∗U − V^∗V), D \rangle + O(t^2) 
\end{aligned} $$

Thus

$$ \frac{\partial}{\partial U} ‖U^∗U − V^∗V‖_F^2 = 4U(U^∗U − V^∗V) $$

Similarly, we can get 

$$ \frac{\partial}{\partial V} ‖U^∗U − V^∗V‖_F^2 = -4V(U^∗U − V^∗V) $$

Summary, we have the partial derivatives of the objective function:

$$ \begin{gather*}
    \frac{\partial f(U,V)}{\partial U} = \mathcal{A}^* (\mathcal{A}(UV^*)-b)V + 4\lambda U(U^∗U − V^∗V)    \\
    \frac{\partial f(U,V)}{\partial V} = \mathcal{A}^* (\mathcal{A}(UV^*)-b)^*U - 4\lambda V(U^∗U − V^∗V)  \\
\end{gather*} $$

Now we can use BCD to solve the problem.

$$ \begin{gather*}
    U^{k+1} = U^k - t^{k+1} \frac{\partial f(U,V)}{\partial U} \Big|_{U^k,V^k}  \\
    V^{k+1} = V^k - t^{k+1} \frac{\partial f(U,V)}{\partial V} \Big|_{U^{k+1},V^k}
\end{gather*} $$






----

# 2

Consider the **sparse phase retrieval** problem \(b = |Ax_0|^2 + e ∈ \mathbb{R}^m\). 
We can solve it via the following model 

$$ \min_{x,y∈\mathbb{C}^n} \frac{1}{2} ‖\mathcal{A}(xy^∗) − b‖_2^2 + λ‖x − y‖_2^2 + ρ‖x‖_1 + δ‖y‖_1 $$ 

where \(\mathcal{A} : \mathbb{C}^{n×n} → \mathbb{R}^m, \mathcal{A}(X)_j = 〈a_ja_j^∗, X〉 =: 〈A_j, X〉\).       
Please design an solving algorithm via BCD and give the iterated scheme. Tips: You can solve each subproblems via Proximal Gradient Descent.



**solution**

Let 

$$ f(x,y) = \frac{1}{2} ‖\mathcal{A}(xy^∗) − b‖_2^2 + λ‖x − y‖_2^2 + ρ‖x‖_1 + δ‖y‖_1 $$

$$ \begin{aligned}
    \frac{\partial}{\partial x} \frac{1}{2} ‖\mathcal{A}(xy^∗) − b‖_2^2 
    &= \mathcal{A}^* (\mathcal{A}(xy^∗)-b)y \\
    &= \sum_{j=1}^m (〈a_ja_j^∗, xy^∗〉 - b_j) a_ja_j^∗ y \\
    &= \sum_{j=1}^m (a_j^∗ x a_j^*y - b_j)a_j^*y \; a_j  \\
\end{aligned} $$

Similarly, 

$$ \frac{\partial}{\partial y} \frac{1}{2} ‖\mathcal{A}(xy^∗) − b‖_2^2 = \sum_{j=1}^m (a_j^∗ x a_j^*y - b_j)a_j^*x \; a_j $$

So the BCD algorithm with Proximal Gradient Descent is 

$$ g_1^{k+1} = \mathcal{A}^* (\mathcal{A}(x^{k}y^{k*})-b)y^{k} + 2\lambda (x^{k}-y^{k}) $$

$$ \begin{aligned}
    x^{k+1} &= \text{Prox}_{\alpha_k \rho \|\cdot\|_1} x^{k} - \alpha_k g_1^{k+1} \\
\end{aligned} $$

$$ g_2^{k+1} = \mathcal{A}^* (\mathcal{A}(x^{k+1}y^{k*})-b)^* x^{k+1} - 2\lambda (x^{k+1}-y^{k}) $$

$$ y^{k+1} = \text{Prox}_{\beta_k \delta \|\cdot\|_1} y^{k} - \beta_k g_2^{k+1} $$


where \(\text{Prox}_{\|\cdot\|_1} \) see [proximal-of-l_1-norm](../Algorithms/Proximal.md#proximal-of-l_1-norm)


