# string = 'hello world'
# f = open('hello world.txt','w')
# f.write(string)
# f.close()
# 机器学习 = ['决策树','神经网络']
#
# for i in 机器学习:
#     print(i)


#A,b = 1.5,'hello'
#a = b = c = 10
#print(A,b)

=======================================================================
'''
import math
#import math as m    #math库用m代替
print(math.sin(0))
'''
=======================================================================

#===列表的操作===
Li = [2.1,'hello',print('hehe'),True,[0.0,1]]
#标号  0     1        2           3     4
#     -5    -4        -3          -2    -1
#列表中的数据类型可以是python中任意的数据类型

#注意此列表中有print函数，打印出列表的值时
#列表中调用的print函数的输出不在打印的列表值中
#而是单独打印出来
print(Li[0])
print(Li[-3])#这里打印列表中print的值，输出是None，即print函数的返回值
print(Li[-4])


#列表值的切片操作，左闭右开区间
print(Li[0:2])
print(Li[:])#列表中所有元素，从头取到尾
print(Li[::-1])#从头取到尾，步长为-1，列表元素反着输出

#列表的操作：增、删、改、查
#改
Li[0] = 100
#删一个
Li.remove(Li[1])
#删多个
del Li[-2:] #从-2开始往右的都删了
#del Li  #列表直接删了
#添加，默认是添加到列表尾端

#方法append拓展一个任意的数据类型，是一个！多个出错eg.是一个列表拓展进去
Li.append(['string',1.5])

Li.extend(['yuansu',4.0])

#方法extend是把这些拆成单个元素拓展，弥补append
#但同样extend函数里面写的时候也是只能写
#一个数据类型，知识拓展进去时后可以被拆成单个元素，而不是像append一样拓展子表

Li.insert(0,'hehehehe111')  #插入，在第0个元素之前，注意会改变编号！！！
print(Li)

=================================================================================

#Li = [2.1,'hello',True,[0.0,1]]
x = []
for i in range(10):    #默认从0开始，（0，9）左闭右开，range(10)相当于range(0,10)
    x.append(i)
    print(x)

y = [i for i in range(10)]#第一个i表示列表中的元素，空格后是对i的解释
y = [i**2 for i in range(10)]
y = [i**2 for i in range(10) if i%2==1]
print('y:',y)

==================================================================================

#===求曲边图形的面积===
import math
n = 10
width = 2*math.pi/n
#方案一
# x = []
# for i in range(n):
#     x.append(i*width)
# y = [abs(math.sin(i)) for i in x]
# s = sum(y)*width
# print(s)

#方案二
S = sum([abs(math.sin(i*width))*width for i in range(10)])
print(S)

==================================================================================

#冒泡排序法用条件判断和循环
x = [1,2,6,0.3,2,0.5,-1,2.4]
for i in range(len(x)):
    for j in range(i):
        if x[j] > x[i]:
            x[j],x[i] = x[i],x[j]
print(x)

==================================================================================

#===字符串===
string = 'my name'
string = "my name"
#三个单引号也可以
string = """my name"""

example_string = 'my'+' name'+'???'
example_string = '='*100    #字符串打印100次

res = string[0]
res = string[0:4]
#string[0] = 'A',字符串与列表不同，字符串值不可修改
res = string.split(sep = ' ')   #sep是识别分割的特定变量，这里用空格作为分隔符，若不写sep则任何返回为空的东西都可以做分隔符
#split打散后，存入res的是一个列表
print(res)

==================================================================================

#===字典===
import re
dic = {'A':0.1  , 0.5:[1,2,3]} #字典是由键值对构成的
#eg.A:B中冒号前面的是键，冒号后面的是值
#重要！！！——键A的类型不能是可变类型，如列表
#键不可重复，否则该键的值以最后赋值的为准

#字典的增、删、改、查
#重要！！！——字典中元素是没有顺序关系的，与列表、字符串不同，检索不能用位置编号
#重要！！！——而是用检索键的方式进行
#print(dic.keys())#打印字典里的所有键
#print(dic.values())#打印字典里的所有值
#print(dic.items())#键和值
res = dic['A']
dic['A'] = 7
dic[0.5] = [3,2,1]  #注意！！！dic中的0.5是键，就是一个标量作为键名字，不要多打其他符号
print(dic['A'])

#新增一个键值对
dic['B'] = 123

#删除操作
del dic['B']

#批量新增
dic.update({1.5:[] , 'a':print('hello')})

dic = {i:i**2 for i in range(10)}

lyric = 'The night begin to shine, the night begin to shine.'
lyric = lyric.lower()
#lyric = re.sub(',','AAAAA',lyric)    #把逗号用AAAAA替换了，在lyric中执行这个操作
#lyric = re.sub('[,.?;:"\]','AAAAA',lyric)
#重要！！！把,.?等等标点符号，全部用AAAAA替换了，在lyric中执行该操作

lyric = re.sub('[,.?":;\']','',lyric)#这里替换处不是空格，而是空
words = lyric.split()

word = set(words)
#set 构建了一个集合，集合里面元素不重复，无序

# res = words.count('shine')#可以用方法count进行简单的计数
# print(res)

dic = {i:words.count(i) for i in word}#整句话中各单词出现频次
print(dic)

====================================================================================


#===文件操作与Walden字数统计===

import os
import re
print(os.getcwd())#打印出工程的当前目录

#f = open('Walden.txt', 'r')#要导入文件在工程目录下时
f = open('D:/python/my projects/test/Walden.txt','r')
#注意!!!win下的系统层级是用\的，但python中是/ 要注意换过来，或者用\\
#注意！！！或者前面加r eg.r'D:\python\my projects\test'不用改斜线方向
txt = f.read()
#txt = f.read(50)获取前50个字符
#txt = f.readlines()
#文件按行读取，最终输出的是列表，每换一行就以字符串保存进列表，包括换行符
#txt = f.readlines(10)读前10行
f.close()

lyric = txt.lower()
lyric = re.sub('[,.?":;\'-]','',lyric)
words = lyric.split()
word = set(words)
dic = {i:words.count(i) for i in word}

print(dic)

=======================================================================================

#====字数统计方案优化=====
import re
f = open('D:/python/my projects/test/Walden.txt','r')
txt = f.read()
f.close()
lyric = txt.lower()
lyric = re.sub('[,.?":;\'-]','',lyric)
words = lyric.split()#经过操作后，words是一个列表
#====方案一=====，用set构建集合去重，速度很慢
# word = set(words)
# dic = {i:words.count(i) for i in word}

#dic.keys()#打印字典里的所有键
#dic.values()#打印字典里的所有值
#dic.items()#键和值

#===方案二=======
dic = {}
for word in words:
    if word in dic.keys():   #判断字典中有没有键是已经出现过的
        dic[word] += 1
    else:
        dic[word] = 1   #之前没出现过，放入字典并计一次数
res = sorted(dic.items(),key=lambda x:x[1],reverse=True)
#sorted排序使用
print(res)


========================================================================================

#=====函数======
def count(x,z=0):
    for i in x:
        if i%2==1:
            z = z+1
    return z

res = count([1,2,3,4,5])

#x:x[1]是指以x为自变量，返回值是x[1]
#在函数y（x）中我们看到x是一个列表['the',7346]
#其中x[0] = 'the'而x[1] = 7346，所以返回值是x[1]，即为7346
y = lambda x:x[0]
res = y(['the',7346])
print(res)



========================================================================================
#=====面向对象=====

class Human:
#__init__是初始化，一旦类被实例化成了对象zhangfei = Human()这句一写
#就被初始化了def __init__里面的东西就会被执行
#def sqrt则不同，他需要被对象调用了，才执行
    def __init__(self,sex=None,age=None):
        self.sex = sex
        self.age = age
        #print('0hello')

    def sqrt(self,x):
        #print('1hello')
        return x**2

#self 在写sqrt后自己生成的，可以改成其它的，这个是对象的对应入口

zhangfei = Human(sex='男')
res = zhangfei.sqrt(10)
res = zhangfei.age
res = zhangfei.sex
print(res)


========================================================================================
#=====模块======

#方案一
# from def_fun import count
# from def_fun import Human
#
# res = count([1,2,3])
# zhangfei = Human()
#
# print(res)

#方案二
import def_fun
res =def_fun.count([1,2,3])
print(res)













