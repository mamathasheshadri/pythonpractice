def testCase(n):
    
    if n <= 0:
        return
    X = int(input("No. of elements:"))
    print (sumofSquares(X))
    testCase(n-1)

def sumofSquares(X):
    
    if X == 0:
        return 0
    Y = int(input("Enter the number:"))
    if Y > 0:
         
         return Y*Y + sumofSquares(X-1)
    return sumofSquares(X-1)


if __name__ == "__main__":
    
    n = int(input('No. of test cases:'))

    testCase(n)
