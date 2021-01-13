# -*- coding: utf-8 -*-

# --------------------------------------------------------
# Enrique_Escalante-Notario
# Instituto de Fisica, UNAM
# email: <enriquescalante@gmail.com>
# Distributed under terms of the GPLv3 license.
# WriteParameters.py
# --------------------------------------------------------


Mod = open("modelos.txt","r")
Para = open("models.txt","w")

import sympy as sp

conta = 1
model = []
for linea in Mod:

	if conta == 6:
		model.append(list(map(sp.Rational,linea[:-1].split(sep=","))))
	if conta == 7:
		model.append(list(map(sp.Rational,linea[:-1].split(sep=","))))
	if conta == 8:
		model.append(list(map(sp.Rational,linea[:-1].split(sep=","))))
	if conta == 9:
		model.append(list(map(sp.Rational,linea[:-1].split(sep=","))))
	if conta == 10:
		model.append(list(map(sp.Rational,linea[:-1].split(sep=","))))
	if conta == 11:
		model.append(list(map(sp.Rational,linea[:-1].split(sep=","))))
	if conta == 12:
		model.append(list(map(sp.Rational,linea[:-1].split(sep=","))))
	if conta == 13:
		model.append(list(map(sp.Rational,linea[:-1].split(sep=","))))
	if conta == 14:
		conta = 0
		Para.write(str(model)+"\n")
		model = []
	conta += 1