#pattern 13
n=int(input())
val=10
for r in range(n):
    for s in range(r+1):
        print(val,end=" ")
        val=val+10
    print()
