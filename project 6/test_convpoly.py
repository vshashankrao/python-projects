"""
Author: Suneeta Ramaswami

Basic test code for the the Point, ConvPoly, EquiTriangle, 
Rectangle, and Square objects (Problem 2, Assignment 6)
"""

from convpoly import *

if __name__ == "__main__":
    print("This module provides some basic test code for the classes in Assignment 6.")

    p1 = Point(1, 1)
    p2 = Point(3, 0)
    p3 = Point(4, 1)
    p4 = Point(3, 3)
    p5 = Point(2, 3)


    print("p1: ", p1)
    print("p2: ", p2)
    print("Distance b/w p1 and p2: ", p1.distance(p2))
    print()

    print(p1, end = " ")
    p1.rotate(45)
    print("rotated by 45 degrees is: ", p1)
    print()

    print(p1, end = " ")
    p1.rotate(-45)
    print("rotated by -45 degrees is: ", p1)
    print()

    print(p2, end = " ")
    p2.translate(-2, 3)
    print("translated by (-2, 3): ", p2)
    print()

    print(p2, end = " ")
    p2.translate(2, -3)
    print("translated by (2, -3): ", p2)
    print()

    if p2.right_of(p1, p3):
        print(p1, p3, p2, " make a right turn. (CORRECT!)")
    else: 
        print(p1, p3, p2, " do not make a right turn. (INCORRECT!)")
    print()

    if p5.left_of(p1, p3):
        print(p1, p3, p5, " make a left turn. (CORRECT!)")
    else: 
        print(p1, p3, p5, " do not make a left turn. (INCORRECT!)")
    print()

    print("--------------------------------")
    P = ConvPoly(p1, p2, p3, p4, p5)
    print("Convex polygon P has been created as follows: ")
    print(P)
    print()

    print("The perimeter of P is ", P.perimeter())
    print()

    P.translate(-2, 3)
    print("P translated by (-2, 3): ")
    print(P)
    print()

    P.rotate(45)
    print("Now P is rotated by 45 degrees: ")
    print(P)
    print()

    print("The perimeter of P is ", P.perimeter())
    print("(The answer should be the same as the previous one.)")
    print()

    P.rotate(-45)
    P.translate(2, -3)
    print("Rotated and translated P back to its original position")
    print(P)
    print()

    q = Point(3, 1)
    if P.contains(q):
        print("P contains the point ", q, "(CORRECT!)")
    else: 
        print("P does not contain the point ", q, "(INCORRECT!)")

    q = Point(3, -1)
    if P.contains(q):
        print("P contains the point ", q, "(INCORRECT!)")
    else: 
        print("P does not contain the point ", q, "(CORRECT!)")
    print()


    print("The vertices of P are (this checks __getitem__ and __len__): ")
    for i in range(len(P)):
        print(P[i])
    print()

    print("Checking iter and next: ")
    i = iter(P)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    try:
        print(next(i))
    except StopIteration: 
        print("A StopIteration was (correctly) caught.")

    print("--------------------------------")
    T = Triangle(Point(1,2), Point(5,2), Point(1,5))
    print("A triangle T has been created: ")
    print(T)

    print("The perimeter of T is ", T.perimeter())
    print("The area of T is ", T.area())

    T.rotate(90)
    print("T, after it has been rotated by 90 degrees: ")
    print(T)

    try:
        T = Triangle(Point(1, 1), Point(2, 2), Point(3, 3))
    except:
        print("An exception was (correctly) caught when creating a triangle with collinear vertices")
    
    print("--------------------------------")
    E = EquiTriangle(3)
    print("An equilateral triangle E with side length 3 has been created: ")
    print(E)

    print("The perimeter of E is ", E.perimeter())
    print("The area of E is ", E.area())

    E.rotate(90)
    print("E, after it has been rotated by 90 degrees: ")
    print(E)

    print("--------------------------------")
    R = Rectangle(3, 4)
    print("A rectangle R with width 3 and height 4 has been created.")
    print("Its vertices are: ")
    for v in R:
        print(v)

    print("The perimeter of R is ", R.perimeter())
    print("The area of R is ", R.area())

    R.translate(-1, 2)
    print("R has been translated by (-1, 2). Its vertices are: ")
    for v in R:
        print(v)

    print("--------------------------------")


    S = Square(5)
    print("A square S of side length 5 has been created: ")

    print("Its vertices are: ")
    for i in range(len(S)):
        print(S[i])

    print("The perimeter of S is ", S.perimeter())
    print("The area of S is ", S.area())


    print()
    print("That's all for now. Goodbye!")
