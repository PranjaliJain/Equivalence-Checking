# Checking satisfiability of a formula.
#
# This example shows:
#  1. How to build a formula
#  2. How to perform substitution
#  3. Printing
#  4. Satisfiability checking
from pysmt.shortcuts import Symbol, And, Not, Xor, is_sat

import dimacs

vars_cnt, clauses, comments = dimacs.read_dimacs('cnf_bench/test/test3.cnf')

res, rev_st = dimacs.dimacs_to_pysmt(vars_cnt, clauses, comments)

vars_cnt2, clauses2, comments2 = dimacs.read_dimacs('cnf_bench/test/test3.cnf')

res2, rev_st2 = dimacs.dimacs_to_pysmt(vars_cnt2, clauses2, comments2)

# sat_res = is_sat(res)
# assert sat_res # SAT
# print("dimacs := %s is SAT? %s" % (res, sat_res))
# assert not sat_res # UNSAT

f = Xor(res, res2)

sat_res = is_sat(f)
print("dimacs := %s is SAT? %s" % (f, sat_res))
# varA = Symbol("A") # Default type is Boolean
# varB = Symbol("B")
# f = And([varA, Not(varB)])
# g = f.substitute({varB:varA})

# res = is_sat(f)
# assert res # SAT
# print("f := %s is SAT? %s" % (f, res))

# res = is_sat(g)
# print("g := %s is SAT? %s" % (g, res))
# assert not res # UNSAT

