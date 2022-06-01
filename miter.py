
from pysmt.shortcuts import Symbol, And, Not, Or, is_sat, Xor
import dimacs

vars_cnt, clauses, comments = dimacs.read_dimacs('cnf_bench/Multi-AND/mand4.cnf')
res1, rev_st1 = dimacs.dimacs_to_pysmt(vars_cnt, clauses, comments)

vars_cnt, clauses, comments = dimacs.read_dimacs('cnf_bench/Multi-AND/mand3.cnf')
res2, rev_st2 = dimacs.dimacs_to_pysmt(vars_cnt, clauses, comments)

print(vars_cnt, clauses, comments)
print("number of clauses: ", len(clauses))
print(res1, rev_st1)
f = Xor(res1, res2)

sat_res = is_sat(f)
print("dimacs := %s is SAT? %s" % (f, sat_res))
print("If UNSAT, given circuits are equal")