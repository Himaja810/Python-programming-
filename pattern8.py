# Enter your code here. Read input from STDIN. Print output to STDOUT
#pattern 8 
n=int(input ())
def print_tri(rows):
    for i in range(rows):
        print(" " * i + "*" * (rows - i))
print_tri(n)
