# Maximum Principles 极大值原理




## Problems

!!! question "8"

    设 \(U\) 是有界开集，\(\partial U\) 光滑。令 \(u\) 是一致椭圆方程

    $$ Lu = -\sum_{i, j=1}^n a^{ij}(x) \partial_j \partial_i u = 0 \text{  in  } U $$

    的光滑解。
    假设 \(a^{ij}\) 的导数有界。

    令 \(v \triangleq |Du|^2+\lambda u^2\)，证明如果 \(\lambda\) 足够大，则

    $$ Lv \le 0 \text{  in  }  U $$

    并得到

    $$ \|Du\|_{L^\infty(U)} \le C( \|Du\|_{L^\infty(\partial U)} + \|u\|_{L^\infty(\partial U)} ) $$


**proof**

由于 \(Lu = 0\)，则

$$ \begin{aligned}
    0 = -\nabla (Lu) = \sum_{i,j=1}^n \nabla a^{ij} \; \partial_j \partial_i u + a^{ij}  \partial_j \partial_i \nabla u \\
\end{aligned} $$

对于

$$ v = \nabla u \cdot \nabla u + \lambda u^2 $$

考虑

$$ \begin{aligned}
    Lv  &= - \sum_{i,j=1}^n a^{ij} \partial_j \partial_i (\nabla u \cdot \nabla u) 
        - \lambda \sum_{i,j=1}^n a^{ij} \partial_j \partial_i u^2 \\
    &= -2 \sum_{i,j=1}^n a^{ij} (\partial_j \nabla u \cdot \partial_i \nabla u + \nabla u \cdot \partial_j \partial_i \nabla u)
        - 2 \lambda \sum_{i,j=1}^n a^{ij} (\partial_j u \; \partial_i u + u \; \partial_j \partial_i u) \\
    &= -2 \sum_{i,j=1}^n a^{ij} \partial_j \nabla u \cdot \partial_i \nabla u + 2 \sum_{i,j=1}^n \nabla u \cdot \nabla a^{ij} \; \partial_j \partial_i u
        - 2 \lambda (\nabla u)^T A \nabla u + 2\lambda u Lu \\ 
\end{aligned} $$


<!-- $$ \begin{aligned}
    Lv  &= -\sum_{k=1}^n \sum_{i,j=1}^n a^{ij} \partial_j \partial_i (\partial_k u)^2 
        - \lambda \sum_{i,j=1}^n a^{ij} \partial_j \partial_i u^2 \\
    &= -2 \sum_{k=1}^n \sum_{i,j=1}^n a^{ij} (\partial_j \partial_k u \; \partial_i \partial_k u + \partial_k u \; \partial_j \partial_i \partial_k u)
        - 2 \lambda \sum_{i,j=1}^n a^{ij} (\partial_j u \; \partial_i u + u \; \partial_j \partial_i u) \\
\end{aligned} $$ -->

注意到，

1 . 由一致椭圆条件，

$$ \begin{aligned}
    \sum_{i,j=1}^n a^{ij} \partial_j \nabla u \cdot \partial_i \nabla u 
    &= \sum_{i=1}^k  \sum_{i,j=1}^n a^{ij} \partial_j (\partial_k u) \; \partial_i (\partial_k u)    \\
    &\ge  \sum_{i=1}^k \theta |\nabla \partial_k u|^2 = \theta | \nabla^2 u |^2 \\
\end{aligned}$$

2 .

$$ \begin{aligned}
    \sum_{i,j=1}^n \nabla u \cdot \nabla a^{ij} \; \partial_j \partial_i u 
    &\le \sum_{i,j=1}^n |\nabla a^{ij}| |\nabla u|  \; \partial_j \partial_i u \\
    &\le C(A) |\nabla u| \sum_{i,j=1}^n |\partial_j \partial_i u| \quad (a^{ij} \text{ has bounded derivatives})  \\
    &\le C(A) |\nabla u| \; n |\nabla^2 u| \quad (\text{by Hölder inequality})  \\
\end{aligned} $$

3 . 由一致椭圆条件

$$ (\nabla u)^T A \nabla u \ge \theta |\nabla u|^2 $$

4 . 

$$ uLu = 0 $$

因此，我们有


$$ \begin{aligned}
    Lv &\le -2 \theta |\nabla^2 u|^2 + 2 C(n,A) |\nabla u|\;|\nabla^2 u| - 2 \lambda \theta |\nabla u|^2 \\
    &\le C(n,A)(\epsilon |\nabla^2 u|^2 + \frac{1}{\epsilon} |\nabla u|^2) - 2\theta |\nabla^2 u|^2 - 2\lambda \theta |\nabla u|^2 \\
    &= (\epsilon C(n,A) - 2\theta) |\nabla^2 u|^2 + (\frac{C(n,A)}{\epsilon} - 2\lambda \theta) |\nabla u|^2 \\
\end{aligned} $$

我们可以令 \(2\theta = \epsilon C(n,A)\)，那么我们有

$$ Lv \le (\frac{C^2}{2\theta} - 2\lambda \theta)|\nabla u|^2 $$

则只要 \(\lambda > \frac{C^2}{4\theta^2}\)，就有 \(Lv \le 0\).

那么应用极大值原理，我们有

$$ \max_{U} |Du|^2 \le \max_{U} v \le \max_{\partial U} v \le \max_{\partial U} |Du|^2 + \max_{\partial U} \lambda |u|^2 \le C(n, A)(\max_{\partial U} |Du| + \max_{\partial U} |u|)^2 $$

因此

$$ \max_{U} |Du| \le C(\max_{\partial U} |Du| + \max_{\partial U} |u|) $$









