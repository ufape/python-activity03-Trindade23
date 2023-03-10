# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 3 - Problem 1
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
A entrada contém dois valores inteiros.
Exemplo:
Digite um valor inteiro para X: 15
Digite um valor inteiro para Y: 12

Processes:
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos
números impares entre eles.

Output(s):
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores
ímpares que estão entre os valores fornecidos na entrada que deverá caber
em um inteiro.
Exemplo:
A soma dos números ímpares entre 15 e 12 é: 13

"""


def main():
  contador = 0
  x = int(input("Digite um valor inteiro para X: "))
  y = int(input("Digite um valor inteiro para X: "))

  if x > y:
    x,y = y,x
    
  for i in range(y+1, x):
    if i % 2 == 1:
      contador = contador + i
      
  print(f"A soma dos números ímpares entre {x} e {y} é: {contador}")


if __name__ == '__main__':
    main()

