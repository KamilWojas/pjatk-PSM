# -*- coding: utf-8 -*-
"""PSM_Zadanie_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aSgQj5RgaCNlXwk_xTwk-IWE7-kzsTrn
"""

import math

def sin_taylor(x, n):


  if n <= 0:
    raise ValueError("Liczba wyrazów szeregu musi być dodatnia.")

  sum_of_terms = 0
  sign = 1
  for i in range(1, n + 1):
    term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    sum_of_terms += sign * term
    sign *= -1

  return sum_of_terms

def main():

  try:
    x = float(input("Podaj wartość argumentu x: "))
  except ValueError:
    print("Wartość x musi być liczbą.")
    return

  try:
    n = int(input("Podaj liczbę wyrazów szeregu Taylora: "))
  except ValueError:
    print("Liczba wyrazów szeregu musi być liczbą całkowitą.")
    return

  if n <= 0:
    print("Liczba wyrazów szeregu musi być dodatnia.")
    return

  sin_value = sin_taylor(x, n)

  print(f"Wartość sin({x}) obliczona z wykorzystaniem {n} wyrazów szeregu Taylora wynosi: {sin_value}")

if __name__ == "__main__":
  main()