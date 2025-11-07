# 类的约束

## 写一个简单的支付功能
class QQpay:
    def pay(self,money):
        print('使用QQ支付%s元' % money)
class Alipay:
    def pay(self,money):
        print('使用支付宝支付%s元' % money)
a = Alipay()
a.pay(100)

b = QQpay()
b.pay(200)

## 统一一下付款方式
class QQpay:
    def pay(self,money):
        print('使用QQ支付%s元' % money)
class Alipay:
    def pay(self,money):
        print('使用支付宝支付%s元' % money)

def pay(obj,money):
    obj.pay(money)

pay(Alipay(),100)
pay(QQpay(),200)
"""
输出
    使用支付宝支付100元
    使用QQ支付200元
"""

## 再添加微信支付，但是没有统一标准，换个程序员可能产生混乱的代码
class QQpay:
    def pay(self,money):
        print('使用QQ支付%s元' % money)
class Alipay:
    def pay(self,money):
        print('使用支付宝支付%s元' % money)
class Wechatpay:
    def fukuan(self,money):
        print('使用微信支付%s元' % money)
def pay(obj,money):
    print("************")
    obj.pay(money)

pay(Alipay(),100)
pay(QQpay(),200)

Wechatpay().fukuan(300)

# 抽象基类+@abstramethod

from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,money):
        pass
class Alipay(Payment):
    def pay(self,money):
        print(f"支付宝支付{money}元")
class QQpay(Payment):
    def pay(self,money):
        print(f"QQ支付{money}元")

class Badpay(Payment):
    def __init__(self):
        pass
Alipay().pay(100)   # 输出
Badpay()    # 输出 TypeError: Can't instantiate abstract class Badpay without an implementation for abstract method 'pay'

# 结构化鸭子类型
from typing import Protocol
class Payable(Protocol):
    def pay(self,money:float ) -> None: ...
def make_payment(payer:Payable,amount:float):
    payer.pay(amount)
class Alipay:
    def pay(self,money):
        print(f'支付宝支付{money}元')
class Wechatpay:
    def pay(self,money):
        print(f'微信支付{money}元')
make_payment(Alipay(),100)
make_payment(Wechatpay(),200)
"""
输出
    支付宝支付100元
    微信支付200元
"""