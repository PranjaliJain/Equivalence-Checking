import pyeda
from pyeda.boolalg.expr import exprvar, Or, And, expr2dimacscnf
a, b, c = map(exprvar, 'abc')
f1 = Or(And(~a, ~b, ~c), And(~a, ~b, c), And(a, ~b, c), And(a, b, c), And(a, b, ~c))
ex = f1.to_cnf()
exp, dimacs = expr2dimacscnf(ex)
print(dimacs)
f2 = Or(And(~a, ~b, c), And(a, ~b, c), And(a, b, c), And(a, b, ~c))
ex = f2.to_cnf()
exp, dimacs = expr2dimacscnf(ex)
print(dimacs)
# print(ex)