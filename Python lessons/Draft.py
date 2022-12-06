# a = 'fn, coin, we, trust'
# ch = 'f'
# if a[0] in ch:
#    a = a.replace(a[0] ,'i', 1)
# print(a)

# a = 3.49
# c = a * 0.6
# x = int(input(print('count day1')))
# y = int(input(print('count day2')))
# d = x * c
# b = y * a
# s = d + b
#
# print(f'bill day1: {round(d, 2)}:'
#       f'bill day2: {round(b, 2)}:'
#       f'bill day1+day2: {round(s, 2)}:')

# x = int(input('x='))
# y = int(input('y='))
# print(f'gumar: {x+y}:')
# print( f'tarberutyun: {x-y}:')
# print( f'artadrtal: {x*y}:')
# print( f'qanord: {x/y}:')
# print( f'amboghj: {x//y}:')
# print( f'mnacord: {x%y}:')
# print(f'gumar: {x**y}:')

# anun = input('anun')
# azg = input('azganun')
# tariq = int(input('tariq'))
# if tariq < 18:
#     print(f'Hallo {anun} {azg}. You are {tariq} years old. You are under 18')
# else:
#     print(f'Hallo {anun} {azg}. You are {tariq} years old. You are over 18')

# name = input('input text')
# print('arajin',name[0])
# print('verjin',name[-1])
# print('mejtegh',name[int(len(name)/2)])

# name = input('input text')
# x = len(name)
# if x%2 == 0:
#     print(name[: int(x//2)])
# else:
#     print(name[int(x//2)])

# name = input('input text')
# print(str.istitle(name[0]))
# print(str.islower(name[0]))
# if int(len(name))%2==0:
#     print('even',len(name))
# else:
#     print('odd',len(name))
# print(str.count(name,'a'))
# print(str.isalpha(name))
# print(str.islower(name))
# print(str.isupper(name))
# print(str.find(name, 'a'))
# print(str.replace(name, 'a', 'b', 1))

# x = float(input('number'))
# if x%7 == 0:
#     print(True)
# else:
#     print(False)

# print(len(input('n')) == 3)

# x = float(input('x'))
# y = float(input('y'))
# z = float(input('z'))
# # print(min(x, y, z))
#
# if x < y and x < z:
#     print(x)
# elif y < x and y < z:
#     print(y)
# else:
#     print(z)

# a = float(input('x'))
# b = float(input('y'))
# c = float(input('z'))
# if a + b > c and b + c > a and c + a > b and a > 0 and b > 0 and c > 0:
#     p = (a + b + c) / 2
#     S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(S)
# else:
#     print('not rectangle')


# phone = '+37494179999'
# if len(phone) == 12 and phone[0] in '+': #and str.isdigit(phone[1:] > 0):
#     print('Your phone number is:', phone)
# else:
#     print('sekurte')

# x = 0
# while x < 10:
#     x = x + 1
#     print(x)

# n = int(input('n'))
# x = 0
# sum = 0
# while x < n:
#     x = x + 1
#     sum = sum + x
# print(sum)
# n = int(input('n'))
# while int(n):
#     print('fghj')


# a = ''
# st = 'sdfdgfhg23543654'
# for i in st:
#    if i not in a:
#       a = a + i
# print(a)

# a = ''
# st = input('text')
# for i in st:
#    if str.isupper(i):
#      a = a + str.lower(i)
#    elif str.islower(i):
#        a = a + str.upper(i)
#    else:
#        a = a + i
# print(a)

# x = -11
# while x < 1:
#     x = x + 1
#     print(x)

# a = ''
# n = '12345'
# for i in range((len(n) - 1), -1, -1):
#     a = a + n[i]
# print(a)

# n = int(input('n'))
# x = 0
# s = 1
# while x < n:
#     x = x + 1
#     s = s * x
# print(s)
# d = 1
# for i in range(1, n + 1):
#     d *= i
# print(d)

# n = 35
# m = 94
# falg = 0
# for x in range(36):
#     for y in range(36):
#         if x + y == 35 and 2 * x + 4 * y == 94:
#             print(x, y)
#             falf = 1
# if falg == 0:
#     print('No sol..!')

# for i in range(101):
#     print(i, '-', i * 9/5 + 32)

# lyst_1 = [1, 3, 66, 4, 6, 7, 8, 9, 33, 54, 77, 79]
# lyst_2 = []
#
# for i in lyst_1:
#     if i % 2 == 0:
#         lyst_2.append(i)
# lyst_2.sort()
# print(lyst_2[-1])

#
# list_1 = [13, 65, 77, 52, 10, 11, 98, 8, 6, 42, 52]
# list_odd = []
# list_even = []
#
# for i in list_1:
#     if i % 2 == 0:
#         list_even.append(i)
#     else:
#         list_odd.append(i)
# print(list_even,list_odd)

# n = 0
# num_list = [43, 900, 567, 88, 988, 0, 52, 988, 27, 29]
# num_list.sort(reverse=True)
# print(num_list)
# for i in num_list:
#     if i < num_list[0]:
#         print(i)
#         break

# num_list = [43, 900, 567, 88, 988, 0, 52, 988, 27, 29]
# p = num_list[0]
# m = max(num_list)
# for i in num_list:
#     if m > i > p:
#         p = i
# print(p)

# name_list = []
# while True:
#     name = input('name')
#     if not name:
#         break
#     if name and name not in name_list:
#         name_list.append(name)
# print(name_list)

# list_1 = []
# list_2 = []
# list_int =[]
# n = input('Numbers')
# num = n.split(sep=' ')
# print(num)
# for i in num:
#     i = int(i)
#     list_int.append(i)
#     avg = sum(list_int) / len(list_int)
# for i1 in list_int:
#     if i1 > avg:
#         list_1.append(i1)
#     elif i1 == avg:
#         list_1.append(i1)
#         list_2.append(i1)
#     else:
#         list_2.append(i1)
# print(list_1, list_2, sep='\n')

# tuple_1 = (1, 55, 54, 'abc', 90, 102, 'asdasd', 'b')
# tuple_2 = ('bbb', 56, 14, 11, 99, 'a')
# for i in tuple_1:
#     if i in tuple_2:
#         print(True)
#         break
# else:
#     print(False)

# tuple_1 = (4, 5, 5, 2, 3, 2, 3, 4, 5, 5, 3)
# list_1 = []
# for i in tuple_1:
#     if i not in list_1:
#         list_1.append(i)
# for i in list_1:
#     j = tuple_1.count(i)
#     print(i, j, sep='-')

# tuple_1 = (11, '55', 54, 'abc', 90, 102, 'asdasd', 'qwerty')
# list_1 = []
# for i in tuple_1:
#     if isinstance(i, int):
#         list_1.append(i)
# print((sum(list_1)/len(list_1) ** 2))

# tuple_1 = (11, 100, 101, 999, 1001)
# print(tuple_1[-2])

# tuple_1 = (11, [22, 33], 44, 55)
# tuple_1[1][0] = 222
# print(tuple_1)

# list_1 = [11, 25, 84, 51, 105]
# # sum_ = 0
# # for i in list_1:
# #     sum_ += i
# # print(sum_)

# list_1 = [-10, -5, -84, 0, -20]
# a = list_1[0]
# for i in list_1:
#      if i > a:
#           a = i
# print(a)

# tuple_1 = (45, 45, 45, 45)
# tuple_2 = ('a', 'a', 'a_', 'a')
# a = tuple_1[0]
# b = tuple_2[0]
# for i in tuple_1:
#     if i != a:
#         print(False)
#         break
# else:
#     print(True)
# for i in tuple_2:
#     if i != b:
#         print(False)
#         break
# else:
#     print(True)

# str_1 = 'We write a  sdfghjkjhgfghj python program bh'
# list_1 = str.split(str_1)
# lenn = 0
# name = None
# for i in list_1:
#     if len(i) > lenn:
#         lenn = len(i)
#         name = i
# print(name)

# list_1 = ['www.google.com', 'www.wikipedia.org', 'www.gov.am', 'www.dzen.ru']
# for i in list_1:
#     l1 = str.split(i, '.')
#     print(l1[2])

# tuple_1 = (5, -6, 0.5, 8, 3)
# list_1 = list(tuple_1)
# list_2 = []
# for i in tuple_1:
#     a = min(list_1)
#     list_2.append(a)
#     list_1.remove(a)
# print(list_2)
#
# list_1 = [1, 2, 3, 5]
# str_ = ''
# for i in list_1:
#     str_ = str_ + str(i)
# print((int(str_) ** 2))

# 110
# Напишите программу, которая будет запрашивать у пользователя цело-
# численные значения и сохранять их в виде списка. Индикатором оконча-
# ния ввода значений должен служить ноль. Затем программа должна вы-
# вести на экран все введенные пользователем числа (кроме нуля) в порядке
# возрастания – по одному значению в строке. Используйте для сортировки
# либо метод sort, либо функцию sorted

# list_1 = []
# while True:
#     n = input('Number:')
#     if n == '':
#         break
#     if n == 0 or n[-1] != '0':
#         print('Incorrect number')
#     if n not in list_1:
#         list_1.append(n)
# print(sorted(list_1))

# 1
# tuple_1 = (1, 2, -3, 4)
# tuple_2 = (3, 5, 2, 1)
# tuple_3 = (2, -2, 0, 1)
# list_1 = list(zip(tuple_1, tuple_2, tuple_3))
# list_f = []
# for i in list_1:
#     j = sum(i)
#     list_f.append(j)
# print(tuple(list_f))

# 2
# sum_ = 0
# list_1 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, -6, 2, 8)]
# for i in list_1:
#     for j in i:
#         sum_ += j
# print(sum_)
#
# # mi toghov
#
# print(sum(sum(list(i)) for i in list_1))

# list_1 = [12, 41, 5, 8, 0, 11, -7, 9, -1]
# list_2 = [36, -12, 0, 18, -1, 12, 45, 21]
# list_f = []
# for i in list_1:
#     if i in list_2:
#         list_f.append(i)
# print(tuple(sorted(list_f)))

# tuple_1 = ((1, 2), (2, 3), (3, 4))
# print(list(list(i) for i in tuple_1))

# a = [1, 2, 3]
# b = [2, 3, 4, 5]
# list_1 = []
# list_1 += b
# for i in a:
#     if i not in list_1:
#         list_1.append(i)
# print(list_1)
#
# list_2 = []
# for i in a:
#     if i in b and i not in list_2:
#         list_2.append(i)
# print(list_2)
#
# list_3 = []
# for i in a:
#     if i not in b:
#         list_3.append(i)
# print(list_3)
#
# list_4 = []
# for i in a:
#     if i not in b:
#         list_4.append(i)
# for j in b:
#     if j not in a:
#         list_4.append(j)
# print(list_4)

# word = 'Herb the sage sage, the herb.'
# list_1 = word.split()
# list_2 = []
# for i in list_1:
#     i = str.lower(i)
#     if '.' in i:
#         i = i.replace('.', '')
#     if ',' in i:
#         i = i.replace(',', '')
#     list_2.append(i)
# list_3 = list_2[::-1]
# if list_3 == list_2:
#     print(True)
# else:
#     print(False)


# # #1
# word = input('Word:')
# v = {'a', 'e', 'i', 'o', 'u'}
# final = []
# word_s = word.split()
# for i in word:
#     if i in v and i not in final:
#         final.append(i)
# print(final)

# dict_auto = {}
# while True:
#     car = input('Model Price')
#     if car == '':
#         find = input('Model')
#         if find not in dict_auto:
#             print(None)
#         else:
#             print(dict_auto.get(find))
#     else:
#         car_s = car.split()
#         dict_auto.update({car_s[0]: car_s[1]})

# dict_1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict_2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
# dict_1.update(dict_2)
# print(dict_1)

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# print(200 in sample_dict.values())

# n = 8
# dict_1 = dict()
# for i in range(1, n+1):
#     dict_1[i] = i ** 2
#     print(i, '-', i ** 2)
# print(dict_1)

# dict_1 = {'P': 82, 'M': 65, 'H': 75}
# n = sorted(dict_1.values())
# for i, j in dict_1.items():
#     if j == n[0]:
#         print(i)

# 1
# sample_dict = {"name": "Kelly",
#                "age": 25,
#                "salary": 8000,
#                "city": "New york"}
# keys = ["name", "salary"]
# print({keys[0]: sample_dict.get(keys[0]), keys[1]: sample_dict.get(keys[1])})

# 2
# sampleDict = {"class 1": {"student_1": {"name": "Mike",
#                                         "marks": {"physics": 70,
#                                                   "history": 80}},
#                           "student_2": {"name": "Jack",
#                                         "marks": {"physics": 80,
#                                                   "history": 75}}},
#               "class 2": {"student_1": {"name": "Jon",
#                                         "marks": {"physics": 79,
#                                                   "history": 40}},
#                           "student_2": {"name": "Steven",
#                                         "marks": {"physics": 90,
#                                                   "history": 62}}}}
# while True:
#         name = input('Enter student name:')
#         subject = input('Enter subject:')
#         if name == '' or subject == '':  # ???stegh 2 angama hacnum???
#             print('END')
#             break
#         else:
#             for i in sampleDict.values():
#                 for j in i.values():
#                     for k in j.values():
#                         if k == name:
#                             print(j.get('marks').get(subject))
#
# def anun_tariq(a, b):
#     return a, b
#
#
# print(anun_tariq('gegham', '24'))

# list_1 = [3, 4, 8, 1, 9, 3, 6, 8, 9]
#
#
# def list_uniq(list_n):
#     print(list(set(list_n)))


#
#
# list_(list_1)

# str_1 = 'in coin we trust'
# list_0 = []
# list_i = ['a', 'e', 'i', 'o', 'u']
#
#
# def isvowels(i):
#     return i in list_i
#
#
# def vowels_append(str_):
#     for j in str_:
#         if isvowels(j):
#             list_0.append(j)
#     return list_0
#
#
# def vowelscount(str_new):
#     new_dict = dict()
#     v_a = vowels_append(str_new)
#     for i in v_a:
#         new_dict[i] = [v_a.count(i)]
#     return new_dict

# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# dict_1 = dict()
# for i in range(1, 100):
#     dict_1[i] = [is_prime(i)]
#
# list_1 = [2, 2, 5, 6, 4, 8, 9, 11, 12, 16, 17]
# for i in list_1.copy():
#     if i % 2 == 0:
#         list_1.remove(i)
# print(list_1)

# year = range(1, 2023)
# month = range(1, 13)
# day1 = range(1, 32)
# day2 = range(1, 31)
# day_p = range(1, 29)
# main_dict = dict()
# month_dict = dict()
# day1_dict = dict()
# for i in year:
#     main_dict[i] = month_dict
# for j in month:
#     month_dict[j] = day1_dict
# print(main_dict)
# # inp = input('date')
# # list_inp = inp.split('.')
# # d = list_inp[0]
# # m = list_inp[1]
# # y = list_inp[3]

# text = 'aabaa'
# for i in range(len(text) // 2):
#     if text[i] != text[len(text) - i - 1]:
#         print(False)
#         break
# else:
#     print(True)

