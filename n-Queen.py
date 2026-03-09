from Tools.demo.queens import Queens
from numpy.ma.extras import row_stack
from scipy.stats import ansari


def n_queens(n,arr):
    if n==0:return arr
    size=len(arr)
    row=size-n
    for y in range(size):
        if possible(arr, row, y, size):
            arr[row][y] = 1
            res = n_queens(n - 1,  arr)
            if res: return res
            arr[row][y] = 0

    return None

def possible(arr,x,y,n):
    for i in range(n):
        if arr[i][y]==1:return False
    i, j = x, y
    while j >= 0 and i >= 0:
        if arr[i][j] == 1: return False
        i -= 1
        j -= 1

    i, j = x, y
    while j < n and i >= 0:
        if arr[i][j] == 1: return False
        i -= 1
        j += 1
    return True

# n=4
# print(n_queens(n,[[0]*n for _ in range(n)]))
def solveNQueens( n):
    arr=n_queens(n,[[0]*n for _ in range(n)])
    ans=[]
    for i in range(n):
        q=""
        for j in range(n):
            if arr[i][j]==1:q+="Q"
            else:q+="."
        ans.append(q)
    print(ans)
    return ans
solveNQueens(4)