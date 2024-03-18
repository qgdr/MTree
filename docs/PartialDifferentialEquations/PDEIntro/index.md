# 偏微分方程简介

本章介绍各个偏微分方程的定义以及一些常用的结论。

## 准备符号

令多重指标(multiindex) \( \alpha=(\alpha_1, ... , \alpha_n), \quad \alpha_n \ge 0 \)，

$$ |\alpha| := \alpha_1 + ... + \alpha_n $$

$$ \alpha ! := \alpha_1!\cdots\alpha_n! $$

$$ \begin{pmatrix} |\alpha| \\ \alpha \end{pmatrix} := \frac{ |\alpha|!}{\alpha!} $$

对于多元变量 \( x=(x_1, ... , x_n) \)，

$$ x^\alpha := x_1^{\alpha_1}\cdots x_n^{\alpha_n} $$

$$ D^\alpha u(x) := \frac{\partial^{|\alpha|} u(x)}{\partial x^{\alpha_1}\cdots\partial x^{\alpha_n}} $$

$$ D^k u(x) = \\{ D^\alpha u(x) \mid |\alpha|=k \\} $$

nabla算子

$$ \nabla u = (\frac{\partial u}{\partial x_i}, ..., \frac{\partial u}{\partial x_n}) $$

Laplace算子

$$ \Delta u = \nabla\cdot\nabla u = \frac{\partial^2 u}{\partial x_i^2} + ... + \frac{\partial^2 u}{\partial x_n^2} $$

## Problems

!!! question
    2 . \( D^k u(x) \) 有几项？
!!! solve  
    事实上，就是将 \(n\) 个苹果，放进 \(k\) 个盒子，那么显然有 \( \begin{pmatrix}n+k-1\\ k \end{pmatrix} \) 种放法。 

!!! question
    3 . 证明 **多项式定理** (Multinomial Theorem)：

    $$ (x_1 + ... + x_n)^k = \sum_{|\alpha|=k} \begin{pmatrix} |\alpha| \\ \alpha \end{pmatrix} x^\alpha $$

!!! solve
    对于 \( x^\alpha = x_1^{\alpha_1}\cdots x_n^{\alpha_n} \) 的项，有多少种选法？
    先从 \(k\) 个中选 \(\alpha_1\) 个 \(x_1\)， 再从 \(k-\alpha_1\) 个中选 \(\alpha_2\) 个 \(x_2\)，...，最后从 \(k-\sum_{i=1}^{n-1} \alpha_i\) 个中选 \(\alpha_n\) 个 \(x_n\)。
    总共有 
    
    $$ \frac{k!}{\alpha_1! (k-\alpha_1)!} \frac{(k-\alpha_1)!}{\alpha_2! (k-\alpha_1-\alpha_2)!} \cdots \frac{(k-\alpha_1-\cdots-\alpha_{n-1})!}{\alpha_n! (k-\alpha_1-\cdots-\alpha_{n})!} = \frac{k!}{\alpha!} $$ 
    
    种选法。 

!!! question
    4 . 证明 **莱布尼兹公式** (Leibniz's Formula)：

    $$ D^\alpha(uv) = \sum_{\beta\le\alpha}\begin{pmatrix} \alpha \\ \beta \end{pmatrix} D^\beta u D^{\alpha-\beta}v $$

!!! solve  
    我们有 \( D^\alpha (uv) = \partial^{\alpha_1}_{x_1} \cdots \partial^{\alpha_n}_{x_n} (uv) \)， 那么 \(D^\beta u D^{\alpha-\beta}v = \partial^{\beta_1}_{x_1} \cdots \partial^{\beta_n}_{x_n} u \cdot \partial^{\alpha_1-\beta_1}_{x_1} \cdots \partial^{\alpha_n-\beta_n}_{x_n} v \) 有多少种选法？   
    它有 \( \begin{pmatrix} \alpha_n \\ \beta_n \end{pmatrix}\cdots \begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix}  = \frac{\alpha_1!\cdots\alpha_n!}{\beta_1!\cdots\beta_n! (\alpha_1-\beta_1)!\cdots (\alpha_n-\beta_n)!} \)
    种选法。 
