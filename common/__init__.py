"""
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。  
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求1000以内的水仙花数（3位数） 
"""
# i = 100
# while i < 1000:
#     x = i // 100
#     y = (i - x*100) // 10
#     z = i - x*100 - y*10
#     if (i == x**3 + y**3 + z**3):
#         print(i)
#         i += 1
#     else:
#         i += 1


"""
打印99乘法表
"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d' %(i,j,i*j),end='  ')
#     print('')

"""
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8] 
问题1.对列表a 中的数字从小到大排序
问题2.排序后去除重复的数字
"""
# a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]

# print(sorted(a,reverse=True))
# print(set(a))


"""
如果有一个列表a=[1,3,5,7,11]
问题：
1.如何让它反转成[11,7,5,3,1]
2.如果取到奇数位值的数字，如[1,5,11]
"""
# a = [1,3,5,7,11]
# b = []
# for i in range(len(a)):
#     if (i)%2 != 0:
#         continue
#     else:
#         b.append(a[i])
# print(b)
# print(a[::2])

# print(sorted(a,reverse=True))
# a.reverse
# print(a)


"""
如何判断一个数组是对称数组：
要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
用Python代码判断，是对称数组打印True，不是打印False,如：
x = [1, "a",  0, "2", 0, "a", 1]
"""
# x = [1, "a",  0, "2", 0, "a", 1]
# a = x[0:len(x)//2]
# print(a)
# b = x[-1:(len(x)//2)*-1-1:-1]
# print(b)
# if a == b:
#     print('True')
# else:
#     print('False')

"""
如果一个正整数等于除它本身之外其他所有除数之和，就称之为完全数。
例如：6是完全数，* 因为6 = 1+2+3；
下一个完全数是28 = 14+7+4+2+1。 
求1000以下的完全数
"""


for i in range(1,1001):
    sum_num = []
    for j in range(1,i):
        if i % j == 0:
            sum_num.append(j)
    if sum(sum_num) == i:
        print(i)

