students = []

def add_student(name, age, courses):
    student = {
        "name": name,
        "age": age,
        "courses": courses
    }
    students.append(student)

def remove_student(name):
    global students
    students = [student for student in students if student["name"] != name]

def get_student(name):
    for student in students:
        if student["name"] == name:
            return student
    return None

def list_students():
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Courses: {', '.join(student['courses'])}")

# 添加學生
add_student("Alice", 20, ["Math", "CompSci"])
add_student("Bob", 22, ["English", "History"])

# 列出所有學生
list_students()

# 獲取特定學生的資訊
student = get_student("Alice")
if student:
    print(f"Found student: {student}")
else:
    print("Student not found")

# 刪除學生
remove_student("Bob")
list_students()