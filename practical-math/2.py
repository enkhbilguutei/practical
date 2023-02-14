#Generate the matrix into echelon form and find its rank. 

def echelon_form_and_rank(A):
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        if r >= m:
            break
        for i in range(r, m):
            if A[i][c] != 0:
                A[i], A[r] = A[r], A[i]
                break
        else:
            continue
        pivot = A[r][c]
        A[r] = [x / pivot for x in A[r]]
        for i in range(r + 1, m):
            if A[i][c] != 0:
                scale = A[i][c]
                A[i] = [A[i][j] - scale * A[r][j] for j in range(n)]
        r += 1
    return A, r


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
echelon_form, rank = echelon_form_and_rank(A)
print("Echelon form:")
for row in echelon_form:
    print(row)
print("Rank:", rank)
