n = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(n):
    minf = i
    for j in range(i, n):
        if A[j] < A[minf]:
            minf = j
    v = A[i]
    if i != minf:
        A[i] = A[minf]
        A[minf] = v
        count += 1
print(*A)
print(count)
