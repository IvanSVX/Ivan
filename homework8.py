my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(len(my_list))
a = 0 # индекс списка
while my_list[a] >= 0 and a < 13:
    if my_list[a] == 0:
        a = a + 1
        continue
    elif my_list[a] > 0:
        print(my_list[a])
        a = a + 1
        continue
    else:
        break
        #eajfrvear