# Poincaré 不等式

[Lawrence C.Evans Partial differential equations 5.8.1](../index.md#lawrence-cevans-partial-differential-equations)

我们曾在 [GNS 不等式的有界情况](./SobolevInequalities.md#bounded) 的最后提到过          
\(u\) 能否被 \(Du\) 控制与 \(u\) 是否存在等于 0 的部分是有很大区别的。              
因此我们建立 Poincaré 不等式就是为了消除 \(u\) 上下平移带来的影响。


记

$$ (u)_U = {-\mkern -19mu\int}_{U} u $$

为 \(u\) 在 \(U\) 上的平均。

## Poincare's inequalities

令 \(U \subset R^n\) 是 *有界连通开集* ，\(\partial U\) 是 \(C^1\) 的。       
设 \(1 \le p \le \infty\)，那么存在常数 \(C=C(n,p,U)\) 使得对于任何 \(u \in W^{1,p}(U)\)

$$ \|u-(u)_U\|_{L^p(U)} \le C \|Du\|_{L^p(U)} $$





















## Problems

!!! Question

固定 \(\alpha>0\)，\(U \subset R^n\) 是有界 **连通** 开集，且

$$ E_u = \{x\in U | u(x)=0\}, \quad \mu(E_u) \ge \alpha $$

那么

$$ \|u\|_{L^{p^*}(U)} \le C(n, U, p, \alpha) \|Du\|_{L^{p}(U)} $$

---

我们证明的技巧与证明 Poincaré 一样，使用反证法。