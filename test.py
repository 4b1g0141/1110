class Student:
    def __init__(self, id, name, major):
        self._id = id
        self._name = name
        self._major = major
 
s1 = Student('4b1g001', 'A', '資工')
print("學生s1學號=",s1._id)
print("學生s1姓名=",s1._name)
print("學生s1學科=",s1._major)

s2 = Student('4b1g002', 'B', '資工')
print("學生s2學號=",s2._id)
print("學生s2姓名=",s2._name)
print("學生s2學科=",s2._major)
