# 10 номер
# Метод половинного деления

# Импорт арккосинуса
from math import acos
# Функция, в которой нужно найти корень
def f(x):
  return acos((1-x**2)/(1+x**2))-x
l, r = 2, 3
# Пока не найдём корень, т.е. r примерно не будет равно l
while r-l>0.0001:
  m = (l+r)/2
  fm = f(m)
  if fm==0:
    break
  if f(l)*fm<0:
    r = m
  else:
    l = m
print(m)
