# 不等式 Inequalities

本节介绍一些常用的不等式。

## 共轭指数 conjugate indices

设 \(p, p' \ge 1\)，若

$$ \frac{1}{p} + \frac{1}{p'} = 1 $$

则称 \(p'\) 是 \(p\) 的共轭指数，\(p' = \frac{p}{p-1}\).        
特别的，若 \(p=1\) 规定 \(p' = \infty\)；若 \(p=\infty\) 规定 \(p' = 1\)。

## Young 不等式

对于 \(a,b\ge 0\)

$$ ab \le \frac{a^p}{p} + \frac{b^{p'}}{p'} $$

当 \(p=p'=2\) 时， 就是均值不等式。

当然，我更喜欢另一种理解方式，对于 \(\theta \in [0,1]\)

$$ a^{\theta} b^{1-\theta} \le \theta a + (1-\theta) b $$

这反映了 算术平均 大于 集合平均，并且在技术上可以由均值不等式直接推导出来，但是实际上他是由于 \(\ln x\) 的凸性得到的。

![Young](media/images/Inequalities/Young_ManimCE_v0.18.0.png)


## Hölder 不等式

Hölder 不等式有多个，我们对于函数版本和离散版本都进行介绍。

**1**.

对于 \(a_i, b_i \in \mathbb{R}, i = 1,2,\dots,n\), \(1\le p\le \infty\)

$$ \sum_{i=1}^n a_i b_i \le \left( \sum_{i=1}^n |a_i|^p \right)^{\frac{1}{p}} \left( \sum_{i=1}^n |b_i|^{p'} \right)^{\frac{1}{p'}} $$

我更喜欢下面的形式，对于 \(a_i, b_i \in \mathbb{R}\), \(\theta \in [0,1]\)

$$ \sum_{i=1}^n |a_i|^\theta |b_i|^{1-\theta} \le ( \sum_{i=1}^n |a_i| )^{\theta} ( \sum_{i=1}^n |b_i| )^{1-\theta} $$

我们介绍两种典型的证明方法

当 \(\symbf{a} = \symbf{0}\) 或 \(\symbf{b} = \symbf{0}\) 时，显然成立。    
否则，不妨设 \(\sum_{i=1}^n a_i = 1, \sum_{i=1}^n b_i = 1\)，那么由 [Young 不等式](./index.md#young) 可以得到

$$ \begin{gather*}
    |a_i|^\theta |b_i|^{1-\theta} \le \theta |a_i| + (1-\theta) |b_i|       \\
    \Rightarrow \sum_{i=1}^n |a_i|^\theta |b_i|^{1-\theta} \le \sum_{i=1}^n \theta |a_i| + \sum_{i=1}^n (1-\theta) |b_i| = \theta + (1-\theta) = 1
\end{gather*} $$

不等式得证。

第二种方法在本质上和第一种方法是一样的。

$$ \begin{gather*}
    |a_i|^\theta |b_i|^{1-\theta} \le \theta \lambda^{1-\theta} |a_i| + (1-\theta) \frac{1}{\lambda^\theta}  |b_i|       \\
    \Rightarrow \sum_{i=1}^n |a_i|^\theta |b_i|^{1-\theta} \le \theta \lambda^{1-\theta} \sum_{i=1}^n  |a_i| + (1-\theta) \frac{1}{\lambda^\theta} \sum_{i=1}^n |b_i|
\end{gather*} $$

令 \(\lambda = \dfrac{\sum_{i=1}^n |b_i|}{\sum_{i=1}^n |a_i|}\)，则不等式变为

$$ \sum_{i=1}^n |a_i|^\theta |b_i|^{1-\theta} \le (\theta + 1-\theta) (\sum_{i=1}^n  |a_i|)^\theta (\sum_{i=1}^n |b_i|)^{1-\theta} $$

我们再说连续版本

**2**.

对于 \(a_i, b_i, c_i \in \mathbb{R}, i = 1,2,\dots,n\), 
以及 \(\alpha, \beta, \gamma \in [0,1],  \alpha + \beta + \gamma = 1\)

$$ \sum_{i=1}^n |a_i|^\alpha |b_i|^\beta |c_i|^\gamma \le ( \sum_{i=1}^n |a_i|)^\alpha (\sum_{i=1}^n |b_i|)^\beta (\sum_{i=1}^n |c_i|)^\gamma $$

使用两次 **1** 得证。

更进一步， 对于 \(a_{ij}, j=1,2,\dots,m, i=1,2,\dots,n\) 以及 \(\alpha_j\in [0,1], \sum_{j=1}^m \alpha_j = 1 \) 有

$$ \sum_{i=1}^n \left( \prod_{j=1}^m |a_{ij}|^{\alpha_j} \right) \le \prod_{i=1}^m \left( \sum_{i=1}^n |a_{ij}| \right)^{\alpha_j} $$


**3**.

对于函数 \(f, g\)

$$ \int_\Omega fg \le \left( \int_\Omega |f|^p \right)^{\frac{1}{p}} \left( \int_\Omega |g|^{p'} \right)^{\frac{1}{p'}} $$

即

$$ \|fg\|_1 \le \|f\|_p \|g\|_{p'} $$

或者，对于 \(\theta \in [0,1]\)

$$ \int_\Omega |f|^\theta |g|^{1-\theta} \le  (\int_\Omega |f|)^\theta (\int_\Omega |g|)^{1-\theta} $$

证明和 **1** 类似，不妨设 \(\int|f| = \int |g| = 1 \)


$$ \begin{gather*}
    |f(x)|^\theta |g(x)|^{1-\theta} \le \theta |f(x)| + (1-\theta) |g(x)|       \\
    \Rightarrow \int_\Omega |f|^\theta |g|^{1-\theta} 
    \le \int_\Omega \theta |f| + \int_\Omega (1-\theta) |g| = 1
\end{gather*} $$


!!! Remark

    注意 **1** 和 **3** 之间的关系，实际上只要取 \(f, g\) 是简单函数，

    $$ f = \sum_{i=1}^n a_i \chi_{[i, i+1)}, g = \sum_{i=1}^n b_i \chi_{[i, i+1)} $$

    那么

    $$ \int_R fg = \sum_{i=1}^n a_i b_i \le \left( \sum_{i=1}^n |a_i|^p \right)^{\frac{1}{p}} \left( \sum_{i=1}^n |b_i|^{p'} \right)^{\frac{1}{p'}} = \|f\|_p \|g\|_{p'} $$

    ----

    当 \(\mu(\Omega)\) 有界时，我们取 \(g=\chi_\Omega\)，那么有

    $$ \int_\Omega f = \int_\Omega fg \le \left( \int_\Omega |f|^p \right)^{\frac{1}{p}}\left( \int_\Omega 1^{p'} \right)^{\frac{1}{p'}} = |\Omega|^{\frac{p-1}{p}}\|f\|_p $$



**4**.

与 **2** 类似，对于 \(f_j, j = 1,2,\dots,m\), \(\alpha_j \in [0,1], \sum_{j=1}^m \alpha_j = 1\)

$$ \int_\Omega \prod_{j=1}^m |f_j|^{\alpha_j} \le \prod_{j=1}^m \left( \int_\Omega |f_j| \right)^{\alpha_j} $$

也即

$$ \|f_1\cdots f_m\|_1 \le \|f_1\|_{p_1} \cdots \|f_m\|_{p_m}, \quad 1\le p_j \le \infty , \sum_{j=1}^m \frac{1}{p_j} = 1 $$



## Minkowski 不等式

同样也有离散和连续版本

**1**.

对于 \(\symbf{a} , \symbf{b} \in \mathbb{R}^n, 1\le p< \infty\)

$$ \|\symbf{a} + \symbf{b}\|_p \le \|\symbf{a}\|_p + \| \symbf{b}\|_p $$

**2**.

对于函数 \(f, g \in L^p(\Omega), 1\le p <\infty\)

$$ \|f+g\|_{L^p} \le \|f\|_{L^p} + \|g\|_{L^p} $$

这两个不等式都描述了一个事实， 即范数 \(l_p, L^p\) 的三角不等式! 证明也极其类似。

我们为了简化问题，不妨将向量（函数）单位化，将原问题改写为

$$ \|a\symbf{x} + b\symbf{y}\|_p \le \|a\symbf{x}\|_p + \|b \symbf{y}\|_p = a + b $$

其中 \(\|\symbf{x}\|_p = \|\symbf{x}\|_p\ = 1, \quad a, b \ge 0\).
那么不等式等价于

$$ \sum_{i=1}^n |a x_i + b y_i |^p \le (a + b)^p $$

但是由 [Hölder 不等式](./index.md#holder)，我们有

$$ |a x_i + b y_i |^p \le (a+b)^{p-1}(a |x_i|^p + b |y_i|^p ) $$

求和则有

$$ \sum_{i=1}^n |a x_i + b y_i |^p \le (a+b)^{p-1} \sum_{i=1}^n  (a |x_i|^p + b |y_i|^p ) = (a+b)^p  $$

得证.       
绝大多数教材上的标准证法都与上面的等价。

连续版本同理，

$$ \int_\Omega |a f(x) + b g(x)|^p \le (a+b)^{p-1}\int_\Omega a|f(x)|^p + b|g(x)|^p = (a+b)^p$$

where \(\|f\|_p = \|g\|_p = 1\) 

对于 \(p=\infty\) 是不言自明的。


**3**.

对于 \(\symbf{a}_i \in \mathbb{R}^n, i=1, 2,\dots,m ,\quad 1\le p\le \infty\)

$$ \|\sum_{i=1}^m \symbf{a}_i\|_p \le \sum_{i=1}^m \|\symbf{a}_i\|_p $$

在函数情况下类比有

**4**.

设 \(f(x, y)\) 是 \(\mathbb{R}^n \times \mathbb{R}^m\) 上的可测函数，\(1\le p <\infty\)。
且对几乎处处的 \(y\in \mathbb{R}^m\)，\(f_y(x) := f(x,y) \in L^p(\mathbb{R}^n)\)，且

$$ \int_{\mathbb{R}^n} \|f_y(x)\|_{L^p(\mathbb{R}^n)}dy = \int_{\mathbb{R}^n} \left(\int_{\mathbb{R}^m} |f(x, y)|^p dx \right)^{\frac{1}{p}} dy < \infty $$

则

$$ \| \int_{\mathbb{R}^n} f_y(x)dy \|_{L^p(\mathbb{R})^n} \le \int_{\mathbb{R}^n} \|f_y(x)\|_{L^p(\mathbb{R}^n)}dy $$

证明需要一些技巧


[周民强 实变函数论 6.4 定理 6.20](../../Library/《实变函数论第二版》周民强+北京大学2008年5月第2版.pdf)












