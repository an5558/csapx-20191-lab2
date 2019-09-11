import turtle as tt
import snippet
import math
"""
CSAPX Lab 2: Recursion Squares

A program that recursively draws a square design given a depth and a side length.

author: Ayane Naito
"""

"""
Draws a series of insccribed squares recursively given a side length and depth. Changes colors of the lines between
orange and blue, where the square of the highest level depth is drawn in blue. Colors alternate from that starting point.
    :param length: side length of the largest square (square at depth = 1)
    :param depth: number of levels of recursion desired
    :pre-condition: Turtle is in bottom left corner facing east with pen down.
    :post: Turtle is in bottom left corner facing east with pen down.
"""
def draw_rec(length, depth):
    if depth % 2 == 0:
        tt.color('orange')
    else:
        tt.color('blue')
    if depth == 0:
        pass
    else:
        tt.forward(length)
        tt.left(90)
        tt.forward(length/2)
        tt.left(45)
        if depth % 2 == 0:
            tt.color('blue')
        else:
            tt.color('orange')
        draw_rec(((length/2)/math.sqrt(2)), depth-1)
        if depth % 2 == 0:
            tt.color('orange')
        else:
            tt.color('blue')
        tt.right(45)
        tt.forward(length/2)
        tt.left(90)
        tt.forward(length)
        tt.left(90)
        tt.forward(length / 2)
        tt.left(45)
        if depth % 2 == 0:
            tt.color('orange')
        else:
            tt.color('blue')
        draw_rec(((length/2)/math.sqrt(2)), depth - 1)
        if depth % 2 == 0:
            tt.color('orange')
        else:
            tt.color('blue')
        tt.right(45)
        tt.forward(length / 2)
        tt.left(90)

def main():
    snippet.init(500, 4)
    tt.down()
    draw_rec(450, 0)
    tt.done()

if __name__ == '__main__':
    main()