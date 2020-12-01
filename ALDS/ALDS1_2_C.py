def BubbleSort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if int(C[j][1]) < int(C[j-1][1]):
                v = C[j]
                C[j] = C[j-1]
                C[j-1] = v
    return C

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(C[minj][1]) > int(C[j][1]):
                minj = j
        if minj != i:
            v = C[i]
            C[i] = C[minj]
            C[minj] = v
    return C

n = int(input())
c = list(map(str, input().split()))

bubble = BubbleSort(list(c), n)
print(*bubble)
print('Stable')

selection = SelectionSort(list(c), n)
print(*selection)

if bubble == selection:
    print('Stable')
else:
    print('Not stable')
