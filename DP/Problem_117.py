"""
red , green and blue tiles

Using a combination of grey square tiles and oblong tiles chosen from: red tiles (measuring two units),
green tiles (measuring three units), and blue tiles (measuring four units), it is possible to tile a row 
measuring five units in length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?

f(0) = 1
f(1) = 1
f(2) = 2: 2 grey and 2 red blocks possible
f(3) = 4: 3 grey or 3 green so 2 ways, 2 red one grey so 2 ways
f(4) = 7: 4 grey or 4 blue so 2 ways, 2 grey 2 red so 3 ways, 1 grey 3 green so 2 ways 
f(5) = 15: 5 grey so one way, 3 grey 2 red so 4 ways, 2 grey 1 green so 3 ways, 1 grey 4 blue 2 ways, 1 grey 4 red so 3,
            1 red 1 green so 2 ways.
f(6) = 29: 6 grey 6 blue = 2, 4 grey 2 red= 5, 3 grey 3 green = 4, 2 grey 4 blue = 3, 2 red 4 blue = 2, 
"""
def counting_blocks(m):

    a, b, c, d = 0, 0, 0, 1

    for i in range(m):
        a, b, c, d = b, c, d, (a+b+c+d)

    return d


if __name__ == "__main__":
    # m, n = map(int, input().split())
    # m, n = 7, 3
    print(counting_blocks(0))
    print(counting_blocks(1))
    print(counting_blocks(2))
    print(counting_blocks(3))
    print(counting_blocks(4))
    print(counting_blocks(5))
    print(counting_blocks(50))