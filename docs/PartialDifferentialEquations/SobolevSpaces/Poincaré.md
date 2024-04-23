# Poincaré 不等式

[Lawrence C.Evans Partial differential equations 5.8.1](../index.md#lawrence-cevans-partial-differential-equations)

我们曾在 [GNS 不等式的有界情况](./SobolevInequalities.md#bounded) 的最后提到过          
\(u\) 能否被 \(Du\) 控制与 \(u\) 是否存在等于 0 的部分是有很大区别的。              
因此我们建立 Poincaré 不等式就是为了消除 \(u\) 上下平移带来的影响。


记

$$ (u)_U = {-\mkern -19mu\int}_{U} u $$

为 \(u\) 在 \(U\) 上的平均。

## Poincare's inequalities

令 \(U \subset R^n\) 是 *有界连通开集* ，\(\partial U\) 是 \(C^1\) 的。       
设 \(1 \le p \le \infty\)，那么存在常数 \(C=C(n,p,U)\) 使得对于任何 \(u \in W^{1,p}(U)\)

$$ \|u-(u)_U\|_{L^p(U)} \le C \|Du\|_{L^p(U)} $$







[Rellich-Kondrachov Compactness Theorem](./SobolevInequalities2.md#rellich-kondrachov-compactness-theorem-2)            
[Du=0, u=c a.e.](./Approximation.md#local-approximation) Corollary













## Problems

!!! Question

    固定 \(\alpha>0\)，\(U \subset R^n\) 是有界 **连通** 开集，     
    设 \(1 \le p \le \infty\)，那么存在常数 \(C=C(n,p,U)\) 使得对于任何 \(u \in W^{1,p}(U)\) 且

    $$ E_u = \{x\in U | u(x)=0\}, \quad \mu(E_u) \ge \alpha $$

    都有

    $$ \|u\|_{L^{p}(U)} \le C(n, U, p, \alpha) \|Du\|_{L^{p}(U)} $$

    ---

    我们证明的技巧与证明 Poincaré 一样，使用反证法。

    否则存在 \(k=1, \cdots \)

    $$ \|u_k\|_{L^{p}(U)} > k \|Du_k\|_{L^{p}(U)}, \quad \mu(\{x\in U | u(x)=0\}) \ge \alpha $$

    令 \(v_k = \frac{u_k}{\|u_k\|_{L^{p}(U)}}\)，则 

    $$ \|v_k\|_{L^{p}(U)} = 1, \quad \mu(E_{v_k}=\{x\in U | v_k(x)=0\}) \ge \alpha, \quad \|Dv_k\|_{L^{p}(U)} < \frac{1}{k} $$

    因此 \(\|v_k\|_{W^{1,p}(U)}\) 有界，            
    那么由 [Rellich-Kondrachov 紧性定理](./SobolevInequalities2.md#rellich-kondrachov-compactness-theorem-2)
    （这里用到了 \(\partial U\) 是 \(C^1\) 的条件）

    $$ W^{1,p}(U) \subset\subset L^p(U) $$

    嵌入将有界序列映成相对紧序列，则 \(v_k\) 存在收敛子列

    $$ v_{k_j} \to v \in L^p(U), \quad \|v\|_{L^{p}(U)} = 1 $$

    但是对于 \(\forall \phi \in C_c^\infty(U)\)，

    $$ \int_U v D^\alpha\phi = \lim_{j\to \infty} \int_U v_{k_j} D^\alpha\phi = -\lim_{k_j\to \infty} \int_U D^\alpha v_{k_j}\phi $$

    但是由 [Holder 不等式]

    $$ \Big|\int_U D^\alpha v_{k_j}\phi \Big| \le \|D^\alpha v_{k_j}\|_{L^p(U)} \|\phi\|_{L^{\frac{p}{p-1}}(U)} < \frac{1}{k_j} \|\phi\|_{L^p(U)} \to 0 $$

    所以

    $$ Dv = 0 \text{ a.e. in } U $$

    那么由 [Du=0, u=c a.e.](./Approximation.md#local-approximation) Corollary

    $$ v = c \text{ a.e. in } U $$

    但是由于 

    $$ \begin{align}
        0 & = \lim_{j\to \infty} \int_U |v_{k_j}-v|^p   
        = \lim_{j\to \infty} \int_U |v_{k_j}-c|^p                 \\
        &\ge \lim_{j\to \infty} \int_{E_{v_{k_j}}} |v_{k_j}-c|^p  \\
        &\ge \alpha |c|^p   
    \end{align} $$

    因此只能 \(c=0\)，那么 \(v=0 \text{ a.e. in } U\)，但是这与 \(\|v\|_{L^p(U)} = 1\) 矛盾!            
    因此存在这样一个常数 \(C=C(n,U,p,\alpha)\) 使得

    $$ \|u\|_{L^{p}(U)} \le C(n, U, p, \alpha) \|Du\|_{L^{p}(U)} $$