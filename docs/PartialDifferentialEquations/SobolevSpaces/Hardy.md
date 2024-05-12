# Hardy Inequality

## Discrete Hardy Inequality 离散 哈代 不等式

在数学分析中我们知道 如果 \(\lim_{n\to\infty} a_n=a\)，那么序列的 **Cesàro summation** 切萨罗求和(平均) 

$$ \sigma_n \triangleq \frac{1}{n}\sum_{k=1}^n a_k , \quad \lim_{n\to\infty} \sigma_n = a $$

在研究该级数收敛性时，得到对于 \(p>1\)

$$ \|\sigma\|_p \le \frac{p}{p-1}\|a\|_p $$

即（为了简单，这里令 \(t^p=|t|^p\)）

$$ \sum_{n=1}^\infty \sigma_n^p \le \left(\frac{p}{p-1}\right)^p \sum_{n=1}^\infty a_n^p $$


## Integral Hardy Inequality 积分 哈代 不等式


令 

$$ F(x) = \frac{1}{x}\int_0^x f(t)dt $$

对于 \(p>1\) ，我们有

$$ \|F\|_p \le \frac{p}{p-1} \|f\|_p $$

即

$$ \int_0^\infty \Big|\frac{1}{x}\int_0^x f(t)dt \Big|^p dx \le \left(\frac{p}{p-1}\right)^p \int_0^\infty |f(t)|^p dt  $$


**证明**

$$ \begin{aligned}
    \|F\|_p &= \left( \int_0^\infty \Big|\int_0^1 f(xt) dt \Big|^p dx \right)^{\frac{1}{p}} \\
    &\le \int_0^1 \left( \int_0^\infty |f(xt)|^p dx \right)^{\frac{1}{p}} dt \qquad \text{Minkovski's Inequality} \\
    &= \int_0^1 \left( \frac{1}{t}\int_0^\infty |f(y)|^p dt \right)^{\frac{1}{p}} dt \\
    &= \|f\|_p  \int_0^1 t^{-1/p} dt  = \frac{p}{p-1}\|f\|_p
\end{aligned} $$



