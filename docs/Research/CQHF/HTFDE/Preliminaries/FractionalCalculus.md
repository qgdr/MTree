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
    &= (f\chi_{R_+}) * \overbrace{u * \cdots * u}^n \\
    &= (f\chi_{R_+}) * \frac{x^{n-1}}{(n-1)!} \\
    &= \int_0^x \frac{(x-t)^{n-1}}{(n-1)!}f(t) dt
\end{align} $$

将 \(n\) 连续化， 我们得到

$$ _{RL}I^q f(t) = \frac{1}{\Gamma(q)} \int_0^t (t-s)^{q-1} f(s) ds $$

当然，如果你清楚的记得各个部分所表示的内容， 那么不妨记 \( \Gamma(q) = (q-1)! \)

那么 \(\Gamma(q)\) 又是怎么得出来的？   
同样从 n 次积分公式出发，什么函数积分是不变的？     
当然是指数函数 \(e^x\)，我们有

$$ \begin{align}
    e^x &= \int_{-\infty}^x \int_{-\infty}^{x_1} \cdots \int_{-\infty}^{x_{n-1}} e^{x_n} dx_1 \cdots dx_{n} \\
    &= e^x * \frac{x^{n-1}}{(n-1)!} \\
    &= \int_{-\infty}^x \frac{(x-t)^{n-1}}{(n-1)!}e^t dt
\end{align} $$

令 \(x=0\) 自然就有

$$ 1 = \int_{-\infty}^0 \frac{(-t)^{n-1}}{(n-1)!}e^t dt = \int_0^{\infty} \frac{t^{n-1}}{(n-1)!}e^{-t} dt $$

我们有理由相信上式可以连续化,即

$$ \Gamma(q) = \int_0^{\infty} t^{q-1} e^{-t} dt $$


而且，由于我们通过卷积来理解多重积分，那么由于卷积性质

$$ x_1(t)*x_2(t) \stackrel{\mathcal{L}}{\longleftrightarrow} X_1(s)X_2(s) $$

我们天然期望从 **频域** 角度对它进行分析

而由于积分算子 \(u(t)\) 对应的 Laplace 变换是 \(\frac{1}{s}\)，我们很容易猜想

$$ \frac{x^{q-1}}{\Gamma(q)} \stackrel{\mathcal{L}}{\longleftrightarrow} \frac{1}{s^q} $$

进而，对于 \(p>0, q>0\)

$$ \frac{t^{p-1}}{\Gamma(p)} * \frac{t^{q-1}}{\Gamma(q)} = \frac{t^{p+q}}{\Gamma(p+q)} $$

取 \(t=1\)，我们就得到了

$$ B(p, q) = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p+q)} = \int_0^1 t^{p-1}(1-t^{q-1}) dt $$


## Riemann-Liouville 分数阶导数

我们能定义正的分数阶积分，但想要直接定义分数阶导数貌似有点困难。        
Riemann-Liouville 的做法是先分数阶积分，再整数阶导数。 （相对应的 Caputo 选择先整数阶微分，再积分）。     
对于 \(q>0\)，\(q\) 阶 Riemann-Liouville 微分为

$$ _{RL}D^q f(t) = \frac{1}{\Gamma(n-q)} \frac{d^n}{dt^n}\int_0^t (t-s)^{n-q-1} f(s) ds, \quad n-1<q<n $$

## Hadamard 积分

在力学和工程学中观察到某些过程的对数性质。

让我们重写 Riemann-Liouville 的积分公式

$$ _{RL}I^q_{x_0, x} g(x) = \frac{1}{\Gamma(q)} \int_{x_0}^x (x-y)^{q-1} g(y) dy $$

令 \(s=e^y\), \(t=e^x\), \(a=e^{x_0}\)，\(f(s)=f(e^y) = g(y)\), 那么

![hadamard](./Hadamardlog.png)

$$ _{RL}I^q_{x_0, x} f(e^x) = \frac{1}{\Gamma(q)} \int_{a}^t (\log \frac{t}{s})^{q-1} f(s) \frac{ds}{s} $$

那么，我们就形式的记

$$ _{H}I^q_{a, t} f(t) = \frac{1}{\Gamma(q)} \int_{a}^t (\log \frac{t}{s})^{q-1} f(s) \frac{ds}{s} $$


## Hadamard 导数

又由于 \(\dfrac{d}{dy}g(y) = s\dfrac{d}{ds}f(s)\)，
因此我们形式地定义算子 \(\delta=t\dfrac{d}{dt}\)，并类似的得到

$$ _{H}D^q f(t) = \frac{1}{\Gamma(n-q)} \delta^n \int_0^t (\log\frac{t}{s})^{n-q-1} f(s) \frac{ds}{s}, \quad n-1<q<n $$

这样，它在实际上就是 Riemann-Liouville 的积分公式，只不过要自变量要经过对数变换。
