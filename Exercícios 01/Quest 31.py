A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
C = []
for x in range(0, len(A)):
    somaC = A[x] + B[x]
    C.append(somaC)
print(C)
