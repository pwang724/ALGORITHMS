import collections
import bisect

Student = collections.namedtuple("Student", ("name", "grade_point_average"))

def comp_gpa(student):
    return (-student.grade_point_average , student.name)

#weird:
# 1. assumes that list of students is already sorted despite not being encapsulated in a class
# with a defined comparator for sorting GPA
# 2. goal is presumably to find a student, but multiple students can have the same GPAs.
# if searching for (3.5, B) and list has (3.5, A) and (3.5, B), it'll return false
def search_student(students, target, comp_gpa):
    list_conv = [comp_gpa(s) for s in students]
    i = bisect.bisect_left(list_conv, comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target

if __name__ == '__main__':
    # bob = ('Bob', 30, 'male')
    # print 'Representation:', bob
    #
    # jane = ('Jane', 29, 'female')
    # print '\nField by index:', jane[0]
    #
    # print '\nFields by index:'
    # for p in [bob, jane]:
    #     print '%s is a %d year old %s' % p

    A = Student('Aa', 3.5)
    B = Student('Bb', 3.5)
    list = [A, B]
    search_student(list, B, comp_gpa)