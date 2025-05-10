import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bushra7755@",
    database="student_db"
)
cursor = conn.cursor()
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, course))
    conn.commit()
    print("Student added.\n")
def view_students():
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    for student in results:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Course: {student[3]}")
    print()
def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    query = "DELETE FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print("Student deleted.\n")
def menu():
    while True:
        print("=== Student Info System (MySQL) ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice.\n")

menu()

cursor.close()
conn.close()
