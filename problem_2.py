# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 3 - Problem 2
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
A entrada contém um valor inteiro N (2 < N < 1000).

Processes:
Leia 1 valor inteiro N (2 < N < 1000).

A seguir, mostre a tabuada de N:
1 x N = N 
2 x N = 2N
...
10 x N = 10N

Output(s):
Imprima a tabuada de N, conforme o exemplo fornecido.

"""


def main():
    n = int(input())
    if n > 2 and n < 1000:
      i = 1
      while (i < 10 + 10):
        print(i,"x", n, "=", (i * n))
        i += 1


if __name__ == '__main__':
    main()
