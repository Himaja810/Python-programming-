# Enter your code here. Read input from STDIN. Print output to STDOUT
#pattern5
n= int(input())
for w in range(n,0,-1):
    for v in range(w):
        print("*",end="")
    print()
