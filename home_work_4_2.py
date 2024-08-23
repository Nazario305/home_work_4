my_list = [1, 4, 0, 6, 8, 0, 2, 3, 5]

update_list = my_list[::2]
# print(update_list)

x2_update_list = [x * my_list[len(my_list)-1] for x in update_list]
# print(x2_update_list)


result = sum(x2_update_list)
print(result)