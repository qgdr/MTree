# HW4

[HW4pdf](../HWpdf/Li%20-%20Homework%205%20of%20Optimization-2024”.pdf)

## 1.solve the following low-rank matrix recovery problem via Project Gradient descent

$$ \min_{\text{rank}(X) \le r} \frac{1}{2} \| \mathcal{A}(X) - b\|_2^2 $$

where \(b = A(X_0) = (〈A_j , X_0〉)_{j=1}^m\) with \(A_j ∈ R^{n_1×n_2}\) with \(m = \mathcal{O}((n_1 + n_2)r)\). Please refer to the following paper.

[Jain P, Meka R, Dhillon I. Guaranteed rank minimization via singular value projection[J]. Advances in Neural Information Processing Systems, 2010, 23.](https://arxiv.org/abs/0909.5457)




## 2. exercises 2.13 of [最优化：建模、算法与理论][Wen]


Give the statement of the subgradient of the following functions:

(a) \(f(x) = \|Ax-b\|_2 + \|x\|_2\)

(b) \(f(x) = \inf_y \|Ay-x\|_\infty\)

---

**solution**

(a) Let \(f_1(x) = \|x\|_2,  f_2(x) = \|Ax-b\|_2 , f(x) = f_1(x) + f_2(x) \)        
So, we have

$$ \partial f(x) = \partial f_1(x) + \partial f_2(x) $$

and now, we get the subgradient of \(f_1(x), f_2(x)\), separately.

1 .  

$$ \partial f_1(x) = \begin{cases}
    \dfrac{x}{||x||_2} , & x \neq 0 \\
    \{ g : \|g\|_2 \le 1 \}, & x = 0
\end{cases} $$

2 .  
If \(Ax-b \neq 0\), then we have

$$ \partial f_2(x) = \{ \frac{A^T(Ax-b)}{||Ax-b||_2} \} $$

But if \(Ax_0-b = 0\), replaced the variable, if \(g\) is a subgradient of \(f_2(x)\), then for \(\forall x \) , we have

$$ g^T(x-x_0) \le \|Ax - b\|_2 = \|Ax - Ax_0\|_2 = \| A(x-x_0) \|_2 $$

Let \(A=U Σ V^T\) is the singular value decomposition of \(A\)， where \(Σ = \text{diag}(\sigma_1, \sigma_2, \dots, \sigma_r, 0, \dots, 0), \sigma_i > 0\), and let \(y = V^T(x-x_0)\), we have

$$ g^T V y \le \|Σy\|_2 = ((\sigma_1 y_1)^2 + (\sigma_2 y_2)^2 + \dots + (\sigma_r y_r)^2)^\frac{1}{2} $$

let \(h^T = g^TV, \; h = V^T g, \; g=V h\), and let

$$ z_i = \begin{cases}
    \sigma_i y_i,  & 1 \le i \le r\\ 
    y_i,  & r+1 \le i \le n
\end{cases}  $$

Thus we get for \(\forall z\)

$$ h^T [\frac{z_1}{\sigma_1}, \dots, \frac{z_r}{\sigma_r}, \dots, z_{r+1}, \dots, z_n]^T \le (z_1^2 + \dots + z_r^2)^\frac{1}{2} $$

which means, \(h_i = 0, i = r+1, \dots, n \)，which means \(h \bot \text{span}\{e_{r+1}, \dots, e_n\} \Leftrightarrow  g \bot NULL(A) \).

And then, the inequality is equivalent to 

$$ [\frac{h_1 }{\sigma_1}, \cdots , \frac{h_r }{\sigma_r}][z_1, \cdots, z_r] \le (z_1^2 + \dots + z_r^2)^\frac{1}{2} $$

That is equivalent to

$$ \frac{h_1^2 }{\sigma_1^2} + \cdots + \frac{h_r^2 }{\sigma_r^2} \le 1 $$

\(g = Vh\)

But we tidy up the finall result buy let \(h_i = \sigma_i u_i, 1 \le i \le r \), we get

$$ \partial f_2(x) = \{ g = V \Sigma u : \|u\|_2 \le 1 \} $$

So we summary that

$$ \partial f_2(x) = \begin{cases}
    \dfrac{A^T(Ax-b)}{||Ax-b||_2} , & Ax-b \neq 0 \\
    \{ g = V \Sigma u : \|u\|_2 \le 1 \}, & Ax-b = 0
\end{cases} $$

!!! tip

    Indeed, it is sufficient to show that 

    $$ y^Tg g^Ty \le y^TA^T Ay \quad \Leftrightarrow \quad gg^T \preceq A^TA $$

    it is easy to varify that

    $$ A^TA - gg^T = V\Sigma U^T U \Sigma V^T - V\Sigma u u^T \Sigma V^T = V(\Sigma^2 - \Sigma u u^T \Sigma) V^T \succ 0  $$


Thus we get the subgradient of \(f(x)\)

$$ \partial f(x) = \partial f_1(x) + \partial f_2(x) = \begin{cases}
    \dfrac{A^T(Ax-b)}{||Ax-b||_2} + \dfrac{x}{||x||_2} , & Ax-b \neq 0, x \neq 0 \\
    \dfrac{A^T(Ax-b)}{||Ax-b||_2} + \{ g : \|g\|_2 \le 1 \}, & Ax-b \neq 0, x = 0 \\
    \dfrac{x}{||x||_2} + \{ g = V \Sigma u : \|u\|_2 \le 1 \}, & Ax-b = 0, x \neq 0 \\
    \{ g = V \Sigma u + v : \|u\|_2, \|v\|_2 \le 1\}, & Ax-b = 0, x = 0
\end{cases} $$



----

(b) 

$$ f(x) = \inf_y \|Ay-x\|_\infty $$ 

and it can be get at \(\hat{y}\), so we replace the variable as

$$ \|A\hat{y}-\hat{x}\|_\infty = \inf_y \|Ay-\hat{x}\|_\infty = f(\hat{x}) $$

To solve his problem, we need strong geometric instincts.

Let \(\hat{z} = A\hat{y}\), and take \([i], i=1, \cdots , r\) are the indices which

$$ |\hat{x}_{[i]} - \hat{z}_{[i]}| = \max_{i} |\hat{x}_{[i]} - \hat{z}_{[i]}| = \|\hat{x}-A\hat{y}\|_\infty $$

Now we give the result directly.

$$ \partial f(\hat{x}) = \begin{cases}
    \{g \in \text{span}\{ e_{[1]} , ..., e_{[r]} \} : \\
    \qquad \qquad g^T A = 0, \\
    \qquad \qquad(\hat{x}_{[i]} - \hat{z_{[i]}}) g_{[i]} \ge 0 ,  \quad   1 \le i \le r    \\
    \qquad \qquad \sum_{i=1}^r \text{sign}(\hat{x}_{[i]} - \hat{z_{[i]}}) g_{[i]} = 1 \},  
    & \hat{x} \neq A\hat{y} \\
    \{g: g^TA = 0, \sum_{i=1}^n |g_i| \le 1\}      & \hat{x} = A\hat{y}  
\end{cases} $$

!!! tip

    we suggest a lemma here. Let 

    $$ f(x) = \|x\|_\infty $$

    And, denote the indices \([i], i=1, \cdots , r\) satisfy 

    $$ |x_{[i]}| = \|x\|_\infty , 1 \le i \le r$$

    then , the subgradient of \(f(x)\) is

    $$ \partial f(x) = \begin{cases} 
        \{g \in \text{span}\{ e_{[1]} , ..., e_{[r]} \}:    \\
        \qquad \qquad x_{[i]}g_{[i]} \ge 0,  \quad 1 \le i \le r              \\
        \qquad \qquad \sum_{i=1}^r \text{sign}(x_{[i]}) g_{[i]} = 1 \}, & x \neq 0 \\
        \{g: \sum_{i=1}^n |g_i| \le 1\} & x = 0
        \end{cases} $$

    That is obvious.  

    <iframe height=600 width=200% src="../maxx_1.html" frameborder="0" allowfullscreen></iframe>  

    And from this , we can kown that the  feasible set of the conjugate function of \(\|x\|_\infty\) is where \(g\) can get, which is \(\|g\|_1 \le 1\).


Now, we can see the subgradient of the original problem has just one more condition which is \(g^T A = 0\), meaning that \(g\) is orthogonal to the column space of \(A\).



















[Wen]: ../index.md#最优化建模算法与理论