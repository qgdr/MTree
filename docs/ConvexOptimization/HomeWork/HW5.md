# HW5

[HW5pdf](../HWpdf/Li%20-%20Homework%206%20of%20Optimization-2024”.pdf)


## 1. proximal operator

$$ \text{Prox}_{f}(b) = \arg\min_{x} f(x) + \frac{1}{2} \|x-b\|_2^2  $$

### 1.1

Please solve the proximal of \(l_1\) norm \(f (x) = ‖x‖_1 = \sum_{j=1}^n |x_j |\).    
Tips: You can solve it by Moreau decomposition and the projection on the \(l_\infty\) ball


In this case ,

$$ \text{Prox}_{f}(b) = \arg\min_{x} ‖x‖_1 + \frac{1}{2} \|x-b\|_2^2  $$

**First solution**:

Let \(x = \text{Prox}_{f^*}(b) \) .        
Since \(f(x)= \|x\|_1\) is a convex function, we have 

$$ b-x \in \partial f(x) = \{g : g_i = \begin{cases}
    \text{sign}(x_i), & \text{if } x_i \neq 0 \\
    [-1, 1], & \text{if } x_i = 0
\end{cases} \} $$

So, 

$$ x_i = \begin{cases}
    0, & \text{if } |b_i| \le 1 \\
    \text{sign}(b_i)(|b_i|-1 ), & \text{if } |b_i| > 1
\end{cases} $$


**Second solution**:

From [Moreau decomposition](../Algorithms/Proximal.md#moreau-decomposition), we have 

$$ b = \text{Prox}_{f}(b) + \text{Prox}_{f^*}(b) $$

where \(f^* (x) = \mathbb{I}_{\|x\|_\infty \le 1}\), that is

$$ \text{Prox}_{f}(b) = b - \text{Prox}_{f^*}(b) = b-\mathcal{P}_{\|x\|_\infty \le 1} (b) $$

But it's obvious that 

$$ \mathcal{P}_{\|x\|_\infty \le 1} (b) = \tilde{b} \quad \text{  where  } \quad \tilde{b}_i = \begin{cases}
    b_i, & \text{if } |b_i| \le 1 \\
    \text{sign}(b_i), & \text{if } |b_i| > 1
\end{cases} $$

So

$$ \begin{align}
    \text{Prox}_{f}(b)_i &= b_i - \text{Prox}_{f^*}(b)_i 
    = b_i - \mathcal{P}_{\|x\|_\infty \le 1} (b)_i         \\
    &= b_i - \tilde{b}_i    \\
    &= b_i - \begin{cases}
        b_i, & \text{if } |b_i| \le 1 \\
        \text{sign}(b_i), & \text{if } |b_i| > 1
    \end{cases}         \\
    &= \begin{cases}
        0, & \text{if } |b_i| \le 1 \\
        \text{sign}(b_i)(|b_i|-1 ), & \text{if } |b_i| > 1
    \end{cases}
\end{align} $$



### 1.2

Example 8.1 of [最优化：建模、算法与理论][Wen]

Please compute the proximal operator of \(f (x) = − \sum_{j=1}^n \ln x_j\) .


**solution**.

$$ \text{Prox}_{f}(b) = \arg\min_{x\succ 0} f(x) + \frac{1}{2} \|x-b\|_2^2  $$

Since \(f(x)= − \sum_{j=1}^n \ln x_j\) is a convex function, 
let \(x=\text{Prox}_{f^*}(b)\) .

We have

$$ b-x \in \partial f(x) = \{g : g_i = -\frac{1}{x_i} \} $$

That is

$$ b_i = x_i - \frac{1}{x_i} \quad \Leftrightarrow \quad x_i = \frac{b_i+\sqrt{b_i^2+4}}{2} $$



### 1.3

Exercise 8.4 of [最优化：建模、算法与理论][Wen]

Please compute the proximal operator of

$$ f (X) = − \ln \det(X) \quad \text{ where } \quad \text{dom}(f ) = S^n_{++} $$

**solution**.

Since \(f(X)= − \ln \det(X)\) is a convex function, for any \(Y \in S^n\)

$$ \text{Prox}_{f}(Y) = \arg\min_{X \succ 0} − \ln \det(X) + \frac{1}{2} \|X-Y\|_F^2  $$

where [最优化：建模、算法与理论 2.1.2][Wen]

$$ \|A\|_F = \sqrt{Tr(AA^T)} \quad \Rightarrow \quad \|A\|_F^2 = Tr(AA^T) $$

$$ \begin{align}
    Tr((A+tV)(A^T+tV^T)) &= Tr(AA^T)+t (Tr(AV^T)+Tr(VA^T))+t^2Tr(VV^T) \\
    &= Tr(AA^T)+2t\cdot Tr(A^T V)+t^2 \cdot Tr(VV^T)
\end{align} $$

Thus \(\nabla \|A\|_F^2 = 2A\),      
So we can get \(\text{Prox}_{f}(Y)\), if 

$$ \begin{align}
    0 &= \nabla (f(X) + \frac{1}{2} \|X-Y\|_F^2)     \\
    &= \nabla (− \ln \det(X) + \frac{1}{2} \|X-Y\|_F^2)     \\
    &= -X^{-T} + X-Y
\end{align}  $$

We can select the \(X\) such that

$$ Y=X-X^{-1}, \quad X\in S^n_{++} $$

Because , let \(Y = U\Lambda_Y U^T\), where \(\Lambda_Y = \text{diag}(\lambda_1, \dots, \lambda_n)\), 
and now let

$$ X = U\Lambda_X U^T, \quad \Lambda_X = \text{diag}(\frac{\lambda_i + \sqrt{\lambda_i^2+4}}{2}) $$

That satisfy \(X \succ 0\) and \(Y=X-X^{-1}\).


## 2

Please solve the following low-rank matrix recovery problem via Proximal Gradient descent 

$$ \min_{X∈R^{n_1 ×n_2}} λ‖X‖_∗ + \frac{1}{2} ‖\mathcal{A}(X) − b‖_2^2 $$

where \(b = \mathcal{A}(X_0) = (〈A_j, X_0〉)_{j=1}^m\) with \(A_j ∈ R^{n_1×n_2}\) with \(m = \mathcal{O}((n_1 + n_2)r)\), and \(‖ · ‖_∗\) is the nuclear norm.

[最优化：建模、算法与理论 8.1.3 2][Wen]

**solution**.


We want to solve the problem

$$ \min_{X∈R^{n_1 ×n_2}} f(x) + h(x) $$

where

$$ f(x) =  \frac{1}{2} ‖\mathcal{A}(X) − b‖_2^2 \qquad h(x) =λ\|X\|_* $$

Let the \(X=U\Sigma V^T\) is the SVD of \(X\), then

$$ \|X\|_* = Tr(\sqrt{XX^T}) = \sum_{i=1}^r \sigma_i$$

We have

$$ \nabla f(x) = \mathcal{A}^*(\mathcal{A}(X) − b) = \sum_{j=1}^m (Tr(A_j^TX) − b_j)A_j $$

So, the proximal gradient descent is

$$ \begin{align}
    Y^k &= X^k - t_k \nabla f(X^k)  \\
    &=X^k - t_k \sum_{j=1}^m (Tr(A_j^TX^k) − b_j)A_j        \\
    X^{k+1} &= \text{Prox}_{t_k h}(Y^k)     \\
    &= \arg\min_{X∈R^{n_1 ×n_2}} t_k \lambda\|X\|_* + \frac{1}{2} ‖X - Y^k ‖_F^2    \\
\end{align} $$

where [SVT](../Algorithms/Proximal.md#nuclear-norm)

$$ \text{Prox}_{t_k h}(Y) = \text{SVT}(Y, t_k\lambda) = U (D - t_k \lambda I)^+ V^T, \quad Y = U D V^T $$








## 3


Given the convex problem 
\(\min_x ‖x‖_1\), s.t. \(‖A^∗(Ax − b)‖_∞ ≤ ε\), where \(A^∗ ∈ R^{n×m}\) is the transpose of the matrix \(A ∈ R^{m×n}\) with \(m < n\). Please design an solving algorithm based on dual algorithm. You should give the iterated scheme in detail.


**solution**.

refer [Foucart A Mathematical Introduction to Compressive Sensing 15.2](./Foucart%20和%20Rauhut%20-%202013%20-%20A%20Mathematical%20Introduction%20to%20Compressive%20Sensing.pdf)


Let \(f(x) = \|x\|_1, h(x) = \mathbb{I}_{\|x\|_\infty \le \epsilon}\), then the problem is

$$ \begin{gather*}
    \min f(x) + h(y)    \\
    \text{s.t.} \quad  y = A^∗(Ax − b)  \\
\end{gather*} $$

The Lagrange dual function is

$$ \begin{align}
    L(x,y,\nu) &= f(x) + h(y) + \text{Re}(\nu^*(A^∗(Ax − b)-y))   \\
    &= \left( f(x)+ \langle A^*A\nu, x \rangle \right) - \langle A\nu, b \rangle + \left( h(y) - \langle \nu, y \rangle \right)     \\
\end{align} $$

Then

$$ \begin{align}
    g(\nu) &= \min_{x,y} L(x,y,\nu) \\
    &= \min_{x,y} \left( f(x)+ \langle A^*A\nu, x \rangle \right) - \langle A\nu, b \rangle + \left( h(y) - \langle \nu, y \rangle \right)     \\
    &= - f^*(-A^*A\nu) - h^*(\nu) - \langle \nu, A^* b \rangle     \\
    &= -\mathbb{I}_{\|A^*A\nu\|_\infty \le 1} - \epsilon \|\nu\|_1 -  \langle \nu, A^* b \rangle     \\
\end{align} $$


Now, ower Lagrange dual problem is

$$ \begin{align}
    \max_{\|A^*Az\|_\infty \le 1} - \epsilon \|z\|_1 -  \langle z, A^* b \rangle     \\
\end{align} $$


So, using Poximal Gradient Descent, we have the scheme

$$ \begin{align}
    y^{k+1} &=  \epsilon \nabla\|z^k\|_1 + A^* b        \\
    z^{k+1} &= \text{Prox}_{f^*(-A^*Az)} (z^k - t_k y^{k+1})       \\
    &= \mathcal{P}_{ \|A^*Az\|_\infty \le 1} (z^k - t_k y^{k+1})   \\
\end{align} $$






[Wen]: ../index.md#最优化建模算法与理论
