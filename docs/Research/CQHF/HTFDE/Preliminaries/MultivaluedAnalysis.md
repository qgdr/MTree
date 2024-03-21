# 多值分析

For a normed space \((X, \|\cdot\|)\) ,let 

$$ \begin{gather*}
    \mathscr{P}_{cl}(X) = \{ Y \in \mathscr{P}: Y \textsf{ is closed } \}   \\
    \mathscr{P}_{b}(X) = \{ Y \in \mathscr{P}: Y \textsf{ is bounded } \}   \\
    \mathscr{P}_{cp}(X) = \{ Y \in \mathscr{P}: Y \textsf{ is compact } \}   \\
    \mathscr{P}_{cp,c}(X) = \{ Y \in \mathscr{P}: Y \textsf{ is compact and convex } \}   \\
    \mathscr{P}_{cl, b}(X) = \{ Y \in \mathscr{P}: Y \textsf{ is closed and bounded } \}   
\end{gather*} $$


A multivalued map \(G: X \to \mathscr{P}(X)\)

3 . 称为 **上半连续**(upper semi-continuous (u.s.c.))， 若


```julia
--8<-- "docs/Research/CQHF/HTFDE/Preliminaries/MA.jl:usc"
```

4 . 称为 **下半连续**(lower semi-continuous (l.s.c.))， 若

```julia
--8<-- "docs/Research/CQHF/HTFDE/Preliminaries/MA.jl:lsc"
```

!!! think
    我们在凸优化中定义过所谓 [下半连续](../../../../ConvexOptimization/ConvexFunction/index.md#下半连续)。他是由单值函数的连续性来定义的。  
    而在多值函数中，没有了实数的 **序关系** 和 **连续性**，那么应该用何种方式来替代呢？     
    在多值函数中，我们使用了 **集合的序关系关系** 以及由 **开集** 所描绘的连续性。  
    如果不理解，对于一个下半连续函数 \(f(x)\) ，不妨令 \( G(x) = \{y | y \le f(x)\}\)，是不是就一目了然了。