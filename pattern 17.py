#pattern 17
def alphapat(n):
    num = 65
    spaces=0
    stars = n
    for r in range(n):
        for s in range(spaces):
            print(" ", end=" ")
        for s in range(stars):
            ch = chr(num)
            print(ch, end=" ")
            num += 1
        num = 65
        
        print()
        
        
        spaces += 1
        stars -= 1
n = int(input())
alphapat(n)
