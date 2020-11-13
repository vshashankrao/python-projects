"""
Object Oriented Programming, Spring 2019
Test module for Problem 1, Assignment #6
"""

from quad import *

if __name__ == "__main__":
    q0 = Quadratic(0, 0, 0)
    q1 = Quadratic(0, 0, 5)
    q2 = Quadratic(0, 3, -2)
    q3 = Quadratic(3, -5, 4)
    q4 = Quadratic(2, 4, 2)
    q5 = Quadratic(2, -5, 2)

    print("Six quadratic expressions have been created.")
    print("They are printed below:\n")

    print("q0: ", q0)
    print("q1: ", q1)
    print("q2: ", q2)
    print("q3: ", q3)
    print("q4: ", q4)
    print("q5: ", q5)

    print("Quadratic expression q2 evaluated at -1 equals ", q2.evaluate(-1))
    print("Quadratic expression q5 evaluated at -1 equals ", q5.evaluate(-1))


    roots_list = [q0.roots(), q1.roots(), q2.roots(), q3.roots(), q4.roots(), q5.roots()]

    for i in range(len(roots_list)):
        if len(roots_list[i]) == 0:
            print("Quadratic expression # ", i, " has no real roots.")
        elif len(roots_list[i]) == 1:
            print("Quadratic expression # ", i, " has one real root: ", roots_list[i][0])
        elif len(roots_list[i]) == 2:
            print("Quadratic expression # ", i, " has two real roots: ",
                  roots_list[i][0], " and ", roots_list[i][1])
        else:
            print("Quadratic expression # ", i, " has infinitely many roots.")

    q6 = q5 + q2
    print("sum:", q6)
    q7 = q5 - q4
    print("diff:", q7)
    q8 = q5 * q4
    print("mult:", q8)
    q9 = q1 * q2
    print("mult:", q9)
    q10 = q5.scale(3)
    print("scale:", q10)
    
    
