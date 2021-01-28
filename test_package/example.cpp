#include <mp/nl.h>
#include <mp/problem.h>

// taken from https://github.com/ampl/mp/blob/master/test/data/element.nl
constexpr auto nl = "g3 0 1 0	# problem element\n"
" 1 0 1 0 0	# vars, constraints, objectives, ranges, eqns\n"
" 0 1	# nonlinear constraints, objectives\n"
" 0 0	# network constraints: nonlinear, linear\n"
" 0 1 0	# nonlinear vars in constraints, objectives, both\n"
" 0 1 0 1	# linear network variables; functions; arith, flags\n"
" 0 0 0 0 0	# discrete variables: binary, integer, nonlinear (b,c,o)\n"
" 0 1	# nonzeros in Jacobian, gradients\n"
" 0 0	# max name lengths: constraints, variables\n"
" 0 0 0 0 0	# common exprs: b,c,o,c1,o1\n"
"F0 0 -3 element\n"
"O0 0\n"
"f0 4\n"
"n1\n"
"n2\n"
"n3\n"
"v0\n"
"b\n"
"0 0 2\n"
"k0\n"
"G0 1\n"
"0 0\n";

int main()
{
    mp::Problem p;
    mp::ReadNLString(nl, p);

    return 0;
}
