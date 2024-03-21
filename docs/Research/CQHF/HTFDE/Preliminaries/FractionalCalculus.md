# 分数阶微积分

## Riemann-Liouville 分数阶积分

我们首先思考一下整数阶积分，我们都知道 Cauchy 积分公式

$$ \int_0^x \int_0^{x_1} \cdots \int_0^{x_{n-1}} f(x_n) dx_1 \cdots dx_{n} = \int_0^x \frac{(x-t)^{n-1}}{(n-1)!}f(t) dt $$

一般来说，大家都是用数学归纳法来证明这个定理的，但是我们有更直观的理解

<iframe height=700 width=200% src="../nintplt.html" frameborder="0" allowfullscreen></iframe>

实际上，如果你熟悉 [卷积](../../../../RealAnalysis/Convolution/index.md) ，
你会知道对 \(f\) 积分 就是 \(f * u\)，其中 \(u\) 是阶跃函数。
那么 

$$ \begin{align}
    \int_0^x \int_0^{x_1} \cdots \int_0^{x_{n-1}} f(x_n) dx_1 \cdots dx_{n}
    &= f * \overbrace{u * \cdots * u}^n \\
    &= f * \frac{x^{n-1}}{(n-1)!} \\
    &= \int_0^x \frac{(x-t)^{n-1}}{(n-1)!}f(t) dt
\end{align} $$

将 \(n\) 连续化， 我们得到

$$ _{RL}I^q f(t) = \frac{1}{\Gamma(q)} \int_0^t (t-s)^{q-1} f(s) ds $$

当然，如果你清楚的记得各个部分所表示的内容， 那么不妨记 \( \Gamma(q) = (q-1)! \)
