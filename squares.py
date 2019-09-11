import turtle as tt
import snippet
"""
CSAPX Lab 2: Recursion Squares

A program that recursively draws a square design given a depth and a side length.

author: Ayane Naito
"""
def draw_square(length):
    tt.forward(length)
    tt.left(90)
    tt.forward(length)
    tt.left(90)
    tt.forward(length)
    tt.left(90)
    tt.forward(length)
    tt.left(90)

def draw_squares(length, depth):
    if depth == 0:
        pass
    elif depth == 1:
        draw_square(length)
    else:
        #draw_square(length/2)
        tt.forward(length/2)
        tt.left(90)
        tt.forward(length/4)
        tt.left(45)
        draw_squares(length/6, depth-1)
        tt.right(45)
        tt.forward(length/4)
        tt.left(90)
        tt.forward(length/2)
        tt.left(90)
        tt.forward(length/4)
        tt.left(45)
        draw_squares(length/6, depth-1)
        tt.right(45)
        tt.forward(length/4)
        """
        tt.forward(length/6)
        tt.left(90)
        tt.forward(length/3)
        tt.right(90)
        tt.forward(length/6)
        tt.right(90)
        tt.forward(length/6)
        tt.right(90)
        tt.forward(length/6)
        #tt.right(90)
        #tt.forward(length/3)
        #draw_squares(length/6, depth-1)
        
        
        draw_squares(length//depth, depth-1)
        tt.left(135)
        tt.forward(length//depth)
        draw_squares(length//depth, depth-1)
        """

def main():
    snippet.init(500, 4)
    tt.down()
    draw_squares(700, 3)
    tt.done()

if __name__ == '__main__':
    main()