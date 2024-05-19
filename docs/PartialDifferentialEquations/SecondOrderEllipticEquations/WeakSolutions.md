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

$$ B[u,v] = \langle f,v \rangle \quad \forall v \in H $$



















## Problems



!!! question "2"

    设 \(U\subset \mathbb{R}^n\) 是有界开集，\(\partial U\) 光滑，
    \(a^{ij}, b^i, c \in L^\infty(U)\) 光滑，且 \(L\) 一致椭圆。
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

    设 \(U\subset \mathbb{R}^n\) 有界开集，
    对于 **双调和方程 biharmonic equation** 的如下边值问题：

    $$ \begin{cases}
        \Delta^2 u = f & \text{in } U \\
        u=\frac{\partial u}{\partial \nu}{} = 0 & \text{on } \partial U
    \end{cases} $$

    若函数 \(u\in H_0^2(U)\) 满足

    $$ \int_U \Delta u \Delta v \; dx = \int_U fv \; dx \quad \forall v\in H_0^2(U) $$

    则称 \(u\) 是问题的弱解。

    给定 \(f\in L^2(U)\)， 证明问题存在唯一弱解。


**proof**

我们仿照二阶椭圆方程的方法，利用 Lax-Milgram 定理来证明。       
令

$$ B[u,v] = \int_U \Delta u \Delta v \; dx \quad u,v\in H_0^2(U) $$

我们验证 Lax-Milgram 定理的假设条件。

**1**

$$ \begin{aligned}
    |B[u,v]| &\le \int_U |\Delta u| |\Delta v| \; dx \\
    &\le  \|\Delta u\|_{L^2} \|\Delta v\|_{L^2}    \\
    &\le  n\|u\|_{H_0^2} \|v\|_{H_0^2}
\end{aligned} $$

最后一步是因为

$$ \begin{aligned}
    \|\Delta u\|_{L^2}^2 &= \int_U |\Delta u|^2 \; dx 
    = \int_U  |\sum_{i=1}^n D_{ii} u|^2 \; dx    \\
    &\le \int_U  n \sum_{i=1}^n| D_{ii} u|^2 \; dx  \quad \text{by Cauchy} \\
    &\le n \sum_{|\alpha|=2} \int_U |D^{\alpha} u|^2 \; dx \le n \|u\|_{H_0^2}^2
\end{aligned} $$

**2**

$$ \begin{aligned}
    B[u,u] &= \int_U |\Delta u|^2 \; dx = \|\Delta u\|_{L^2}^2 \\
\end{aligned} $$

我们试图构建不等式

$$ \beta \|u\|_{H_0^2}^2  \le  \|\Delta u\|_{L^2}^2 $$

!!! Lemma

    对于 \(u\in H_0^2(U)\)， 存在一个常数 \(C=C(n,U)\) 使得

    $$ \|u\|_{H_0^2} \le C \|\Delta u\|_{L^2} $$
    
    ---

    我们先证明当 \(u\in C_c^\infty(U)\) 时成立，再由稠密性得到对 \(H_0^1(U)\) 成立。

    当 \(u\in C_c^\infty(U)\) 时

    $$ \|\Delta u \|_{L^2}^2 = \sum_{i,j=1}^n \int_U |\partial_i^2 u|^2 \; dx $$

    但是注意到 由 Gauss-Green 公式 

    $$ \int_U \partial_i^2 u \partial_j^2 u = -\int_U \partial_i u \; \partial_i \partial_j^2 u 
    = \int_U \partial_{ij} u \; \partial_{ij} u $$

    所以

    $$ \begin{aligned} 
        \|\Delta u \|_{L^2}^2 &= \int_U |\Delta u|^2 \; dx = \int_U \sum_{i,j=1}^n \partial_i^2 u \partial_j^2 u \; dx \\
        &= \sum_{i,j=1}^n \int_U  |\partial_{ij}u|^2 \; dx  = \| \nabla^2 u\|_{L^2}^2 \\
    \end{aligned} $$



    事实上由于 \(u\in H_0^2(U) \subset H_0^1(U), \nabla u \in H_0^1(U), i=1, \cdots, n\)，
    那么根据 [Poincaré 不等式](../SobolevSpaces/SobolevInequalities.md#w_01-pu) Corrollary ，我们有

    $$ \begin{gather*} 
        \|u\|_{L^2}^2 \le C_1(n, U)\|\nabla u\|_{L^2}^2 = C_1(n, U)\|Du\|_{L^2}^2   \\
        \|\nabla u\|_{L^2}^2 \le C_2(n, U)\|\nabla^2 u\|_{L^2}^2 = C_2(n, U) \sum_{|\alpha|=2} \int_U |D^\alpha u|^2 \; dx  \\
    \end{gather*} $$

    因此

    $$ \begin{aligned}
        \|u\|_{H_0^2}^2 &= \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2 + \|\nabla^2 u\|_{L^2}^2 \le C(n, U) \|\nabla^2 u\|_{L^2}^2
    \end{aligned} $$

    所以我们有了

    $$ \|u\|_{H_0^2} \le C(n, U) \|\Delta u\|_{L^2} $$

    而对于任意 \(u\in H_0^2(U)\)，存在 \(u_m \in C_c^\infty(U), \|u_m-u\|_{H_0^2} \to 0\)，那么

    $$  \|\Delta u_m-\Delta u\|_{L^2} \le \|u_m-u\|_{H_0^2} \to 0 $$

    因此

    $$ \|u_m\|_{H_0^2} \to \|u\|_{H_0^2}, \quad \|\Delta u_m\|_{L^2} \to \|\Delta u\|_{L^2} $$

    不等式两边取极限得到

    $$ \|u\|_{H_0^2} \le C(n, U) \|\Delta u\|_{L^2} \quad \forall u\in H_0^2(U) $$





因此，存在 \(\beta>0\) 使得

$$ B[u,u] \ge \beta \|u\|_{H_0^2}^2 $$


至此，我们证明了 \(B[\;, \;]\) 满足 Lax-Milgram 定理的假设条件。

又因为 \(f\in L^2(U)\)，所以

$$ \langle F, v \rangle \triangleq \int_U fv \; dx \le \|f\|_{L^2} \|v\|_{L^2} \le \|f\|_{L^2} \|v\|_{H_0^2} $$

\(F\) 是有界线性泛函。
那么由 Lax-Milgram 定理，存在唯一的 \(u\in H_0^2(U)\) 使得


$$ \int_U \Delta u \Delta v \; dx = B[u, v] = \int_U fv \; dx \quad \forall v\in H_0^2(U) $$


!!! question "4"

    设 \(U\subset \mathbb{R}^n\) 是 **连通有界** 开集，\(\partial U\) 光滑。

    Neumann 问题：

    $$ \begin{cases}
        -\Delta u = f & \text{in } U \\
        \frac{\partial u}{\partial \nu} = 0 & \text{on } \partial U
    \end{cases} $$

    若函数 \(u\in H^1(U)\) 满足

    $$ \int_U Du \cdot Dv \; dx = \int_U fv \; dx \quad \forall v\in H^1(U) $$

    则称 \(u\) 是 Neumann 问题的一个弱解。

    设 \(f\in L^2(U)\)，证明弱解存在当且仅当

    $$ \int_U f \; dx = 0 $$


**proof**

必要性显然，我们证明充分性。              
令 

$$ H_\sigma^1 = \{u\in H^1(U): \int_U u \; dx = 0 \} $$

则 \(H_\sigma^1\) 是一个 Hilbert 空间。实际上它是 \(H^1(U)\) 的闭子空间，他的闭性由

$$ |\int_U f-\int_U g| \le \|f-g\|_{L^1} \le |U|^{1/2}\|f-g\|_{L^2}  $$

保证。而且 \(\|u\|_{H_\sigma^1} = \|u\|_{H^1}\).

现在我们构造 \(H_\sigma^1\) 中的双线性映射。

$$ B[u,v] = \int_U Du \cdot Dv \; dx \quad u,v \in H_\sigma^1 $$

我们验证 Lax-Milgram 定理的假设条件。

**1**

$$ \begin{aligned}
    |B[u,v]| &\le  \int_U |Du| |Dv| \; dx \le \|Du\|_{L^2} \|Dv\|_{L^2} \le \|u\|_{H_\sigma^1} \|v\|_{H_\sigma^1}
\end{aligned} $$

**2**

$$ B[u,u] = \int_U |Du|^2 \; dx = \|Du\|_{L^2}^2 $$

但是由 [Poincaré 不等式](../SobolevSpaces/Poincaré.md#poincares-inequalities) ，我们有

$$ \|u\|_{L^2} = \|u-(u)_U\|_{L^2} \le C(n,U) \|Du\|_{L^2} $$

因此存在 \(\beta = \frac{1}{C(n,U)^2} > 0\) 使得

$$ \beta \|u\|_{H_\sigma^1}^2 \le B[u,u] $$

因此 \(B[\;, \;]\) 满足 Lax-Milgram 定理的假设条件。

同样的，我们令

$$ \langle F, v \rangle \triangleq \int_U fv \; dx \le \|f\|_{L^2} \|v\|_{L^2} \le \|f\|_{L^2} \|v\|_{H_\sigma^1} $$

因此对于任意的 \(v\in H^1(U)\)，令 \(\tilde{v} = v - (v)_U \in H_\sigma^1\)， \((v)_U\int_U f=0\).

存在唯一的 \(u\in H_\sigma^1\) 使得

$$ B[u, \tilde{v}] = \langle F, \tilde{v} \rangle = \int_U f\tilde{v} \; dx = \int_U fv \; dx $$

而 

$$ B[u, \tilde{v}] = \int_U Du \cdot D\tilde{v} \; dx = \int_U Du \cdot Dv \; dx = B[u,v] $$

也就是原问题有解。



!!! question "5"

    解释怎么定义 具有 Robin 边界条件的 Poisson 方程

    $$ \begin{cases}
        -\Delta u = f & \text{in } U \\
        u + \frac{\partial u}{\partial \nu} = 0 & \text{ on } \partial U
    \end{cases} $$

    \(u\in H^1(U)\)，的弱解。

    给定 \(f\in L^2(U)\)，讨论存在唯一性。


**solution**

对于 \(u, v\in C^\infty(U)\) ，研究 \(Lu\) 与 \(v\) 的 \(L^2\) 内积，利用 Gauss-Green 公式，我们可以得到

$$ \begin{aligned}
    \int_U -\Delta u v \;dx &= \int_U Du \cdot Dv \; dx - \int_{\partial U} v \frac{\partial u}{\partial \nu} \; dS \quad (\text{by Gauss-Green}) \\
    &=  \int_U Du \cdot Dv \; dx + \int_{\partial U} uv \; dS \quad (u + \frac{\partial u}{\partial \nu} = 0 \text{ on } \partial U )
\end{aligned}$$

那么我们可以定义弱解 \(u\in H^1(U)\) 为满足

$$  \int_U Du \cdot Dv \; dx + \int_{\partial U} Tu \; Tv \; dS = \int_U fv \; dx \quad \forall v\in H^1(U) $$

其中 \(T\) 是 [迹算子](../SobolevSpaces/Extensions.md#trace)

-----

我们立即定义

$$ B[u,v] = \int_U Du \cdot Dv \; dx + \int_{\partial U} Tu \; Tv \; dS \quad  u, v\in H^1(U) $$

我们验证 Lax-Milgram 定理的假设条件。

**1**

$$ \begin{aligned}
    |B[u,v]| &\le  \int_U |Du| |Dv| \; dx + \int_{\partial U} |Tu| |Tv| \; dS   \\ 
    &\le \|Du\|_{L^2(U)} \|Dv\|_{L^2(U)} + \|Tu\|_{L^2(\partial U)} \|Tv\|_{L^2(\partial U)}
\end{aligned} $$

但是我们有 \(\|Du\|_{L^2(U)} \le \|u\|_{H^1(U)}\)，以及[迹定理](../SobolevSpaces/Extensions.md#trace-theorem)

$$ \|Tu\|_{L^2(\partial U)} \le C(n, U) \|u\|_{H^1(U)} \quad \forall u\in H^1(U) $$

因此

$$ |B[u,v]| \le C(n, U) \|u\|_{H^1(U)} \|v\|_{H^1(U)} $$


**2**


$$ B[u, u] = \|Du\|_{L^2(U)}^2 +  \|Tu\|_{L^2(\partial U)}^2 $$

我们只要能证明

$$ \|u\|_{H^1(U)} \le C(n, U) \left( \|Du\|_{L^2(U)} + \|Tu\|_{L^2(\partial U)} \right)^2 $$

即可。

!!! Lemma
       

    设 \(U \subset \mathbb{R}^n\) 是有界开集，\(\partial U\) 是 \(C^1\) 光滑的。        
    那么存在 \(C=C(n, U)\) 使得

    $$ \|u\|_{H^1(U)} \le C(n, U) \left( \|Du\|_{L^2(U)} + \|Tu\|_{L^2(\partial U)} \right) 
    \quad \forall u\in H^1(U) $$

    ---

    **proof**

    否则，存在 \(u_k \in H^1(U), k=1, 2, ...\) 使得 \(\|u_k\|_{H^1(U)}=1\)，且

    $$ \|Du_k\|_{L^2(U)} + \|Tu_k\|_{L^2(\partial U)} < \frac{1}{k} $$

    由于 \(H^1\) 是 Hilbert 空间，属于自反 Banach 空间，而  \(u_k\) 一致有界，
    那么由 [Kakutani 定理]()     
    见 [Brezis Functional Analysis, Sobolev Spaces and Partial Differential Equations Theorem 4.17](../../Library/Brezis%20-%202011%20-%20Functional%20Analysis,%20Sobolev%20Spaces%20and%20Partial%20Di.pdf)

    存在弱收敛子列，仍记为 

    $$ u_k \rightharpoonup u  \text{ in }  H^1(U) \Rightarrow
    \begin{gather*}
        u_k \rightharpoonup u  \text{ in }  L^2(U)   \\
        Du_k \rightharpoonup Du  \text{ in }  L^2(U)
    \end{gather*}$$         

    又因为 \(\partial U\) 是 \(C^1\) 光滑的，根据 [Rellich-Kondrachov Compactness Theorem](../SobolevSpaces/SobolevInequalities2.md#rellich-kondrachov-compactness-theorem-2)，我们有

    $$ H^1(U) \subset\subset L^2(U) $$

    所以存在子列，仍记为 \(u_k\) ，使得 

    $$ \begin{gather*}
        u_k \to u \text{ in } L^2(U)
        Du_k \rightharpoonup Du  \text{ in }  L^2(U)   \\
    \end{gather*}  $$

    由 [一致有界原理]()         
    参考 [Brezis Functional Analysis, Sobolev Spaces and Partial Differential Equations Corollary 2.3](../../Library/Brezis%20-%202011%20-%20Functional%20Analysis,%20Sobolev%20Spaces%20and%20Partial%20Di.pdf)

    $$ \|Du\|_{L^2(U)} \le  \liminf_{k\to\infty} \|Du_k\|_{L^2(U)} \to 0 $$

    那么有 \(Du = 0 \text{  a.e.}\)，
    <!-- 那么 -->

    我们就有

    $$ \begin{aligned}
        \|u_k-u\|_{H^1(U)}^2 &= \|u_k-u\|_{L^2(U)}^2 + \|Du_k-Du\|_{L^2(U)}^2   \\
        &= \|u_k-u\|_{L^2(U)}^2 + \|Du_k\|_{L^2(U)}^2 \\
        &\to 0 \text{  as  } k\to\infty
    \end{aligned}  $$

    因此我们得到 \(u_k \to u \text{  in  }  H^1(U)\).

    所以

    $$ \|u\|_{L^2(U)} = \|u\|_{H^1(U)} = \lim_{k\to\infty} \|u_k\|_{H^1(U)} = 1 $$

    而 \(Du = 0 \text{  a.e.}\)，以及根据 [引理](../SobolevSpaces/Approximation.md#local-approximation) Corollary ，
    \(u\) 在每个连通分支上都几乎处处等以一个常数 \(u=c_\alpha \text{ a.e.}\)

    但是根据 [迹定理](../SobolevSpaces/Extensions.md#trace-theorem)，以及 \(u_k \to u \text{  in  }  H^1(U)\)

    $$ \begin{aligned}
        \|Tu\|_{L^2(\partial U)} &=  \lim_{k\to\infty} \|Tu_k\|_{L^2(\partial U)} \to 0 \text{ as  } k\to\infty \\
        \Rightarrow u=0 \text{  a.e. on  } \partial U
    \end{aligned}$$

    那么根据 [迹零定理](../SobolevSpaces/Extensions.md#trace-zero-functions)，
    \(u\in H_0^1(U)\)，但是由 Poincaré 不等式

    $$ \|u\|_{L^2(U)} \le C(n, U) \|Du\|_{L^2(U)} = 0 $$

    说明 \(u=0 \text{  a.e.}\) ，这与 \(\|u\|_{L^2(U)}=1\) 矛盾！

    因此存在 \(C=C(n, U)\) 使得

    $$ \|u\|_{H^1(U)} \le C(n, U) \left( \|Du\|_{L^2(U)} + \|Tu\|_{L^2(\partial U)} \right) $$


根据引理，我们得到存在 \(\beta>0\) 使得

$$ \beta \|u\|_{H^1(U)}^2 \le C(n, U) \|Du\|_{L^2(U)}^2 + \|Tu\|_{L^2(\partial U)}^2 $$

现在，我们验证了 \(B[\;, \;]\) 满足 Lax-Milgram 条件，那么由 Lax-Milgram 定理，

对于 \(v\in H^1(U)\)，存在唯一的 \(u\in H^1(U)\) 使得

$$ B[u,v] = \int_U fv \; dx $$

即弱解存在。


