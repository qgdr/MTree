# 线性多步法 (Linear Multistep Methods)

[Finite Difference Methods 5.9, Chapter 6][textbook]

考虑 [IVP](./index.md#初值问题-initial-value-problems)

$$ u'(t) = f(u(t), t) $$

分别对两边用有限差分替代

$$ \frac{\sum_{j=0}^r \alpha_j U^{n+j}}{k} = \sum_{j=0}^r \beta_j f(U^{n+j}, t_{n+j}) $$

就得到了 \(r\) 步 LMM 公式

$$ \sum_{j=0}^r \alpha_j U^{n+j} = k\sum_{j=0}^r \beta_j f(U^{n+j}, t_{n+j}) $$

\(U^{n+r}\) 由前面的 \(n-1\) 个 \( U^{n+r-1}, U^{n+r-2}, \cdots, U^{n} \) 和 \(f\) 在这些点处的值按等式获得。











[textbook]: ../index.md#finite-difference-methods-for-ordinary-and-partial-differential-equations