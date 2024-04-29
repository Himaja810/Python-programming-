# Upper half of the diamond
n=int(input())
spaces = 0
stars = 2 * n  - 1
for r in range(n - 1, 0, -1):
    for s in range(spaces):
        print(" ", end=" ")
    for r in range(stars):
        print("*", end=" ")
    print()
    spaces += 1
    stars -= 2

# Lower half of the diamond
spaces = n-1
stars = 1
for r in range(n):
    for s in range(spaces):
        print(" ", end=" ")
    for r in range(stars):
        print("*", end=" ")
    print()
    spaces -= 1
    stars += 2
