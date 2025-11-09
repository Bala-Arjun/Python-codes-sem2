str = input()
str_list = list(str)
for i in range(len(str_list) - 1):
    for j in range(len(str_list) - 1):
        if str_list[j] > str_list[j + 1]:
            str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]
sorted_str = "".join(str_list)
print(sorted_str)
