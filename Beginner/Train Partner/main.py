import sys

def f(x):
        if x % 8 == 0:
            return(str(int(x)-1) + "SL")
        
        if x % 8 == 1:
            return str(int(x)+3) + "LB"

        if x % 8 == 2:
            return str(int(x)+3) + "MB"

        if x % 8 == 3:
            return str(int(x)+3) + "UB"

        if x % 8 == 4:
            return str(int(x)-3) + "LB"

        if x % 8 == 5:
            return str(int(x)-3) + "MB"

        if x % 8 == 6:
            return str(int(x)-3) + "UB"

        if x % 8 == 7:
            return str(int(x)+1) + "SU"

        return ""
    


numEjemplos = int(sys.stdin.readline()) 
input = []

for n in range(1, numEjemplos + 1):
    input.append(int(sys.stdin.readline()))

for n in input:
    print( str(f(n)) )



