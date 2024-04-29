#pattern 12
n = int(input())


spaces = 0
stars = 2 * n  - 1
for r in range(n - 1, -1, -1):
    for s in range(spaces):
        print(" ", end=" ")
    for s in range(stars):
        print(s+1, end=" ")
    print()
    spaces += 1
    stars -= 2
