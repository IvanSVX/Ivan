#result1 = get_matrix(2, 2, 10)
#result2 = get_matrix(3, 5, 42)
#result3 = get_matrix(4, 2, 13)

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        if n <= 0:
            return matrix
        i = [value] * m
        matrix.append(i)
    return matrix

#result1 = get_matrix(2, 2, 10)
#print(result1)

#result2 = get_matrix(3, 5, 42)
#print(result2)

#result3 = get_matrix(4, 2, 13)
#print(result3)

result4 = get_matrix(0, 1, 2)
print(result4)
