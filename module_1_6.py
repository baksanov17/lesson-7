# Словарь
my_dict = {'Vasia':175, 'Vika':160 }
print(my_dict)
print(my_dict.get('Vasia')), print(my_dict.get('Dima'))
my_dict.update({'Anton': 165,'Andrey': 174})
print(my_dict)
my_dict.pop('Vasia') # команда del полностью удаляет значение, а рор изымает из словаря, но сохраняет данные
print(my_dict)
# Множество
my_set = {1,2,3,5,5,1,2,9,7,8,9,10}
print(my_set)
my_set.update({53,49})
print(my_set.discard(2))
print(my_set)

