# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
for n in range(a):
    for p in range(n+1):
        print("*",end="")
    print()
