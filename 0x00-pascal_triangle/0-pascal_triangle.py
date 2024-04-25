#!/usr/bin/python3

"""
 fact - function that calculates the factorial of a number
 n - is a number to calculate the factorial
  return - factorial on n
"""


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def cal_coefficient(i, j):
    return fact(i) // (fact(j) * fact(i - j))

"""
 pascal_triangle - function that returns a list of lists of 
 integers representing the Pascal’s triangle of n
 
 n - is the number of rows of Pascal’s triangle
 
 return - list of lists of integers representing Pascal’s triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
       row = [cal_coefficient(i, j) for j in range(i + 1)]
       triangle.append(row)

    return triangle
