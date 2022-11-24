def generatenum(n):
    for i in range(1,n+1):
        print(i, end=' ')
        
def divisibleby5(n):
    for i in range(1,n+1):
        if i%5==0:
            print(i,end=' ')

def divisibleby12(n):
    for i in range(1,n+1):
        if i%12==0:
            print(i,end=' ')