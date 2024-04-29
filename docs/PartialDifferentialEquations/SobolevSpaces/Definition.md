# Sobolev 空间的定义

前面我们定义了弱导数，现在我们定义 Sobolev 空间。

## 定义 Defination

给定 \(1 \le p \le \infty\)，则 Sobolev 空间 \(W^{k, p}(\Omega)\) 定义为    

对于所有多重指标 \(\alpha, |\alpha| \le k\)，存在弱偏导数 \(D^\alpha u\)，且 \(D^\alpha u \in L^p(\Omega)\)

的所有局部可积函数构成的集合。即

$$ W^{k, p}(\Omega) = \{ u \in L_{\text{loc}}^1(\Omega) : D^\alpha u \in L^p(\Omega) \text{ for all } |\alpha| \le k \} $$







## 弱导数的性质

我们需要先说明一些弱导数的性质，对于 \(u, v \in W^{k,p}(\Omega)\)

(i)

$$ D^\alpha D^\beta u = D^{\alpha+\beta} u, \quad |\alpha|+|\beta| \le k $$

(ii)

$$ D^\alpha (\lambda u + \mu v) = \lambda D^\alpha u + \mu D^\alpha v , |\alpha| \le k $$

(iii)       
**Leibniz's 公式**                
若 \(\zeta \in C_c^\infty(\Omega)\)，则 \(\zeta u \in W^{k, p}(\Omega)\) 且

$$ D^\alpha (\zeta u) = \sum_{\beta \le \alpha} \binom{\alpha}{\beta} D^\beta \zeta D^{\alpha-\beta} u $$


## 范数 Norm


如果 \(u \in W^{k, p}(\Omega)\)，我们定义他的 **范数** 为

$$ \|u\|_{W^{k, p}(\Omega)} = \begin{cases}
    \left( \sum_{|\alpha|\le k}\int_\Omega |D^\alpha u|^p dx \right)^{\frac{1}{p}} &  1 \le p < \infty \\
    \sum_{|\alpha| \le k} \text{ess sup}_{\Omega} |D^\alpha u|           & p = \infty
\end{cases}  $$



我们说明 \(\|\cdot\|_{W^{k, p}(\Omega)}\) 是一个范数，即满足

1 . 正定性：        
\(\|u\|_{W^{k, p}(\Omega)} \ge 0\)，且 \(\|u\|_{W^{k, p}(\Omega)} = 0 \Leftrightarrow u = 0 \text{ a.e.}\)，这是显然的，因为 \(0 = \|u\|_{W^{k, p}(\Omega)} \ge \|u\|_{L^p(\Omega)} \Rightarrow u = 0 \text{ a.e.}\)

2 . 齐次性：        
\(\|\lambda u\|_{W^{k, p}(\Omega)} = |\lambda| \|u\|_{W^{k, p}(\Omega)} \quad \forall \lambda \in R\)

3 . 三角不等式：        
对于 \(1 \le p<\infty\)，以及 \(u, v \in W^{k, p}(\Omega)\)，可以得到

$$ \begin{align}
    \|u + v\|_{W^{k, p}(\Omega)} 
    &= \left( \sum_{|\alpha|\le k}\int_\Omega |D^\alpha (u + v)|^p dx \right)^{\frac{1}{p}} \\
    &\le \left( \sum_{|\alpha|\le k} \left(\|D^\alpha u\|_{L^p(\Omega)} + \|D^\alpha v\|_{L^p(\Omega)}\right)^p \right)^{\frac{1}{p}} \\
    &\le \left( \sum_{|\alpha|\le k}\int_\Omega |D^\alpha u|^p dx \right)^{\frac{1}{p}} + \left( \sum_{|\alpha|\le k}\int_\Omega |D^\alpha v|^p dx \right)^{\frac{1}{p}} \\
    &= \|u\|_{W^{k, p}(\Omega)} + \|v\|_{W^{k, p}(\Omega)}
\end{align} $$

第一个不等号使用了 Minkowski 不等式

$$ \|D^\alpha u + D^\alpha v\|_{L^p(\Omega)} \le \|D^\alpha u\|_{L^p(\Omega)} + \|D^\alpha v\|_{L^p(\Omega)} $$

第二个不等号使用了离散形式的 Minkowski 不等式

$$ \left(\sum_{i=1}^{n} |a_k + b_k|^p\right)^{\frac{1}{p}} \le \left(\sum_{i=1}^{n} |a_k|^p\right)^{\frac{1}{p}} + \left(\sum_{i=1}^{n} |b_k|^p\right)^{\frac{1}{p}} $$

!!! Lemma

    事实上，当 \(1 \le p < \infty\) 时，

    $$  \left( \sum_{|\alpha|\le k}\int_\Omega |D^\alpha u|^p dx \right)^{\frac{1}{p}} 
    \Leftrightarrow \sum_{|\alpha| \le k} \|D^\alpha u\|_{L^p(\Omega)} $$

    我更喜欢后一种直接相加这种暴力方式，实际上我们也会在 [Hölder 空间](./HölderSpaces.md#holder_1) 中见识这样的操作。

    事实上 \(\sum_{|\alpha| \le k} \|D^\alpha u\|_{L^p(\Omega)}\) 明显满足范数的定义。
    而且

    $$ \left( \sum_{|\alpha|\le k}\|D^\alpha u\|_{L^p(\Omega)}^p dx \right)^{\frac{1}{p}} 
    \le \sum_{|\alpha| \le k} \|D^\alpha u\|_{L^p(\Omega)} 
    \le \left(\sum_{|\alpha| \le k} 1 \right)^{\frac{p-1}{p}}\left(\sum_{|\alpha| \le k} \|D^\alpha u\|_{L^p(\Omega)}^p \right)^\frac{1}{p} $$

     




!!! Example

    令 \(\{r_k\}_{k=1}^\infty\) 是 \(U=B^0(0, 1)\) 的可数稠密子集。

    $$ u(x) = \sum_{k=1}^\infty \frac{1}{2^k} |x -r_k|^{-\alpha} \quad x\in U$$

    那么对于 \(\alpha <\frac{n-p}{p}\)， \(u\in W^{1,p}(U) \).              
    如果 \(0< \alpha <\frac{n-p}{p}\)， \(u\in W^{1,p}(U) \) 但在每个开子集上都是无界的。


    ----


    **证明**

    令 

    $$ u_m(x) = \sum_{k=1}^m \frac{1}{2^k} |x -r_k|^{-\alpha} $$ 

    是非负渐升可测函数列，

    **1**.

    那么由 [Beppo-Levi 渐升定理] 

    $$ \begin{align}
        \int_U |u(x)|^p dx &= \int_U \lim_{m\to \infty} |u_m(x)|^p dx \\
        &= \lim_{m\to \infty} \int_U \left( \sum_{k=1}^m \frac{1}{2^k} |x -r_k|^{-\alpha} \right)^p dx \\
    \end{align}  $$

    然而由 Hölder 不等式，我们得到

    $$ \sum_{k=1}^m \frac{1}{2^k} |x -r_k|^{-\alpha} 
    \le \left(\sum_{k=1}^m \frac{1}{2^k}  \right)^{\frac{p-1}{p}}\left( \sum_{k=1}^m \frac{1}{2^k} |x -r_k|^{-\alpha p} \right)^{\frac{1}{p}} 
    \le \left( \sum_{k=1}^m \frac{1}{2^k} |x -r_k|^{-\alpha p} \right)^{\frac{1}{p}} $$

    所以

    $$ \begin{align}
        \int_U \left( \sum_{k=1}^m \frac{1}{2^k} |x -r_k|^{-\alpha} \right)^p dx 
        &\le \int_U \sum_{k=1}^{m} \frac{1}{2^k} |x -r_k|^{-\alpha p} dx \\
        &= \sum_{k=1}^{m} \frac{1}{2^k} \int_{B^0(0, 1)} |x -r_k|^{-\alpha p} dx    \\
        &\le \sum_{k=1}^{m} \frac{1}{2^k} \int_{B^0(r_k, 2)} |x -r_k|^{-\alpha p} dx   \qquad (B(0, 1)\subset B(r_k, 2)) \\
        &= \sum_{k=1}^{m} \frac{1}{2^k} \int_{B^0(0, 2)} |x|^{-\alpha p} dx     \\
        &\le \int_0^2 \int_{\partial B(0, r)} r^{-\alpha p} dS dr
        = n\alpha(n)  \int_0^2 r^{-\alpha p}r^{n-1} dr     \\
        &= n\alpha(n)  \int_0^2 r^{n-\alpha p-1} dr
    \end{align}  $$

    其中 \(\alpha(n)\) 是 \(n\) 维单位球的体积，\(n\alpha(n)\) 等于 \(n\) 维单位球的表面积。   

    当 \(\alpha < \frac{n-p}{p} < \frac{n}{p}\) 时，\(n-\alpha p > 0\)

    $$ \int_0^2 r^{n-\alpha p-1} dr = r^{n-\alpha p} \Big|_0^2 = 2^{n-\alpha p} < \infty $$

    这意味着 

    $$ \int_U |u(x)|^p dx = \lim_{m\to \infty} \int_U |u_m(x)|^p dx \le \lim_{m\to \infty} n\alpha(n) 2^{n-\alpha p} = n\alpha(n) 2^{n-\alpha p} < \infty $$

    因此 \(u \in L^p(U)\).

    在上面的证明过程中，我们实际上证明了 \(u_m \in L^p(U)\)，

    $$ |u_m(x)| < |u(x)| \Rightarrow |u_m(x)-u(x)| \le 2|u(x)| $$

    但是 \(u \in L^p(U)\) 

    那么由 [控制收敛定理] 

    $$ \lim_{m\to \infty} \|u_m - u\|_{L^p(U)} \to 0 $$


    **2**.

    （在这里我们使用 \(\nabla f\)，表示函数的梯度， \(Df\) 则表示弱导数。）

    对于 \(f = |x|^{-\alpha}\)，我们有

    $$ \nabla f = -\alpha |x|^{-\alpha-2} x $$

    我们希望证明 \(Df = \nabla f \quad \text{a.e.}\)

    事实上，对于 \(\phi \in C_c^\infty(R^n)\)，

    $$ \begin{align}
        \int_{R^n} f(x) \nabla \phi 
        &= \int_{B(0, \epsilon)} |x|^{-\alpha} \nabla \phi(x)dx
            + \int_{B(0, \epsilon)^c} |x|^{-\alpha} \nabla \phi(x)dx \\
        &= I_1 + I_2
    \end{align} $$

    由于 \(\nabla \phi(x)\) 有界，故

    $$ \begin{align}
        I_1 &\le C(\phi)\int_{B(0, \epsilon)} |x|^{-\alpha} dx \\
        &= C(\phi)\int_0^\epsilon \int_{\partial B(0, r)} r^{-\alpha} dS dr  \\
        &= C(\phi, n)\int_0^\epsilon r^{n-\alpha-1} dr    \quad (\alpha =\frac{n}{p} -1 < n)      \\
        &= C \epsilon^{n-\alpha}   \to 0 \quad \text{as } \epsilon \to 0
    \end{align} $$

    而由 [Gauss-Green 公式]

    $$ \begin{align}
        I_2 &= \int_{B(0, \epsilon)} |x|^{-\alpha} \nabla \phi(x)dx \\
        &= \int_{\partial B(0, \epsilon)} |x|^{-\alpha} \phi(x) \nu dS 
            - \int_{B(0, \epsilon)} \phi(x) \nabla |x|^{-\alpha} x dx \\
    \end{align} $$

    但是，由于 \(\phi\) 有界，所以

    $$ \begin{align}
        \int_{\partial B(0, \epsilon)} |x|^{-\alpha} \phi(x) \nu dS 
        &\le C(\phi) \int_{\partial B(0, \epsilon)} |x|^{-\alpha} dS         \\
        &= C(\phi) n\alpha(n) \epsilon^{-\alpha}  \epsilon^{n-1}             \\
        &= C(\phi, n) \epsilon^{n-\alpha-1}       \to 0 \quad \text{as } \epsilon \to 0 
        \quad (\alpha =\frac{n}{p} -1 < n -1)
    \end{align} $$


    因此当 \(\epsilon \to 0\) 时，有

    $$ \int_{R^n} |x|^{-\alpha} \nabla \phi(x)dx  = - \int_{R^n} \phi(x) \nabla |x|^{-\alpha} x dx = \int_{R^n} \phi(x)\alpha |x|^{-\alpha-2} x$$

    因此 \(Df = \nabla f\) a.e.



    **3**.

    对于

    $$ u_m(x) = \sum_{k=1}^m \frac{1}{2^k} |x -r_k|^{-\alpha} $$

    由 2 ,对于 \(|\alpha|=1\)

    $$ \begin{align}
        D^\alpha u_m(x) &= \sum_{k=1}^m \frac{1}{2^k} D^\alpha |x -r_k|^{-\alpha}
            \le \sum_{k=1}^m \frac{1}{2^k} |\nabla |x -r_k|^{-\alpha} |    \\
        &= \sum_{k=1}^m \frac{1}{2^k} \Big|\frac{1}{|x -r_k|^{\alpha+1}} \frac{x-r_k}{|x -r_k|} \Big|    \\
        &\le \sum_{k=1}^m \frac{1}{2^k} \frac{1}{|x -r_k|^{\alpha+1}}
    \end{align} $$

    几乎重复 1 中的过程，但这次我们证明 \(D^\alpha u_m\) 是 \(L^p(U)\) 中的 Cauchy 列。

    $$ \begin{align}
        \int_U |D^\alpha u_m(x) - D^\alpha u_n(x)|^p dx 
        & \le \int_U \left( \sum_{k=m}^n \frac{1}{2^k} \frac{1}{|x -r_k|^{\alpha+1}} \right)^p  dx    \\
        &\le \left(\sum_{k=m}^n \frac{1}{2^k}  \right)^{p-1} \int_U \sum_{k=m}^n \frac{1}{2^k} |x -r_k|^{-(\alpha+1) p}          \\
        &\le \frac{1}{2^{(m-1)(p-1)}} \sum_{k=m}^n \frac{1}{2^k} \int_U |x -r_k|^{-(\alpha+1) p} dx    \\
        &\le \sum_{k=m}^n \frac{1}{2^k} \int_{B(0, 2)} |x|^{-(\alpha+1) p} dx       \\
        &= n\alpha(n) \frac{1}{2^{m-1}} \int_0^2 r^{-(\alpha+1) p} r^{n-1} dx       \\
        &= n\alpha(n) \frac{1}{2^{m-1}} \int_0^2 r^{n-(\alpha+1) p-1} dr
    \end{align} $$

    又因为 \((\alpha+1)p < \frac{n}{p} p = n\)，所以

    $$ \int_0^2 r^{n-(\alpha+1) p-1} dr = 2^{n-(\alpha+1) p} < \infty $$

    故

    $$ \int_U |D^\alpha u_m(x) - D^\alpha u_n(x)|^p dx < \frac{1}{2^{m-1}} C(n, \alpha, p)  \to 0 \quad \text{as } m,n \to \infty $$

    因此 \(D^\alpha u_m\) 是 \(L^p(U)\) 中的 Cauchy 列，存在极限 \(v \in L^p(U)\)。

    那么对于任意的 \(\forall \phi \in C_c^\infty(U)\)，由于 [引理](#strong2weak-convergence)

    $$ \begin{align}
        \int_U u(x) D^\alpha \phi(x) dx &= \lim_{m\to \infty} \int_U  u_m(x) D^\alpha \phi(x) dx \\
        &= \lim_{m\to \infty} -\int_U D^\alpha u_m(x) \phi(x) dx \\
        &= -\int_U v \phi(x) dx
    \end{align} $$

    所以 \(D^\alpha u = v(x) \quad \text{a.e.}\)

    因此 \(u \in W^{1, p}(U)\).

    ----

    如果 \(\alpha > 0\)，那么 \(|x-r_k|^{-\alpha} \to \infty \; \text{ as } x \to r_k \)，
    而对于 \(U\) 中的任意开集 \(V\)，由于 \(\{r_k\}_{k=1}^\infty\) 是稠密的，必然存在 \(r_j \in V\)，
    那么 \(|x-r_j|^{-\alpha}\) 在 \(V\) 无界，则 \(u(x) > \frac{1}{2^j}|x-r_j|^{-\alpha}\) 也是无界的。


从上面这个例子我们把握到了如何证明 \(W^{1,p}(U)\) 的完备性，自然的我们试图证明 \(W^{k,p}(\Omega)\) 的完备性。

----




## Completeness 完备性


<font color="Black_Pink">
对于 \(1\le p \le \infty\)，Sobolev 空间 \(W^{k,p}(\Omega)\) 是 Banach 空间
</font>

**证明**

设 \(\{u_m\}_{m=1}^\infty\) 是 \(W^{k,p}(\Omega), 1\le p < \infty\) 中的Cauchy列，           
那么根据范数定义

$$ \|u\|_{W^{k,p}(\Omega)} = \left( \sum_{|\alpha| \le k} \|D^\alpha u\|_{L^p(\Omega)}^p \right)^{\frac{1}{p}} \ge \|D^\beta u\|_{L^p(\Omega)} \quad \forall |\beta| \le k $$

函数列 \(\{D^\alpha u_m\}_{m=1}^\infty, |\alpha| \le k\) 显然也是 \(L^p(\Omega)\) 中的 Cauchy 列。      
那么设

$$ D^\alpha u_m \to u_\alpha \text{ in } L^p(\Omega), \quad |\alpha| \le k $$

特别的 \(u_m \to u \text{ in } L^p(\Omega)\)。

对于任意的 \(\phi \in C_c^\infty(\Omega)\)，

$$ \begin{align}
    \int_\Omega u D^\alpha \phi dx &= \lim_{m\to \infty} \int_\Omega  u_m D^\alpha\phi dx \\
    &= \lim_{m\to \infty} (-1)^{|\alpha|} \int_\Omega D^\alpha u_m \phi dx \\
    &= (-1)^{|\alpha|} \int_\Omega u_\alpha \phi dx
\end{align} $$

因此 \(u_\alpha = D^\alpha u \text{ a.e.}\)，
\(u \in W^{k,p}(\Omega)\)， 

$$ u_m \to u \text{ in } W^{k,p}(\Omega) $$

\(W^{k,p}(\Omega)\) 完备，是 Banach 空间。

!!! Lemma

    ### Strong2Weak Convergence

    事实上，我们那这里极限和积分交换了次序

    $$ \int_\Omega u \psi dx
    = \int_\Omega \lim_{m\to \infty} u_m \psi dx = \lim_{m\to \infty} \int_\Omega  u_m \psi dx $$

    这是因为

    $$ \int_\Omega |u - u_m| \psi dx 
    \le \|u-u_m\|_{L^p}\|\psi\|_{L^{p^*}} , \text{ where } \frac{1}{p^*} + \frac{1}{p} = 1 $$

    当然用 泛函分析 的语言可以描述为，强收敛 \(\Rightarrow\) 弱收敛


特别的，对于 \(p=\infty\)，

$$ \|u\|_{W^{k,\infty}(\Omega)} = \sum_{|\alpha| \le k} \|D^\alpha u\|_{L^\infty(\Omega)} $$

证明过程类似，只不过在 引理 中不等式变成

$$ \int_\Omega |u - u_m| \psi dx \le \|u-u_m\|_{L^\infty}\|\psi\|_{L^{1}} $$

