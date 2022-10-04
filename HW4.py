# Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), 
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь 
# my_dict, состоящий всего из одного элемента «first_one» 
# со значением «we can do it». Воссоздайте эту функцию.

def biggest_dict(some_dict, **kwargs):
    for i in kwargs:
        some_dict[i] = kwargs[i]
    return some_dict

my_dict = {'first_one':'we can do it'}
m_dict ={input('Ведите ключ: '): input('Введите значение ключа : ') for _ in range(int(input('Сколько новых записей введем в словарь? : ')))}

my_dict = biggest_dict(my_dict, **m_dict)
for i in my_dict:
    print(i, my_dict[i])