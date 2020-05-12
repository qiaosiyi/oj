# coding=UTF-8
# 学习使用sorted函数，传入一个比
class Student:
  def __init__(self, name, grade, age):
    self.name = name
    self.grade = grade
    self.age = age
  def __repr__(self):
    return "%s %d %d" % (self.name, self.grade, self.age)

def my_cmp(self, other):
    return self.grade - other.grade
    
def my_cmp2(self,other):
    if self.grade > other.grade:
      return 1
    elif self.grade == other.grade:
      if self.age < other.age:
        return 1
      else:
        return -1
    else:
      return -1

student_objects = [
    Student('john', 92, 15),
    Student('jane', 94, 12),
    Student('dave', 94, 10)
    ]

print sorted(student_objects,cmp=my_cmp2,reverse=True)









    