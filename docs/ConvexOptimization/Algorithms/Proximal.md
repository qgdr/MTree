# 近似点 Proximal

## 近似算子 Proximal Operator

$$ \text{Prox}_f(b) = \arg \min_{x\in \text{dom}f} f(x) + \frac{1}{2} \|x-b\|^2  $$

如果 $f$ 是适当的闭凸函数，那么 \(\text{Prox}_f(b)\) 是唯一的。


对于矩阵的情况

$$ \text{Prox}_f(Y) = \arg \min_{X\in \text{dom}f} f(X) + \frac{1}{2} \|X-Y\|_F^2 $$


### 近似算子与次梯度 Proximal and Subgradient

如果 \(f\) 是适当的闭凸函数，那么

$$ x = \text{Prox}_f(b) \quad \Leftrightarrow \quad b-x \in \partial f(x) $$

$$ x = \text{Prox}_{tf}(b) \quad \Leftrightarrow \quad b-x \in t\partial f(x) , t>0 $$

矩阵情况相同

$$ X = \text{Prox}_{f}(Y) \quad \Leftrightarrow \quad Y-X \in \partial f(X) $$

!!! interpretation

    这是因为 [最优化：建模、算法与理论 2.1.2][Wen]

    $$ \|A\|_F = \sqrt{Tr(AA^T)} \quad \Rightarrow \quad \|A\|_F^2 = Tr(AA^T) $$

    $$ \begin{align}
        Tr((A+tV)(A^T+tV^T)) &= Tr(AA^T)+t (Tr(AV^T)+Tr(VA^T))+t^2Tr(VV^T) \\
        &= Tr(AA^T)+2t\cdot Tr(A^T V)+t^2 \cdot Tr(VV^T)
    \end{align} $$

    即 \(\nabla \|A\|_F^2 = 2A\), 

    那么 \(X =  \text{Prox}_{f}(Y)\) 等价于

    $$ O \in \partial_X (f(X) + \frac{1}{2}\|X-Y\|^2) = \partial f(X) + X - Y $$


### Moreau decomposition

$$ b = \text{Prox}_{f}(b) + \text{Prox}_{f^*}(b) $$

矩阵情况相同

$$ Y = \text{Prox}_{f}(Y) + \text{Prox}_{f^*}(Y) $$


## Examples

### Proximal and Projection 近似与投影

$$ \begin{align}
    \text{Prox}_{I_C}(b) &= \arg\min_{x} I_C(x) + \frac{1}{2} \|x-b\|^2 \\
    &= \arg\min_{x\in C} \|x-b\|^2 \\
    &= \mathcal{P}_C(b) 
\end{align} $$


### proximal of \(l_1\) -norm

请解决 \(l_1\) 范数 \(f (x) = ‖x‖_1 = \sum_{j=1}^n |x_j |\) 的近似点.    


$$ \text{Prox}_{f}(b) = \arg\min_{x} ‖x‖_1 + \frac{1}{2} \|x-b\|_2^2  $$

**First solution**:

令 \(\hat{x} = \text{Prox}_{f^*}(b) \) .        
因为 \(f(x)= \|x\|_1\) 是凸函数， 我们有 

$$ b-\hat{x} \in \partial f(\hat{x}) = \{g : g_i = \begin{cases}
    \text{sign}(x_i), & \text{if } x_i \neq 0 \\
    [-1, 1], & \text{if } x_i = 0
\end{cases} \} $$

所以，

$$ \hat{x}_i = \begin{cases}
    0, & \text{if } |b_i| \le 1 \\
    \text{sign}(b_i)(|b_i|-1 ), & \text{if } |b_i| > 1
\end{cases} $$


**Second solution**:

根据 [Moreau decomposition](./Proximal.md#moreau-decomposition)， 我们有

$$ b = \text{Prox}_{f}(b) + \text{Prox}_{f^*}(b) $$

其中 \(f^* (x) = \mathbb{I}_{\|x\|_\infty \le 1}\)，即

$$ \text{Prox}_{f}(b) = b - \text{Prox}_{f^*}(b) = b-\mathcal{P}_{\|x\|_\infty \le 1} (b) $$

但是，我们显然有 

$$ \mathcal{P}_{\|x\|_\infty \le 1} (b) = \tilde{b} \quad \text{  where  } \quad \tilde{b}_i = \begin{cases}
    b_i, & \text{if } |b_i| \le 1 \\
    \text{sign}(b_i), & \text{if } |b_i| > 1
\end{cases} $$

所以

$$ \begin{align}
    \text{Prox}_{f}(b)_i &= b_i - \text{Prox}_{f^*}(b)_i 
    = b_i - \mathcal{P}_{\|x\|_\infty \le 1} (b)_i         \\
    &= b_i - \tilde{b}_i    \\
    &= b_i - \begin{cases}
        b_i, & \text{if } |b_i| \le 1 \\
        \text{sign}(b_i), & \text{if } |b_i| > 1
    \end{cases}         \\
    &= \begin{cases}
        0, & \text{if } |b_i| \le 1 \\
        \text{sign}(b_i)(|b_i|-1 ), & \text{if } |b_i| > 1
    \end{cases}
\end{align} $$







### Nuclear Norm

我们考虑 [核范数](../../LinearAlgebra/MatrixNorm.md#nuclear-norm) 的近似点。        
这个问题又被称为 **奇异值阈值 Singular Value Thresholding ( SVT )**，
参考文献 [Cai](./Cai%20等%20-%202008%20-%20A%20Singular%20Value%20Thresholding%20Algorithm%20for%20Matrix.pdf)

$$ \text{Prox}_{t\|\cdot\|_{2*}}(Y) = \arg \min_{X\in R^{m\times n}} t\|X\|_{2*}  + \frac{1}{2} \|X-Y\|_F^2, \quad t > 0 $$

其中 \(\|X\|_{2*} = \sum_{i=1}^r \sigma_i(X), \; r = \text{rank}(X)\).        

我们给出两种获得近似点的方法，不妨设 \(m\le n\).

!!! solution

    核范数 \( \|X\|_{2*} \) 是一个凸函数，      所以 \(\|X\|_{2*}  + \frac{1}{2} \|X-Y\|_F^2\) 强凸，       \(\text{Prox}_{\|\cdot\|_{2*}}(Y)\) 有唯一解.

    设 \(X = \text{Prox}_{\|\cdot\|_{2*}}(Y)\)

    ----

    **First solution**:

    因为 [近似点与次梯度](./Proximal.md#proximal-and-subgradient)，   

    $$ Y-X \in t\partial \|X\|_{2*} $$

    我们来计算一下 核范数 的次梯度 参考 [Watson 1992](./Watson%20-%201992%20-%20Characterization%20of%20the%20subdifferential%20of%20some%20ma.pdf)，

    令 \(X = U\Sigma_r V^T, U \in R^{m \times r}, V \in R^{n \times r}, \Sigma_r = \text{diag}( \sigma_1, \dots, \sigma_r) \) 是约化 SVD ，则

    $$  \partial \|X\|_{2*} = \{ UV^T+W : \|W\|_2 \le 1, U^TW = 0, WV = O \} $$

    现在令 

    $$ Y = U\Sigma V^T = U_0 \Sigma_0 V_0^T + U_1 \Sigma_1 V_1^T $$

    其中 

    $$ \Sigma = \text{diag}(\Sigma_0 , \Sigma_1), \quad  \Sigma_0 \succ t, \Sigma_1 \preceq t , \quad U = [U_0 | U_1], V = [V_0 | V_1] $$

    令

    $$ X = U_0 (\Sigma_0-tI) V_0^T $$

    那么

    $$ Y-X = t (U_0 V_0^T + U_1 \frac{\Sigma_1}{t} V_1^T) $$

    其中 

    $$ \begin{gather*}
        W \triangleq U_1 \frac{\Sigma_1}{t} V_1^T, \quad \|W\| \le 1, \\
        U_0^TW = U_0^T U_1 \frac{\Sigma_1}{t} V_1^T = O \frac{\Sigma_1}{t} V_1^T = O, \quad WV=O
    \end{gather*} $$

    所以

    $$ Y-X \in t\partial \|X\|_{2*} $$

    因此

    $$ \text{Prox}_{\|\cdot\|_{2*}}(Y)  = U_0 (\Sigma_0-tI) V_0^T = U (\Sigma - tI)^+ V^T $$

    ----

    **Second solution**:

    不妨设 \(Y = D = \text{diag}(d_1, \dots, d_m), d_1 \ge \cdots \ge d_m \ge 0\) 是对角阵，            
    设 \(X = U\Sigma V^T, \text{diag}(\sigma_1, \dots, \sigma_m), \sigma_1 \ge \cdots \ge \sigma_m \ge 0\)，      
    我们说明

    $$ \|X-Y\|_F^2 \ge \sum_{i=1}^m (d_i - \sigma_i)^2 $$

    事实上

    $$ \begin{align}
        \|X-Y\|_F^2 &= Tr((X-Y)(X-Y)^T) = Tr(XX^T) + Tr(YY^T) - 2Tr(XY^T) \\
        &= \sum_{i=1}^m \sigma_i^2 + \sum_{i=1}^m d_i^2 - 2 Tr(U\Sigma V^T D) \\
    \end{align} $$

    因此我们只需要证明 \(Tr(U\Sigma V^T D) \le \sum_{i=1}^m d_i\sigma_i \)，

    展开得到

    $$ \begin{gather*}
        Tr(U\Sigma V^T D) = \sum_{i,j}^m d_i\sigma_j u_{ij}v_{ij} 
        \le \sum_{i,j}^m d_i\sigma_j p_{ij} = d^T P \sigma, \quad p_{ij} = |u_{ij}v_{ij}| \\
        \quad \sum_{i=1}^m p_{ij} = \sum_{i=1}^m |u_{ij}v_{ij}| \le \|U_j\|_2\|V_j\|_2 = 1, \quad \sum_{j=1}^m p_{ij} \le 1
    \end{gather*} $$

    那么

    $$ \sum_{i,j}^m d_i\sigma_j p_{ij} \le \sum_{k=1}^m d_k\sigma_k $$

    是广义的 Chebyshev 不等式

    我们把 \(p_{ij} \ge 0 , \sum_{i=1}^m p_{ij} \le 1 \quad \sum_{j=1}^m p_{ij} \le 1\) 称为 **概率条件**。

    我们这里证明 广义的 Chebyshev 不等式

    因为 \(d_i\sigma_j + d_j\sigma_i \le d_i\sigma_i + d_j\sigma_j\)，（顺序和大于乱序和）          
    所以我们可以使用调整法，如果 \(p_{12}\) 和 \(p_{21}\) 都大于 \(0\)，那么令 \(q = \min\{p_{12}, p_{21}\}\)，
    因为 \(d_1\sigma_2 + d_2\sigma_1 \le d_1\sigma_i + d_1\sigma_j\)，      
    那么我们令

    $$ \begin{bmatrix}
        p'_{11} & p'_{12}   \\
        p'_{21} & p'_{22}   
    \end{bmatrix} = 
    \begin{bmatrix}
        p_{11} + q & p_{12} - q \\
        p_{21} - q & p_{22} + q
    \end{bmatrix}, \quad
    p'_{ij} = p_{ij} \text{  else  } $$

    那么我们很容易验证 

    $$ \sum_{i,j}^m d_i\sigma_j p_{ij} \le \sum_{i,j}^m d_i\sigma_j p'_{ij} $$

    且 \(P'\) 满足概率条件。

    且 \(p'_{12}, p'_{21}\) 中至少有一个变成 \(0\).

    因此我们可以继续上面的步骤，直到第一行 **或** 第一列除了 \(p_{11}\) 都是 \(0\)，        
    不妨设 \(p_{1j}=0, j=2,...,m\) ，我们令

    $$ p'_{11} = \sum_{i=1}^m p_{i1} \le 1, \quad p'_{i1} = 0 ,\; i = 2,...,m $$

    我们知道 \(\sum_{i=1}^m p_{i1} d_i\sigma_i \le \sum_{i=1}^m p_{i1} d_i\sigma_1 \)，即

    $$ \sum_{i,j}^m d_i\sigma_j p_{ij} \le \sum_{i,j}^m d_i\sigma_j p'_{ij} $$

    但这样第一行 **和** 第一列 除了 \(p_{11}\) 都是 \(0\)，且仍旧满足 概率条件。        

    我们运用数学归纳法，一直调整 \(P\)，直到 \(P\) 成为 对角阵，且保持 概率条件，       
    不妨设最后调整至 \(Q = \text{diag}(q_1, \dots, q_m) , q_k \in [0 ,1]\)，那么我们有

    $$ Tr(U\Sigma V^T D) \le \sum_{i,j} d_i\sigma_j p_{ij} \le \sum_{k=1}^m d_k\sigma_k q_{k} \le \sum_{k=1}^m d_k\sigma_k $$

    因此，我们有

    $$ \|X-Y\|_F^2 \ge \sum_{i=1}^m (d_i - \sigma_i)^2 $$

    当 \(X = \Sigma\) 时取等。

    那么现在原问题就变成了

    $$ \arg\min_{\sigma} t\|\sigma\|_1 + \frac{1}{2} \|d-\sigma\|_2^2, \quad t > 0 $$

    参考 [\(l_1\)](./Proximal.md#proximal-of-l_1-norm)，我们知道当

    $$ \sigma = (d-t1)^+ $$

    时取得最小值。


    因此总结下来，对于 \(Y=UDV^T\)，

    $$ \text{Prox}_{\|\cdot\|_{2*}}(Y) = U (D - tI)^+ V^T $$





[Wen]: ../index.md#最优化建模算法与理论
