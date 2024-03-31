# HW3

[HW3pdf](../HWpdf/Homework4-Optimization-2024.pdf)


## 1. Exercise 4.24 of [Convex Optimization][textbook]

Complex  \(l_1\)-, \(l_2\)- and \(l_\infty\)-norm approximation.

Consider the problem

$$ \text{minimize} \|Ax - b\|_p $$

where \(A \in C^{m\times n}, b \in C^m\), and \(x \in C^n\).    
For \(p\le 1\), the complex \(l_p\)-norm is defined by

$$ \|y\|_p = \left(\sum_{i=1}^m |y_i|^p\right)^{1/p} $$

For \(p=1,2, \text{and} \infty\), express the complex \(l_p\)-norm approximation problem as a QCQP or SOCP with real variables and date.


!!! solve











[textbook]: ../index.md#ee364a-convex-optimization-i-professor-stephen-boyd-stanford-university
[ref2]: ../index.md#最优化建模算法与理论