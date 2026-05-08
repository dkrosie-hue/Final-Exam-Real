class LabelGenerator:
    """Class to generate desired labels on demand"""
    def __init__ (self, prefix, start=1):
        self._prefix = prefix
        self._count = start
    
    def next_label(self):
        label = f"{self._prefix}{self._count}"
        self._count += 1
        return label

class Student:

    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        return self._grade

    def set_grade(self, new_grade):
        self._grade = new_grade

    def __str__(self):
        return f"{self._name}: {self._grade}"

def highest_student(students):

    best_student = students[0]

    for student in students:
        if student.get_grade() > best_student.get_grade():
            best_student = student

    return best_student

def main():

    s1 = Student("Dylan", 95)
    s2 = Student("Anna", 88)
    s3 = Student("Chris", 100)

    students = [s1, s2, s3]

    print(highest_student(students))

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    figures = LabelGenerator("P ", 0) 
    print(figures.next_label()) 
    print(figures.next_label())
    print(figures.next_label())
