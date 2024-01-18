numbers = [5, 6, 7, 8]
length = len(numbers)

total_operations = 0

for counter in range(length - 1):
    for i in range(length - 1):
        total_operations += 1
        if numbers[i] > numbers[i+1]:
            old_value = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = old_value

print("Total operations:", total_operations)
print("Length:", length)
print("Sorted numbers:", numbers)
