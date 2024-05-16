# HW6

## 1

Low-rank Matrix Recovery. 
Given the observation \(b = \mathcal{A}(X_0) + e ∈ \mathbb{R}^m\), where the mapping \(\mathcal{A}(X) = (〈A_j, X〉)_{j=1}^m\) for any matrix \(X ∈ \mathbb{R}^{n_1×n_2}\) and \(m < \min\{n_1, n_2\}, e ∈ \mathbb{R}^m\) is the possible error or noise. 
We aim to recover the unknown lowrank matrix \(X_0\) from the observations \(b\). Consider the matrix regularized least absolute deviation (Matrix RLAD) model 

$$ \min_X ‖\mathcal{A}(X) − b‖_1 + λ‖X‖_∗ $$

where \(‖·‖_∗\) is the nuclear norm and \(‖·‖_1\) is the \(l_1\) norm.
Please design an solving algorithm based on ADMM and give the closed solution of each subproblem.



**solution**

!!! Try

    The augmented Lagrangian function is

    $$ \mathcal{L}_\rho(y, X ;\nu) = ‖y‖_1 + λ‖X‖_∗ + \nu^T(y - \mathcal{A}(X)+b) + \frac{\rho}{2}‖y - \mathcal{A}(X)+b‖_2^2 $$

    The ADMM algorithm is

    step 1:

    $$ \begin{aligned}
        y^{k+1} &= \arg\min_y \mathcal{L}_\rho(y, X^k ;\nu^k) \\
        &= \arg\min_y \|y\|_1 + (\nu^k)^T y + \frac{\rho}{2}‖y - \mathcal{A}(X^k)+b‖_2^2 \\
    \end{aligned} $$

    That is 

    $$ \begin{aligned}
        0 &= \partial \|y^{k+1}\|_1 + \nu^k + \rho(y^{k+1} - \mathcal{A}(X^k)+b)        \\
        &=  \partial \|y^{k+1}\|_1 + \rho y^{k+1} + \nu^k- \rho (\mathcal{A}(X^k)-b) \\
    \end{aligned} $$

    Let \(z = -\nu^k+ \rho (\mathcal{A}(X^k)-b)\)

    $$ y^{k+1}_i = \begin{cases}
        0, & \text{if } |z_i| \leq 1 \\
        \text{sign}(z_i)\frac{|z_i|-1}{ρ}, & \text{if } |z_i| > 1
    \end{cases} $$


    step 2:

    $$ \begin{aligned}
        X^{k+1} &= \arg\min_X \mathcal{L}_\rho(y^{k+1}, X ;\nu^k) \\
        &= \arg\min_X λ‖X‖_∗ - (\nu^k)^T\mathcal{A}(X) + \frac{\rho}{2}‖y^{k+1} - \mathcal{A}(X)+b‖_2^2
    \end{aligned} $$

    can not give a closed solution.

    step 3:

    $$ \begin{aligned}
        \nu^{k+1} &= \nu^k + \tau \rho(y^{k+1} - \mathcal{A}(X^k) + b) \\
    \end{aligned} $$



Now, we insert a variable \(Z=X\) into the Lagrangian function.

$$ \begin{aligned}
    \mathcal{L}_\rho (y, X, Z; \nu, \Lambda) 
    =&  ‖y‖_1 + λ‖X‖_∗ + \nu^T(y - \mathcal{A}(Z)+b) + \Lambda^T(Z - X)    \\
    &+ \frac{\rho_1}{2}‖y - \mathcal{A}(Z)+b‖_2^2 + \frac{\rho_2}{2}‖Z - X‖_2^2
\end{aligned}   $$

Then we can get the following ADMM algorithm.

Step 1:

$$ \begin{aligned}
    y^{k+1} &= \arg\min_y \mathcal{L}_\rho(y, X^k, Z^k ;\nu^k, \Lambda^k) \\
    &= \arg\min_y ‖y‖_1 + (\nu^k)^T y + \frac{\rho_1}{2}‖y - \mathcal{A}(Z^k)+b‖_2^2    \\
    &= \text{Prox}_{\|\cdot\|_1/ρ_1} (\mathcal{A}(Z^k)-b-\frac{\nu^k}{\rho_1})
\end{aligned} $$

Let \(z = -\nu^k+ \rho (\mathcal{A}(Z^k)-b)\)

$$ y^{k+1}_i = \begin{cases}
    0, & \text{if } |z_i| \leq 1 \\
    \text{sign}(z_i)\frac{|z_i|-1}{ρ_1}, & \text{if } |z_i| > 1 \\
\end{cases} $$

Step 2:

$$ \begin{aligned}
    X^{k+1} &= \arg\min_X \mathcal{L}_\rho(y^{k+1}, X , Z^k ;\nu^k, \Lambda^k) \\
    &= \arg\min_X λ‖X‖_∗ - (\Lambda^k)^T X + \frac{\rho_2}{2}‖Z^k-X‖_2^2       \\
    % &= \arg\min_X ‖X‖_∗  + \frac{\rho_2}{2\lambda}‖Z^k+\frac{1}{\rho_2}\Lambda^k-X‖_2^2       \\
    &= \text{Prox}_{\frac{\lambda}{\rho_2}\|·\|_*} (Z^k+\frac{1}{\rho_2}\Lambda^k)    \\
    &= \text{SVT}_{\frac{\lambda}{\rho_2}} (Z^k+\frac{1}{\rho_2}\Lambda^k)
\end{aligned} $$

Step 3:

$$ \begin{aligned}
    Z^{k+1} &= \arg\min_Z \mathcal{L}_\rho(y^{k+1}, X^{k+1}, Z ;\nu^k, \Lambda^k) \\
    &= \arg\min_Z  -(\nu^k)^T\mathcal{A}(Z) + (\Lambda^k)^T Z +  \frac{\rho_1}{2}‖y^{k+1} - \mathcal{A}(Z)+b‖_2^2 + \frac{\rho_2}{2}‖Z - X^{k+1}‖_2^2    \\
    &= \arg\min_Z    \frac{\rho_1}{2}‖y^{k+1} +b + \frac{\nu^k}{\rho_1} - \mathcal{A}(Z)‖_2^2 + \frac{\rho_2}{2}‖Z+\frac{1}{\rho_2}\Lambda^k - X^{k+1}‖_2^2    \\
\end{aligned} $$

That is 

$$ \begin{gather*}
    \rho_1 \mathcal{A}^* (\mathcal{A}(Z) - y^{k+1} - b - \frac{\nu^k}{\rho_1}) + \rho_2(Z+\frac{1}{\rho_2}\Lambda^k - X^{k+1}) \\
    \Rightarrow
    Z = (\rho_2 I + \rho_1 \mathcal{A}^*\mathcal{A})^{-1}( \rho_1 \mathcal{A}^*(y^{k+1} + b + \frac{\nu^k}{\rho_1}) + \rho_2 X^{k+1} - \Lambda^k)
\end{gather*} $$

Step 4:

$$ \nu^{k+1} = \nu^k + \tau \rho_1(y^{k+1} - \mathcal{A}(Z^{k+1}) + b) $$

$$ \Lambda^{k+1} = \Lambda^k + \tau \rho_2(Z^{k+1} - X^{k+1}) $$




## 2

Robust PCA. Given the observation \(b = \mathcal{A}(L_0 + S_0) + e ∈ R^m\), where the mapping \(\mathcal{A}(X) = (〈A_j, X_0〉)_{j=1}^m\) for any \(X ∈ R^{n_1×n_2}\) and \(m < \min\{n_1, n_2\}, e ∈ R^m\) is the possible error or noise. We aim to recover the unknown low-rank matrix \(L_0\) and sparse matrix \(S_0\) from the observations \(b\). Consider the Matrix Lasso model with two variables 

$$ \min_{L,S} \frac{1}{2ρ} ‖\mathcal{A}(L + S) − b‖_2^2 + λ‖L‖_∗ + ‖S‖_1.$$

where \(‖·‖_∗\) is the nuclear norm and \(‖·‖_1\) is the \(l_1\) norm. Please design an solving algorithm based on ADMM and give the closed solution of each subproblem.


**solution**

The Lagrangian function is

$$ \begin{aligned}
    \mathcal{L}_{\mu}(X, L, S; \nu) =&  \frac{1}{2ρ} ‖\mathcal{A}(X) − b‖_2^2 + λ‖L‖_∗ + ‖S‖_1 \\
    &+ \nu^T(\mathcal{A}(X) - L - S - b) + \frac{\mu}{2}‖\mathcal{A}(X) - L - S - b ‖_2^2  \\
    =&  \frac{1}{2ρ} ‖\mathcal{A}(X) − b‖_2^2 + λ‖L‖_∗ + ‖S‖_1 \\
    &+ \frac{\mu}{2}‖\mathcal{A}(X) - L - S - b + \frac{\nu}{\mu}‖_2^2  - \frac{1}{2\mu}\|\nu\|_2
\end{aligned} $$


Step 1:

$$ \begin{aligned}
    X^{k+1} &= \arg\min_X \mathcal{L}_{\mu}(X, L^k, S^k ;\nu^k) \\
    &= \arg\min_X \frac{1}{2ρ} ‖\mathcal{A}(X) − b‖_2^2 + \frac{\mu}{2}‖\mathcal{A}(X) - L^k - S^k - b + \frac{\nu^k}{\mu}‖_2^2\\
\end{aligned} $$

The point can be get by

$$ \begin{gather*}
    0 = \frac{1}{\rho}\mathcal{A}^*(\mathcal{A}(X) − b)+ \mu \mathcal{A}^*(\mathcal{A}(X) - L - S - b + \frac{\nu}{\mu}) \\
    \Rightarrow X = ((\frac{1}{\rho}+\mu)\mathcal{A}^*\mathcal{A})^{\dagger }\mathcal{A}^*((\frac{1}{\rho}+\mu)b + \mu(L + S) + \nu)
\end{gather*} $$

$$ X^{k+1} = ((\frac{1}{\rho}+\mu)\mathcal{A}^*\mathcal{A})^{\dagger } \;
\mathcal{A}^*((\frac{1}{\rho}+\mu)b + \mu(L^k + S^k) + \nu^k) $$


Step 2:

$$ \begin{aligned}
    L^{k+1} &= \arg\min_L \mathcal{L}_{\mu}(X^{k+1}, L, S^k ;\nu^k) \\
    &= \arg\min_L λ‖L‖_∗ + \frac{\mu}{2}‖\mathcal{A}(X^{k+1}) - L - S^k - b + \frac{\nu^k}{\mu}‖_2^2 \\
    &= \text{Prox}_{\frac{\lambda}{\mu}\|\cdot\|_*} (\mathcal{A}(X^{k+1}) - S^k - b + \frac{\nu^k}{\mu})    \\
    &= \text{SVT}_{\frac{\lambda}{\mu}} (\mathcal{A}(X^{k+1}) - S^k - b + \frac{\nu^k}{\mu})
\end{aligned} $$



Step 3:

$$ \begin{aligned}
    S^{k+1} &= \arg\min_S \mathcal{L}_{\mu}(X^{k+1}, L^{k+1}, S ;\nu^k) \\
    &= \arg\min_S ‖S‖_1 + \frac{\mu}{2}‖\mathcal{A}(X^{k+1}) - L^{k+1} - S - b + \frac{\nu^k}{\mu}‖_2^2 \\
    &= \text{Prox}_{\frac{1}{\mu}\|·\|_1} (\mathcal{A}(X^{k+1}) - L^{k+1} - b + \frac{\nu^k}{\mu})    \\
\end{aligned} $$

Let \(z = \mathcal{A}(X^{k+1}) - L^{k+1} - b + \frac{\nu^k}{\mu}\)

$$ S^{k+1}_i = \text{sign}(z_i)((|z_i|-\frac{1}{\mu})^+)  $$



Step 4:

$$ \nu^{k+1} = \nu^k + \tau \mu(\mathcal{A}(X^{k+1}) - L^{k+1} - S^{k+1} - b) $$


