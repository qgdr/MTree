# 逼近 Approximation

最近我在用一个广为人知的定理，但突然发现不知道怎么证了，翻了好多书都没有证明，于是为了证明这个结果，顺便补充这一章。

!!! question
    \(\Omega\) 是 \(R^n\) 中的开集。        
    若 \(u\in L_{\text{loc}}^1(\Omega)\) 对任何 \(\phi \in C_c^\infty(\Omega)\) 满足

    $$ \int_{\Omega} u \phi = 0 $$

    则 \(u = 0 \text{ a.e.}\) 

我们分几步来证明。

**1**.

首先我们能想到的是

!!! Lemma

    [Folland Real Analysis  Proposition 2.23](../index.md#参考教材)          
    [周民强 实变函数论 4.2 例 6](../index.md#参考教材)  是一个实数版本。

    对于 \(u \in L^1(\Omega)\)，\(u=0 \text{ a.e.}\) 等价于
    
    $$ \int |u| = 0 $$

    也等价于，对于任意 **可测子集** \(E \subset \Omega\)，

    $$ \int_E u = 0 $$

    ----

    \(\Rightarrow\) &emsp; 是显然的

    $$ \Big| \int_E u \Big| \leq \int_E |u| = \int \chi_E |u| \leq \int |u| = 0 $$

    \(\Leftarrow\) &emsp; 否则 \(u_+, u_-\) 必有一个非零，不妨设 \(E = \{x: u_+(x) > 0 \}\)，且 \(\mu(E) > 0\)，
    则

    $$ \int_E u = \int_E u_+ > 0 $$

    矛盾。      
    证毕。


有了这样的引理，我们好像只需要证明，光滑函数能逼近可测集的 **特征函数** 就好了，但需要一些细节。

**2**.

!!! Theorem
    参考 [Folland Real Analysis Theorem 8.14 Proposition 8.17](../index.md#参考教材)   的证明

    \(\Omega\) 是 \(R^n\) 中的开集。    
    对于任何 **紧包含** 于 \(\Omega\) 的可测子集 \(E \subset\subset \Omega, \; \text{i.e.} \; \overline{E} \subset \Omega\)，  
    存在开集 \(W\)，使得 \(E \subset\subset W \subset\subset \Omega\)，
    和一列 **一致有界** 函数 \(\phi_n \in C^\infty_c(\Omega), \text{supp}(\phi_n) \subset W\)，满足

    $$ \lim_{n\to\infty} \phi_n = \chi_E \; \text{a.e.} $$



证明的核心技术就是 **磨光函数** mollifier 。     

因为 \(\overline{E} \subset \Omega\)，故存在 \(\epsilon_0 > 0\) ，使得 \(\text{dist}(\overline{E}, \partial\Omega) > 2\epsilon_0\)。      
那么令 \(W = \{x: \text{dist}(x, \overline{E}) < \epsilon_0 \}\)，则 \(W\) 是一个开集，且 \(W \subset\subset \Omega\)。

由于 \(E\) 有界，故 \(\int_\Omega \chi_E = \mu(E) < \infty\) 是可积函数。      
令 \(\eta(x)\) 是 **磨光子** ，\(\eta(x) \in C^\infty_c(\Omega), \text{supp}(\eta) \subset B(0, 1)\) ，令 

$$ \eta_\epsilon(x) = \frac{1}{\epsilon^n} \eta(\frac{x}{\epsilon}) $$

则 \(\int \eta_\epsilon = 1 \) ，且 \(\text{supp}(\eta_\epsilon) \subset B(0, \epsilon)\)。

对于 \(0 < \epsilon  <\epsilon_0\)，令 

$$\phi_\epsilon(x) = \eta_\epsilon(x) * \chi_E(x) 
= \int_\Omega \eta_\epsilon(x-y) \chi_E(y) dy 
= \int_{\overline{B(0, \epsilon)}} \chi_E(x-y) \eta_\epsilon(y)  dy $$

则  \(\text{supp}(\phi_\epsilon) = \overline{E + B(0, \epsilon)} \subset \overline{W}\) ，
且 \(\phi_\epsilon \in C^\infty_c(\overline{W})\)。        

现在我们说明 \(\phi_\epsilon\) 一致有界：

$$ | \phi_\epsilon(x) | \le \int_{\overline{W}} \eta_\epsilon(x-y) |\chi_E(y)| dy \le \int_\Omega \eta_\epsilon(x-y) dy = 1 $$

接下来我们说明 当 \(\epsilon \to 0\) ， \(\phi_\epsilon \to \chi_E\)
（ Folland Real Analysis Theorem 8.14 ）        
记 \(f(x) = \chi_E(x)\)，\(\int |f| = \mu(E) =: M\) 可积，那么 

$$ \begin{align}
    |f * \eta_\epsilon(x) - f(x)| &= \Big| \int_{\overline{W}} f(x-y)-f(x) \eta_\epsilon(y) dy \Big| \\
    &\le  \int_{\overline{B(0, \epsilon)}} |f(x-y)  - f(x)|\eta_\epsilon(y) dy  \\
    &= \int_{\overline{B(0, 1)}} |f(x-\epsilon z)  - f(x)| \eta(z) dz  \\
\end{align} $$

那么

$$ \begin{align}
    \int_{\overline{W}} |f * \eta_\epsilon - f| &\le \int_{\overline{W}} \int_{\overline{B(0, 1)}} |f(x-\epsilon z)  - f(x)| \eta(z) dz dx    \\
    &= \int_{\overline{B(0, 1)}} \eta(z) \int_{\overline{W}} |f(x-\epsilon z)  - f(x)|  dx dz    \\
\end{align} $$

由于 \(\int_{\overline{W}} |f(x-\epsilon z)  - f(x)| < 2\int |f| = 2M\)， 则

$$ \eta(z) \int_{\overline{W}} |f(x-\epsilon z)  - f(x)|  dx < 2M\eta(z) $$

被 **可积函数控制** 。        
我们又有 

$$\int_{\overline{W}} |f(x-\epsilon z)  - f(x)| \to 0, \; \text{as} \; \epsilon \to 0 $$

（参考 [Folland Real Analysis Lemma 8.4 Proposition 8.5](../index.md#参考教材) ）       
这是因为可积函数可由连续函数逼近。              
[Folland Real Analysis Theorem 2.26](../../Library/[Gerald_B._Folland]_Real_Analysis__Modern_Techniq.pdf)           
参考 [Folland Real Analysis Proposition 7.9](../../Library/[Gerald_B._Folland]_Real_Analysis__Modern_Techniq.pdf)     
[周民强 实变函数论 定理 4.18 4.19](../../Library/《实变函数论第二版》周民强+北京大学2008年5月第2版.pdf)

因此由 **控制收敛定理** ，

$$ \int_{\overline{B(0, 1)}} \eta(z) \int_{\overline{W}} |f(x-\epsilon z)  - f(x)|  dx dz \to 0, \; \text{as} \; \epsilon \to 0 $$

即

$$  \int_{\overline{W}} |\phi_\epsilon(x) - \chi_E(x)| \to 0, \; \text{as} \; \epsilon \to 0  $$

依测度收敛，则由 **Riesz 定理** ，存在子列 \(\phi_n\) 几乎处处收敛

$$ \phi_n(x) \stackrel{a.e.}{\longrightarrow} \chi_E(x)  $$

且 \(|\phi_\epsilon(x)| \le 1\)。

**3**.

现在我们证明对任意可测紧子集 \(E \subset\subset \Omega\)，\(\int_E u = 0\)。

设 \(E \subset\subset W \subset\subset \Omega\)，和 \(\phi_n \in C^\infty_c(\Omega), \text{supp}(\phi_n) \subset W, |\phi_n(x)| \le 1\)，是我们在 2 步中获得的。     
因为 \(u \in L_{\text{loc}}^1(\Omega)\)，因此 \(\int_{\overline{W}} |u| < \infty\)。

考虑函数族 \( u_n(x) = u(x) \phi_n(x) \)，我们有 \( |u_n(x)| \le |u(x)|\)，被可积函数控制。         
又由原命题中 \(u\) 的条件，

$$ \int_{\overline{W}} u_n = \int_{\Omega} u \phi_n = 0 $$

而 \(\lim_{n\to\infty} u_n(x) = u(x)\chi_E(x)\)，那么由 **控制收敛定理** ，

$$ \int_E u = \int_{\overline{W}} u\chi_E = \lim_{n\to\infty} \int_{\overline{W}} u_n dx = 0 $$

因此综合 1 ，我们知道 \(u\) 在 \(\Omega\) 上任意可测紧子集上都是 0 。       
而 \(\Omega \subseteq R^n\) 是 \(\sigma\)-finite 的，所以 \(u\) 在 \(\Omega\) 上任意可测子集上的积分都是 0 ，
因此 \(u = 0 \; \text{a.e.} \)，证毕。