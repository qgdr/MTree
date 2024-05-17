#  Convolution 卷积

设 \(f,g\) 是 \(\mathbb{R}^n\) 上的可测函数，我们定义他们的卷积为

$$ f*g(x) = \int_{\mathbb{R}^n} f(x-t)g(t)dt = \int_{\mathbb{R}^n} f(t)g(x-t)dt $$


## 卷积的理解

卷积 Convolution 是什么？       
其实我更喜欢他的另一个名字 <font color="red">叠加 Superposition</font>.

参考 [奥本海默 信号与系统](../../Library/Alan%20V.%20Oppenheim_%20Alan%20S.%20Willsky%20-%20信号与系统%20.pdf)

\(f*g\) 可以理解为把函数（信号） \(g(x)\) 向右平移 \(t\) 后的 \(f(t)\) 相加。   
这个叠加是 **线性**  的！


## 卷积的性质

有了 线性叠加 的理解，我们能很直观的看到

Part 1:

祖暅原理

$$ \int_{\mathbb{R}^n} f*g(x) dx = \int_{\mathbb{R}^n} f(t) dt \int_{\mathbb{R}^n} g(t)dt $$


Part 2:

$$ D(f*g) = Df * g = f * Dg $$

若 \(g\in C^k(\mathbb{R}^n), f\in L^1(\mathbb{R}^n)\)，则 \(f*g \in C^k(\mathbb{R}^n)\)


