#nsertionSort
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while(i > -1 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key   

def findRange(A):
    range = A[-1] - A[0]

def findmedian(A):
    if(len(A) % 2 == 0):
        median = (A[len(A) // 2] + A[(len(A) //2) - 2]) / 2
    else:
        median = A[len(A) // 2]