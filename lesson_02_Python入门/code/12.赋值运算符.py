# 赋值运算符
# = 可以将等号右侧的值赋值给等号左侧的变量
# +=  a += 5 相当于 a = a + 5 
# -=  a -= 5 相当于 a = a - 5 
# *=  a *= 5 相当于 a = a * 5 
# **= a **= 5 相当于 a = a ** 5 
# /=  a /= 5 相当于 a = a / 5 
# //= a //= 5 相当于 a = a // 5 
# %=  a %= 5 相当于 a = a % 5 
a = 10
# a = a + 5
# a += 5
a -= 5
a *= 5
a **= 2
a /= 25
a = 25.0 # 在对浮点数做算术运算时，结果也会返回一个浮点数
a //= 5
a = 5
a %= 4

print('a =',a)
