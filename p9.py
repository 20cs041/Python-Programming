#creating student class
class student:
    FirstName = 'Khushbu'
    rollNumber = 0

    #Creating function for rollnumber and name
    def info(self, rollNumber, FirstName):
        self.FirstName = FirstName
        self.rollNumber = rollNumber


# Creating a class exam from class student.
class exam(student):
    marks_list = []

    # function marks to set the marks of that student.
    def marks(self, marks_list):
        self.marks_list = marks_list
        return marks_list


# Creating a class result from class exam.
class result(exam):
    marks_gain = 0

    # Function to obtain the total of the marks of a student.
    def result_of_student(self, marks_gain):
        totalMarks = 0
        for item in marks_gain:
            totalMarks += item
        return totalMarks


# Creating an object of result class.
a = result()
student_name = input("Enter the name of the student : ")
student_id = input("Enter the Roll Number of the student : ")

# Setting the details.
a.info(student_id, student_name)
print(f"Enter the marks of {student_name} in 6 subject : \n")
marks = []
for i in range(0, 6):
    marks.append(int(input()))

# Setting the marks.
marks_obtain = a.marks(marks)
total = a.result_of_student(marks_obtain)
print(f"Total of {student_name} mark's is : {total}")
