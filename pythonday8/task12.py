#swaps elements in a list at two specified indices.
L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

index_1 = int(input())
index_2 = int(input())
op_1 = L[index_1]
op_2 = L[index_2]
swap = L[index_1] = op_2
swap_2 = L[index_2]=op_1
print(L)