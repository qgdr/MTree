# 偏微分方程简介

本章介绍各个偏微分方程的定义以及一些常用的结论。

## 准备符号

查看 [Lawrence C.Evans Partial differential equations Appendix A](../index.md#lawrence-cevans-partial-differential-equations)

令多重指标(multiindex) \( \alpha=(\alpha_1, ... , \alpha_n), \quad \alpha_n \ge 0 \)，

$$ |\alpha| := \alpha_1 + ... + \alpha_n $$

$$ \alpha ! := \alpha_1!\cdots\alpha_n! $$

$$ \begin{pmatrix} |\alpha| \\ \alpha \end{pmatrix} := \frac{ |\alpha|!}{\alpha!} $$

对于多元变量 \( x=(x_1, ... , x_n) \)，

$$ x^\alpha := x_1^{\alpha_1}\cdots x_n^{\alpha_n} $$

$$ D^\alpha u(x) := \frac{\partial^{|\alpha|} u(x)}{\partial x_1^{\alpha_1}\cdots\partial x_n^{\alpha_n}} 
= \frac{\partial^{\alpha_1} }{\partial x_1^{\alpha_1}} \cdots \frac{\partial^{\alpha_n}}{\partial x_n^{\alpha_n}}u(x) $$

事实上，对于 \(u(x)\in C^k\)，\(\frac{\partial^2 u(x)}{\partial x_1x_2} = \frac{\partial^2 u(x)}{\partial x_2 x_1} \)，微分顺序可交换。 
因此在定义 \(D^k u(x)\) 的时候，将不同微分次序的前导数看成是同一个。

$$ D^k u(x) = \{ D^\alpha u(x) \mid |\alpha|=k \} $$

nabla算子

$$ \nabla u = (\frac{\partial u}{\partial x_i}, ..., \frac{\partial u}{\partial x_n}) $$

Laplace算子

$$ \Delta u = \nabla\cdot\nabla u = \frac{\partial^2 u}{\partial x_i^2} + ... + \frac{\partial^2 u}{\partial x_n^2} $$

## Problems

!!! question
    2 . \( D^k u(x) \) 有几项？

!!! solution
    观察上面 \(D^\alpha u(x)\) 的定义， 
    就是将 \(k\) 个苹果（偏导数\(\partial^k\)），放进 \(n\) 个盒子（\(\partial x_i, i=1, ..., n\)），允许空盒子。   
    那么显然有 \( \begin{pmatrix}n+k-1\\ k \end{pmatrix} \) 种放法。 

!!! question
    3 . 证明 **多项式定理** (Multinomial Theorem)：

    $$ (x_1 + ... + x_n)^k = \sum_{|\alpha|=k} \begin{pmatrix} |\alpha| \\ \alpha \end{pmatrix} x^\alpha $$

!!! proof
    对于 \( x^\alpha = x_1^{\alpha_1}\cdots x_n^{\alpha_n} \) 的项，有多少种选法？      
    先从 \(k\) 个中选 \(\alpha_1\) 个 \(x_1\)， 再从 \(k-\alpha_1\) 个中选 \(\alpha_2\) 个 \(x_2\)，...，最后从 \(k-\sum_{i=1}^{n-1} \alpha_i\) 个中选 \(\alpha_n\) 个 \(x_n\)。    
    总共有 
    
    $$ \frac{k!}{\alpha_1! (k-\alpha_1)!} \frac{(k-\alpha_1)!}{\alpha_2! (k-\alpha_1-\alpha_2)!} \cdots \frac{(k-\alpha_1-\cdots-\alpha_{n-1})!}{\alpha_n! (k-\alpha_1-\cdots-\alpha_{n})!} = \frac{k!}{\alpha!} $$ 
    
    种选法。 

!!! question
    4 . 证明 **莱布尼兹公式** (Leibniz's Formula)：

    $$ D^\alpha(uv) = \sum_{\beta\le\alpha}\begin{pmatrix} \alpha \\ \beta \end{pmatrix} D^\beta u D^{\alpha-\beta}v $$

!!! prove  
    我们有 \( D^\alpha (uv) = \partial^{\alpha_1}_{x_1} \cdots \partial^{\alpha_n}_{x_n} (uv) \)，      
    而我们知道 \(\partial_i(uv) = (\partial_i u) v + u (\partial_i v) \)。
    归纳得 

    $$ \partial_i^{\alpha_i}(uv) = \sum_{\beta_i=0}^{\alpha_i} \begin{pmatrix} \alpha_i \\ \beta_i \end{pmatrix} (\partial_i^{\alpha_i-\beta_i} u)(\partial_i^{\beta_i} v)  $$

    这也被称为问分法则的 莱布尼兹公式。

    那么 \(D^\beta u D^{\alpha-\beta}v = \partial^{\beta_1}_{x_1} \cdots \partial^{\beta_n}_{x_n} u \cdot \partial^{\alpha_1-\beta_1}_{x_1} \cdots \partial^{\alpha_n-\beta_n}_{x_n} v \) 有多少种选法？   
    它有 \( \begin{pmatrix} \alpha_n \\ \beta_n \end{pmatrix}\cdots \begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix}  = \frac{\alpha_1!\cdots\alpha_n!}{\beta_1!\cdots\beta_n! (\alpha_1-\beta_1)!\cdots (\alpha_n-\beta_n)!} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix} \)
    种选法。 


!!! question

    5 . 设 \(f: R^n \to R\) 是光滑函数，证明

    $$ f(x) = \sum_{|\alpha|\le k} \frac{1}{\alpha !} D^{\alpha} f(0) x^{\alpha} + O(\|x\|^{k+1}) $$

    这称为多元函数的 **Taylor 公式**

!!! prove

    固定 \(x\)，令 \(g(t) = f(tx)\)，那么由单变量的 Taylor 公式 （看 [Cauchy](../../FractionalDifferentialEquations/RLFIDF.md#分数阶微积分引入)），有

    $$ \begin{align}
        g(t) &= \sum_{i=0}^k \frac{1}{i!} g^{(i)}(0) t^i + \int_0^t g^{(k+1)}(s)\frac{(t-s)^k}{k!} ds \\
        &= \sum_{i=0}^k \frac{1}{i!} g^{(i)}(0) t^i + g^{(k+1)}(\xi) \frac{t^{k+1}}{(k+1)!}, \quad \xi \in [0, t] \\
    \end{align} $$

    则

    $$ f(x) = g(1) = \sum_{i=0}^k \frac{1}{i!} g^{(i)}(0) + g^{(k+1)}(\xi) \frac{1}{(k+1)!}, \quad \xi \in [0, 1] $$

    但
    
    $$ \begin{gather}
        g'(t) =\frac{d f(tx)}{dt} =  \nabla(f(tx)) \cdot x = \sum_{i=0}^n \partial_i f(tx) x_i  \\
        g''(t) =\frac{d}{dt}(\partial_i f(tx) x_i) 
        = \sum_{i,j} \partial_{ij} f(tx) x_i x_j 
        = \sum_{|\alpha|=2} \begin{pmatrix} 2 \\ \alpha \end{pmatrix} D^{\alpha} f(tx) x^{\alpha}  \\
        \cdots \\
        g^{(k+1)}(t) = \frac{d^k}{dt^k} f(tx) 
        = \sum_{i_1, \cdots, i_{k+1}} \partial_{i_1} \cdots \partial_{i_{k+1}} f(tx) x_{i_1} \cdots x_{i_{k+1}} 
        = \sum_{|\alpha|=k+1} \begin{pmatrix} k+1 \\ \alpha \end{pmatrix} D^{\alpha} f(tx) x^{\alpha}
    \end{gather} $$

    所以有

    $$ \begin{align} 
        f(x) &= \sum_{i=0}^k \frac{1}{i!} g^{(i)}(0) x^i + g^{(k+1)}(\xi) \frac{1}{(k+1)!} \\
        &= \sum_{i=0}^k \frac{1}{i!} \sum_{|\alpha|=i} \begin{pmatrix} i \\ \alpha \end{pmatrix} D^{\alpha} f(0) x^{\alpha} 
        + \frac{1}{(k+1)!}\sum_{|\alpha|=k+1} \begin{pmatrix} k+1 \\ \alpha \end{pmatrix} D^{\alpha} f(\xi x) x^{\alpha} \\
        &= \sum_{|\alpha|\le k} \frac{1}{\alpha !} D^{\alpha} f(0) x^{\alpha}
        + \frac{1}{(k+1)!} \sum_{i_1, \cdots, i_{k+1}} \partial_{i_1} \cdots \partial_{i_{k+1}} f(\xi x) x_{i_1} \cdots x_{i_{k+1}} \\
    \end{align} $$

    由于 \(f\) 光滑，所以当 \(x\) 足够小时， 有 \(|\partial_{i_1} \cdots \partial_{i_{k+1}} f(\xi x)| < C(x, n), \quad  \xi \in [0, 1]\) 

    而 
    
    $$ \frac{1}{(k+1)!} \sum_{i_1, \cdots, i_{k+1}} \partial_{i_1} \cdots \partial_{i_{k+1}} f(\xi x) x_{i_1} \cdots x_{i_{k+1}} < C(x, k+1)(|x_1|+\cdots+|x_n|)^{k+1} = O(\|x\|^{k+1}) $$

    故当 \(x \to 0\)，有

    $$ f(x) = \sum_{|\alpha|\le k} \frac{1}{\alpha !} D^{\alpha} f(0) x^{\alpha} + O(\|x\|^{k+1}) $$




