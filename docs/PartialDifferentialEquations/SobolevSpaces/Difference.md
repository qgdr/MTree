# Difference quotients 差商

本节研究 \(W^{k, p}(\Omega)\) 的可微性，核心方法是用 **差商**  \(D^h u\) 去逼近。       

我们会有这样的疑问：弱导数存在，函数可微吗？

我们将使用差商逼近导数，那么我们提出两个基本问题问题：

对于 \(u\in W^{1, p}(\Omega)\)，\(D^h u\) 是否逼近 \(Du\)?         

对于 \(u\in L^p(\Omega)\) ， \(D^h u\) 有界是否能推出可微或弱导数存在 ？

我们将回答这些问题。

## Difference quotients and weak derivatives 差商与弱导数

### \(D^hu\) 被 \(Du\) 控制





### \(D^hu\) 有界则弱导存在

我们先给出 **反例**

!!! Example

    考虑有界区间 \(\Omega\) 上的阶跃函数

    $$ u(x) = \begin{cases} 0 & x < 0 \\ 1 & x \geq 0 \end{cases} $$

    那么

    $$ D^hu(x) = \frac{u(x+h)-u(x)}{h} = \begin{cases} \frac{1}{h} & x \in [-h, 0) \\ 0 & \text{otherwise} \end{cases} $$

    对于 \(V\subset\subset \Omega\)，

    $$ \int_V  |D^hu(x)| \le \frac{1}{h} \cdot h = 1 $$

    但是我们知道 \(u(x)\) 没有弱导数，或者说他的导数是 \(\delta(x)\) 函数。

    所以当 \(p=1\) 是 \(\|D^hu\|_{L^p(V)} \le C\) 还不能推出弱导数的存在性。

    但是当 \(p>1\) 时，上面的情况不会出现，即 \(\|D^hu\|_{L^p(V)} \to \infty \text{ as } h\to 0\). 



