#1
int_a = 55
str_b = 'курсор'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}


print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

#2
lst_d = [1, 2, 3]
lst_d.extend([4,5])
print(lst_d)
print(id(lst_d))

#3
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

#4
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

5

print("Anna has {} apples and {} peaches.".format(3, 7))

#6

print('Anna has {1}, apples and {0} peaches'.format(3, 7))


7

print('Anna has {apples}, apples and {peaches} peaches'.format(apples = 3, peaches = 7))

8

print("Anna has {0:5} apples and {1:3} peaches.".format(3, 7))

9

a = 3
b = 7
print(f'Anna has {a} apples and {b} peaches')

10

a = 3
b = 5
print('Anna has %s, apples and %s peaches' % (a, b))

11

apples = 3
peaches = 7
dict1 = {'a': apples, 'b': peaches}
print("Anna has %(a)s apples and %(b)s peaches" % dict1)

lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)


12

lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)

13

list_1 = [x ** 3 for x in range(7)]
print(list)

14


reg = []
for num in range (10):
    if num % 2 == 0:
        reg.append((num // 2))
    else:
        reg.append(num * 10)
print(reg)


14

d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)


15

d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)

16

d_5 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d_5[x] = x ** 3
print(d_5)


17

d_6 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d_6[x] = x ** 3
    else:
        d_6[x] = x
print(d_6)


18

foo = lambda x, y: x if x < y else y


19

def foo_8 (x,y, z):
    if y < x and x > z:
        return z
    else:
        return y

20

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(lst_to_sort)

21

lst_to_sort.sort(reverse=True)
print(lst_to_sort)

22

lst_2 = list(map(lambda x: x * 2, lst_to_sort))
print(lst_2)

23

list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(lambda x, y: x + y, list_A, list_B))
print(list_C)

24

from functools import reduce
sum = reduce(lambda a, b : a + b, lst_to_sort)
print(sum)

25

lst_3 = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(lst_3)

26

d = range(-10, 10)
fun_1 = list(filter(lambda x: x < 0, d))
print(fun_1)

27

list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_3 = list(filter(lambda x: x in list_1,list_2))
print(list_3)
