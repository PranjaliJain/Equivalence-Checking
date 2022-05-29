
from pysmt.shortcuts import Symbol, And, Not, is_sat, Xor
import dimacs

vars_cnt, clauses, comments = dimacs.read_dimacs('test1.cnf')

res, rev_st = dimacs.dimacs_to_pysmt(vars_cnt, clauses, comments)
# varA = Symbol("A")
f = Xor(res, res)

sat_res = is_sat(f)
# assert sat_res # SAT
print("dimacs := %s is SAT? %s" % (res, sat_res))
print("if UNSAT, given circuits are equal")
# assert not sat_res # UNSAT
