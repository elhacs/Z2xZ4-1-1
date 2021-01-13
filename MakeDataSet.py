# -*- coding: utf-8 -*-

# --------------------------------------------------------
# Enrique_Escalante-Notario
# Instituto de Fisica, UNAM
# email: <enriquescalante@gmail.com>
# Distributed under terms of the GPLv3 license.
# MakeDataSet.py
# --------------------------------------------------------


import sympy as sp
import itertools

# Carga los modelos
MOD = open("models.txt")
DS = open("dataset.txt","w")


# Estados no masivos

def NoMassivesStates():
	conjunto1 = [sp.Rational(1),sp.Rational(1),sp.Rational(0),sp.Rational(0),sp.Rational(0),sp.Rational(0),sp.Rational(0),sp.Rational(0)]
	conjunto2 = [sp.Rational(-1),sp.Rational(-1),sp.Rational(0),sp.Rational(0),sp.Rational(0),sp.Rational(0),sp.Rational(0),sp.Rational(0)]
	conjunto3 = [sp.Rational(-1),sp.Rational(1),sp.Rational(0),sp.Rational(0),sp.Rational(0),sp.Rational(0),sp.Rational(0),sp.Rational(0)]
	conjunto4 = [sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.)]
	conjunto5 = [sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.)]
	conjunto6 = [sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.)]
	conjunto7 = [sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(-1/2.),sp.Rational(-1/2.)]
	conjunto8 = [sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.),sp.Rational(1/2.)]
	states1 = list(set(itertools.permutations(conjunto1,8)))
	states2 = list(set(itertools.permutations(conjunto2,8)))
	states3 = list(set(itertools.permutations(conjunto3,8)))
	states4 = list(set(itertools.permutations(conjunto4,8)))
	states5 = list(set(itertools.permutations(conjunto5,8)))
	states6 = list(set(itertools.permutations(conjunto6,8)))
	states7 = list(set(itertools.permutations(conjunto7,8)))
	states8 = list(set(itertools.permutations(conjunto8,8)))
	return states1 + states2 + states3 + states4 + states5 + states6 + states7 + states8

# Sectores que estoy considerando

# 10 puntos fijos.
Sector02 = [
[0, 2, 0, 0, 0, 0, 0, 0], 
[0, 2, 1, 0, 0, 0, 0, 0], 
[0, 2, 1, 1, 0, 0, 0, 0], 
[0, 2, 0, 0, 0, 0, 1, 0], 
[0, 2, 1, 0, 0, 0, 1, 0], 
[0, 2, 0, 1, 0, 0, 1, 0], 
[0, 2, 1, 1, 0, 0, 1, 0], 
[0, 2, 0, 0, 0, 0, 1, 1], 
[0, 2, 1, 0, 0, 0, 1, 1], 
[0, 2, 1, 1, 0, 0, 1, 1] 
]

# 12 puntos fijos.


Sector10 = [
[1, 0, 0, 0, 0, 0, 0, 0], 
[1, 0, 0, 0, 1, 0, 0, 0], 
[1, 0, 0, 0, 0, 1, 0, 0], 
[1, 0, 0, 0, 1, 1, 0, 0], 
[1, 0, 0, 0, 0, 0, 1, 0], 
[1, 0, 0, 0, 1, 0, 1, 0], 
[1, 0, 0, 0, 0, 1, 1, 0], 
[1, 0, 0, 0, 1, 1, 1, 0], 
[1, 0, 0, 0, 0, 0, 1, 1], 
[1, 0, 0, 0, 1, 0, 1, 1], 
[1, 0, 0, 0, 0, 1, 1, 1], 
[1, 0, 0, 0, 1, 1, 1, 1], 
]


nomassive = NoMassivesStates()

# las WL identicas son 1-2 y 5-6.
for model in MOD:
	Ns = []

	V1 = sp.Matrix(list(map(sp.Rational,model[2:-3].split("], [")[0].split(","))))
	V2 = sp.Matrix(list(map(sp.Rational,model[2:-3].split("], [")[1].split(","))))
	W1 = sp.Matrix(list(map(sp.Rational,model[2:-3].split("], [")[2].split(","))))
	W2 = sp.Matrix(list(map(sp.Rational,model[2:-3].split("], [")[3].split(","))))
	W3 = sp.Matrix(list(map(sp.Rational,model[2:-3].split("], [")[4].split(","))))
	W4 = sp.Matrix(list(map(sp.Rational,model[2:-3].split("], [")[5].split(","))))
	W5 = sp.Matrix(list(map(sp.Rational,model[2:-3].split("], [")[6].split(","))))
	W6 = sp.Matrix(list(map(sp.Rational,model[2:-3].split("], [")[7].split(","))))

	V11 = sp.Matrix(V1[:8])
	V12 = sp.Matrix(V1[8:])

	for state in nomassive:
		N1 = 0
		N2 = 0
		VP11 = sp.Matrix(state).dot(V11)
		VP12 = sp.Matrix(state).dot(V12)
		if type(VP11) == sp.core.numbers.Integer:
			N1 = N1 + 1
		if type(VP12) == sp.core.numbers.Integer:
			N2 = N2 + 1
	Ns.append(N1)
	Ns.append(N2)

	
	for fijo in Sector02:
		N1 = 0
		N2 = 0
		Vlocal =  sp.Rational(fijo[0])*V1 + sp.Rational(fijo[1])*V2 + sp.Rational(fijo[2])*W1 + sp.Rational(fijo[3])*W2  + sp.Rational(fijo[4])*W3 + sp.Rational(fijo[5])*W4 + sp.Rational(fijo[6])*W5 + sp.Rational(fijo[7])*W6
		Vlocal1 = sp.Matrix(Vlocal[:8])
		Vlocal2 = sp.Matrix(Vlocal[8:])

		for state in nomassive:
			VP1 = sp.Matrix(state).dot(Vlocal1)
			VP2 = sp.Matrix(state).dot(Vlocal2)
			if type(VP1) == sp.core.numbers.Integer:
				N1 = N1 + 1
			if type(VP2) == sp.core.numbers.Integer:
				N2 = N2 + 1
		Ns.append(N1)
		Ns.append(N2)

	for fijo in Sector10:
		N1 = 0
		N2 = 0
		Vlocal =  sp.Rational(fijo[0])*V1 + sp.Rational(fijo[1])*V2 + sp.Rational(fijo[2])*W1 + sp.Rational(fijo[3])*W2  + sp.Rational(fijo[4])*W3 + sp.Rational(fijo[5])*W4 + sp.Rational(fijo[6])*W5 + sp.Rational(fijo[7])*W6
		Vlocal1 = sp.Matrix(Vlocal[:8])
		Vlocal2 = sp.Matrix(Vlocal[8:])

		for state in nomassive:
			VP1 = sp.Matrix(state).dot(Vlocal1)
			VP2 = sp.Matrix(state).dot(Vlocal2)
			if type(VP1) == sp.core.numbers.Integer:
				N1 = N1 + 1
			if type(VP2) == sp.core.numbers.Integer:
				N2 = N2 + 1
		Ns.append(N1)
		Ns.append(N2)
	print(max(Ns))
	DS.write(str(Ns)[1:-1]+"\n")