# Enter your code here. Read input from STDIN. Print output to STDOUT
#pattern4
n=int(input ())
spaces=0
stars = n
for r in range(n):
    for s in range (spaces):
        print(" ", end = "")
    for r in range (n):
        print("*", end="")
    print()
    spaces = spaces+1
