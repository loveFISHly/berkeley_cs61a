"""
Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

Pick a positive integer x as the start.
If x is even, divide it by 2.
If x is odd, multiply it by 3 and add 1.
Continue this process until x is 1.

Print the hailstone sequence starting at x and return its length.
"""

def hailstone(x):
    count = 1
    while x != 1:
        print(x)
        if x%2 == 0:
            x = x//2
        else:
            x = 3 * x + 1
        count += 1
    print(x)
    return count
