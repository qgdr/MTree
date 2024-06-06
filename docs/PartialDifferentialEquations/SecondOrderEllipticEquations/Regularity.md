# Regularity 正则性


## Problems

!!! question "7"

    令具有紧支集的 \(u\in H^1(\mathbb{R}^n)\) 是半线性方程

    $$ -\Delta u + c(u) = f $$

    的弱解，其中 \(f\in L^2(\mathbb{R}^n)\)，\(c:R\to R\) 是光滑函数，
    且 \(c(0)=0, c'(0)\ge 0\). 并且假设 \(c(u)\in L^2(\mathbb{R}^n)\)

    证明 \(u\in H^2(\mathbb{R}^n)\). 以及

    $$ \|D^2 u\|_{L^2} \le C \|f\|_{L^2}  $$


**proof**

\(u\in H^1(\mathbb{R}^n)\) 是方程弱解，则满足

$$ \int_{\mathbb{R}^n} Du \cdot Dv + c(u) v \; dx = \int_{\mathbb{R}^n} fv\; dx \quad \forall v \in H^1(\mathbb{R}^n) $$

且 \(\text{supp}(u)\) 有界。

现在，对于某个 \(k\in \{1, ..., n\}\)，令

$$ v \triangleq -D_k^{-h}(D_k^h u) $$

带入弱解条件，有

$$ \int_{\mathbb{R}^n} -Du \cdot DD_k^{-h}D_k^h u - c(u) D_k^{-h}D_k^h u \; dx = \int_{\mathbb{R}^n} -f D_k^{-h}D_k^h u\; dx  $$

由差分的 分部积分 公式，我们得到

$$ \begin{aligned}
    - \int_{\mathbb{R}^n} Du \cdot DD_k^{-h}D_k^h u 
    &= \int_{\mathbb{R}^n} -Du \cdot D_k^{-h}D_k^h Du       \\
    &= \int_{\mathbb{R}^n} D_k^h Du \cdot D_k^h Du  \\
    &= \int_{\mathbb{R}^n} |D_k^h Du|^2 
\end{aligned} $$

以及

$$ \begin{aligned}
    - \int_{\mathbb{R}^n} c(u) D_k^{-h}D_k^h u 
    &= \int_{\mathbb{R}^n} D_k^{h}c(u) \; D_k^h u       \\
    &= \int_{\mathbb{R}^n} c'(\xi_u) D_k^h u \; D_k^h u  \\
    & \ge 0
\end{aligned} $$

得到

$$ \begin{aligned}
    \int_{\mathbb{R}^n} |D_k^h Du|^2 &\le -\int_{\mathbb{R}^n} f D_k^{-h}D_k^h u\; dx   \\
    &\le \epsilon \int_{\mathbb{R}^n} |D_k^{-h} D_k^h u|^2 + \frac{1}{4\epsilon} \int_{\mathbb{R}^n} f^2
\end{aligned} $$

但是在 [差商与弱导数](../SobolevSpaces/Difference.md#dhu-du) 中我们得到

$$ \|D_k^{-h}(D_k^h u)\|_{L^2} \le C \| D(D_k^h u)\|_{L^2} = C \| D_k^h Du\|_{L^2} $$

其中常数 \(C=C(n)\) 与 \(u\) 的选取无关。

所以，我们有

$$ \begin{aligned}
    \int_{\mathbb{R}^n} |D_k^h Du|^2 
    & \le \epsilon \int_{\mathbb{R}^n} |D_k^{-h} D_k^h u|^2 + \frac{1}{4\epsilon} \int_{\mathbb{R}^n} f^2 \\
    & \le \epsilon C \|D_k^h Du\|_{L^2}^2 + \frac{1}{4\epsilon} \|f\|_{L^2}^2
\end{aligned} $$

选择 \(\epsilon\) 足够小，\(\epsilon C = \frac{1}{2}\)，则有

$$ \|D_k^h Du\|_{L^2}^2 \le C \|f\|_{L^2}^2 $$

再次由 [差商与弱导数](../SobolevSpaces/Difference.md#dhu-du) ，我们知道

$$ Du \in H^1(\mathbb{R}^n), \quad  \| D^2 u\|_{L^2}^2 \le C \|f\|_{L^2}^2 $$


证毕。
