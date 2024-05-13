# Hardy Inequality

## Discrete Hardy Inequality 离散 哈代 不等式

在数学分析中我们知道 如果 \(\lim_{n\to\infty} a_n=a\)，那么序列的 **Cesàro summation** 切萨罗求和(平均) 

$$ \sigma_n \triangleq \frac{1}{n}\sum_{k=1}^n a_k , \quad \lim_{n\to\infty} \sigma_n = a $$

在研究该级数收敛性时，得到对于 \(p>1\)

$$ \|\sigma\|_p \le \frac{p}{p-1}\|a\|_p $$

即（为了简单，这里令 \(t^p=|t|^p\)）

$$ \sum_{n=1}^\infty \sigma_n^p \le \left(\frac{p}{p-1}\right)^p \sum_{n=1}^\infty a_n^p $$

**证明**

$$ \begin{aligned}
    \sigma_n^p - \frac{p}{p-1} \sigma_n^{p-1}a_n 
    &= \sigma_n^p(1-\frac{np}{p-1}) + \frac{(n-1)p}{p-1} \sigma_n^{p-1} \sigma_{n-1} \\ 
    &\le  \sigma_n^p(1-\frac{np}{p-1}) + \frac{(n-1)p}{p-1} \left( \frac{p-1}{p} \sigma_n^p + \frac{1}{p} \sigma_{n-1}^p \right) \\
    &= \sigma_n^p(n-\frac{np}{p-1}) + \frac{n-1}{p-1}\sigma_{n-1}^p \\
    &= \frac{1}{p-1} \left( (n-1)\sigma_{n-1}^p - n\sigma_n^p \right)
\end{aligned} $$

求和得到

$$ \begin{aligned}
    \sum_{n=1}^N \sigma_n^p - \frac{p}{p-1} \sum_{n=1}^N \sigma_n^{p-1} a_n \le -\frac{1}{p-1}Nb_N^p \le 0 
\end{aligned} $$

那么

$$ \begin{aligned}
    \sum_{n=1}^N \sigma_n^p &\le \frac{p}{p-1} \sum_{n=1}^N \sigma_n^{p-1} a_n \\
    &\le   \frac{p}{p-1} \left(\sum_{n=1}^N \sigma_n^{p}\right)^{\frac{p-1}{p}} \left( \sum_{n=1}^N a_n^p \right)^{\frac{1}{p}} \\
\end{aligned} $$

因此

$$ \sum_{n=1}^\infty \sigma_n^p \le \left(\frac{p}{p-1}\right)^p \sum_{n=1}^\infty a_n^p $$



## Integral Hardy Inequality 积分 哈代 不等式


令 

$$ F(x) = \frac{1}{x}\int_0^x f(t)dt $$

对于 \(p>1\) ，我们有

$$ \|F\|_p \le \frac{p}{p-1} \|f\|_p $$

即

$$ \int_0^\infty \Big|\frac{1}{x}\int_0^x f(t)dt \Big|^p dx \le \left(\frac{p}{p-1}\right)^p \int_0^\infty |f(t)|^p dt  $$

**证明 1**

$$ \begin{aligned}
    F^p(x) - \frac{p}{p-1} F^{p-1}(x)f(x) 
    &= F^p(x) - \frac{p}{p-1} F^{p-1}(x)(xF(x))' \\
    &= F^p(x) - \frac{p}{p-1}F^p(x) - \frac{p}{p-1}x F^{p-1}(x)F'(x)       \\
    &= -\frac{1}{p-1} (xF^p(x))' \\ 
\end{aligned} $$

那么

$$ \begin{aligned}
    \int_0^\infty |F(x)|^p dx 
    &\le \frac{p}{p-1} \int_0^\infty F^{p-1}(x)f(x) -\frac{1}{p-1} xF^p(x) \Big|_0^A    \\
    &\le \frac{p}{p-1} \int_0^\infty F^{p-1}(x)f(x) \\
    &\le \frac{p}{p-1} \left(\int_0^\infty |F(x)|^p dx\right)^{\frac{p-1}{p}}\left(\int_0^\infty |f(x)|^p dx\right)^{\frac{1}{p}} \\
\end{aligned} $$

因此

$$ \|F\|_p \le \left(\frac{p}{p-1}\right)^p \|f\|_p $$



**证明 2**

$$ \begin{aligned}
    \|F\|_p &= \left( \int_0^\infty \Big|\int_0^1 f(xt) dt \Big|^p dx \right)^{\frac{1}{p}} \\
    &\le \int_0^1 \left( \int_0^\infty |f(xt)|^p dx \right)^{\frac{1}{p}} dt \qquad \text{Minkovski's Inequality} \\
    &= \int_0^1 \left( \frac{1}{t}\int_0^\infty |f(y)|^p dt \right)^{\frac{1}{p}} dt \\
    &= \|f\|_p  \int_0^1 t^{-1/p} dt  = \frac{p}{p-1}\|f\|_p
\end{aligned} $$




## 高维 Hardy 不等式

[Evans PDE 5.8 Thoorem 8](../index.md#lawrence-cevans-partial-differential-equations)

设 \(n \ge 3\)，设 \(u\in H^1(\Omega)\) 。
那么对于 \(r>0\) 使得 \(B(0,r)\subseteq \Omega\)，有 \(\dfrac{u}{|x|} \in L^2(B(0,r))\) 且

$$ \int_{B(0,r)} \frac{u^2}{|x|^2}  dx \le C(n) \int_{B(0,r)} |Du|^2 + \frac{u^2}{r^2} dx $$

**证明**

（实际上我还没有更好的理解，只能使用教材中的方法）

由于 

$$ D(|x|) = \frac{x}{|x|}, \quad D(\frac{1}{|x|}) = -\frac{x}{|x|^3} $$

所以我们可以将左边表示为

$$ \begin{aligned}
    \int_{B(0,r)} \frac{u^2}{|x|^2} dx &= -\int_{B(0,r)} u^2 D(\frac{1}{|x|}) \cdot D(|x|) dx \\
\end{aligned} $$

注意到，由 [Gauss-Green 公式]()

$$ \begin{aligned}
    \int_{\partial B(0,r)} u^2 \frac{1}{|x|} D(|x|) \cdot \nu dS
    =& \int_{B(0,r)} D(u^2 \frac{1}{|x|}) \cdot D(|x|) dx + \int_{B(0,r)} u^2 \frac{1}{|x|} \Delta(|x|) dx \\
    =& \int_{B(0,r)} u^2 D(\frac{1}{|x|}) \cdot D(|x|) dx       \\
    &+\int_{B(0,r)} 2uDu \cdot \frac{x}{|x|^2} dx + \int_{B(0,r)} (n-1) \frac{u^2}{|x|^2} dx    \\
    =& (n-2)\int_{B(0,r)} \frac{u^2}{|x|^2} dx + \int_{B(0,r)} 2uDu \cdot \frac{x}{|x|^2} dx
\end{aligned} $$

因此

$$ \begin{aligned}
    (n-2) \int_{B(0,r)} \frac{u^2}{|x|^2} dx 
    &= -\int_{B(0,r)} 2uDu \cdot \frac{x}{|x|^2} dx + \int_{\partial B(0,r)} u^2 \frac{x}{|x|^2} \cdot \nu dS   \\
    &= -\int_{B(0,r)} 2uDu \cdot \frac{x}{|x|^2} dx + \int_{\partial B(0,r)} u^2 \frac{1}{r} dS \\
    &\le \int_{B(0,r)} \lambda|Du|^2 + \frac{1}{\lambda}\frac{u^2}{|x|^2} dx + \int_{\partial B(0,r)} u^2 \frac{1}{r} dS 
\end{aligned} $$

又注意到

$$ \begin{aligned}
    r\int_{\partial B(0,r)} u^2 dS &= \int_{\partial B(0,r)} u^2 x \cdot \nu dS 
        = \int_{B(0,r)} \text{div}(u^2x) dx \\
    &= \int_{B(0,r)} nu^2 + 2uDu \cdot x dx \\
    &\le \int_{B(0,r)} nu^2 + \frac{1}{\mu} |x|^2|Du|^2 + \mu u^2 dx    \\
    &\le \int_{B(0,r)} \frac{1}{\mu} r^2|Du|^2 + (n+\mu) u^2 dx 
\end{aligned} $$

我们得到

$$ \begin{aligned}
    \frac{1}{r} \int_{\partial B(0,r)} u^2 dS \le \int_{B(0,r)} \frac{1}{\mu}|Du|^2 + \frac{n+\mu }{r^2}u^2 dx 
\end{aligned} $$


所以，我们有

$$ \begin{aligned}
    (n-2-\frac{1}{\lambda}) \int_{B(0,r)} \frac{u^2}{|x|^2} dx 
    &\le \int_{B(0,r)} (\lambda+ \frac{1}{\mu})|Du|^2 +  \frac{n+\mu }{r^2}u^2 dx  \\
\end{aligned} $$

即

$$ \int_{B(0,r)} \frac{u^2}{|x|^2} dx \le C(n) \int_{B(0,r)} |Du|^2 + \frac{u^2}{r^2} dx $$


!!! Corollary

    若 \(n\ge 3\) ，对于 \(u\in H^1(R^n)\)，令 \(r\to \infty\)，那么

    $$ \int_{B(0,r)} \frac{u^2}{r^2} dx \le \frac{1}{r^2} \int_{R^n} u^2 dx = \frac{1}{r^2} \|u\|_{L^2(R^n)}^2 \to 0 $$

    但是

    $$ \int_{B(0,r)} \frac{u^2}{r^2} dx \to \int_{R^n} \frac{u^2}{|x|^2} dx ,\qquad 
    \int_{B(0,r)} |Du|^2 \to \int_{R^n} |Du|^2 $$

    所以

    $$ \int_{R^n} \frac{u^2}{|x|^2} dx \le C(n) \int_{R^n} |Du|^2 $$

    我们给出一个具体的 \(C\)，取 \(\lambda=\dfrac{2}{n-2}, \mu \to \infty\)，\(C(n)=\lambda(n-2-\frac{1}{\lambda})^{-1}=\dfrac{4}{(n-2)^2}\)


