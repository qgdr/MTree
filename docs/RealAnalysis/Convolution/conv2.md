# Convolution 2 卷积 2

在认识了 \(L^p\) 空间后，我们进一步认识一下卷积

## 连续性

对于 \(1\le p < \infty\)，如果 \(f\in L^p(\mathbb{R}^n), g\in L^{p'}(\mathbb{R}^n)\)，则 \(f*g\in C(\mathbb{R}^n)\)

**proof**

$$ \begin{aligned}
    f*g(x)-f*g(y) &= \int_{\mathbb{R}^n} (f(x-t)-f(y-t))g(t)dt \\
    &\le \|f-\tau_{y-x}f\|_{L^{p}(\mathbb{R}^n)}\|g\|_{L^{p'}(\mathbb{R}^n)}   \\
\end{aligned} $$

其中  \(\tau_{y-x}f(t) = f(t+y-x)\)， \(\tau\) 称为平移算子。

当 \(y-x\to 0\) 时， \(\|f-\tau_{y-x}f\|_{L^{p}(\mathbb{R}^n)} \to 0\)，        
因此 \(f*g(x)-f*g(y) \to 0\)，那么 \(f*g\in C(\mathbb{R}^n)\)。

我们简要说明为何 \(\|f-\tau_{y-x}f\|_{L^{p}(\mathbb{R}^n)} \to 0\)。
这是因为 \(C_c^\infty(\mathbb{R}^n)\) 在 \(L^p(\mathbb{R}^n)\) 中 **稠密**，    
因此对任意的 \(\forall \epsilon>0\) ， 我们可以找到 \(\phi\in C_c^\infty(\mathbb{R}^n)\) 使得 \(\|f-\phi\|_{L^{p}(\mathbb{R}^n)} < \epsilon\).
那么，

$$ \begin{aligned} \|f-\tau_{y-x}f\|_{L^{p}(\mathbb{R}^n)} 
&\le \|f-\phi\|_{L^{p}(\mathbb{R}^n)} + \|\tau_{y-x}\phi-\tau_{y-x}f\|_{L^{p}(\mathbb{R}^n)} + \|\phi-\tau_{y-x}\phi\|_{L^{p}(\mathbb{R}^n)}        \\
&= 2\|f-\phi\|_{L^{p}(\mathbb{R}^n)} + \|\phi-\tau_{y-x}\phi\|_{L^{p}(\mathbb{R}^n)}        \\
&< 2\epsilon +  \|\|\phi'\|_{L^\infty}(y-x)\|_{L^{p}(\mathbb{R}^n)}       \\
% &< 2\epsilon + \left( \int_{\mathbb{R}^n} \|\phi'(t)\|_{L^\infty}^p dt \right)^{\frac{1}{p}}        \\
&= 2\epsilon +  \|\phi'\|_{L^\infty}|y-x|\mu(\text{supp}(\phi)+B(0,y-x))       \\
&\to 2\epsilon \quad \text{ as } y-x\to 0.
\end{aligned} $$

所以 \(\|f-\tau_{y-x}f\|_{L^{p}(\mathbb{R}^n)} \to 0\).



## Young 不等式

\(f\in L^1(\mathbb{R}^n), g\in L^p(\mathbb{R}^n), 1\le p < \infty\)，则

$$ \|f*g\|_{L^p(\mathbb{R}^n)} \le \|f\|_{L^1(\mathbb{R}^n)} \|g\|_{L^p(\mathbb{R}^n)} $$

**proof**

我们利用 [Minkowski 不等式](../Inequalities/index.md#minkowski) 4

记 \(G_x(y) := f(x)g(y-x)\)，则

$$ \begin{aligned}
    \|f*g\|_{L^p(\mathbb{R}^n)} &= \|\int_{\mathbb{R}^n} G_x(y) dx\|_{L^p} \\
    &\le \int_{\mathbb{R}^n}\| G_x(y) \|_{L^p} \; dx         \quad \text{ by Minkowski} \\
    &= \int_{\mathbb{R}^n} f(x)\|g\|_{L^p} \;dx \\
    &= \|f\|_{L^1} \|g\|_{L^p}
\end{aligned} $$




