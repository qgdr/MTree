# 光滑逼近 Approximation

## Urysohn 定理

令 \(U, V\) 是 \(R^n\) 中的开集，\(V \subset\subset U\)。
则存在一个光滑函数 \(\zeta\) 使得 \(\zeta(x) \equiv 1, x\in V\)，\(\zeta(x) = 0, x \text{  near  } U\)

**证明**

因为 \(\overline{V} \subset \Omega\)，故存在 \(\epsilon_0 > 0\) ，使得 \(\text{dist}(\overline{V}, \partial\Omega) > 2\epsilon_0\)。      
那么令 \(W = \{x: \text{dist}(x, \overline{V}) < \epsilon_0 \}\)，则 \(W\) 是一个开集，且 \(V \subset\subset W \subset\subset \Omega\)。

令 \(\eta(x)\) 是 **磨光函数**，\(\eta_\epsilon(x) = \frac{1}{\epsilon^n} \eta(\frac{x}{\epsilon})\) ，  \(\int_\Omega \eta_\epsilon = 1\)     
那么令 \(0 < \epsilon < \epsilon_0\)，  \(\zeta=\eta_\epsilon * \chi_W \)， \(\zeta\) 是一个光滑函数，且 \(0 \le \zeta(x) \le 1, x\in \Omega\)

当 \(x\in V\) 时，\(B(x, \epsilon) \subset W\)

$$ \zeta(x) = \int_{B(0, \epsilon)} \chi_W (x-y) \eta_\epsilon(y) dy =  \int_{B(x, \epsilon)} \chi_W (y) \eta_\epsilon(x-y) dy =  \int_{B(0, \epsilon)} 1 \eta_\epsilon(y) dy = 1 $$

当 \(x\to \partial \Omega\) 时，\(\text{dist}(x, \overline{V}) > 2\epsilon\)， \(B(x, \epsilon) \subset W^c\)，同理得 \(\zeta(x) = 0\)


## 单位分解定理 Partition of Unity

### 有限版本

