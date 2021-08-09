# Task №1

a = 5

b = 7

c = a + b

d = a - b

print( {c,d})

# Task №2

x = int(input('Введите значение "х:"'))

y = int(input('Введите значение "y:"'))

e = (abs(x)-abs(y))/(1+abs(x * y))

print(e)

# Task №3

l = int(input('Введите значение "l_длина ребра куба:"'))

v = l ** 3

s = 4 * l ** 2

print({v,s})

# Task №4

k = (a + b)/2   #Среднее арифметическое

g = (a + b)**(1/2)  #Среднее геометрическое

print({g,k})

# Task №5

u = int(input('Введите значение "u_катет:"')) #Катет прямоугольного треугольника

w = int(input('Введите значение "w_катет:"')) #Катет прямоугольного треугольника

s_triangle = (u * w)/2

t_hypotenuse = (u ** 2 + w ** 2) ** 1/2

print([s_triangle,t_hypotenuse])
