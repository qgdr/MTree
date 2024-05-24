# # problem
#
# uₜ = ∂ₓ(a(x)∂ₓu) + f(x, t)        (x, t) \in (0, 1)×(0, T]
# u(0, t) = β₀(t),    u(1, t) = β₁(t)
# u(x, 0) = α(x)


ξ = 2 // 3

function a(x::T) where T <: AbstractFloat
    if x <= ξ
        return 1//10 - 9//100 * x
    else
        return BigFloat(1//100)
    end
end

aₗ = BigFloat(1//10 - 9//100 *ξ)
aᵣ = BigFloat(1//100)


using Plots


# function f(x::BigFloat, t::BigFloat)
#     if x <= ξ
#         return 9//100 * π * exp(-1//10 * π^2 * t) * (cos(π * x) - π * x * sin(π * x))
#     else
#         return 6//100 * π^2 * exp(-1//10 * π^2 * t) * sin(4 * π * x)
#     end
# end
# fₗ = 9//100 * π * (cos(π * BigFloat(ξ)) - π * ξ * sin(π * BigFloat(ξ)))
# fᵣ = 6//100 * π^2 * sin(4 * π * BigFloat(ξ))

# function α(x::BigFloat)
#     if x <= ξ
#         return sin(π * x)
#     else
#         return sin(4 * π * x)
#     end
# end

α(x::BigFloat) = 0
β₀(t) = 0

β₁(t) = 0



function u_exact(x::BigFloat, t::BigFloat)
    if x <= ξ
        return sin(π * x) * exp(-1//10 * π^2 * t)
    else
        return sin(4 * π * x) * exp(-1//10 * π^2 * t)
    end
end

function ∂ₓu_exact(x::BigFloat, t::BigFloat)
    if x <= ξ
        return π * cos(π * x) * exp(-1//10 * π^2 * t)
    else
        return 4 * π * cos(4 * π * x) * exp(-1//10 * π^2 * t)
    end
end

K(x::BigFloat, t::BigFloat) = a(x) * ∂ₓu_exact(x, t)

# ## difference scheme
#
# ∂ₜUⱼⁿ = ∂ₓ(aⱼ₋ ∂̄̄ₓ Uⱼⁿ⁺¹) + Fⱼⁿ⁺¹      j=1,⋯, s+1; n=0, ⋯, N-1
# ∂ₜUⱼⁿ = ∂ₓ(aⱼ₋ ∂̄̄ₓ Uⱼⁿ) + Fⱼⁿ          j=s+2, ⋯, J-1; n=0, ⋯, N-1
# aⱼ₋ = a(xⱼ₋)          j- = j-1/2
# aₛ₊ = 1/(κ/aₗ + (1-\kappa)/aᵣ)


T = 1

J = 50
h = 1 // J

r = 20
τ = r * h^2
N = Int(T // τ)

r = τ / h^2

s = Int(floor(ξ / h))
κ = ξ/h - s


println("J = $J, N = $N, r=τ/h^2 = $τ/h^2 = $r, ξ = xₛ + κh = $s*$h + $κ h")

@show (1//2 - κ)*(fᵣ - fₗ)


using OffsetArrays

x = OffsetArray(collect(BigFloat, 0:h:1), 0:J)
t = OffsetArray(collect(BigFloat, 0:τ:T), 0:N)



a_mhh = parent(a.(x[1:J] .- h//2)) # mhh := minus half of h ; a_(j-1/2) ; a_(1/2), a_(3/2), ..., a_(J-1/2)
@assert length(a_mhh) == J "a_half length is wrong"

a_mhh[s+1] = 1/(κ/aₗ + (1-κ)/aᵣ)

# plot(x[1:end].-h//2, a_mhh)
# plot!(a)

# ## Calculate Fⱼⁿ
# 
# Fⱼⁿ = 1/h ∫[x_(j-1/2), x_(j+1/2)] f(x, tⁿ) dx

F = OffsetMatrix(zeros(J-1, N+1), 1:J-1, 0:N)       # F_1, F_2, ..., F_(J-1)

# Intfl(x::BigFloat, t::BigFloat) = x*cos(π * x) * 9//100 * π * exp(-1//10 * π^2 * t)
# Intfr(x::BigFloat, t::BigFloat) = -cos(4 * π * x) * 6//400 * π * exp(-1//10 * π^2 * t)

# F[1:s-1, :] = Intfl.( x[1:s].-h//2, t') |> parent |> mat -> diff(mat, dims=1)  / h
# F[s+2:J-1, :] = Intfr.( x[s+2:J].-h//2, t') |> parent |> mat -> diff(mat, dims=1)  / h

# ξ = BigFloat(ξ)
# if  1//2 < κ < 1
#     F[s, :] = ( Intfl.(x[s]+h//2, t') - Intfl.(x[s]-h//2, t') ) / h
#     F[s+1, :] = ( Intfl.(ξ, t') - Intfl.(x[s+1]-h//2, t') + Intfr.(x[s+1]+h//2, t') - Intfr.(ξ, t') ) / h
# elseif 0 < κ < 1//2
#     F[s, :] = ( Intfl.(ξ, t') - Intfl.(x[s]-h//2, t') + Intfr.(x[s]+h//2, t') - Intfr.(ξ, t') ) / h
#     F[s+1, :] = ( Intfr.(x[s+1]+h//2, t') - Intfr.(x[s+1]-h//2, t') ) / h
# elseif 1//2 == κ
#     F[s, :] = ( Intfl.(x[s]+h//2, t') - Intfl.(x[s]-h//2, t') ) / h
#     F[s+1, :] = ( Intfr.(x[s+1]+h//2, t') - Intfr.(x[s+1]-h//2, t') ) / h
# else
#     error("κ is not in (0, 1)")
# end

# # Fⱼⁿ - f(xⱼ, tⁿ) = O(h²)
# @show ( F - f.(x, t')[1:J-1, :] .|> abs |> maximum )

# plot(x[1:J-1], F[:, 0])
# plot!(x[1:J-1], f.(x, t')[1:J-1, 0])


# ## Ex/Im scheme
# 
# ### initial condition

# U_exact = u_exact.(x, t')
U = OffsetMatrix(zeros(BigFloat, J+1, N+1), 0:J, 0:N)     # U_0, U_1, ..., U_J

U[:,0] = α.(x)
U[0,:] = β₀.(t)
U[J,:] = β₁.(t)

using LinearAlgebra

for n in 0:N-1
    # Explicit
    for j = s+2:J-1
        U[j, n+1] = U[j, n]*(1 - r * (a_mhh[j] + a_mhh[j+1]))  + r * (a_mhh[j]*U[j-1, n] + a_mhh[j+1]*U[j+1, n]) + τ * F[j, n]
    end

    # Implicit
    A = diagm(0 => 1 .+r.*(a_mhh[1:s+1] + a_mhh[2:s+2]), 1 => -r.*a_mhh[2:s+1], -1 => -r.*a_mhh[2:s+1])
    b = @. U[1:s+1, n] + τ*F[1:s+1, n+1]
    b[1] += r*a_mhh[1]*U[0, n+1]
    b[s+1] += r*a_mhh[s+2]*U[s+2, n+1]
    @assert size(A) == (s+1, s+1)
    @assert length(b) == (s+1)
    U[1:s+1, n+1] = A \ b
end





# @show plot(a, range=[0, 1])
# @show plot(parent(x), parent(t), u_exact, st=:surface)
# @show plot!(Float64(ξ)*ones(length(parent(t))), parent(t) .|> Float64, u_exact.(ξ, parent(t)) .|> Float64, color=:blue)
# @show plot!(Float64(ξ)*ones(length(parent(t))), parent(t) .|> Float64, -1*ones(length(parent(t))), color=:black)

# display(plot3d!)


U .|> abs |> maximum
