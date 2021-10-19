def Solution(A):
    max_val = max(A)
    if max_val < 0:
        return 1
    else:
        B = range(1,max_val+1)
        C = set(B)-set(A)
        return min(C)

A=[1,2,3]
print (Solution(A))

