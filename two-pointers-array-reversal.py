def array_reverse(list_of_data):
    n = len(list_of_data)
    i = 0
    k = n-1
    while(i < k):
        temporary_value = list_of_data[i]
        list_of_data[i] = list_of_data[k]
        list_of_data[k] = temporary_value
        i += 1
        k -= 1


array_length = int(input("Array Length"))
list_array_data = []
for x in range(0, array_length):
    list_array_data.append(int(input()))
array_reverse(list_array_data)
print(list_array_data)
