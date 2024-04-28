# HW2

[HW2pdf](../HWpdf/Homework2%20of%20Optimization-2024.pdf)

## 1. Exercise 3.18, 3.57 of [Convex Optimization][textbook]

a. \(f(\mathbf{X}) = tr(\mathbf{X}^{-1})\) is convex on \(dom f=S_{++}^n\)

b. \(f(\mathbf{X}) = (\det(\mathbf{X}))^{1/n}\) is concave on \(dom f=S_{++}^n\)

!!! proof

    **a**. consider \(g(t)=f(X+tY)\), where \(X\in S_{++}^n, Y\in S^n\). We have

    $$ \begin{align}
    g(t) &= tr((X+tY)^{-1}) \\
        &= tr((X^{1/2}(I + tZ)X^{1/2})^{-1}) \quad (where \, Z=X^{-1/2}YX^{-1/2} \in S^n)   \\
        &= tr(X^{-1}(I + tZ)^{-1}) \\
        &= tr(X^{-1}U^T(I + t\Lambda)^{-1}U) \quad (where \, \Lambda=UZU^T diagonal, U \, unit)   \\
        &=\sum_{i=1}^n (UX^{-1}U^T)_{ii} (1+t\lambda_i)^{-1}
    \end{align} $$ 

    Since \(UX^{-1}U^T\in S_{++}^n\), we get \((UX^{-1}U^T)_{ii}>0\).      
    And \(X+tY\succ 0\) iif \(I+t\Lambda\succ 0\).   
    If \(Y\neq 0\), then \(\Lambda \neq 0\), when \(1+t\lambda_i>0, i=1,..., n\)

    $$g''(t)=\sum_{i=1}^n (UX^{-1}U^T)_{ii} 2\lambda_i^2
    (1+t\lambda_i)^{-3} > 0$$

    So \(g(t)\) is strictly convex.     
    And then, we have \(f(\mathbf{X}) = tr(\mathbf{X}^{-1})\) is strictly convex.

    ---

    **b**. Similarly, we have

    $$ \begin{align}
    g(t) &= (\det(X+tY))^{1/n} \\
        &= ( \det(X^{1/2}(I + tZ)X^{1/2}) )^{1/n}    \\
        &= ( \det(X)\det(I+t\Lambda) )^{1/n}  \\
        &= (\det(X))^{1/n}\prod_{i=1}^n (1+t\lambda_i)^{1/n}
    \end{align} $$ 

    $$ \begin{align}   
    g''(t) &= g(t) (\sum_{i=1}^n -\frac{n-1}{n^2(1+t\lambda_i)^{2}} + \sum_{i\neq j}\frac{1}{n^2(1+t\lambda_i)(1+t\lambda_j)}) \\
    &= - g(t) (\frac{1}{n}\sum_{i=1}^n \frac{1}{(1+t\lambda_i)^{2}} - (\frac{1}{n}\sum_{i=1}^n \frac{1}{1+t\lambda_i})^2 ) \le 0
    \end{align} $$

    Since \(\det(X)>0\), we get \(g(t)\) is concave. (By the way, we deduce that geometric mean is concave.)  
    And then we have \(f(\mathbf{X}) = (\det(\mathbf{X}))^{1/n}\) is concave.


## 2. Exercise 2.12 of [最优化：建模、算法与理论][ref2], Exercise 3.36 of [Convex Optimization][textbook]

Derive the conjugates of the following functions

a. Max function. \(f(\mathbf{x})=\max_{i=1,..,n} x_i\) on \(R^n\).     

b. Sum of largest elements. \(f(\mathbf{x}) = \sum_{i=1}^r x_{[i]}\) on \(R^n\).     

c. Log function of the Matrix: \(f(\mathbf{X}) = − \ln \det(\mathbf{X}) \).

!!! solution

    $$ f^*(y) = \sup_{x\in dom f} \{ y^T x-f(x)\} $$

    **a**. 

    $$ f(\mathbf{x})=\max_{i=1,..,n} x_i $$

    1. If \(y_i < 0\) for some \(i\), then \(f^*(y) \ge \sup_{x_i < 0}\{y^T (0, ..., x_i, ..., 0) - 0\} = +\infty \).   
    2. If \(\sum_{i=1}^n y_i \neq 1\), then \(f^*(y) \ge \sup_{t}\{y^T ( t, ..., t) - t\} = +\infty \).     
    3. If \(\sum_{i=1}^n y_i = 1\) and \(y_i \ge 0\) for all \(i\), then    
    \(f^*(y) = \sup_{x\in dom f} \{ y^T x-f(x)\} \le \sum_{i=1}^n y_i\max_{i=1}^n x_i - \max_{i=1}^n x_i = 0\).   

    So we have

    $$ f^*(y) = \begin{cases}
        0, & y_i \ge 0 \text{ and } \sum_{i=1}^n y_i = 1 \\
        +\infty, & \text{otherwise}
    \end{cases} $$

    ---

    **b**.

    $$ f(\mathbf{x}) = \sum_{i=1}^r x_{[i]} $$

    Similarly,      

    1. If \(y_i < 0\) for some \(i\), then \(f^*(y) \ge \sup_{x_i < 0}\{y^T (0, ..., x_i, ..., 0) - 0 \} = +\infty \).      
    2. If \(y_i >1\) for some \(i\), then \(f^*(y) \ge \sup_{x_i >0}\{y^T (0, ..., x_i, ..., 0) -x_i \} = +\infty \).    
    3. If \(\sum_{i=1}^n y_i \neq r\), then \(f^*(y) \ge \sup_{t}\{y^T ( t, ..., t) - rt\} = +\infty \).    
    4. If \(\sum_{i=1}^n y_i = r\) and \(0 \le y_i \le 1\), then

    $$\begin{align}    
    y^Tx &= \sum_{i=1}^r y_i x_{[i]} + \sum_{i=r+1}^n y_i x_{[i]} \\
    &\le \sum_{i=1}^r y_i x_{[i]} + \sum_{i=1}^r (1-y_i) x_{[r+1]} \\
    &\le \sum_{i=1}^r y_i x_{[i]} + \sum_{i=1}^r (1-y_i) x_{[i]} = 0 
    \end{align}$$

    It can be get when \(x=0\)
    Summarise:

    $$f^*(y) = \begin{cases}
        0, & 0 \le y_i \le 1 \text{ and } \sum_{i=1}^n y_i = r \\
        +\infty, & \text{otherwise}
    \end{cases} $$

??? warning

    **c**.

    Since \(f(\mathbf{X}) = − \ln \det(\mathbf{X}) \),

    $$ f^*(\mathbf{Y}) = \sup_{\mathbf{X} \in dom f} \{ tr(\mathbf{Y}^T\mathbf{X}) + \ln \det(\mathbf{X}) \}$$


    $$ f^*(\mathbf{Y}) \equiv +\infty, \text{ if } n > 1 $$

    根据奇异值分解， 设 \( Y = U D V^T \), 其中 \( D \) 是对角矩阵, \( U, V \) 是正交矩阵，且 <font color=Red> \( \det(U)=\det(V)=1 \) </font>。

    令 \( X=U \Lambda V^T \)，则 \(tr(Y^TX)=tr( V D U^T U \Lambda V^T) = \sum_{i=1}^n d_i \lambda_i \).  
    若 \(d_1 > 0\)，令 \( \lambda_1 = t^{n-1}, \lambda_i = 1/t, i\geq 2 \)，那么

    $$ tr(Y^TX)+\ln \det(X) = d_1 t^{n-1} + \sum_{i=2}^{n}d_i/t + 0 \to +\infty $$

    若 \(d_1 < 0\)，令 \( \lambda_1 = -t^{n-1}, \lambda_2 = -1/t, \lambda_i = 1/t, i\geq 3 \)，那么

    $$ tr(Y^TX)+\ln \det(X) = -d_1 t^{n-1} + (-d_2+\sum_{i=3}^{n}d_i)/t + 0 \to +\infty $$


!!! solution

    **c**.

    Since \(f(\mathbf{X}) = − \ln \det(\mathbf{X}) ,\quad \text{dom}f=S^n_{++} \), 
    we claim that \(f(X)\) is convex! [最优化：建模、算法与理论 例 2.5][ref2]
    
    For \(\mathbf{Y} \in S^n\)

    $$ f^*(\mathbf{Y}) = \sup_{\mathbf{X} \in S^n_{++}} \{ Tr(\mathbf{Y}^T\mathbf{X}) + \ln \det(\mathbf{X}) \} $$

    Let \(Y = U\Lambda_Y U^T\), where \(U\) is an orthogonal matrix, \(\Lambda_Y\) is a diagonal matrix.

    Then,

    $$ \begin{align} 
        f^*(Y) 
        &= \sup_{X \in S^n_{++}} \{ Tr(Y^TX) + \ln \det(X) \} \\
        &= \sup_{X \in S^n_{++}} \{ Tr(U\Lambda_Y U^T X) + \ln \det(X) \}    \\
        &= \sup_{X \in S^n_{++}} \{ Tr(\Lambda_Y U^T XU) + \ln \det(U X U^T) \} \\
        &= \sup_{Z \in S^n_{++}} \{ Tr(\Lambda_Y Z) + \ln \det(Z) \}
    \end{align} $$

    If there is a \(\lambda_i \ge 0\)，Let 
    
    $$ Z=\text{diag}(1, ..., \underbrace{t}_i, ..., 1) $$

    Then 

    $$ f^*(Y) \ge Tr(\Lambda_Y Z) + \ln \det(Z) = t\lambda_i + \ln t  + c \to +\infty \text{ as } t \to +\infty $$

    So, \(f^*(Y) = +\infty\) if \((-Y) \notin S^n_{++}\).

    On th other hand, if \((-Y) \succ 0\), since \(Tr(Y^TX)\) is linear, and \( -\ln \det(X) \) is convex,
    we know that  
    
    $$ g_Y(X) \triangleq Tr(Y^TX) + \ln \det(X) $$ 
    
    is **concave**!

    So if there is an \(X\) such that \(\nabla g_Y(X) = 0 \), then \(g_Y(X) = f^*(Y)\) is the maximum value . However 

    $$ \nabla g_Y(X) = Y+X^{-T} $$

    Hence \((-Y)\succ 0\), we can let \(X = (-Y)^{-1} = -Y^{-1} \in S^n_{++} \), where

    $$ g_Y((-Y)^{-1}) = Tr(-YY^{-1}) + \ln(\det(-Y)^{-1}) = -Tr(I) - \ln\det(-Y) = -n-\ln\det(-Y) $$

    Summary, we get

    $$ f^*(Y) = \begin{cases}
    -n-\ln\det(-Y), & \text{if } -Y \succ 0 \\
    +\infty, & \text{otherwise}
    \end{cases} $$









## 3. Exercise 2.6 of [最优化：建模、算法与理论][ref2]

Compute the gradient of the functions with matrix variables.

a. \(f (\mathbf{X}) = Tr (\mathbf{X}^T\mathbf{A}\mathbf{X})\), where \(\mathbf{X} ∈ R^{m×n}\), \(\mathbf{A} ∈ R^{m×m}\) (may not symmetrix);

b. \(f (\mathbf{X}) = \ln \det(\mathbf{X})\), where \(\mathbf{X} ∈ R^{n×n}\) and domain is \(\{\mathbf{X} | \det(\mathbf{X}) > 0\}\).

!!! solution

    **a**.

    $$ \begin{align}
    f(X+tV)-f(X) &= Tr((X^T+tV^T)A(X+tV))-Tr(X^TAX) \\
        &= t Tr(V^TAX) + t Tr(X^TAV) + t^2 Tr(V^TAV) \\
        &= t Tr((AX)^T V) + t Tr((A^TX)^T V) + O (t^2)
    \end{align} $$

    So, \( \nabla f(X) = AX+A^TX \)

    ---

    **b**.

    Let

    $$ \begin{align}
    f(X+tV)-f(X) &=\ln\det (X+tV) - \ln \det (X) \\
        &= \ln(\det(X+tV)/\det(X)) \\
        &= \ln(\det(I+tVX^{-1}))    \\
        &= \ln(1+Tr(VX^{-1})t+O(t^2))  \\
        &= Tr((X^{-T})^T V) + O(t^2)
    \end{align} $$

    So, \( \nabla f(X) = X^{-T} \)






[textbook]: ../index.md#ee364a-convex-optimization-i-professor-stephen-boyd-stanford-university
[ref2]: ../index.md#最优化建模算法与理论