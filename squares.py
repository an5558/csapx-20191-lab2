import turtle as tt
"""
CSAPX Lab 2: Recursion Squares

A program that recursively draws a square design given a depth and a side length.

author: Ayane Naito
"""

def draw_squares(length, depth):
    if depth == 0:
        pass
    elif depth == 1:
        tt.forward(length)
        tt.left(90)
        tt.forward(length)
        tt.left(90)
        tt.forward(length)
        tt.left(90)
        tt.forward(length)
        tt.left(90)
    else:
        draw_squares(length//3, depth-1)
        tt.left(45)
        tt.