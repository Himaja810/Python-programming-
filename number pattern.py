# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
for n in range(a):
    for i in range(n+1):
        print(i+1,end="")
    print()
