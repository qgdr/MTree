# Eigvalues and Eigenfunctions 


<!-- 考虑算子的特征根，即使得方程

$$ \begin{cases}
    Lu = \lambda u & \text{  in  } U  \\
    u = 0 & \text{  on  } \partial U \\
\end{cases} $$

存在弱解的 \(\lambda\)。 -->

## Problems


!!! question "13"

    <font size="3">
    **柯朗极大值原理 Courant minimax principle**

    假设 \(U\) 是有界开集，\(\partial U\) 光滑。令

    $$ Lu = \sum_{i, j=1}^n -\partial_j (a^{ij}(x)  \partial_i u) \text{  in  } U  $$

    其中 \(((a^{ij}))\) 对称，且一致椭圆。
    
    假设 \(L\) 的特征根为 \(0<\lambda_1 < \lambda_2 \le \cdots \)，证明

    $$ \lambda_k = \max_{S\in \Sigma_{k-1}} \min_{u\in S^{\bot},\|u\|_{L^2}=1} B[u,u] \quad (k=1,2,\cdots) $$

    其中 \(\Sigma_{k-1}\) 是 \(H_0^1(U)\) 全体 \(k-1\) 维子空间构成的集合。


**proof**

设 \(\lambda_k\) 对应的特征函数 \(w_k\) 构成 \(L^2(U)\) 的一组标准正交基，

$$ \int_U w_k^2 = 1 \quad \text{and} \quad \int_U w_k w_l = 0 \quad \text{for} \quad k \ne l $$

并且 \(\phi_k := \dfrac{w_k}{\lambda_k^{1/2}}\) 是以内积 \(B[\;, \;]\) 诱导的 \(H_0^1(U)\) 的标准正交基。即

$$ B[\phi_k, \phi_k] = 1 \quad \text{and} \quad B[\phi_k, \phi_l] = 0 \quad \text{for} \quad k \ne l $$

并且 \(\phi_k\) 在 \(L^2(U)\) 中正交，\(\|\phi_k\|_{L^2(U)}=\dfrac{1}{\lambda_k}\).



"\(\ge\)":

对于任意 \(S\in \Sigma_{k-1}\)，不妨设他的一组基为 \(s_1, \cdots, s_{k-1}\)，      
那么存在 \(\mu\in \mathbb{R}^{k} \neq \mathbf{0}\)，
使得 \(u = \sum_{i=1}^k \mu_i \phi_i \in S^{\bot}\)，即

$$ \mu^T \begin{bmatrix}
    \phi_1 \\ \vdots \\ \phi_k
\end{bmatrix} \cdot \begin{bmatrix}
    s_1, \cdots, s_{k-1}
\end{bmatrix} = 0 $$

有非零解。

不妨令 \(\|u\|_{L^2}=1\)，即

$$ 1 = \sum_{i=1}^k \mu_i^2 \|\phi_i\|_{L^2}^2 = \sum_{i=1}^k \frac{\mu_i^2}{\lambda_i} $$

那么

$$ B[u,u] = \sum_{i=1}^k \mu_i^2 \le \lambda_k \sum_{i=1}^k \frac{\mu_i^2}{\lambda_i} = \lambda_k $$

因此，对任意 \(S\in \Sigma_{k-1}\)，

$$ \min_{u\in S^{\bot},\|u\|_{L^2}=1} B[u,u] \ge \lambda_k $$

"\(\le\)":

令 \(S= \text{span}\{\phi_1, \cdots, \phi_{k-1}\}\)，
那么对于任意 \(u\in S^{\bot}\)，\((u, \phi_i) = 0, i=1, \cdots, k-1\)，     
因此 \(u = \sum_{i\ge k} \mu_i \phi_i\)，这意味着

$$ B[u, u] = \sum_{i\ge k} \mu_i^2 \ge \lambda_k \sum_{i\ge k} \frac{\mu_i^2}{\lambda_i} = \lambda_k \|u\|_{L^2}^2 $$

当 \(u=w_k=\lambda^{1/2}\phi_k\) 时取等。

因此当 \(S= \text{span}\{\phi_1, \cdots, \phi_{k-1}\}\) 时

$$ \lambda_k = \min_{u\in S^{\bot},\|u\|_{L^2}=1} B[u,u] $$

综上，

$$ \lambda_k = \max_{S\in \Sigma_{k-1}} \min_{u\in S^{\bot},\|u\|_{L^2}=1} B[u,u] $$





