# int , float, str, list , dict

#кортеж   tuple - это тип данных в питоне
# отличия списка от списка(list) тем что
# кортеж -неизменяемый

#Создание кортежа вот такие скобки ()
# tuple=()
# print(tuple)
# print(type(tuple))
#     0 1 2
# list=[1,2,3]
# list[0]=4
# print(list)

# удалить, заменить элемент в кортеже
# добавление(concatenate) может быть кортеж с кортежом
#Пример1.
# tuple_numbers=(1,2,3)
# tuple_numbers_2=(6,7)
# tuple_numbers+=tuple_numbers_2
# print(tuple_numbers)

#Задание1. tuple=(3,4) tuple2=(9,10)
#tuple=(3,4,9,10)

#Пример2. tuple=(6,2,9,1) вывести его длину, max и min
# tuple=(6,2,9,1)
# print("вывод длины",len(tuple))
# print("вывод макса",max(tuple))
# print("вывод min", min(tuple))
#Задание2. tuple=(9,1,2,5)  вывести его длину, max и min

#Пример3. tuple=(2,3,4) вывести его сумму.
# tuple=(2,3,4)
# print(sum(tuple))

#Задание3. tuple=(5,1,3) вывести его сумму.

#Пример4. узнать сколько там есть цифр 2 в кортеже

# tuple=(2,3,4,2,2)
# print(tuple.count(2))

#Задание4. узнать сколько там есть цифр 4 в кортеже
# tuple=(4,1,4,6,8)


#Пример5.вывести значения кортежа по for
#      0 1 2 3 4
tuple=(3,2,3,4,3) # len(tuple)=5

for i in range(len(tuple)): # 0<len(tuple) 0<5 1<5 2<5 3<5  4<5    5<5false
  print(tuple[i])  # tuple[0]=3 tuple[1]=2 tuple[2]=3 tuple[3]=4 tuple[4]=3
#Задание5.вывести значения кортежа по for
tuple=(3,1,4)












