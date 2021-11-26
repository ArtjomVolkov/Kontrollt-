#f=int(input("Сколько вы хотите зверьков от 1 до 9? =>"))
#if f>9:
#	print("Надо меньше 10")
#elif f<1:
#	print("Не меньше 0")
#else:
#	a=str("^---^")
#	b=str(" o o ")
#	c=str("! = !/")
#	print(a*f)
#	print(b*f)
#	print(c*f)
#print()
#a=""
#while a not in[1,2,3,4,5,6,7,8,9]:
#    try:
#        a=int(input("Сколько зверьков показать (от 1 до 9) => "))
#    except ValueError:
#        print("Напишите число от 1 до 9: ")
#for i in range(a):
#    print(" ^---^ ", end=(" "))
#print()
#for i in range(a):
#    print("( o o )", end=(" "))
#print()
#for i in range(a):
#    print("! = !/)", end=(" "))
#print()
#print(" ^---^"" ""\n( o o )"" ""\n! = !/)")
#Задание 2
#c = int(input("Показатель степени => "))
#n = int(input("Предел => "))
#i = 1
#while i ** c <= n:
#    print(i ** c, end=" ")
#    i += 1
#print()
#print(n,"Последнее число,"
#      " возведенное в степень =>", i - 1)
#Задание 3
#from random import *
#print("Известны оценки по физике каждого из  учеников класса. Определить минимальную и максимальную оценки. (Оценки и количество учеников получаем случайным образом")
#print()
#maxOcenka=0
#minOcenka=5
#kolvo=randint(1,25)
#for i in range(kolvo):
#	ocenka=randint(1,5)
#	if ocenka<5:
#		ocenka=ocenka
#	print(ocenka, end=" ")
#	if ocenka>maxOcenka:
#		maxOcenka=ocenka
#	if ocenka<minOcenka:
#		minOcenka=ocenka
#print()
#print("Минимальная оценка => ",minOcenka)
#print("Максимальная оценка => ",maxOcenka)
#Задание 4
#a = 0
#b = 0
#for i in range (8):
# a = a + 3
# b += 2
# print (a,"час =>",b ,"клеток")
# print (end =" ")
#Задание 5
#a=int(input("Сколько котлет у Губки Боба? =>"))
#b=int(input("Сколько на одну сковородку помещается котлет? =>"))
#for i in range (a):
#	c=a//b
#print(f"Понадобится {c} сковородки")
#for i in range (a):
#	k=a%b
#print(f"Останется {k} котлет")
