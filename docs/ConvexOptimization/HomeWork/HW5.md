# HW5

[HW5pdf](../HWpdf/Li%20-%20Homework%206%20of%20Optimization-2024”.pdf)


## 1. proximal operator

$$ \text{Prox}_{f}(b) = \arg\min_{x} f(x) + \frac{1}{2} \|x-b\|^2  $$

### 1.1

Please solve the proximal of \(l_1\) norm \(f (x) = ‖x‖_1 = \sum_{j=1}^n |x_j |\).    
Tips: You can solve it by Moreau decomposition and the projection on the \(l_\infty\) ball


In this case ,

$$ \text{Prox}_{f}(b) = \arg\min_{x} ‖x‖_1 + \frac{1}{2} \|x-b\|_2^2  $$

**First solution**:

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

From Moreau decomposition, we have 

$$ b = \text{Prox}_{f}(b) + \text{Prox}_{f^*}(b) $$

where \(f^* (x) = \mathbb{I}_{\|x\|_\infty \le 1}\), that is

$$ \text{Prox}_{f}(b) = b - \text{Prox}_{f^*}(b) = b-\mathcal{P}_{\|x\|_\infty \le 1} (b) $$

But its obviously that 

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


