
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
#print_params(a)      #вызов с одним аргументом (не работает)
#print_params(a, b)   #вызов с двумя аргументами (не работает)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [2, 'строчечка', False]
values_dict = {'a': 3, 'b': 'строкуля', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)