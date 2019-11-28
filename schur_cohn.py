def multiply(a,k):
    return [x*k for x in a]
def divide(a,k):
    return [x/k for x in a]
def minus(a, b):
    if len(a) != len(b):
        raise Exception("length of a not equal b")
    rs = []
    for i in range(len(a)-1):
        rs.append(a[i]-b[i])
    if (a[-1]-b[-1]) != 0:
        rs.append(a[-1]-b[-1])
    return rs
def isStability(A):
    while len(A) > 2:
        if A[-1] >= 1:
            return False
        else:
            K = A[-1]
            B = A[::-1]
            A = divide(minus(A, multiply(B, K)),(1-K*K)) #(A-K*B)/(1-K*K)
    if A[-1] >= 1:
        return False
    return True


print(isStability([1,2,0.3]))