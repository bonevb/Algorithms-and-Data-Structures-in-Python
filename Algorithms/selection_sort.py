def selection_sort(L):
    for i in range(len(L)):
        min_position = i
        for j in range(i + 1, len(L)):
            if L[min_position] > L[j]:
                min_position = j

        L[min_position], L[i] = L[i], L[min_position]

    return L


L = [3, 2, 1, 5, 6, 4, 7, 9, 8, 11, 10]
print(selection_sort(L))
