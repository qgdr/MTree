# Fourier Transform Methods 傅里叶变换方法


## 定义

如果 \(u\in L^1(\mathbb{R}^{n})\)，
我们定义 Fourier 变换为 \(\mathcal{F}u =\hat{u}\)

$$ \hat{u}(y) := \frac{1}{(2\pi)^{n/2}} \int_{\mathbb{R}^{n}} u(x) e^{-i x \cdot y} dx \quad (y \in \mathbb{R}^{n})$$

Fourier 逆变换 \(\mathcal{F}^{-1}=\check{u} \)

$$ \check{u}(y) := \frac{1}{(2\pi)^{n/2}} \int_{\mathbb{R}^{n}} u(x) e^{i x \cdot y} dx \quad (y \in \mathbb{R}^{n}) $$


## Plancherel's Theorem

假设 \(u\in L^1(\mathbb{R}^{n})\cap L^2(\mathbb{R}^{n})\).那么 \(\hat{u}, \check{u} \in L^2(\mathbb{R}^{n})\) 且

$$ \|\hat{u}\|_{L^2(\mathbb{R}^{n})} = \|\check{u}\|_{L^2(\mathbb{R}^{n})} = \|u\|_{L^2(\mathbb{R}^{n})} $$


## Fourier Transform 的性质

1 .

$$ \int_{\mathbb{R}^{n}} u\; \bar{v}\; dx = \int_{\mathbb{R}^{n}} \hat{u}\; \bar{\hat{v}}\; dy $$

2 .

$$ u = \mathcal{F}^{-1} \circ \mathcal{F} u = (\hat{u})\check\; $$

3 .

$$ (D^\alpha u)\hat\; = (iy)^\alpha \hat{u} $$


4 . 
设 \(u,v\in L^1(\mathbb{R}^{n})\cap L^2(\mathbb{R}^{n})\)，则

$$ (u*v)\hat\; = (2\pi)^{n/2} \hat{u}\hat{v}, \quad  $$


## Fractional Sobolev Space 分数阶Sobolev空间

设 \(0 < s < \infty\) ， \(u\in L^2(\mathbb{R}^{n})\).
那么当 \((1+|y|^s)\hat{u}\in L^2(\mathbb{R}^{n})\) 时， \(u\in H^s(\mathbb{R}^{n})\) ,并且令

$$ \|u\|_{H^s(\mathbb{R}^{n})} = \|(1+|y|^s)\hat{u}\|_{L^2(\mathbb{R}^{n})} = \left(\int_{\mathbb{R}^{n}} (1+|y|^s)^2\hat{u}^{2}dy\right)^{1/2} $$



## Problems

!!! question "20"

    若 \(u\in H^s(\mathbb{R}^{n})\)，且 \(s > n/2\)，则 \(u\in L^\infty(\mathbb{R}^{n})\)，且

    $$ \|u\|_{L^\infty(\mathbb{R}^{n})} \leq C(s,n) \|u\|_{H^s(\mathbb{R}^{n})} $$

!!! remark

    回忆 [Morry 不等式](./SobolevInequalities2.md#morrey) 以及 [广义 Sobolev 不等式](./SobolevInequalities2.md#general-sobolev-inequalities-sobolev) 

    我们知道，对于 \(k>n/p\)，

    $$ W^{k,p}(\mathbb{R}^n) \subset W^{k-1,p^*}(\mathbb{R}^n) \subset \cdots \subset W^{k-l+1,p^{(l-1)}}(\mathbb{R}^n) \subset C^{k-l-1, \gamma}(\mathbb{R}^n) \subset L^\infty(\mathbb{R}^n) $$

    这里我们用 Fourier 变换来证明相似的结果。

由 [性质](./Fourier.md#fourier-transform) \(u = (\hat{u})\check\;\),

$$ \begin{aligned}
    |u(x)| &= \frac{1}{(2\pi)^{n/2}} \Big|\int_{\mathbb{R}^n} e^{iy \cdot x} \hat{u}(y) dy\Big|  \\
    &= C(n) \Big|\int_{\mathbb{R}^n} \frac{e^{-iy \cdot x}}{1+|y|^s} (1+|y|^s)\hat{u}(y) dy\Big|  \\
    &\le C(n)\|(1+|y|^s)\hat{u}(y)\|_{L^2(\mathbb{R}^n)}\left(\int_{\mathbb{R}^n} \left(\frac{|e^{-iy \cdot x}|}{1+|y|^s}\right)^2 dy \right)^{\frac{1}{2}} \\
\end{aligned} $$


但是

$$ \begin{aligned}
    \int_{\mathbb{R}^n}\left(\frac{|e^{-iy \cdot x}|}{1+|y|^s}\right)^2 dy 
    &\le \int_{\mathbb{R}^n}\frac{1}{1+|y|^{2s}} dy     \\
    &= n\alpha(n)\int_{0}^{\infty} \frac{r^{n-1}}{1+r^{2s}}  dr \\ 
    &= \alpha(n) \int_{0}^{\infty} \frac{1}{1+t^{2s/n}}  dt  \quad (t=r^n)
\end{aligned}$$

由于 \(2s > n\) 因此 

$$ \int_{0}^{\infty} \frac{1}{1+t^{2s/n}}  dt < 1 + \int_1^\infty \frac{1}{t^{2s/n}} dt = 1 - \frac{1}{1-2s/n} < \infty $$

所以

$$ \|u(x)\|_{L^\infty(\mathbb{R}^n)} \le C(s, n)\|u\|_{H^s(\mathbb{R}^n)} $$







