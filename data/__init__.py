from functools import reduce
# a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

# b = [i for i in a if i > 0]
# print(len(b))
# c = [i for i in a if i < 0]
# print(len(c))

# a = 'axbyczdj'
# b = a[::2]
# print(b)

# a = 1
# print('%03d' % a)

# a = [1, 3, 5, 7]
# a.insert(3,a[0])
# print(a[1:])

# a = 3
# b = 4
# a,b = b,a
# print('a=%d,b=%d' %(a,b))

# a = [1, 3, 10, 9, 21, 35, 4, 6]

# times = range(1,len(a))[::-1]
# print(list(times))
# for i in times:
#     for j in range(i):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
#     print('第%s轮交换数据为%s' %((len(a)-i),a))
# print(a)

# a = [1, 3, 6, 9, 7, 3, 4, 6]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# print(list(set(a)))

# a = 10
# b = reduce(lambda x,y: x*y,range(1,a+1))
# print(b)
# def digui(n):
#     if n == 1:
#         return 1
#     else:
#         return n*digui(n-1)

# print(digui(10))

# a = 0
# b = 1
# while b < 100:
#     print(b,end=',')
#     a,b = b,a+b


# def mi(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x*mi(x,n-1)
# print(mi(3,3))

