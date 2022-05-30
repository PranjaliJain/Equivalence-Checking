
from pysmt.shortcuts import Symbol, And, Not, Or, is_sat, Xor
import dimacs

vars_cnt, clauses, comments = dimacs.read_dimacs('cnf_bench/Multi-AND/mand4.cnf')

res, rev_st = dimacs.dimacs_to_pysmt(vars_cnt, clauses, comments)

print(vars_cnt, clauses, comments)
print("number of clauses: ", len(clauses))
print(res, rev_st)
# varA = Symbol("A")
f = Xor(res, res)

sat_res = is_sat(f)
# assert sat_res # SAT
print("dimacs := %s is SAT? %s" % (res, sat_res))
print("if UNSAT, given circuits are equal")
# assert not sat_res # UNSAT
lst = [f,f,f]
miter = Or(lst)
print("miter", miter)

sat_res = is_sat(miter)
print("is SAT miter ", sat_res)