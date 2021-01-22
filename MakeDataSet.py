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
MOD = open("modelstest.txt", "r")
DS = open("dataset.txt", "w")
f = open("nomassive.txt","w")

# Estados no masivos

def NoMassivesStates():
    conjunto1 = [sp.Rational(1), sp.Rational(1), sp.Rational(0),
                 sp.Rational(0), sp.Rational(0), sp.Rational(0),
                 sp.Rational(0), sp.Rational(0)]
    conjunto2 = [sp.Rational(-1), sp.Rational(-1), sp.Rational(0),
                 sp.Rational(0), sp.Rational(0), sp.Rational(0),
                 sp.Rational(0), sp.Rational(0)]
    conjunto3 = [sp.Rational(-1), sp.Rational(1), sp.Rational(0),
                 sp.Rational(0), sp.Rational(0), sp.Rational(0),
                 sp.Rational(0), sp.Rational(0)]
    conjunto4 = [sp.Rational(-1/2.), sp.Rational(-1/2.), sp.Rational(- 1/2.),
                 sp.Rational(-1/2.), sp.Rational(-1/2.), sp.Rational(-1/2.),
                 sp.Rational(-1/2.), sp.Rational(-1/2.)]
    conjunto5 = [sp.Rational(1/2.), sp.Rational(1/2.), sp.Rational(-1/2.),
                 sp.Rational(-1/2.), sp.Rational(-1/2.), sp.Rational(-1/2.),
                 sp.Rational(-1/2.), sp.Rational(-1/2.)]
    conjunto6 = [sp.Rational(1/2.), sp.Rational(1/2.), sp.Rational(1/2.),
                 sp.Rational(1/2.), sp.Rational(-1/2.), sp.Rational(-1/2.),
                 sp.Rational(-1/2.), sp.Rational(-1/2.)]
    conjunto7 = [sp.Rational(1/2.), sp.Rational(1/2.), sp.Rational(1/2.),
                 sp.Rational(1/2.), sp.Rational(1/2.), sp.Rational(1/2.),
                 sp.Rational(-1/2.), sp.Rational(-1/2.)]
    conjunto8 = [sp.Rational(1/2.), sp.Rational(1/2.), sp.Rational(1/2.),
                 sp.Rational(1/2.), sp.Rational(1/2.), sp.Rational(1/2.),
                 sp.Rational(1/2.), sp.Rational(1/2.)]
    states1 = list(set(itertools.permutations(conjunto1, 8)))
    states2 = list(set(itertools.permutations(conjunto2, 8)))
    states3 = list(set(itertools.permutations(conjunto3, 8)))
    states4 = list(set(itertools.permutations(conjunto4, 8)))
    states5 = list(set(itertools.permutations(conjunto5, 8)))
    states6 = list(set(itertools.permutations(conjunto6, 8)))
    states7 = list(set(itertools.permutations(conjunto7, 8)))
    states8 = list(set(itertools.permutations(conjunto8, 8)))
    total = states1 + states2 + states3 + states4 + states5 + states6 + states7 + states8
    return total


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
    [0, 2, 1, 1, 0, 0, 1, 1]]


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
    [1, 0, 0, 0, 1, 1, 1, 1]]


nomassive = NoMassivesStates()

tipos = [sp.core.numbers.Integer, sp.core.numbers.NegativeOne,
         sp.core.numbers.One, sp.core.numbers.Zero]

conta = 1

# las WL identicas son 1-2 y 5-6.
for model in MOD:
    Ns = []
    V1 = sp.Matrix(list(map(sp.Rational, model[2:-3].split(
        "], [")[0].split(","))))
    V2 = sp.Matrix(list(map(sp.Rational, model[2:-3].split(
        "], [")[1].split(","))))
    W1 = sp.Matrix(list(map(sp.Rational, model[2:-3].split(
        "], [")[2].split(","))))
    W2 = sp.Matrix(list(map(sp.Rational, model[2:-3].split(
        "], [")[3].split(","))))
    W3 = sp.Matrix(list(map(sp.Rational, model[2:-3].split(
        "], [")[4].split(","))))
    W4 = sp.Matrix(list(map(sp.Rational, model[2:-3].split(
        "], [")[5].split(","))))
    W5 = sp.Matrix(list(map(sp.Rational, model[2:-3].split(
        "], [")[6].split(","))))
    W6 = sp.Matrix(list(map(sp.Rational, model[2:-3].split(
        "], [")[7].split(","))))

    V11 = sp.Matrix(V1[:8])
    V12 = sp.Matrix(V1[8:])
    V21 = sp.Matrix(V2[:8])
    V22 = sp.Matrix(V2[8:])
    W11 = sp.Matrix(W1[:8])
    W12 = sp.Matrix(W1[8:])
    W21 = sp.Matrix(W2[:8])
    W22 = sp.Matrix(W2[8:])
    W31 = sp.Matrix(W3[:8])
    W32 = sp.Matrix(W3[8:])
    W41 = sp.Matrix(W4[:8])
    W42 = sp.Matrix(W4[8:])
    W51 = sp.Matrix(W5[:8])
    W52 = sp.Matrix(W5[8:])
    W61 = sp.Matrix(W6[:8])
    W62 = sp.Matrix(W6[8:])
    N1 = 0
    N2 = 0
    for element in nomassive:
        state = sp.Matrix(element)
        VP11 = state.dot(V11)
        VP12 = state.dot(V12)
        VP21 = state.dot(V21)
        VP22 = state.dot(V22)
        WP11 = state.dot(W11)
        WP12 = state.dot(W12)
        WP21 = state.dot(W21)
        WP22 = state.dot(W22)
        WP31 = state.dot(W31)
        WP32 = state.dot(W32)
        WP41 = state.dot(W41)
        WP42 = state.dot(W42)
        WP51 = state.dot(W51)
        WP52 = state.dot(W52)
        WP61 = state.dot(W61)
        WP62 = state.dot(W62)

        if type(VP11) in tipos:
            if type(VP21) in tipos:
                if type(WP11) in tipos:
                    if type(WP21) in tipos:
                        if type(WP31) in tipos:
                            if type(WP41) in tipos:
                                if type(WP51) in tipos:
                                    if type(WP61) in tipos:
                                        N1 = N1 + 1

        if type(VP12) in tipos:
            if type(VP22) in tipos:
                if type(WP12) in tipos:
                    if type(WP22) in tipos:
                        if type(WP32) in tipos:
                            if type(WP42) in tipos:
                                if type(WP52) in tipos:
                                    if type(WP62) in tipos:
                                        N2 = N2 + 1

    Ns.append(N1)
    Ns.append(N2)

    for fijo in Sector02:
        N1 = 0
        N2 = 0
        Vlocal = sp.Rational(fijo[0])*V1 + sp.Rational(fijo[1])*V2 + \
            sp.Rational(fijo[2])*W1 + sp.Rational(fijo[3])*W2 + \
            sp.Rational(fijo[4])*W3 + sp.Rational(fijo[5])*W4 + \
            sp.Rational(fijo[6])*W5 + sp.Rational(fijo[7])*W6
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

# for fijo in Sector10:

    conta = conta + 1
    DS.write(str(Ns)[1:-1]+"\n")
