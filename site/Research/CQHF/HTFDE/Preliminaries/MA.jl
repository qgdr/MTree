# --8<-- [start:usc]
@doc """
    usc(G::MultvalueMap, X::NormedSpace)

The upper semi-continuous function.

# Arguments
- `G::MultvalueMap`: A multivalued map.
- `X::NormedSpace`: A normed space.

"""
function usc(G::MultvalueMap, X::NormedSpace)
    for x0 ∈ X
        G(x0) is closed
        &&
        for N::OpenSet ⊂ X where G(x0) ⊂ N
            ∃ N0 where 
            x0 ∈ N0 
            &&
            G(N0) ⊆ N
        end
    end
end
# --8<-- [end:usc]

# --8<-- [start:lsc]
@doc """
    lsc(G::MultvalueMap, X::NormedSpace)

The lower semi-continuous function.

# Arguments
- `G::MultvalueMap`: A multivalued map.
- `X::NormedSpace`: A normed space.

"""
function lsc(G::MultvalueMap, X::NormedSpace)
    for B::OpenSet ⊂ X
        Y := {y ∈ X where G(y) ∩ B ≠ ∅}
        Y is open
    end
end
# --8<-- [end:lsc]