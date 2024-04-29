#pattern 19
n = int(input())
spaces = n - 1
stars = 1

# Upper half of the diamond
for r in range(n):
    for s in range(spaces):
        print(" ", end=" ")
    for s in range(stars):
        print("*", end=" ")
    print()
    spaces -= 1
    stars += 2

# Lower half of the diamond
spaces = 1
stars = 2 * (n - 1) - 1
for r in range(n - 1, 0, -1):
    for s in range(spaces):
        print(" ", end=" ")
    for s in range(stars):
        print("*", end=" ")
    print()
    spaces += 1
    stars -= 2
