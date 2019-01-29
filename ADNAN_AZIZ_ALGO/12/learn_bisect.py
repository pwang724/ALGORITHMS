import collections
import bisect

#bisect sorts in ascending order. if tuple, order priority is first element, then second, etc
#bisect left: returns index of insertion point of element after all similar elements if they exist
#bisect right: returns index of insertion point of element after all similar elements
#insort left, insort right: does same, but inserts element inside array

#insort is same as insort right. in terms of insertion, it is same thing, but less elements
# are shifted so computationally more efficient


Student = collections.namedtuple("Student", ("name", "gpa"))

def comp_gpa(student):
    return (-student.gpa, student.name)

#bisect works if sort works in ascending order
def search_student(students, target, comp_gpa):
    student_list = [comp_gpa(s) for s in students]
    i = bisect.bisect_left(student_list, comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target


class student:
    def __init__(self):
        self.named_tuple = collections.namedtuple("Student", ("name", "gpa"))
        self.student_list = []

    def comp_gpa(self, student):
        return (-student.gpa, student.name)

    def add_student(self, student):
        student = self.named_tuple(student[0],student[1])
        bisect.insort_left(self.student_list, self.comp_gpa(student))

    def return_student(self, student):
        student = self.named_tuple(student[0],student[1])
        i = bisect.bisect_left(self.student_list, self.comp_gpa(student))
        return i < len(self.student_list) and self.student_list[i] == self.comp_gpa(student)

if __name__ == '__main__':
    s = student()
    s.add_student(['a', 3.4])
    s.add_student(['c', 3.6])
    s.add_student(['b', 3.5])
    print(s.student_list)
    print(s.return_student(['b', 3.5]))