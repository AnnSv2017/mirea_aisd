# 10 вариант
# Метод Хорд

# Импорт арккосинуса
from math import acos
# Функция, в которой нужно найти корень
def f(x):
  return acos((1-x**2)/(1+x**2))-x
a, b = 2, 3
x0 = a
# Идём пока не найдём корень или пока разница между x и x0(предыдущее значение x) почти не станут равны
while True:
  x = a-(f(a)*(b-a))/(f(b)-f(a))
  if f(x)==0:
    print(x)
    break
  if f(x)*f(b)>0:
    b = x
  else:
    a = x
  if abs(x-x0)<=0.0001:
    print(x)
    break
  x0 = x
