# 矩阵范数

我们仅需要一点点泛函分析的知识

对于一个线性算子 \(A \in \mathcal{L}(X, Y)\)，我们定义他的范数是

$$ \|A\|_{\mathcal{L}(X, Y)} = \sup_{x \in X} \frac{\|Ax\|_Y}{\|x\|_X} $$

注意：这里的范数都是对应空间的范数，而不是欧式距离！

现在我们考虑 \(A\) 是矩阵 \(X=Y=R^n\), 范数为 \(\|\cdot\|_p, p=1, 2, \infty\) 的情况。

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

且能取到，令 $j\in [1, n]$ 使得 $\sum_{i=1}^n|a_{ij}|$ 最大, 那么令 $x= e_j$,
则 $\| e_j\|_1=1$ and $\|A e_j\|_1=\sum_{i=1}^n|a_{ij}|$

## \(\|A\|_2\) 

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