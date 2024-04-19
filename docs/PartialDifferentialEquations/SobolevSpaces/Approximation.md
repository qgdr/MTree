# 光滑逼近 Approximation

## Urysohn 引理

令 \(U, V\) 是 \(R^n\) 中的开集，\(V \subset\subset U\)。
则存在一个光滑函数 \(\zeta\) 使得 \(\zeta(x) \equiv 1, x\in V\)，\(\zeta(x) = 0, x \text{  near  } U\)

**证明**

<video src="../media/videos/Sobolev/720p30/Urysohn.mp4" width="100%"  type="video/mp4" controls="controls" frameborder="0" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" oallowfullscreen="true" msallowfullscreen="true"></video>


因为 \(\overline{V} \subset \Omega\)，故存在 \(\epsilon_0 > 0\) ，使得 \(\text{dist}(\overline{V}, \partial\Omega) > 2\epsilon_0\)。      
那么令 \(W = \{x: \text{dist}(x, \overline{V}) < \epsilon_0 \}\)，则 \(W\) 是一个开集，且 \(V \subset\subset W \subset\subset \Omega\)。

令 \(\eta(x)\) 是 **磨光函数**，\(\eta_\epsilon(x) = \frac{1}{\epsilon^n} \eta(\frac{x}{\epsilon})\) ，  \(\int_\Omega \eta_\epsilon = 1\)     
那么令 \(0 < \epsilon < \epsilon_0\)，  \(\zeta=\eta_\epsilon * \chi_W \)， \(\zeta\) 是一个光滑函数，且 \(0 \le \zeta(x) \le 1, x\in \Omega\)

当 \(x\in V\) 时，\(B(x, \epsilon) \subset W\)

$$ \zeta(x) = \int_{B(0, \epsilon)} \chi_W (x-y) \eta_\epsilon(y) dy =  \int_{B(x, \epsilon)} \chi_W (y) \eta_\epsilon(x-y) dy =  \int_{B(0, \epsilon)} 1 \eta_\epsilon(y) dy = 1 $$

当 \(x\to \partial \Omega\) 时，\(\text{dist}(x, \overline{V}) > 2\epsilon\)， \(B(x, \epsilon) \subset W^c\)，同理得 \(\zeta(x) = 0\)


## 单位分解定理 Partition of Unity

### 有限版本

设 \(U\) 有界且 \(U \subset\subset \bigcup_{i=1}^N V_i\)， 其中 \(V_i\) 是开集， 那么存在 \(\zeta_i \in C^\infty, i=1, \dots, N\) 使得

$$ \begin{cases}
    0 \le \zeta_i \le 1, \quad \text{supp} \zeta_i \subset V_i \quad (i=1, \dots, N) \\
    \sum_{i=1}^N \zeta_i(x) = 1,  \quad x \in U
\end{cases} $$


**证明**

因为 \(U \subset\subset \bigcup_{i=1}^N V_i\)，其中 \(V_i\) 是开集，        
我们可以找到 \(W_i \subset\subset V_i\)，
使得 \(U \subset\subset \bigcup_{i=1}^N W_i \subset\subset \bigcup_{i=1}^N V_i\)。            
（由于 \(U \in R^n\) 有界，所以 \(\bar{U}\) 是紧的，每个点都有开集 \(U_x \subset\subset V_i\) 对于某个 \(i\)，\(U_x\) 是一个开覆盖，所以有有限开覆盖 \(U \subset\subset \bigcup_{i=1}^M U_{x_i}\)，将他们分组到各自属于的 \(V_i\)，令每一组的并为 \(W_i\)，则 \(U \subset\subset \bigcup_{i=1}^N W_i\)，且 \(W_i \subset\subset V_i\) ）

对于每个 \(W_i, V_i, i=1, \dots, N\)，存在 \(\phi_i \in C^\infty\) 使得

$$ \phi_i(x) = \begin{cases} 1, \quad x \in W_i \\ 0, \quad x \in V_i^c \end{cases} $$

即 \(\text{supp}(\phi_i) \subset V_i\)，
令

$$ \phi_0(x) = \begin{cases} 1, \quad x \in U \\ 0, \quad x \in \left(\bigcup_{i=1}^N W_i\right)^c \end{cases} $$

那么，令

$$ \zeta_i = \frac{\phi_i}{\sum_{i=1}^N \phi_i + 1-\phi_0}, \quad i=1, \dots, N $$

那么，\(\text{supp}(\sum_{i=1}^N \phi_i + 1-\phi_0) \supset \bigcup_{i=1}^N W_i + \left(\bigcup_{i=1}^N W_i\right)^c \supset \bigcup_{i=1}^N V_i\)，因此 \(\zeta_i\) 在 \(V_i\) 上有定义。      
又有 \(\text{supp}\zeta_i = \text{supp}\phi_i \subset V_i\)，       
而

$$ \sum_{i=1}^N \zeta_i = \sum_{i=1}^N \frac{\phi_i}{\sum_{i=1}^N \phi_i + 1-\phi_0} = \frac{\sum_{i=1}^N \phi_i}{\sum_{i=1}^N \phi_i + 1-\phi_0} = 1 \quad \text{on } U  $$

满足我们需要的条件

<video src="../media/videos/Sobolev/720p30/POU.mp4" width="100%"  type="video/mp4" controls="controls" frameborder="0" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" oallowfullscreen="true" msallowfullscreen="true"></video>