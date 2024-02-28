# 偏微分方程简介

本章介绍各个偏微分方程的定义以及一些常用的结论。

## 准备符号

令 \\( \alpha=(\alpha_1, ... , \alpha_n), \quad \alpha_n \ge 0 \\)，

$$ |\alpha| := \alpha_1 + ... + \alpha_n $$
$$ \alpha ! := \alpha_1!\cdots\alpha_n! $$

$$ D^\alpha u(x) := \frac{\partial^{\alpha_1} u}{\partial x^{\alpha_1}}\cdots\frac{\partial^{\alpha_n} u}{\partial x^{\alpha_n}} $$
$$ D^k u(x) = \\{ D^\alpha u(x) \mid |\alpha|=k \\} $$

nabla算子
$$ \nabla u = (\frac{\partial u}{\partial x_i}, ..., \frac{\partial u}{\partial x_n}) $$
Laplace算子
$$ \Delta u = \nabla\cdot\nabla u = \frac{\partial^2 u}{\partial x_i^2} + ... + \frac{\partial^2 u}{\partial x_n^2} $$

## Exercise

> \\( D^k u(x) \\) 有几项？
> 
> 事实上，就是将 \\(n\\) 个苹果，放进 \\(k\\) 个盒子，那么显然有 \\( \begin{pmatrix}n+k-1\\\\ k \end{pmatrix} \\) 种放法。
<!-- 
<div class="warning">
\(D^k u(x)\) 有几项？
</div> -->
