class Course:
    def __init__(self,id,name,credit,elective,teacher,time):
        self._id = id
        self._name = name
        self._credit =credit
        self._elective=elective
        self._teacher =teacher
        self._time =time


c1 = Course ('abc','esp32','3','Y','john','3h')
print("課程代碼=",c1._id)
print("課程名稱=",c1._name)
print("學分數=",c1._credit)
print("必選修=",c1._elective)
print("任課老師=",c1._teacher)
print("上課時間=",c1._time)