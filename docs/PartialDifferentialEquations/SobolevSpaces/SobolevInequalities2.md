# Sobolev 不等式 $\mathbf{II}$



## Morrey 不等式

!!! Theorem

    <font size="4">

    对于 \(n<p\le\infty\)，有

    $$ \begin{gather*}
        \|u\|_{C^{0, 1-\frac{n}{p}}(R^n)} \le C(n,p)\|u\|_{W^{1,p}(R^n)}    \\
        \text{i.e.} \quad 
        W^{1,p}(R^n) \subset  C^{0, \gamma}(R^n), \quad \gamma = 1-\frac{n}{p}
    \end{gather*} $$

    </font>


### 有界开集的情形

!!! Theorem

    <font size="3">

    设 \(U\subset R^n\) 是有界开集，且 <font color="Red"> \(\partial U\) 是 \(C^1\) 的 </font>
    那么对于 \(n<p\le\infty\)，有

    $$ \begin{gather*}
        \|u\|_{C^{0, 1-\frac{n}{p}}(R^n)} \le C(n,p, U)\|u\|_{W^{1,p}(R^n)}    \\
        \text{i.e.} \quad 
        W^{1,p}(U) \subset  C^{0, \gamma}(U), \quad \gamma = 1-\frac{n}{p}
    \end{gather*} $$

    </font>



我们先看一个反例

!!! Example

    我们用极坐标表示 \(x = \rho \cos \theta, y = \rho \sin \theta, \rho \in (0, 1), \theta \in (0, 2\pi)\)，        
    则 \(U = B(0,1)\setminus \{y=0\}\)

    $$ u(x, y) = \rho^2(\theta - \pi) $$

    ![counterexample](media/videos/Sobolev2/720p30/Counterexample_ManimCE_v0.18.0.gif)

    他在 \(U\) 上可微且 \(Du\) 有界，即 \(u\in W^{1,\infty}(U)\)，但是显然不属于 \(C^{0, \gamma}(U)\)，        
    因为在 \(y=0\) 的上下两侧 \(|u(1/2, \epsilon) - u(1/2, -\epsilon)| > C > 0\)，但是 \(|(1/2, \epsilon) - (1/2, -\epsilon)|^\gamma \to 0 \text{  as  } \epsilon \to 0\)



## General Sobolev inequalities 广义 Sobolev 不等式


