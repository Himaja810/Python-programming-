#pattern 18
def print_pattern18(rows):
    spaces = 0
    stars = rows * 2 - 1 
    for r in range(rows):
        for s in range(spaces):
            print(" ", end=" ")
        for r in range(stars):
            print("*", end=" ") 
        print()
        spaces += 1
        stars -= 2
rows = int(input())
print_pattern18(rows)
