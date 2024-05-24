# # problem
#
# uₜ = ∂ₓ(a(x)∂ₓu) + f(x, t)        (x, t) \in (0, 1)×(0, T]
# u(0, t) = β₀(t),    u(1, t) = β₁(t)
# u(x, 0) = α(x)
Float = Float64

const ξ = 2 // 3

function a(x::T) where T <: AbstractFloat
    if x <= ξ
        return 1//10 - 9//100 * x
    else
        return Float(1//100)
    end
end

const aₗ = Float(1//10 - 9//100 *ξ)
const aᵣ = Float(1//100)


# using Plots


function f(x::Float, t::Float)
    if x <= ξ
        return 9//100 * π * exp(-1//10 * π^2 * t) * (cos(π * x) - π * x * sin(π * x))
    else
        return 6//100 * π^2 * exp(-1//10 * π^2 * t) * sin(4 * π * x)
    end
end

const fₗ = 9//100 * π * (cos(π * Float(ξ)) - π * ξ * sin(π * Float(ξ)))
const fᵣ = 6//100 * π^2 * sin(4 * π * Float(ξ))

Intfl(x::Float, t::Float) = x*cos(π * x) * 9//100 * π * exp(-1//10 * π^2 * t)
Intfr(x::Float, t::Float) = -cos(4 * π * x) * 6//400 * π * exp(-1//10 * π^2 * t)


function α(x::Float)
    if x <= ξ
        return sin(π * x)
    else
        return sin(4 * π * x)
    end
end


β₀(t) = 0

β₁(t) = 0



function u_exact(x::Float, t::Float)
    if x <= ξ
        return sin(π * x) * exp(-1//10 * π^2 * t)
    else
        return sin(4 * π * x) * exp(-1//10 * π^2 * t)
    end
end


function ∂ₓu_exact(x::Float, t::Float)
    if x <= ξ
        return π * cos(π * x) * exp(-1//10 * π^2 * t)
    else
        return 4 * π * cos(4 * π * x) * exp(-1//10 * π^2 * t)
    end
end

K(x::Float, t::Float) = a(x) * ∂ₓu_exact(x, t)

# ## difference scheme
#
# ∂ₜUⱼⁿ = ∂ₓ(aⱼ₋ ∂̄̄ₓ Uⱼⁿ⁺¹) + Fⱼⁿ⁺¹      j=1,⋯, s+1; n=0, ⋯, N-1
# ∂ₜUⱼⁿ = ∂ₓ(aⱼ₋ ∂̄̄ₓ Uⱼⁿ) + Fⱼⁿ          j=s+2, ⋯, J-1; n=0, ⋯, N-1
# aⱼ₋ = a(xⱼ₋)          j- = j-1/2
# aₛ₊ = 1/(κ/aₗ + (1-\kappa)/aᵣ)

using OffsetArrays
using LinearAlgebra

const T = 1

function eierror(J::Int, N::Int, ξ)
    # J = 200
    h = 1 // J
    τ = T // N
    r = τ / h^2

    s = Int(floor(ξ / h))
    κ = ξ/h - s


    println("J = $J, N = $N, r=$r, ξ = $ξ, ξ = xₛ + κh = $s*$h + $κ h")

    @show (1//2 - κ)*(fᵣ - fₗ)



    x = OffsetArray(collect(Float, 0:h:1), 0:J)
    t = OffsetArray(collect(Float, 0:τ:T), 0:N)



    a_mhh = parent(a.(x[1:J] .- h//2)) # mhh := minus half of h ; a_(j-1/2) ; a_(1/2), a_(3/2), ..., a_(J-1/2)
    @assert length(a_mhh) == J "a_half length is wrong"

    a_mhh[s+1] = 1/(κ/aₗ + (1-κ)/aᵣ)

    # plot(x[1:end].-h//2, a_mhh)
    # plot!(a)

    # ## Calculate Fⱼⁿ
    # 
    # Fⱼⁿ = 1/h ∫[x_(j-1/2), x_(j+1/2)] f(x, tⁿ) dx

    F = OffsetMatrix(zeros(J-1, N+1), 1:J-1, 0:N)       # F_1, F_2, ..., F_(J-1)

    F[1:s-1, :] = Intfl.( x[1:s].-h//2, t') |> parent |> mat -> diff(mat, dims=1)  / h
    F[s+2:J-1, :] = Intfr.( x[s+2:J].-h//2, t') |> parent |> mat -> diff(mat, dims=1)  / h

    ξ = Float(ξ)
    if  1//2 < κ < 1
        F[s, :] = ( Intfl.(x[s]+h//2, t') - Intfl.(x[s]-h//2, t') ) / h
        F[s+1, :] = ( Intfl.(ξ, t') - Intfl.(x[s+1]-h//2, t') + Intfr.(x[s+1]+h//2, t') - Intfr.(ξ, t') ) / h
    elseif 0 < κ < 1//2
        F[s, :] = ( Intfl.(ξ, t') - Intfl.(x[s]-h//2, t') + Intfr.(x[s]+h//2, t') - Intfr.(ξ, t') ) / h
        F[s+1, :] = ( Intfr.(x[s+1]+h//2, t') - Intfr.(x[s+1]-h//2, t') ) / h
    elseif 1//2 == κ
        F[s, :] = ( Intfl.(x[s]+h//2, t') - Intfl.(x[s]-h//2, t') ) / h
        F[s+1, :] = ( Intfr.(x[s+1]+h//2, t') - Intfr.(x[s+1]-h//2, t') ) / h
    else
        error("κ is not in (0, 1)")
    end

    # Fⱼⁿ - f(xⱼ, tⁿ) = O(h²)
    # @show ( F - f.(x, t')[1:J-1, :] .|> abs |> maximum )


    # ## Ex/Im scheme
    # 
    # ### initial condition

    U_exact = u_exact.(x, t')
    U = OffsetMatrix(zeros(Float, J+1, N+1), 0:J, 0:N)     # U_0, U_1, ..., U_J

    U[:,0] = α.(x)
    U[0,:] = β₀.(t)
    U[J,:] = β₁.(t)


    A = diagm(0 => 1 .+r.*(a_mhh[1:s+1] + a_mhh[2:s+2]), 1 => -r.*a_mhh[2:s+1], -1 => -r.*a_mhh[2:s+1])
    for n in 0:N-1
        # Explicit (5)
        for j = s+2:J-1
            U[j, n+1] = U[j, n]*(1 - r * (a_mhh[j] + a_mhh[j+1]))  + r * (a_mhh[j]*U[j-1, n] + a_mhh[j+1]*U[j+1, n]) + τ * F[j, n]
        end

        # Implicit (4)
        b = @. U[1:s+1, n] + τ*F[1:s+1, n+1]
        b[1] += r*a_mhh[1]*U[0, n+1]
        b[s+1] += r*a_mhh[s+2]*U[s+2, n+1]
        @assert size(A) == (s+1, s+1)
        @assert length(b) == (s+1)
        U[1:s+1, n+1] = A \ b
    end

    errinf = U_exact - U .|> abs |> maximum
    errinf, errinf/(τ+h^2)
end


using DataFrames

Js = [25, 50, 100, 200, 400]
df1 = [(0., 0.) for i in 1:length(Js)]
df2 = [(0., 0.) for i in 1:length(Js)]

r1, r2 = 1, 20



Threads.@threads for idj in eachindex(Js)
    J = Js[idj]
    N1 = Int(ceil(T*J^2/r1))
    N2 = Int(ceil(T*J^2/r2))
    # println("J = $J, N1 = $N1, N2 = $N2")

    df1[idj] = eierror(J, N1, ξ)
    df2[idj] = eierror(J, N2, ξ)
end

@show df = DataFrame(a=df1, b=df2)



