def non_decreasing_squared_values_of_array(non_decreasing_array):
    sorted_array = []
    left_pointer = 0
    right_pointer = len(non_decreasing_array)-1
    while left_pointer < right_pointer:
        if non_decreasing_array[left_pointer]**2 > non_decreasing_array[right_pointer]**2:
            sorted_array.append(non_decreasing_array[left_pointer] ** 2)
            left_pointer += 1
        else:
            sorted_array.append(non_decreasing_array[right_pointer] ** 2)
            right_pointer -= 1
    return sorted_array[::-1]


array_dec = [-1, 0, 3, 10]
print(non_decreasing_squared_values_of_array(array_dec))
