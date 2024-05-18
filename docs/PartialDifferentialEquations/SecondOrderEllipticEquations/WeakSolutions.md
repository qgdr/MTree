# Weak Solutions 弱解

我们先研究散度形式的解。

设 \(U\) 是 \(\mathbb{R}^n\) 中的 **有界开集** ，\(u: \bar{U} \to \mathbb{R}\) 是未知函数。
这里 \(f:U \to \mathbb{R}\) 是给定函数。
我们研究边值问题。

$$ \begin{cases}
    Lu=f & \text{in } U \\
    u=0 & \text{on } \partial U
\end{cases} $$

其中 \(L\) 代表偏微分算子，具有下面的 **散度形式 divergence form** 。

$$ Lu = -\sum_{i,j=1}^n \partial_j(a^{ij}(x)\partial_i u) + \sum_{i=1}^n b^i(x) \partial_i u + c(x) u $$

且 \(L\) 是满足对称性条件 \(a^{ij}(x) = a^{ji}(x)\) 和 [一致椭圆条件](./index.md#uniformly-elliptic) 

$$ \sum_{i,j=1}^n a^{ij}(x) \xi_i\xi_j \ge \theta |\xi|^2 \quad \text{for a.e.} x \in U, \forall \xi \in \mathbb{R}^n $$

我们下面将假设

\(a^{ij}, b^i, c \in L^\infty(U) \quad (i,j=1,2,...,n)\) 以及 \(f\in L^2(U))

## Motivation 动机

方程两边对一个测试函数 \(v\in C_c^\infty(U)\) 做内积

$$ \begin{aligned}
    \int_U fv dx &= \int_U-\sum_{i,j=1}^n \partial_j(a^{ij}(x)\partial_i u) v + \sum_{i=1}^n b^i(x) \partial_i u v + c(x) u v \; dx \\
    &= \int_U \sum_{i,j=1}^n a^{ij}(x)\partial_i v\partial_j v + \sum_{i=1}^n b^i(x)\partial_i v + c(x)v\\
\end{aligned} $$

第二个等式使用了分部积分 (Gauss-Green 公式) 。由于在 \(\partial U\) 上 \(v = 0\)，所以没有边界项。      
根据逼近定理我们可以将 \(v\) 的空间替换成 \(v\in H^1_0(U)\)，那么最后的恒等式只有当 \(u\in H^1_0(U)\) 时才有意义。 
而当 \(u\in H^1_0(U)\) 时，有 \(u=0 \text{  on  } \partial U\).


## Definations 定义

### Bilinear Form 双线性形式

关于散度形式的椭圆算子，我们定义 **双线性形式** \(B[\;,\;]\)为

$$ B[u,v] := \int_U \sum_{i,j=1}^n a^{ij} \partial_i u\partial_j v + \sum_{i=1}^n b^i\partial_i u + c u v \; dx $$

其中 \(u,v\in H^1_0(U)\).


### Weak Solution 弱解

如果 \(u\in H^1_0(U)\) 满足

$$ B[u,v] = (f, v) \triangleq \int_U fv \; dx \quad \forall v\in H_0^1(U) $$

我们称 \(u\) 是边值问题的一个 **弱解**。        
等式有时称为边值问题的 **变分形式 variational formulation** 。

------

下面我们研究弱解的存在性。

## Lax-Milgram Theorem 拉西-米格朗定理

设 \(H\) 是一个 Hilbert 空间，

$$ B: H \times H \to \mathbb{R} $$

是一个 **双线性映射 bilinear mapping** ，且存在常数 \(\alpha, \beta > 0\) 使得

$$ |B[u,v]| \le \alpha \|u\| \|v\| \quad \forall u,v \in H $$

以及

$$ \beta \|u\|^2 \le B[u,u]  \quad \forall u \in H $$

最后令 \(f: H \to \mathbb{R}\) 是一个 \(H\) 上的有界线性泛函。

那么存在唯一的 \(u\in H\) 使得

$$ B[u,v] = (f,v) \quad \forall v \in H $$


















## Problems

!!! question "2"

    令

    $$ Lu = -\sum_{i,j=1}^n \partial_j(a^{ij}(x)\partial_i u) + c(x) u $$

    证明存在常数 \(\mu>0\) 使得在 \(c(x)\ge -\mu\) 的条件下，相应的 \(B[\;,\;]\) 满足 Lax-Milgram 定理的假设条件，
    即存在常数 \(\alpha, \beta > 0\) 使得对 \(u,v\in H_0^1(U)\) 满足

    $$ \begin{gather*}
        |B[u,v]| \le \alpha \|u\| \|v\| \\
        \beta \|u\|^2 \le B[u,u]
    \end{gather*} $$


**proof**

对于 \(u,v\in H_0^1(U)\)

**1**

$$ \begin{aligned}
    |B[u,v]| &\le \|a^{ij}\|_{L^\infty} \int_U \sum_{i,j=1}^n |\partial_i u| \; |\partial_j v| + \|c\|_{L^2} \int_U |u||v| \; dx \\
    &\le C(n, a^{ij}, c) \left(\sum_{i=1}^n  \|D_i u\|_{L^2} \sum_{i=1}^n  \|D_i v\|_{L^2} + \|u\|_{L^2} \|v\|_{L^2} \right)  \quad \text{by Hölder}\\
    &\le C(n, a^{ij}, c) \left(\sum_{i=1}^n  \|D_i u\|_{L^2}  + \|u\|_{L^2} \right)\left(\sum_{i=1}^n  \|D_i u\|_{L^2}  + \|u\|_{L^2} \right)       \\
    &\le C(n, a^{ij}, c) \|u\|_{H_0^1} \|v\|_{H_0^1}
\end{aligned} $$


**2**


由一致椭圆性条件

$$ \begin{aligned}
    B[u,u] &= \int_U \sum_{i,j=1}^n a^{ij}(x)\partial_i u\partial_j u + c(x) u^2 \; dx\\
    &\ge \theta \|Du\|_{L^2}^2 + \int_U c(x) u^2 dx \\
\end{aligned} $$

我们知道

$$ \|u\|_{H_0^1}^2 = \|u\|_{L^2}^2 + \|Du\|_{L^2}^2  $$

以及 [Poincaré 不等式](../SobolevSpaces/SobolevInequalities.md#w_01-pu) Corrollary ：    
\(U\) 是有界开集，则

$$ \|u\|_{L^2(U)} \le C'(U)\|Du\|_{L^2(U)} $$

我们可以得到

$$ \begin{aligned}
    B[u,u] &\ge \theta \|Du\|_{L^2}^2 - \mu \|u\|_{L^2}^2 \\
    &= \beta\|u\|_{H_0^1}^2 + (\theta-\beta) \|Du\|_{L^2}^2 - (\mu+\beta) \|u\|_{L^2}^2 \\
    &\ge \beta\|u\|_{H_0^1}^2 + (\theta-\beta - (C'(U))^2(\mu+\beta)) \|Du\|_{L^2}^2
\end{aligned} $$

我们令  \(\mu=\beta=\dfrac{\theta}{ 1+ 2(C'(U))^2}\) 即可得到 \(B[u,u] \ge \beta\|u\|_{H_0^1}^2\)

总结可得 Lax-Milgram 定理的假设条件。





!!! question "3"




