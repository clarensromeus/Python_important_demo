
"""
 #* iterators is an object that can contain a countable number of value 
 #* technically an iterator in python is an object which implements the iterator protocol
 #* and using the dunder or magic or special methods  __iter__ and __next__ 
"""


def students(studs):
    try:
        student = []
        for s in studs:
            student.append(s)
        return student
    except TypeError:
        print("not good")


studentResults = students(["Romeus", "Jhonny", "Williams", "Prettison"])
print(f"student: {studentResults}")


# using iterators with a method
def student_with_Iterators(studs):
    student = []
    for s in studs:
        student.append(s)
    return student


res = iter(student_with_Iterators(
    ["Romeus", "Jhonny", "Williams", "Prettison"]))


# * using this way is to iterate over all data from the iterator
# * for those who prefer for in loop might use it as well to iterate upon the iterator's data
while True:
    try:
        st = next(res)
        print(f"student : {st}")
    except StopIteration:
        break

# using iterators with class


class Students:
    __result = 0

    def __init__(self, value, end):
        self.value = value
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if (self.value >= self.end):
            raise StopIteration

        self.__result = self.value
        self.value += 1
        return self.__result


# * now the class turns out to be an iterator which  we can iterate upon to get values
for stud in Students(1, 10):
    print(f"sutudent : {stud}")
