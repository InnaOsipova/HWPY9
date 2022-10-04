# Дана строка в виде случайной последовательности чисел от 0 до 9.

# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), 
# а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте 
# функцию count_it(sequence), 
# принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел

import random as r

def count_it(sequence):
    some_set = set(sequence.split())
    some_dic = {int(num) : sequence.count(num) for num in some_set }
    new_dic ={}
    for k in range(3):
        for i in some_dic:
            if some_dic[i] == max(some_dic.values()):
                new_dic[i] = some_dic.pop(i)
                break
    print(new_dic)

m = [r.randint(0,9) for _ in range(int(input('Введите количество чисел последовательности : ')))]
print(' '.join(map(str, m)))
count_it(' '.join(map(str, m)))
