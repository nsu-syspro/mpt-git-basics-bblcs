arr = [40, 4, 20, 10, 30, 6, 10]

<<<<<<< HEAD
# selection sort:
for i in range(len(arr) - 1):
    min = i
    for j in range(i + 1, len(arr)):
        print("comparing {} and {}".format(arr[j], arr[min]))
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]
=======
for i in range(1, len(arr)):
    a_i = arr[i]
    j = i - 1
    while j >= 0:
        print("comparing {} and {}".format(arr[j], a_i))
        if arr[j] > a_i:
            arr[j + 1] = arr[j]
        else:
            break
        j -= 1
    arr[j + 1] = a_i

>>>>>>> d983130 (Use better sorting algorithm)

print(arr)
