
numbers = [5, 6, 7, 8]
length = len(numbers)
len(numbers)

total_operations = 0
for counter in range(lenght-1):
    for i in range(lenght - 1):
        total_operations += 1
    if numbers[1] > numbers[i+1]:
        old_value = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = old_value
        
print(total_operations)
print(lenght)
print(numbers)
