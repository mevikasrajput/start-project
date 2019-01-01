# def intersect(str1,str2):
#     res=[]
#     for x in srt1:
#         if x in str2:
#             res.append(x)
#     return res
# srt1='Rajuram'
# str2='Rajubala'
# i=intersect(srt1,str2)
# print i

# def maker(m):
#     def make(n):
#         return m**n
#     return make    
# f=maker(2)
# print f(5)

# def maker(n):
#     return lambda m:m**n
# h=maker(5)
# print h(4)

# f=lambda x,y,z:x+y+z
# print f(2,3,4)

# def add(x=1,y=2):
#     return x+y
# print add(6) 

# l=[lambda x: x**2,lambda x:x**3,lambda x:x**4]
# for f in l:
#     # print f(2)
#     print l[0](3)

# def fun1(a):
#     return a**2
#     def fun2(b):
#         return b**3
#         def fun3(c):
#             return c**4
# l=[fun1,fun2,fun3]
# for f in l:
#     print f(2)