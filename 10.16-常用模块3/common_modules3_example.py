# random：生成随机数
import random

print(random.random())      # 输出 0.687012128698404，打印大于0且小于1之间的小数
print(random.uniform(1,3))  # 输出 1.2471191912922766 大于1小于3的小数

print(random.randint(1,5))       # 输出 大于等于1且小于等于5的随机整数
print(random.randrange(1,10,2))  # 输出 大于等于1且小于10之间的随机奇数

ret = random.choice([1,'23',[4,5]])
print(ret)  # 输出 1或者23或者[4,5]

a,b = random.sample([1,'23',[4,5]],2)
print(a,'和',b) # 列表元素任意两个组合

item = [1,3,5,7,9]
random.shuffle(item)
print(item)   # 输出随机的次序

# random:生成随机验证码
import random
import string

def v_code():
    chars = string.ascii_uppercase + string.digits  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' 直接从字符池中随机选字符
    return ''.join(random.choices(chars, k=5))

print(v_code())
