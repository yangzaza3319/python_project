# 添加类和对象的属性

class Myclass:
    class_attr = "这是类属性attribute"    # 类属性：内部添加

    def __init__(self,name):            # 对象属性：内部添加
        self.name = name 
    
    def add_instance_attr(self,age):    # 对象属性：内部添加（通过动态方法）
        self.age = age

## 创建实例
obj1 = Myclass("object1")


## 访问类属和对象属性
print(obj1.name)                 # 输出 object1
print(Myclass.class_attr)        # 输出 这是类属性attribute

## 对象属性（外部添加）

obj1.gender = "Male"             # 动态的给 obj1 添加gender属性
print(obj1.gender)               # 输出 Male

## 类属性：外部添加
Myclass.new_class_attr = "这是新的类属性new_attribute"
print(Myclass.new_class_attr)  # 输出 这是新的类属性new_attribute

## 创建另一个实例，验证类属性的共享性
obj2 = Myclass("obj2")
print(obj2.name)
print(obj2.new_class_attr)

## 在内部通过方法添加对象属性
obj1.add_instance_attr(23)
print(obj1.age) # 输出 23

obj2.add_instance_attr(12)
print(obj2.age) # 输出 12
