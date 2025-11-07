# 对对象的反射
class Foo:
    f = "类的静态变量"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi %s" % self.name)

obj = Foo("小问号",18)

# 检测是否含有name属性和say_hi属性
print(hasattr(obj,"name"))
print(hasattr(obj,"say_hi"))
"""
输出
    True
    True
"""

# 获取属性
print(getattr(obj,"name"))
func = getattr(obj,"say_hi")
func()

print(getattr(obj,"job","不存在"))
"""
输出
    小问号
    Hi 小问号
    不存在
"""
# 对类的反射
class Foo(object):
    staticField = "test"

    def __init__(self):
        self.name = "老问号"

    def func(self):
        return "func"
    
    @staticmethod
    def bar():
        return "bar"

print(getattr(Foo,"staticField"))   # 输出 test
print(getattr(Foo,"func"))          # 输出 <function Foo.func at 0x101001300>
print(getattr(Foo,"bar"))           # 输出 <function Foo.bar at 0x1010013a0>


# 案例：基于反射的用户管理（使用反射前）
class User:
    def login(self):
        print("欢迎来到登录页面")
    def register(self):
        print("欢迎来到注册页面")
    def save(self):
        print("欢迎来到保存页面")

user = User()
while True:
    choose = input('请输入你的选择（login/register/save）>>>').strip()
    if choose == 'login':
        user.login()
        break
    if choose == 'register':
        user.register()
        break
    if choose == 'save':
        user.save()
        break

# 案例：基于反射的用户管理（使用反射后）
class User:
    def login(self):
        print("欢迎来到登录页面")
    def register(self):
        print("欢迎来到注册页面")
    def save(self):
        print("欢迎来到保存页面")

user = User()

while 1:
    choose = input('请输入你的选择（login/register/save）>>>').strip()
    if hasattr(user,choose):
        func = getattr(user,choose)
        func()
        break
    else:
        print('请重新选择')
        continue