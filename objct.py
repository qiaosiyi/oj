import sys
from copy import deepcopy
class Student(object):
	def __init__(self, name, chi, mat, eng):
		self.name = name
		self.chi = chi
		self.mat = mat
		self.eng = eng
		self.total = chi + mat + eng
		if self.chi < 60 or self.mat < 60 or self.eng < 60:
			self.passed = False
		else:
			self.passed = True
	
	def __gt__(self, other):
		
		if self.total > other.total:
			return True
		elif self.total < other.total:
			return False
		else:
			if self.chi > other.chi:
				return True
			elif self.chi < other.chi:
				return False
			else:
				if self.mat > other.mat:
					return True
				elif self.mat < other.mat:
					return False
				else:
					if self.eng > other.eng:
						return True
					elif self.eng < other.eng:
						return False
					else: 
						if self.name < other.name:
							return True
						else:
							return False
	
	def __str__(self):
		return "%s %d %d %d" % (self.name, self.chi, self.mat, self.eng)
def sort_students(students):
	length = len(students)
	for j in range(length):
		for i in range(0, length - 1):
			if students[i+1] > students[i]:
				tmp = deepcopy(students[i+1])
				students[i+1] = deepcopy(students[i])
				students[i] = deepcopy(tmp)

def find_all_students(en_students, students):
	while True:
		next_s = students.pop(0)
		if next_s.total != en_students[-1].total:
			students.insert(0, next_s)
			break
		en_students.append(next_s)

def enroll(students):
	en_students = []
	for rank in range(3):
		en_students.append(students.pop(0))
		find_all_students(en_students, students)
	return en_students
students = []	
if __name__ == "__main__":
	
	for i in range(10):
		line = sys.stdin.readline().strip()
		entries = line.split()
		students.append(Student(name=entries[0], chi=int(entries[1]),mat=int(entries[2]),eng=int(entries[3])))
	sort_students(students)
	
	print('[First round name list]')
	for stu in students:
		print(stu)
		
	print()
	print('[Final name list]')
	for stu in enroll(students):
		print(stu)
