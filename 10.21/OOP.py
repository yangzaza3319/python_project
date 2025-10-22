""" 
模拟一个简单的校园场景，包含 学生（Student） 和 教师（Teacher），两者都继承自 人类（Human） 基类，体现 OOP 核心思想
案例目标
1. 展示类与对象的定义与实例化
2. 演示实例属性vs类属性
3. 实现封装（私有属性）
4. 使用继承与方法重写
5. 体现多态的行为
6. 动态操作属性（增删改查）
"""
class Human:
    """人类基类"""
    species = "Homo sapiens"  # 类属性：所有人类共享
    population = 0            # 类属性：统计总人数

    def __init__(self, name, age):
        self.name = name      # 实例属性
        self.age = age
        Human.population += 1  # 每创建一个对象，总人数+1

    def introduce(self):
        """自我介绍（将被子类重写）"""
        print(f"我是 {self.name}，今年 {self.age} 岁。")

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"


class Student(Human):
    """学生类，继承自 Human"""
    school = "阳光中学"       # 类属性：所有学生共享
    student_count = 0         # 类属性：学生人数

    def __init__(self, name, age, student_id, grades=None):
        super().__init__(name, age)          # 调用父类构造方法
        self.student_id = student_id         # 学号（实例属性）
        self.__grades = grades or []         # 私有属性：成绩列表（封装）
        Student.student_count += 1

    def add_grade(self, grade):
        """添加成绩（封装：通过方法操作私有属性）"""
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("成绩应在 0-100 之间！")

    def get_average(self):
        """计算平均分"""
        return sum(self.__grades) / len(self.__grades) if self.__grades else 0

    def introduce(self):
        """重写父类方法（多态）"""
        avg = self.get_average()
        print(f"我是学生 {self.name}，学号 {self.student_id}，平均分 {avg:.1f}。")

    # 使用 property 安全访问私有属性（进阶）
    @property
    def grades(self):
        return self.__grades.copy()  # 返回副本，防止外部修改


class Teacher(Human):
    """教师类，继承自 Human"""
    department = "综合教研组"  # 类属性
    teacher_count = 0

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject   # 教授科目（实例属性）
        Teacher.teacher_count += 1

    def introduce(self):
        """重写父类方法（多态）"""
        print(f"我是 {self.subject} 老师 {self.name}，欢迎来听课！")

    def grade_student(self, student, grade):
        """给学生打分"""
        student.add_grade(grade)
        print(f"{self.name} 给 {student.name} 打了 {grade} 分。")


"""
演示与测试
"""

if __name__ == "__main__":
    print("=== 创建对象（实例化） ===")
    stu1 = Student("小明", 16, "S1001", [85, 90, 78])
    stu2 = Student("小红", 15, "S1002")
    tea1 = Teacher("李老师", 35, "数学")

    print("\n=== 多态：不同对象调用同名方法 ===")
    stu1.introduce()   # 学生版自我介绍
    tea1.introduce()   # 教师版自我介绍

    print("\n=== 封装：通过方法操作私有属性 ===")
    tea1.grade_student(stu2, 92)
    tea1.grade_student(stu2, 88)
    print(f"{stu2.name} 的成绩：{stu2.grades}")
    print(f"平均分：{stu2.get_average():.1f}")

    print("\n=== 类属性统计 ===")
    print(f"人类总数：{Human.population}")
    print(f"学生人数：{Student.student_count}")
    print(f"教师人数：{Teacher.teacher_count}")

    print("\n=== 动态添加属性（对象级别） ===")
    stu1.nickname = "明明"  # 动态绑定
    print(f"{stu1.name} 的昵称是：{stu1.nickname}")
    # print(stu2.nickname)  # ❌ AttributeError

    print("\n=== 属性查找顺序演示 ===")
    print(f"stu1.school = {stu1.school}")      # 实例无 → 查类 → "阳光中学"
    stu1.school = "星辰中学"                   # 创建实例属性，遮蔽类属性
    print(f"修改后 stu1.school = {stu1.school}")  # 实例属性
    print(f"Student.school = {Student.school}")    # 类属性未变

    print("\n=== 安全属性操作 ===")
    if hasattr(stu1, 'nickname'):
        print("stu1 有昵称属性")
        print("昵称是：", getattr(stu1, 'nickname'))
    
    setattr(stu1, 'email', 'xiaoming@school.com')
    print("已设置邮箱：", stu1.email)

    print("\n=== 对象字典查看 ===")
    print("stu1 实例属性：", stu1.__dict__)
    print("Student 类属性：", Student.__dict__.keys())

"""
输出
=== 创建对象（实例化） ===

=== 多态：不同对象调用同名方法 ===
我是学生 小明，学号 S1001，平均分 84.3。
我是 数学 老师 李老师，欢迎来听课！

=== 封装：通过方法操作私有属性 ===
李老师 给 小红 打了 92 分。
李老师 给 小红 打了 88 分。
小红 的成绩：[92, 88]
平均分：90.0

=== 类属性统计 ===
人类总数：3
学生人数：2
教师人数：1

=== 动态添加属性（对象级别） ===
小明 的昵称是：明明

=== 属性查找顺序演示 ===
stu1.school = 阳光中学
修改后 stu1.school = 星辰中学
Student.school = 阳光中学

=== 安全属性操作 ===
stu1 有昵称属性
昵称是： 明明
已设置邮箱： xiaoming@school.com

=== 对象字典查看 ===
stu1 实例属性： {'name': '小明', 'age': 16, 'student_id': 'S1001', '_Student__grades': [85, 90, 78], 'nickname': '明明', 'school': '星辰中学', 'email': 'xiaoming@school.com'}
Student 类属性： dict_keys(['__module__', '__firstlineno__', '__doc__', 'school', 'student_count', '__init__', 'add_grade', 'get_average', 'introduce', 'grades', '__static_attributes__'])
"""