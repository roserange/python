def stair(n):
    if n<=1:
        return n
    return stair(n-1)+stair(n-2)
def finishthestair(s):
    return(s+1)
s = int(input("Enter no of staircase :"))
print("number of ways =", finishthestair(s))
