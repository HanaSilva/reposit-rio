# -*- coding: utf-8 -*-
"""CPF

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c2ordmiofEQrco9-rjiUClHnsT2IUh38
"""

#Iohanan de Almeida Silva
cpf = "86975134108"

primeiro = 0
segundo  = 0

soma_nove = (int(cpf[0])*10)+(int(cpf[1])*9)+(int(cpf[2]*8))+(int(cpf[3])*7)+(int(cpf[4])*6)+(int(cpf[5])*5)+(int(cpf[6])*4)+(int(cpf[7]*2))+(int(cpf[8])*2)

resto_soma =soma_nove %11

if resto_soma <2:
    primeiro = 0
    print(primeiro)
else:
    primeiro = 11 -resto_soma
    print(primeiro)

soma_segundo = (int(cpf[0])*11) +(int(cpf[1]*10))+(int(cpf[2])*9)+(int(cpf[3])*8) +(int(cpf[4])*7)+(int(cpf[5])*6)+(int(cpf[6])*5)+(int(cpf[7])*4)+(int(cpf[8])*3)+(primeiro*2)

resto_segundo = soma_segundo %11

if resto_segundo <2:
   segundo = 0
else:
 segundo = 11 - resto_segundo

 print(segundo)

if int(cpf[9]) == primeiro and int(cpf[10]) == segundo:
    print("CPF Válido")
else:
   print("Inválido")