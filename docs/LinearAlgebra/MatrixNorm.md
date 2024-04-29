# 矩阵范数

[Roger A.Horn Matrix Analysis 5.6 Matrix norms](./index.md#roger)       
[Boyd Convex optimization A.1](https://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)

##  Inner product and Euclidean norm

### 矩阵内积

$$ \langle A, B \rangle = \sum_{i,j} a_{ij}b_{ij} = Tr(AB^T) = Tr(A^TB) $$

### Frobenius Norm

对于一个矩阵 \(A\)，

$$ \begin{align}
    \|A\|_F  &= \sqrt{\langle A, A \rangle}     \\
    &= \sqrt{\sum_{i,j} |a_{ij}|^2}             \\
    &= \sqrt{Tr(AA^T)} = \sqrt{Tr(A^TA)}        \\
    &= \sqrt{\sum_{i=1}^n \sigma_i^2}
\end{align} $$


其中 \(\sigma_i\) 是 \(A\) 的奇异值。


所以这构成了一个 **内积空间** ，自然有 **Cauchy 不等式**

$$ \langle A, B \rangle \le \|A\|_F \|B\|_F $$

这些范数的定义在不同的书中有些混乱，需要根据具体的情况来选择。

## \(l_p\)-Norm

### sum-absolute-value norm

$$ \|A\|_{\text{sav}} = \sum_{i,j}^n |a_{ij}| $$

### maximum-absolute-value norm

$$ \|A\|_{\text{mav}} = \max_{i,j} |a_{ij}| $$

!!! warning 
    上面这两种范数有的时候会用 \(\|A\|_{p}\) 来表示，相应的算子范数可能会用更奇怪的符号 \(\|| A \||\) 表示。    
    但是因为一般的 \(l_p\) 范数不常用，
    最常用的 Frobenius 范数，我们用 \(\|\cdot\|_F\) 来表示，        
    所以，如果不特殊说明，我们通常用 \(\|\cdot\|_p\) 来表示 **算子范数**！       
    也就是说，我们与 [Boyd Convex optimization A.1](https://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) 保持一致。





## 算子范数 Operator norms






我们仅需要一点点泛函分析的知识

对于一个线性算子 \(A \in \mathcal{L}(X, Y)\)，我们定义他的范数是

$$ \|A\|_{\mathcal{L}(X, Y)} = \sup_{x \in X} \frac{\|Ax\|_Y}{\|x\|_X} $$

!!! warning 

    这里的范数都是对应空间的范数，而不是欧式距离！

我们常见的情况为： \(A\) 是矩阵 \(X=Y=R^n\), **向量范数** 为 \(\|\cdot\|_p, p=1, 2, \infty\) 的情况。

## \(\|A\|_1\) 

对于 \(\|x\|_1 = \sum_{i=1}^m|x_i|\)，我们有

$$ \|A\|_1 = \max_j\sum_{i=1}^m|a_{i,j}| $$

事实上，

$$ \begin{align}
\dfrac{\|A x\|_1}{\| x\|_1} 
&= \dfrac{\|\sum_{j=1}^n A[:,j]x_j\|_1}{\sum_{j=1}^n|x_j|}
\le \dfrac{\sum_{j=1}^n \|A[:,j]\|_1 |x_j|}{\sum_{j=1}^n|x_j|} \\
&\le \dfrac{(\sum_{j=1}^n|x_j|)\max_j \|A[:,j]\|_1}{\sum_{j=1}^n|x_j|} \\
&= \max_j \|A[:,j]\|_1
\end{align} $$

且能取到，令 $j$ 使得 $\|A[:,j]\|_1=\sum_{i=1}^n|a_{ij}|$ 最大, 那么令 $x= e_j$,
则 $\| e_j\|_1=1$ 且 $\|A e_j\|_1=\sum_{i=1}^n|a_{ij}|$

## \(\|A\|_2\) 

也称 **谱范数** spectral norm.     
对于 \(\|x\|_2 = \sqrt{\sum_{i=1}^m|x_i|^2}\)，我们有

$$ \|A\|_2 = \max_j \sigma_j = \sqrt{\lambda_{\max}(A^T A)} $$

直接参考 [svd](svd.md) 即可。


## \(\|A\|_\infty\)

对于 \(\|x\|_\infty = \max_{i=1}^m|x_i|\)，我们有

$$ \|A\|_\infty = \max_i\sum_{j=1}^n|a_{i,j}| $$

事实上，

$$ \begin{align}
\dfrac{\|A x\|_\infty}{\| x\|_\infty} 
&= \dfrac{\max_i |A[i, :]x|}{\max_i|x_i|}
\le \dfrac{\max_i\sum_{j=1}^n |a_{ij}||x_j|}{\max_i|x_i|} \\
&\le \dfrac{\max_i\sum_{j=1}^n |a_{ij}| \max_i |x_j|}{\max_i|x_i|} \\
&= \max_i \|A[i, :]\|_1
\end{align} $$



## 对偶范数 Dual Norm


对偶范数其实也是一种 算子范数，只是这个算子是一个 **泛函**，

$$ F_A: R^{m\times n} \to R, \quad F_A(B) = \langle A, B \rangle = Tr(AB^T) $$

则对于某个 *矩阵范数* \(\|\cdot\|\)

$$ \|A\|_* = \sup_{\|B\|\le 1} \langle A, B \rangle 
= \sup_{B \neq O} \frac{\langle A, B \rangle}{\|B\|} = \sup_{B \neq O} \frac{Tr(AB^T)}{\|B\|} $$



### 核范数 nuclear Norm

对于一个矩阵 \(A\)，我们称 \(\|\cdot\|_2\) [谱范数](./MatrixNorm.md#a_2) 的对偶范数为 核范数 \(\|\cdot\|_{2*}\)

$$ \|A\|_{2*} = \sup_{\|B\|_2\le 1} \langle A, B \rangle $$

那么他到底等于什么呢？事实上，  
令 \(A = U_A\Sigma_A V_A^T,  B = U_B \Sigma_B V_B^T\)

$$ \begin{align}
    \|A\|_{2*} &= \sup_{B \neq O} \frac{Tr(AB^T)}{\|B\|_2}  
    = \sup_{B \neq O} \frac{Tr(U_A\Sigma_A V_A^T V_B \Sigma_B U_B^T)}{\sigma_1(B)} \\
    &= \sup_{B \neq O} \frac{Tr(U_B^TU_A\Sigma_A V_A^T V_B \Sigma_B )}{\sigma_1(B)} 
    = \sup_{B \neq O} \frac{Tr(U\Sigma_A V^T \Sigma_B )}{\sigma_1(B)} \\
    &\le \sup_{B \neq O} \frac{|Tr(U\Sigma_A V^T )| \sigma_1(B)}{\sigma_1(B)} \\
    &= |Tr((V^TU) \Sigma_A)| 
    = |\sum_{i=1}^r \langle v_i, u_i \rangle\sigma_i(A)|  \\
    &\le \sum_{i=1}^r \sigma_i(A)  \\
\end{align} $$

而这个上界明显可以取到，令 \(B = U_A \text{diag}(1) V_A^T\)，           
那么 \(\|B\|_2 = 1\)，且 

$$ Tr(AB^T)=Tr(U_A \Sigma_A \text{diag}(1) U_A^T) = Tr(\Sigma_A \text{diag}(1)) = \sum_{i=1}^r \sigma_i(A) $$

因此

$$ \|A\|_{2*} = \sum_{i=1}^r \sigma_i(A) $$

其中 \(\sigma_i\) 是 \(A\) 的非零奇异值， \(r=\text{rank}(A)\).

同时由范数性质我们还有

$$ \langle A, B \rangle \le \|A\|_{2*} \|B\|_{2} $$