# 共轭函数 (The conjugate function)

设函数 \(f: R^n \to R\)，函数 \(f^*: R^n \to R\)，

$$ f^*(y) = \sup_{x\in \text{dom}f} \{y^T x - f(x)\} $$

称为 \(f\) 的 **共轭函数**(conjugate function)。

!!! view
    我们如何直观的理解什么是共轭函数呢？

    $$ f^*(y) = \sup_{x\in \text{dom}f} \{y^T x - f(x)\} = -\inf_{x\in \text{dom}f} \{f(x) - y^T x\} $$

    <video src="../media/videos/convexfunc/720p30/ConjugateFunc.mp4" width="100%"  type="video/mp4" controls="controls" frameborder="0" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" oallowfullscreen="true" msallowfullscreen="true"></video>

!!! theorem
    共轭函数是无条件凸的！

    ![conjugate](media/images/convexfunc/ConjugateConvex_ManimCE_v0.18.0.png)

