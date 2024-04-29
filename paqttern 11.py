#pattern 11  
n=int(input ())
spaces=n-1
stars = 1
for r in range(n):
    for s in range (spaces):
        print(" ", end = "")
    for s in range (stars):
        print(s+1, end="")
    print()
    spaces = spaces - 1
    stars=stars+2
