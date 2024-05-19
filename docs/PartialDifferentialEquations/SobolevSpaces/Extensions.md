# Extensions 延拓

## Extension Theorem 延拓定理

设\(U\) 有界且 \(\partial U\) 是 \(C^1\) 连续的。
选取一个有界开集 \(V\) 使得 \(U\subset\subset V\)。
那么存在 **延拓算子** 

$$ E : W^{1,p}(U) \to W^{1,p}(\mathbb{R}^n) $$

是有界线性算子，对 \(\forall u\in W^{1,p}(U)\) 满足

1 . 

$$ Eu = u \text{ a.e. in } U $$

2 . 

$$ \text{supp}(Eu) \subset V $$

3 .
存在常数 \(C=C(n,U,V,p)\)，使得

$$ \|Eu\|_{W^{1,p}(\mathbb{R}^n)} \leq C\|u\|_{W^{1,p}(U)} $$





# Trace 迹算子

## Trace Theorem 迹定理

假设 \(U\) 有界且 \(\partial U\) 是 \(C^1\) 连续的。那么存在 **迹算子** 

$$ T: W^{1,p}(U) \to L^p(\partial U) $$ 

是有界线性算子，满足

1 . 
对于 \(u\in W^{1,p}(U)\cap C(\bar{U})\)，有 \(Tu = u|_{\partial U}\).

2 .
存在常数 \(C=C(n,U,p)\) 使得

$$ \|Tu\|_{L^p(\partial U)} \leq C\|u\|_{W^{1,p}(U)} , \quad \forall u\in W^{1,p}(U) $$

我们称 \(Tu\) 为 \(u\) 在 \(\partial U\) 上的 **迹 trace** 。



## Trace-zero functions 迹零函数

设 \(U\) 有界且 \(\partial U\) 是 \(C^1\) 连续的。那么对于 \(u\in W^{1,p}(U)\)，

$$ Tu = 0 \text{ on } \partial U \Leftrightarrow u\in W_0^{1,p}(U) $$

