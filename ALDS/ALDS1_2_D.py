def insertionSort(A, n, g):
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+G] = v
    return A, cnt

def shellSort(A, n):
    cnt = 0
    m = A.len()
    G = list(i*3 + 1 for i in m/9)
    for i in range(m-1):
        insertionSort(A, n, G[i])
    return m, cnt, A

n = int(input())
a = list()

for i in range(n):
    a.append(int(input()))

m, cnt, shell = shellSort(list(a), n)
print(m)
print(*shell)
print(cnt)
