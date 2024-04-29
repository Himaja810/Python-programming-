#pattern 14
n=int(input())
for r in range(1,n+1):
    for s in range(r):
        if r%2==0 :
            print("#",end="")
        else :
            print("*",end="")
    print()
