list1_input = input()
list1 = list(map(int, list1_input.split()))
list2_input = input()
list2 = list(map(int, list2_input.split()))
result = []
for i in range(min(len(list1), len(list2))):
    sum_of_elements = list1[i] + list2[i]
    result.append(sum_of_elements)
print(result)
