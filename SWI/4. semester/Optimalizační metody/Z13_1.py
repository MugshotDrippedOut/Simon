from sympy import symbols, Eq, diff, solve

x1, x2, λ1, λ2 = symbols('x1 x2 λ1 λ2')

# Definujeme funkciu a obmedzenia
f = x1 + 2*x2
g1 = x1**2 - 4
g2 = x2**2 - 4

# Definujeme Lagrangeovu funkciu
L = f - λ1*g1 - λ2*g2

# Vypočítame parciálne derivácie
L_x1 = diff(L, x1)
L_x2 = diff(L, x2)
L_λ1 = diff(L, λ1)
L_λ2 = diff(L, λ2)

# Riešime sústavu rovníc
solution = solve((Eq(L_x1, 0), Eq(L_x2, 0), Eq(L_λ1, 0), Eq(L_λ2, 0)), (x1, x2, λ1, λ2))

print(solution)