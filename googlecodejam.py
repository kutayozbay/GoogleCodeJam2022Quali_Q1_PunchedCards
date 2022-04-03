# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:24:39 2022

@author: Kutay Ozbay

-------------------------------------------------------
Google Code Jam 2022 Qualification Round Question 1
Punched Cards
-------------------------------------------------------
Input:
The first line of the input gives the number of test cases, T. 
T lines follow, each describing a different test case with two integers 
R and C: the number of rows and columns of the punched card that must be drawn.
-------------------------------------------------------
Sample Input:
3
3 4
2 2
2 3


"""


T = int(input())
R = []
C = []
for i in range(T):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    R.append(a)
    C.append(b)

for i in range(T):
    print("Case #" + str(i + 1) +":")
    for j in range(2 * R[i] + 1):
        if(j == 0):
            print(".." + ((C[i] - 1) * "+-") + "+")
        elif((j % 2) == 0):
            print((C[i] * "+-")  + "+")
        elif(j == 1):
            print(".." + ((C[i] - 1) * "|.") + "|")
        else:
            print( (C[i] * "|.") + "|")
