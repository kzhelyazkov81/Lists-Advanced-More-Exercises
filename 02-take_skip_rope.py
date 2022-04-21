message = input()
numbers = []
non_numbers = []
for i in message:
    if 47 < ord(i) < 58:
        numbers.append(i)
    else:
        non_numbers.append(i)

numbers = list(map(int, numbers))
take_list = []
skip_list = []
for i in range(len(numbers)):
    if i % 2 == 0:
        take_list.append(numbers[i])
    else:
        skip_list.append(numbers[i])

result_string = ''
for i in range(len(take_list)):
    for m in range(take_list[i]):
        result_string += non_numbers[0]
        non_numbers.pop(0)
    for n in range(skip_list[i]):
        non_numbers.pop(0)

print(result_string)