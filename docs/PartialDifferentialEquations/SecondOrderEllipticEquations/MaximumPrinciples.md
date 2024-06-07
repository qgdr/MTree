# Maximum Principles 极大值原理




## Problems

!!! question "8"
    <font size="3">

    设 \(U\) 是有界开集，\(\partial U\) 光滑。令 \(u\) 是一致椭圆方程

    $$ Lu = -\sum_{i, j=1}^n a^{ij}(x) \partial_j \partial_i u = 0 \text{  in  } U $$

    的光滑解。
    假设 \(a^{ij}\) 的导数有界。

    令 \(v \triangleq |Du|^2+\lambda u^2\)，证明如果 \(\lambda\) 足够大，则

    $$ Lv \le 0 \text{  in  }  U $$

    并得到

    $$ \|Du\|_{L^\infty(U)} \le C( \|Du\|_{L^\infty(\partial U)} + \|u\|_{L^\infty(\partial U)} ) $$
    
    </font>


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

那么应用 弱极大值原理，我们有

$$ \max_{\bar{U}} |Du|^2 \le \max_{\bar{U}} v \le \max_{\partial U} v \le \max_{\partial U} |Du|^2 + \max_{\partial U} \lambda |u|^2 \le C(n, A)(\max_{\partial U} |Du| + \max_{\partial U} |u|)^2 $$

因此

$$ \max_{\bar{U}} |Du| \le C(\max_{\partial U} |Du| + \max_{\partial U} |u|) $$




!!! question "9"

    <font size="3">

    设 \(U\) 是有界开集，\(\partial U\) 光滑。
    假设 \(u\) 是一致椭圆方程

    $$ \begin{cases}
        Lu = -\sum_{i, j=1}^n a^{ij}(x) \partial_j \partial_i u = f  & \text{  in  } U  \\
        u = 0 & \text{  on  } \partial U \\
    \end{cases} $$

    的光滑解，\(f\) 有界。      
    固定 \(x^0\in \partial U\)，定义在 \(x^0\) 处的 **势垒 barrier** 为一个 \(C^2\) 函数 \(w\)，满足

    $$ Lw \ge 1 \text{  in  } U ,\quad  w(x^0) = 0,\quad w \ge 0 \text{  on  } \partial U  $$

    证明如果 \(w\) 是 \(x^0\) 处的势垒，则存在一个常数 \(C\) 使得

    $$ |Du(x^0)| \le C \Big| \frac{\partial w}{\partial \nu}(x^0) \Big| $$

    </font>



**proof**

根据 弱极大值原理，以及 \(w \ge 0 \text{  on  } \partial U \) ，我们有

$$ \min_{\bar{U}} w = \min_{\partial U} w = w(x^0) = 0 $$

令 \(v = u - \|f\|_{L^\infty(U)} w\)，那么我们有

$$ \begin{cases}
    Lv = Lu - \|f\|_{L^\infty(U)} L w \le f - \|f\|_{L^\infty(U)} 1 \le 0   & \text{ in  } U    \\
    v \le 0   & \text{  on  } \partial U
\end{cases} $$

那么再次使用 弱极大值原理，我们有

$$ \max_{\bar{U}} v = \max_{\partial U} v = v(x^0) = 0 $$

因此，有

$$ 0 \le \frac{\partial v}{\partial \nu}(x^0) = \frac{\partial u}{\partial \nu}(x^0) - \|f\|_{L^\infty(U)}\frac{\partial w}{\partial \nu}(x^0)  $$

即

$$ \frac{\partial u}{\partial \nu}(x^0) \ge \|f\|_{L^\infty(U)}\frac{\partial w}{\partial \nu}(x^0) $$

同理，令 \(v = u + \|f\|_{L^\infty(U)} w\)，我们可以得到

$$ \frac{\partial u}{\partial \nu}(x^0) \le -\|f\|_{L^\infty(U)}\frac{\partial w}{\partial \nu}(x^0) $$


又因为 \(u=0 \text{  on  } \partial U \)，边界光滑，因此 \(Du(x^0) = \dfrac{\partial u}{\partial \nu}(x^0) \)，我们得到

$$ |Du(x^0)| \le \|f\|_{L^\infty(U)} \Big| \frac{\partial w}{\partial \nu}(x^0) \Big| $$



!!! question "10"

    <font size="3">

    假设 \(U\) 是连通有界开集，\(\partial U\) 光滑。        
    证明 Neumann 边界条件的 调和方程

    $$ \begin{cases}
        -\Delta u = 0 & \text{  in  } U  \\
        \frac{\partial u}{\partial \nu} = 0 & \text{  on  } \partial U \\
    \end{cases} $$

    的光滑解只有一种 \(u \equiv C\)，\(C\) 是某个常数。

    </font>


**proof**

(a)

由于 \(-\Delta u = 0\)，对于任意的 \(\forall v \in C^\infty(U)\)，我们有

$$ \begin{aligned}
    0 &= -\int_U \Delta u \; v\;dx  \\
    &= -\int_{\partial U} \frac{\partial u}{\partial \nu} v \; dS + \int_U \nabla u \cdot \nabla v \; dx \quad (\text{by Green formula}) \\
    &= \int_U \nabla u \cdot \nabla v \; dx \qquad \qquad\qquad (\frac{\partial u}{\partial \nu} = 0 \text{  on  } \partial U) \\
\end{aligned} $$

令 \(v=u\)，则有

$$ \int_U |\nabla u|^2 \; dx = 0  \Rightarrow \nabla u = 0 \text{  in  } U $$

且 \(U\) 连通，因此，\(u \equiv C\).


(b)

因为 \(-\Delta u = 0\)，
由 强极大值原理，要么最大值点在 \(U\) 内部取得，则 \(u \equiv C\)；     
要么最大值只能在边界取得 \(x^0\in \partial U\)，\(u(x^0)>u(x) \forall x \in U\)，
则由 Hopf 引理，我们得到 

$$ \frac{\partial u}{\partial \nu}(x^0) > 0 $$

矛盾。

所以只能是 \(u \equiv C\)。



!!! question "11"











