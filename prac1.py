# -*- coding: utf-8 -*-
#1
height = 1.75
weight = 80.5
bmi = weight/(height*height)
print('你的BMI指数为%.2f'%bmi)
print('\n')
if bmi<18.5:
	print("过轻")
elif bmi>=18.5 and bmi<25.0:
	print('正常')
elif bmi>=25.0 and bmi<28.0:
	print('过重')
elif bmi>=28.0 and bmi<32.0:
	print('肥胖')
elif bmi>=32.0:
	print('严重肥胖')
print('\n')

#2
sum = 0
for x in range(101):
	sum = sum + x
print(sum,'\n')

#3
L = ['Bart', 'Lisa', 'Adam']
for s in L:
	print(s)

#4
a=[1,3,23,12,45,2,8,10]
a.sort()
print(a)
