# -*- coding: utf-8 -*-

# --------------------------------------------------------
# Enrique_Escalante-Notario
# Instituto de Fisica, UNAM
# email: <enriquescalante@gmail.com>
# Distributed under terms of the GPLv3 license.
# Nomassivestates.py
# --------------------------------------------------------

import itertools
import sympy as sp

conjunto1 = [1.,1.,0,0,0,0,0,0]
conjunto2 = [-1.,-1.,0,0,0,0,0,0]
conjunto3 = [1.,-1.,0,0,0,0,0,0]
states1 = list(set(itertools.permutations(conjunto1,8)))
states2 = list(set(itertools.permutations(conjunto2,8)))
states3 = list(set(itertools.permutations(conjunto3,8)))

conjunto4 = [1/2.,1/2.,1/2.,1/2.,1/2.,1/2.,1/2.,1/2.]
conjunto5 = [1/2.,1/2.,1/2.,1/2.,1/2.,1/2.,-1/2.,-1/2.]
conjunto6 = [1/2.,1/2.,1/2.,1/2.,-1/2.,-1/2.,-1/2.,-1/2.]
conjunto7 = [1/2.,1/2.,-1/2.,-1/2.,-1/2.,-1/2.,-1/2.,-1/2.]
conjunto8 = [-1/2.,-1/2.,-1/2.,-1/2.,-1/2.,-1/2.,-1/2.,-1/2.]
states4 = list(set(itertools.permutations(conjunto4,8)))
states5 = list(set(itertools.permutations(conjunto5,8)))
states6 = list(set(itertools.permutations(conjunto6,8)))
states7 = list(set(itertools.permutations(conjunto7,8)))
states8 = list(set(itertools.permutations(conjunto8,8)))

conjunto = states1 + states2 + states3 + states4 + states5 + states6 + states7 + states8

nulo = [0.,0.,0.,0.,0.,0.,0.,0.]

f = open("nomassive.txt","w")

for elemento in conjunto:
	s = list(elemento)
	f.write(str(s)+"\n")


f.close()


